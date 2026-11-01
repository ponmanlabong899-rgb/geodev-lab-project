import struct, csv, sys
src, dst = sys.argv[1], sys.argv[2]
d = open(src, "rb").read()
n, hl, rl = struct.unpack("<IHH", d[4:12])
fields = []
i = 32
while d[i] != 0x0D:
    name = d[i:i+11].split(b"\x00")[0].decode()
    fields.append((name, d[i+16]))
    i += 32
rows = []
for r in range(n):
    rec = d[hl + r*rl : hl + (r+1)*rl]
    if rec[0:1] == b"*":
        continue
    pos = 1
    row = []
    for name, ln in fields:
        row.append(rec[pos:pos+ln].decode("utf-8", "ignore").strip())
        pos += ln
    rows.append(row)
with open(dst, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([x for x, _ in fields])
    w.writerows(rows)
print(len(rows), "rows;", [x for x, _ in fields])
