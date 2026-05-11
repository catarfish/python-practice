import pandas as pd
from scipy import stats


def main():
    df = pd.DataFrame({
        "site":     ["Waitaha", "Mackenzie", "Wairau", "Waitaha", "Mackenzie", "Wairau"],
        "year":     [2021, 2021, 2021, 2022, 2022, 2022],
        "flow_m3s": [12.4, 8.1, 15.3, 9.7, 11.2, 14.8],
        "temp_c":   [14.2, 12.1, 16.3, 13.5, 11.8, 15.9]
    })

    # summary statistics — like summary() in R
    df["year"] = df["year"].astype(str)
    print(df.describe())
    print()

    # single column stats
    print("mean:  ", df["flow_m3s"].mean())
    print("median:", df["flow_m3s"].median())
    print("std:   ", df["flow_m3s"].std())
    print("min:   ", df["flow_m3s"].min())
    print("max:   ", df["flow_m3s"].max())
    print()

    # correlation — like cor() in R
    print("correlation between flow and temp:")
    print(df[["flow_m3s", "temp_c"]].corr())

    # split flow by year
    flow_2021 = df[df["year"] == 2021]["flow_m3s"]
    flow_2022 = df[df["year"] == 2022]["flow_m3s"]

    # two-sample t-test — like t.test() in R
    t_stat, p_value = stats.ttest_ind(flow_2021, flow_2022)
    print(f"t-statistic: {t_stat:.3f}")
    print(f"p-value:     {p_value:.3f}")
    print()

    # pearson correlation test — like cor.test() in R
    corr, p_corr = stats.pearsonr(df["flow_m3s"], df["temp_c"])
    print(f"pearson r:   {corr:.3f}")
    print(f"p-value:     {p_corr:.3f}")
    print()

    # shapiro-wilk normality test — like shapiro.test() in R
    stat, p_shapiro = stats.shapiro(df["flow_m3s"])
    print(f"shapiro-wilk p-value: {p_shapiro:.3f}")

if __name__ == "__main__":
    main()