import pandas as pd
import json

def(main):
df = pd.DataFrame({
    "site": ["Monterey", "Mendocino", "Carmel", "Monterey", "Mendocino", "Carmel"],
    "year": [2000,2020, 2000, 2020, 2000, 2020],
    "flow": [500, 200, 300, 100, 400, 300]
})

print(df)

carmel = df[df["site"] == "Carmel"]
print(carmel)

# add a column
df["flow_convert"] = df["flow"].apply(lambda x: x * 1000)
print(df)

summary = df.groupby("site")["flow"].agg(
    max_flow = "max",
    min_flow = "min",
    mean_flow = "mean"
).reset_index()
print(summary)

# convert to json
summary_json = summary.to_dict(orient="records")

# write as json
with open("summary.json", "w") as f:
    json.dump(summary_json, f, indent= 2)

if __name__ == "__main__":
    main()    