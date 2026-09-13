# Data Note

## Watercourses (lines)
- Source: OpenStreetMap via QuickOSM (key: waterway) — https://www.openstreetmap.org
- Features: 120
- Geometry: LineString
- Key columns: waterway, name, osm_id, intermittent, tunnel, surface
- Notes: Good coverage of rivers/streams across Jos North and Jos South. Many segments are unnamed.

## Watercourses (points)
- Source: OpenStreetMap via QuickOSM (key: waterway) — https://www.openstreetmap.org
- Features: 28
- Geometry: Point
- Key columns: waterway, name, osm_id, addr:street, addr:city, ford
- Notes: Likely fords and similar waterway-related nodes.

## Mining/quarry areas
- Source: OpenStreetMap via QuickOSM (key: landuse, value: quarry) — https://www.openstreetmap.org
- Features: 4
- Geometry: Polygon (MultiPolygon)
- Notes: Very sparse — only 4 polygons for an area with extensive documented tin-mining activity. OSM significantly under-represents mining/quarry land use here, which is an important limitation for this project.