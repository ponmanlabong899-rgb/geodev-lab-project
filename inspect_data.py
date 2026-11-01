import csv

with open("water_lines_km.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

print("Rows:", len(rows))
print("Columns:", list(rows[0].keys()))

values = []
for row in rows:
    raw = row["length_km"].strip()
    if raw == "":
        continue
    values.append(float(raw))

print("length_km count:", len(values))
print("length_km smallest:", min(values))
print("length_km largest:", max(values))
print("length_km average:", sum(values) / len(values))
