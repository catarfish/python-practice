import pandas as pd
import plotly.express as px

def main():
    df = pd.DataFrame({
        "site":     ["Waitaha", "Mackenzie", "Wairau", "Waitaha", "Mackenzie", "Wairau"],
        "year":     [2021, 2021, 2021, 2022, 2022, 2022],
        "flow_m3s": [12.4, 8.1, 15.3, 9.7, 11.2, 14.8],
        "temp_c":   [14.2, 12.1, 16.3, 13.5, 11.8, 15.9]
    })

    # scatter plot — like ggplot(aes(x, y, color)) + geom_point()
    fig = px.scatter(
        df,
        x="temp_c",
        y="flow_m3s",
        color="site",
        title="Flow vs temperature by site"
    )
    fig.show()

    # bar chart — like geom_col()
    fig2 = px.bar(
        df,
        x="site",
        y="flow_m3s",
        color="year",
        barmode="group",
        title="Flow by site and year"
    )
    fig2.show()

    # line plot — like geom_line()
    fig3 = px.line(
        df,
        x="year",
        y="flow_m3s",
        color="site",
        markers=True,
        title="Flow over time by site"
    )
    fig3.show()

    # other options: facet_col, facet_row
    # fig.update_layout() and fig.update_traces() are equivalent of theme()

if __name__ == "__main__":
    main()