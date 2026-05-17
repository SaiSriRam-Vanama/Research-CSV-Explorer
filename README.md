# Research CSV Explorer

An interactive CSV data analysis tool built with Jupyter Notebook widgets (ipywidgets). Upload any CSV file and explore it through visualizations, statistics, and geospatial mapping directly in a Jupyter environment.

Powered by **ipywidgets**, **Pandas**, **Matplotlib**, **Seaborn**, **Folium**, and **NumPy**.

## Project Overview

This tool provides a graphical widget-based interface (no code required after launch) for exploring tabular datasets. It is designed for researchers, data analysts, and students who want quick visual insights from CSV files without writing plotting code. The bundled sample dataset contains bibliographic records of climate and environmental research publications, but the tool works with any CSV file.

When you run the script, an interactive dashboard renders in your Jupyter Notebook with:
- A styled header and a file upload button
- Six action buttons in a grid layout
- A dedicated output area where results appear

## Output / Visual Results

Each button produces a specific output in the widget area:

- **View Data** -- Displays the first 5 rows of the dataset as a formatted HTML table (pandas head())
- **Basic Stats** -- Shows descriptive statistics table: count, mean, std, min, 25%, 50%, 75%, max for all numeric columns
- **Histogram** -- Opens a column selector dropdown + generate button. On selection, renders a matplotlib histogram with a KDE curve overlay, e.g. a distribution plot of "Fiscal-Year" showing publication counts over time
- **Scatter Plot** -- Opens X and Y column dropdowns + generate button. On selection, renders a seaborn scatter plot comparing two numeric columns, e.g. "DocID vs Fiscal-Year"
- **Correlation Map** -- Renders a seaborn heatmap of Pearson correlation coefficients between all numeric columns (annotated with values, coolwarm colormap)
- **Geo Visualization** -- Renders an interactive Folium map centered on India (zoomable, pannable) with circle markers at each data point's latitude/longitude. Clicking a marker shows a popup with the row's Title or first column value. If lat/lng columns are missing, the tool auto-generates mock coordinates for demo purposes

## Features

- **CSV Upload** -- Upload a CSV file via the file picker widget; auto-parses into a DataFrame
- **View Data** -- Display the first 5 rows of the loaded dataset
- **Basic Statistics** -- Generate descriptive statistics (count, mean, std, min, quartiles, max)
- **Histogram** -- Select any numeric column and plot a histogram with KDE overlay (includes non-numeric column validation)
- **Scatter Plot** -- Select X and Y axes to generate scatter plots between numeric columns (includes non-numeric column validation)
- **Correlation Heatmap** -- Visualize Pearson correlation between all numeric columns using Seaborn
- **Geo Visualization** -- Plot data points on an interactive Folium map (centered on India by default; auto-generates mock latitude/longitude if columns are missing)

## Dataset

The bundled dataset (`urban_green_space_analysis.csv`) contains bibliographic records of peer-reviewed research publications on urban green spaces, climate adaptation, remote sensing, and environmental policy from the Institute for Global Environmental Strategies (IGES).

Columns: DocID, Type, Poster, Topics, Area, Fiscal-Year, Published, Target, Author, Title, Series, Journal-Title, Volume-Issue, Pages, Copyright, Publisher, ISBN-ISSN, Language, Begins, Related-Website, Tags, Region-Country, Updated-date, URL.

## Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- ipywidgets
- folium
- numpy

## Installation

```bash
pip install pandas matplotlib seaborn ipywidgets folium numpy
```

## Usage

Run the script in a Jupyter Notebook cell:

```python
%run urban_green_space_analysis.py
```

Or open in Jupyter Lab / Notebook and execute the cell. The interactive widget interface will render. Click **Upload Dataset** to load any CSV, then use the six buttons to explore.

## Project Structure

```
research-csv-explorer/
  urban_green_space_analysis.py   -- Main CSVAnalyzer class with widget UI
  urban_green_space_analysis.csv  -- Sample bibliographic dataset
  README.md                       -- This file
```

## How It Works

The `CSVAnalyzer` class in `urban_green_space_analysis.py`:

1. Renders a header, file upload widget, and six action buttons in a 3-column grid
2. On file upload, reads the CSV into a pandas DataFrame and injects mock lat/lng if absent
3. Each button triggers a method that either displays data, statistics, or interactive plots in the output area
4. Histogram and Scatter Plot use inline dropdown widgets to let the user choose columns before plotting

## Author

**Sai Sri Ram Vanama**

- LinkedIn: [saisriramv](https://linkedin.com/in/saisriramv)
- GitHub: [SaiSriRam-Vanama](https://github.com/SaiSriRam-Vanama)

## License

MIT License

Copyright (c) 2026 Sai Sri Ram Vanama

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
