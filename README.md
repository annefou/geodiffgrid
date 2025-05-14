# geodiffgrid
GeoDiffGrid is a tool for creating a grid plot for variable differences between two locations.

## Usage

To create a grid plot (heatmap) for variable differences between two locations:

```python

usage: geodiffgrid.py [-h] [--location1 LOCATION1] [--location2 LOCATION2] [--title TITLE] [--year YEAR]
                      [--variable VARIABLE] [--unit UNIT] [--vmin VMIN] [--vmax VMAX] [--cmap CMAP]
                      input_file output
```

- Example:

```
python geodiffgrid.py  --year 2024  UHI_Fortaleza_2024_pivoted.csv   UHI_Fortaleza_2024_pivoted.jpg
```

![Example](https://raw.githubusercontent.com/annefou/geodiffgrid/refs/heads/main/UHI_Fortaleza_2024_pivoted.jpg)
