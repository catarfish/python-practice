import pandas as pd
import plotly.express as px
from scipy import stats
import numpy as np

def main():

    np.random.seed(42)

    df = pd.DataFrame({
        "site":     np.tile(["Carmel", "Oahu", "Antarctica", "Casablanca"], 3),
        "year":     np.repeat([2020, 2021, 2022],4),
        "flow_m3s": np.random.uniform(5, 25, size = 12),
        "temp_c":   np.random.normal(14,2, size = 12)
    })

    print(df.describe())
    flow_2021 = df[df["year"] == 2021]["flow_m3s"]
    flow_2022 = df[df["year"] == 2022]["flow_m3s"]

    t_stat, p_value = stats.ttest_ind(flow_2021, flow_2022)
    print(f"t.statistic: {t_stat:.3f}")
    print(f"p_value: {p_value:.3f}")

    fig = px.scatter(
        df,
        x = "temp_c",
        y = "flow_m3s",
        color = "site",
        symbol = "site",
        title = "Flow by temperature"
    )
    fig.write_html("plot1.html")

    fig2 = px.line(
        df,
        x = "year",
        y = "flow_m3s",
        color = "site",
        symbol = "site",
        title = "Flow by temperature"
    )
    fig2.write_html("plot2.html")


if __name__ == "__main__":
    main()