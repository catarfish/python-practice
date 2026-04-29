import pandas as pd

def main():
    # Create a dataframe — like data.frame() or tibble() in R
    df = pd.DataFrame({
        "site":     ["Waitaha", "Mackenzie", "Wairau", "Waitaha"],
        "year":     [2021, 2021, 2022, 2022],
        "flow_m3s": [12.4, 8.1, 15.3, 9.7]
    })

    print(df)
    print()

    # filter() in dplyr — df[condition] in pandas
    waitaha = df[df["site"] == "Waitaha"]
    print(waitaha)
    print()

    # select() in dplyr — df[["col1", "col2"]] in pandas
    just_site_flow = df[["site", "flow_m3s"]]
    print(just_site_flow)
    print()

    # arrange() in dplyr — sort_values() in pandas
    sorted_df = df.sort_values("flow_m3s", ascending=False)
    print(sorted_df)
    print()

    # group_by() + summarise() in dplyr
    # groupby() + agg() in pandas
    summary = df.groupby("site")["flow_m3s"].agg(
        mean_flow="mean",
        max_flow="max"
    ).reset_index()
    print(summary)

    df["flow_litres"] = df["flow_m3s"].apply(lambda x: x * 1000)
    print(df)
    print()

    # lambda with multiple columns
    df["label"] = df.apply(lambda row: f"{row['site']}_{row['year']}", axis=1)
    print(df)

if __name__ == "__main__":
    main()