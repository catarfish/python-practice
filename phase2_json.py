import json

def main():
    # A dict — this IS JSON structure
    site_data = {
        "site": "Waitaha",
        "measurements": [
            {"date": "2024-01-01", "flow": 12.4},
            {"date": "2024-01-02", "flow": 13.1}
        ]
    }

    # Convert dict to JSON string — like toJSON() in R
    json_string = json.dumps(site_data, indent=2)
    print(json_string)
    print()

    # Convert JSON string back to dict — like fromJSON() in R
    parsed = json.loads(json_string)
    print(parsed["site"])
    print(parsed["measurements"][0]["flow"])

    # Write JSON to a file
    with open("site_data.json", "w") as f:
        json.dump(site_data, f, indent=2)

    # Read JSON from a file
    with open("site_data.json", "r") as f:
        loaded = json.load(f)
    print(loaded)

if __name__ == "__main__":
    main()