
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os

# Path to CSV (mounted from host)
csv_path = "/data/points.csv"

# Read CSV
df = pd.read_csv(csv_path)

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=[Point(xy) for xy in zip(df.lon, df.lat)],
    crs="EPSG:4326"
)

print("Loaded points:")
print(gdf)

# Example: filter points within a bounding box
bbox = gpd.GeoSeries([Point(174.77, -41.29).buffer(0.01)], crs="EPSG:4326")
filtered = gdf[gdf.geometry.within(bbox.iloc[0])]
print("\nPoints within buffer:")
print(filtered)
