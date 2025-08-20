
"""
analyze_retention.py
Author: Senior Data Analyst
Contact: 24ds1000011@ds.study.iitm.ac.in

Loads quarterly retention data, computes summary stats, and generates
visualizations for executive review.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from pathlib import Path

BENCHMARK = 85.0

def main():
    here = Path(__file__).resolve().parent
    data_path = (here.parent / "data" / "retention_2024.csv")
    out_img = here.parent / "retention_trend.png"

    df = pd.read_csv(data_path)
    df["Quarter"] = pd.Categorical(df["Quarter"], ["Q1","Q2","Q3","Q4"], ordered=True)
    df = df.sort_values("Quarter")

    avg = round(df["RetentionRate"].mean(), 2)
    print(f"Average retention (2024): {avg}")
    print(f"Benchmark target: {BENCHMARK}")

    # Plot: line trend + benchmark
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["Quarter"], df["RetentionRate"], marker="o", linewidth=2, label="Retention Rate")
    ax.axhline(BENCHMARK, linestyle="--", linewidth=1.5, label=f"Industry Target ({BENCHMARK})")
    ax.set_title("Customer Retention Rate — 2024 (Quarterly)")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Retention Rate")
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(PercentFormatter(100))
    for x, y in zip(df["Quarter"], df["RetentionRate"]):
        ax.text(x, y+0.6, f"{y:.2f}%", ha="center", va="bottom", fontsize=9)
    ax.legend(frameon=True)
    fig.tight_layout()
    fig.savefig(out_img, dpi=150)
    print(f"Saved chart to: {out_img}")

if __name__ == "__main__":
    main()
