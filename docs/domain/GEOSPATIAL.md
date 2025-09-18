# Geospatial Data — Practical Guide

## File formats
- GeoPackage, GeoJSON, Shapefile (legacy), CSV + WKT/WKB
- Raster: GeoTIFF/COG, NetCDF, Zarr (cloud-native)

## Catalogs & discovery
- STAC: self-describing catalogs of assets
- OGC APIs: Features, Tiles, Coverages

## Cloud-optimized
- COG: Cloud-Optimized GeoTIFFs (rio-cogeo)
- Zarr + kerchunk for chunked, lazy access

## Minimal examples
```bash
# make a COG from a GeoTIFF
rio cogeo create in.tif out.tif
```

```python
# open Zarr with xarray (NetCDF/CF converted)
import xarray as xr
xr.open_zarr('s3://bucket/dataset.zarr', storage_options={'anon': True})
```

## Copy‑and‑paste recipes

```bash
# Create a cloud‑optimized GeoTIFF with overviews and compression
gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 -co NUM_THREADS=ALL_CPUS in.tif out_cog.tif

# Validate a COG
rio cogeo validate out_cog.tif
```

```bash
# Query an OGC API - Features collection
BASE=https://demo.ldproxy.net/daraa
curl -s "$BASE/collections" | jq '.collections[] | {id,title}'
curl -s "$BASE/collections/waterways/items?limit=5" | jq '.features | length'

# Fetch OGC API - Tiles metadata
curl -s "$BASE/collections/waterways/tiles" | jq '.tileMatrixSets'
```

```python
# Read OGC API - Features into GeoPandas
import geopandas as gpd
gdf = gpd.read_file('https://demo.ldproxy.net/daraa/collections/waterways/items?limit=1000')
print(gdf.head())
```

## Publishing
- Host STAC (e.g., stac-fastapi) or publish to a platform (e.g., PANGAEA with links)
- Provide overviews/thumbnails and spatial metadata (CRS, bbox)

Prereqs/tools: GDAL >= 3.1, rasterio/rio-cogeo, jq, curl, GeoPandas.
