"""
AI Governance Risk Assessment - analysis script

Validates the assessment data in data/, scores the AI risk register on a 5x5
likelihood x impact scale, summarizes the NIST AI RMF and ISO/IEC 42001 gap
assessments, and writes tables and charts to outputs/.

Usage (from the repository root):
    pip install -r scripts/requirements.txt
    python scripts/analyze.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "outputs"

# Risk rating bands for a 5x5 matrix (score = likelihood x impact)
BANDS = [(1, 4, "Low"), (5, 9, "Medium"), (10, 15, "High"), (16, 25, "Critical")]
APPETITE_MAX = 9  # residual risk above this needs formal acceptance

LIKELIHOOD = {1: "Rare", 2: "Unlikely", 3: "Possible", 4: "Likely", 5: "Almost certain"}
IMPACT = {1: "Minimal", 2: "Minor", 3: "Moderate", 4: "Major", 5: "Severe"}

# Colors (validated reference palette)
INK, INK_2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
CURRENT, TARGET = "#2a78d6", "#eb6834"
BAND_COLORS = {"Low": "#0ca30c", "Medium": "#fab219", "High": "#ec835a", "Critical": "#d03b3b"}


def rating(score: int) -> str:
    for lo, hi, name in BANDS:
        if lo <= score <= hi:
            return name
    raise ValueError(score)


def check(cond, msg, errors):
    if not cond:
        errors.append(msg)


def load():
    inv = pd.read_csv(DATA / "ai_system_inventory.csv")
    reg = pd.read_csv(DATA / "ai_risk_register.csv")
    rmf = pd.read_csv(DATA / "nist_ai_rmf_assessment.csv")
    iso = pd.read_csv(DATA / "iso42001_gap_assessment.csv")

    errors = []
    check(inv["System_ID"].is_unique, "Duplicate System_IDs in inventory", errors)
    check(reg["Risk_ID"].is_unique, "Duplicate Risk_IDs in risk register", errors)
    valid_systems = set(inv["System_ID"]) | {"All"}
    bad = set(reg["System_ID"]) - valid_systems
    check(not bad, f"Risk register references unknown systems: {bad}", errors)
    for col in ["Inherent_Likelihood", "Inherent_Impact", "Residual_Likelihood", "Residual_Impact"]:
        check(reg[col].between(1, 5).all(), f"{col} must be 1-5", errors)
    check(len(rmf) == 19, f"NIST AI RMF has 19 categories, found {len(rmf)}", errors)
    for df, name in [(rmf, "NIST AI RMF"), (iso, "ISO 42001")]:
        check(df["Current_Maturity"].between(0, 5).all(), f"{name}: maturity must be 0-5", errors)
        check((df["Target_Maturity"] >= df["Current_Maturity"]).all(),
              f"{name}: target below current", errors)
    if errors:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(errors))
    return inv, reg, rmf, iso


def score_register(reg: pd.DataFrame) -> pd.DataFrame:
    reg = reg.copy()
    reg["Inherent_Score"] = reg["Inherent_Likelihood"] * reg["Inherent_Impact"]
    reg["Inherent_Rating"] = reg["Inherent_Score"].apply(rating)
    reg["Residual_Score"] = reg["Residual_Likelihood"] * reg["Residual_Impact"]
    reg["Residual_Rating"] = reg["Residual_Score"].apply(rating)
    reg["Risk_Reduction_%"] = (100 * (1 - reg["Residual_Score"] / reg["Inherent_Score"])).round(0)
    reg["Within_Appetite"] = np.where(reg["Residual_Score"] <= APPETITE_MAX, "Yes",
                                      "No - requires formal acceptance")
    return reg


def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK_2, labelsize=9)


def heatmaps(reg: pd.DataFrame, path: Path):
    fig, axes = plt.subplots(1, 2, figsize=(13, 6.2))
    for ax, kind in zip(axes, ["Inherent", "Residual"]):
        for li in range(1, 6):
            for im in range(1, 6):
                band = rating(li * im)
                ax.add_patch(plt.Rectangle((im - 0.5, li - 0.5), 1, 1,
                                           facecolor=BAND_COLORS[band], alpha=0.28,
                                           edgecolor="white", linewidth=2))
                ids = reg[(reg[f"{kind}_Likelihood"] == li) & (reg[f"{kind}_Impact"] == im)]["Risk_ID"]
                if len(ids):
                    lines = [", ".join(ids[i:i + 3]) for i in range(0, len(ids), 3)]
                    ax.text(im, li, "\n".join(lines), ha="center", va="center",
                            fontsize=7.5, color=INK, linespacing=1.3)
        ax.set_xlim(0.5, 5.5)
        ax.set_ylim(0.5, 5.5)
        ax.set_xticks(range(1, 6))
        ax.set_xticklabels([f"{k}\n{v}" for k, v in IMPACT.items()], fontsize=8)
        ax.set_yticks(range(1, 6))
        ax.set_yticklabels([f"{v} {k}" for k, v in LIKELIHOOD.items()], fontsize=8)
        ax.set_xlabel("Impact", color=INK_2, fontsize=9)
        ax.set_ylabel("Likelihood", color=INK_2, fontsize=9)
        counts = reg[f"{kind}_Rating"].value_counts()
        summary = " · ".join(f"{b}: {counts.get(b, 0)}" for _, _, b in BANDS[::-1])
        ax.set_title(f"{kind} risk ({len(reg)} risks)\n{summary}", color=INK, fontsize=11)
        style(ax)
        ax.tick_params(length=0)
    legend = [Patch(facecolor=BAND_COLORS[b], alpha=0.5, label=f"{b} ({lo}-{hi})")
              for lo, hi, b in BANDS]
    fig.legend(handles=legend, loc="lower center", ncol=4, frameon=False, fontsize=9,
               labelcolor=INK_2, bbox_to_anchor=(0.5, -0.01))
    fig.suptitle("AI risk heatmap: before and after planned treatment",
                 color=INK, fontsize=13, y=0.99)
    fig.tight_layout(rect=(0, 0.05, 1, 0.97))
    fig.savefig(path, dpi=160, facecolor="white")
    plt.close(fig)


def dumbbell(df: pd.DataFrame, label_col: str, title: str, path: Path, height: float):
    df = df.iloc[::-1].reset_index(drop=True)
    y = np.arange(len(df))
    fig, ax = plt.subplots(figsize=(10, height))
    ax.hlines(y, df["Current_Maturity"], df["Target_Maturity"], color=GRID, linewidth=4, zorder=1)
    ax.scatter(df["Target_Maturity"], y, color=TARGET, s=110, zorder=3, edgecolor="white",
               linewidth=2, label="Target")
    ax.scatter(df["Current_Maturity"], y, color=CURRENT, s=60, zorder=4, edgecolor="white",
               linewidth=2, label="Current")
    for yi, c, t in zip(y, df["Current_Maturity"], df["Target_Maturity"]):
        ax.text(t + 0.15, yi, f"gap {t - c}" if t > c else "at target",
                va="center", fontsize=8, color=INK_2)
    ax.set_yticks(y)
    ax.set_yticklabels(df[label_col], fontsize=9, color=INK)
    ax.set_xlim(-0.2, 5)
    ax.set_xticks(range(6))
    ax.set_xticklabels(["0\nNot performed", "1\nInitial", "2\nRepeatable", "3\nDefined",
                        "4\nManaged", "5\nOptimized"], fontsize=8)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    style(ax)
    ax.set_title(title, color=INK, fontsize=13, loc="left", pad=30)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, frameon=False,
              labelcolor=INK_2, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=160, facecolor="white")
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    inv, reg, rmf, iso = load()
    reg = score_register(reg)

    reg.sort_values(["Inherent_Score", "Residual_Score"], ascending=False).to_csv(
        OUT / "scored_risk_register.csv", index=False)

    by_system = (reg.groupby("System_ID")
                 .agg(Risks=("Risk_ID", "count"),
                      Max_Inherent=("Inherent_Score", "max"),
                      Avg_Inherent=("Inherent_Score", "mean"),
                      Avg_Residual=("Residual_Score", "mean"))
                 .round(1).reset_index())
    names = dict(zip(inv["System_ID"], inv["System_Name"]))
    names["All"] = "Organization-wide"
    by_system.insert(1, "System_Name", by_system["System_ID"].map(names))
    by_system.to_csv(OUT / "risk_by_system.csv", index=False)

    rmf["Gap"] = rmf["Target_Maturity"] - rmf["Current_Maturity"]
    rmf_fn = (rmf.groupby("Function", sort=False)
              .agg(Categories=("Category_ID", "count"),
                   Avg_Current=("Current_Maturity", "mean"),
                   Avg_Target=("Target_Maturity", "mean"))
              .round(2).reset_index())
    rmf_fn.to_csv(OUT / "nist_ai_rmf_function_summary.csv", index=False)

    iso["Gap"] = iso["Target_Maturity"] - iso["Current_Maturity"]
    iso["Label"] = iso["Ref"].astype(str).apply(
        lambda r: f"Clause {r}" if not r.startswith("A.") else r) + "  " + iso["Area"]
    rmf["Label"] = rmf["Category_ID"]

    heatmaps(reg, OUT / "risk_heatmap.png")
    dumbbell(rmf, "Label", "NIST AI RMF maturity by category (current vs. target)",
             OUT / "nist_ai_rmf_maturity.png", 8.5)
    dumbbell(iso, "Label", "ISO/IEC 42001 readiness (current vs. target)",
             OUT / "iso42001_readiness.png", 7.5)

    print(f"AI systems inventoried: {len(inv)}")
    print(f"Risks: {len(reg)}")
    print("Inherent ratings:", reg["Inherent_Rating"].value_counts().to_dict())
    print("Residual ratings:", reg["Residual_Rating"].value_counts().to_dict())
    print(f"Total inherent score: {reg['Inherent_Score'].sum()}, "
          f"residual: {reg['Residual_Score'].sum()}, "
          f"reduction: {100 * (1 - reg['Residual_Score'].sum() / reg['Inherent_Score'].sum()):.0f}%")
    print("Residual above appetite:",
          reg[reg["Residual_Score"] > APPETITE_MAX]["Risk_ID"].tolist())
    print("By category:", reg["Risk_Category"].value_counts().to_dict())
    print("\nTop inherent risks:")
    print(reg.sort_values("Inherent_Score", ascending=False)
          [["Risk_ID", "System_ID", "Risk_Title", "Inherent_Score", "Residual_Score"]]
          .head(8).to_string(index=False))
    print("\nBy system:\n", by_system.to_string(index=False))
    print(f"\nNIST AI RMF avg current {rmf['Current_Maturity'].mean():.2f}, "
          f"target {rmf['Target_Maturity'].mean():.2f}")
    print(rmf_fn.to_string(index=False))
    print(f"\nISO 42001 avg current {iso['Current_Maturity'].mean():.2f}, "
          f"target {iso['Target_Maturity'].mean():.2f}; at 0: "
          f"{iso[iso['Current_Maturity'] == 0]['Ref'].tolist()}")
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
