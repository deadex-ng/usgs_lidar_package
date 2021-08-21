# Building a python Package

In this project I am going to produce an easy to use, reliable and
well designed python module that domain experts and data scientists can use to fetch,
visualise, and transform publicly available satellite and LIDAR data. In particular, the code
will interface with [USGS 3DEP](https://www.usgs.gov/core-science-systems/ngp/3dep) and fetch data using their API.

## Table of Content
- [Introduction](#introduction)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [utils](#utils)
- [tests](#tests)
- [data](#data)
- [laz](#laz)
- [tif](#tif)
- [3D](#3D)
- [pipeline.json](#pipeline.json)
- [regions.txt](#regions.txt)
- [Install](#instalation)
- [Quickstart](#quickstart)

### Introduction
I work at an AgriTech, which has a mix of domain experts, data scientists, data engineers. As part of the data engineering team, I have been tasked to produce an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data. In particular,the code will interface with USGS 3DEP and fetch data using their API. 

## Notebooks
- `vizualization.ipynb` : Notebook file showing **extracted data from las file**, **Geopandas dataframe with extracted data**, **Height Scatter Plot**, **IDW Function**, **Interpolation Points** and **3D render of the Terrain**
- `visualizeTif.ipynb`: Notebook file showing a visual map of a tif file.
- `get_data.ipynb`: Notebook file showing how to get 3DEP data using py3dep and visualizing the data using mtplotlib.

## Scripts 
- `main.py` : This is the script where the parameters(boundaries,region and output file) for the pipeline are set.

## utils
- `file_handler.py` : This is has the class used to set the output file name.
- `get_bounds.py` : This is has the class used to set the boundaries.
- `get_region.py` : This is has the class that is used to set region.

## Tests
- `test_file_handler.py` : This is used to test ```file_handler.py```
- `test_get_bounds.py` : This is used to test ```get_bounds.py```

## data
- Contains csv files that store coordinates

## laz
- Contains .las/.laz files

## tif 
- Contains .tif files

## 3D
- Contains 3D images of the terrain

## pipeline.json 
- This is the pipeline that fetches data from  [USGS](https://s3-us-west-2.amazonaws.com/usgs-lidar-public),preprocess it and stores it in both .las and .tif file

## regions.txt
- This file contains all the regions available in USGS


### Instalation
- **Install Required Python Modules**
``` 
pip install 3deppack
```

### Quickstart 
You can use 3deppack using the command line or as a python libary.
Let's see how you can use the 3deppack as a library

