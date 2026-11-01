import struct, csv, math

def hav(a, b):
    if abs(a[0]) > 180:
        return math.dist(a, b) / 1000
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))

def lengths(path):
    d = open(path, "rb").read()
    pos = 100
    out = []
    while pos < len(d):
        clen = struct.unpack(">i", d[pos+4:pos+8])[0] * 2
        c = d[pos+8:pos+8+clen]
        pos += 8 + clen
        if struct.unpack("<i", c[:4])[0] == 0:
            out.append(0.0)
            continue
        npart, npt = struct.unpack("<ii", c[36:44])
        parts = list(struct.unpack("<%di" % npart, c[44:44+4*npart]))
        o = 44 + 4*npart
        pts = [struct.unpack("<dd", c[o+16*i:o+16*i+16]) for i in range(npt)]
        parts.append(npt)
        tot = 0.0
        for k in range(npart):
            seg = pts[parts[k]:parts[k+1]]
            for i in range(len(seg)-1):
                tot += hav(seg[i], seg[i+1])
        out.append(tot)
    return out

L = lengths("water_crourse_lines.shp")
with open("water_lines.csv", encoding="utf-8") as f:
    rows = list(csv.reader(f))
print("shapes:", len(L), "rows:", len(rows) - 1)
out = [rows[0] + ["length_km"]]
for i, r in enumerate(rows[1:]):
    out.append(r + [str(round(L[i], 4))])
with open("water_lines_km.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(out)
