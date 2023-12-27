# JLCPCB DataSheet Downloader

## Overview
This Python script automates the process of downloading datasheets and images from the JLCPCB "CART" page. It uses part numbers listed in a Bill of Materials (BOM) file to fetch these resources.

## Features
- Reads part numbers from a BOM file (CSV format).
- Downloads datasheets and images for each part number.
- Saves the datasheets and images in the current directory.
- Names the datasheet files according to their respective part numbers.

## Usage
To use this script, follow these steps:
1. Ensure you have a BOM file in CSV format. The script looks for files starting with "bom" or "BOM" and ending with ".csv".
2. Run the script. You can optionally provide the BOM file name as an argument.
   - `python your_script_name.py` (uses default BOM file in the current directory)
   - `python your_script_name.py <bom_file.csv>` (uses the specified BOM file)

## Requirements
- Python environment with the following modules:
  - `requests`
  - `json`
  - `csv`
  - `sys`
  - `os`

## Author
- Daekeun Kang

## Version
- 1.0.0

## Date
- 2023-12-27
