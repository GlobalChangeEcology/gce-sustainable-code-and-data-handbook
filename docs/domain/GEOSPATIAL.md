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

## Publishing
- Host STAC (e.g., stac-fastapi) or publish to a platform (e.g., PANGAEA with links)
- Provide overviews/thumbnails and spatial metadata (CRS, bbox)
