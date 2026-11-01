import csv

def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values

def summarise(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }

def summarise_all(rows):
    results = {}
    for column in rows[0].keys():
        try:
            values = clean_values(rows, column)
        except ValueError:
            continue
        if len(values) == 0:
            continue
        results[column] = summarise(values)
    return results

rows = read_rows("water_lines_km.csv")
print("Rows:", len(rows))
for column, s in summarise_all(rows).items():
    print(column, "| count", s["count"], "| smallest", s["smallest"], "| largest", s["largest"], "| average", round(s["average"], 2))
