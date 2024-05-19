# BirdLife Australia Traprock Key Biodiversity Area (KBA), Change Detection

## Objective
To quantify the changes in land cover in the Traprock KBA, QLD.

## Method
Landsat 8 satellite data was obtained from Digital Earth Australia's Open Data Cube for one date in each of June and December for 2013-2015 and 2021-2023. Each $30m×30m=900m^2$ plot in the study area was represented by one pixel in the dataset. The dates in each period were summarised to provide the per-pixel mean and standard deviation for the period. The last dates in the two periods formed the bi-temporal pair for the change detection. Various composite and NDVI images of the study area and its surrounds were plotted and reviewed. Land cover classifications were developed using NDVI thresholds and K-means classification, from which class change matrices and class change maps were produced. 

## Usage
1. Clone the repository to the [Digital Earth Australia (DEA) Sandbox](https://app.sandbox.dea.ga.gov.au/hub/login?next=%2Fhub%2F)
2. (Recommended) Clone the repository locally to perfom the analysis steps.
3. Delete unwanted files from the data sub-directories.
4. Update relevant parameters in the [global_params.py](./nbk/global_params.py) file.
5. Save a `.geojson` polygon of the study area to the `data/vector ` directory. The filename should be `[study_area_abbrev].geojson` where `study_area_abbrev` matches the parameter in the `nbk/global_params.py` file.
6. Obtain monthly rainfall, mean maximum temperature, and mean minimum temperature data for a waether station close to the study site from the [Bureau of Meterology](http://www.bom.gov.au/climate/data/) in csv format. Extract the `_Data1.csv` files from the downloaded archives and copy the them to the climate directory indicated in the [global_params.py](./nbk/global_params.py) file. Use the names `rainfall.csv`, `temp_mean_max.csv`, and `temp_mean_min.csv`.
7. Complete all relevant steps in the [DEA Data Preparation](./nbk/dea_data_prep.ipynb) notebook. Some steps are optional, depending on the objectives of the study.
8. Complete the steps in the [Exploratory Data Analysis](./nbk/eda.ipynb) notebook and review the potential change classes for the study site.
9. Complete relevant steps in the [Class Data Preparation](./nbk/class_data_prep.ipynb) notebook to create any necessary classification variables.
10. Complete the [Post-classification Analysis](./nbk/post_class_analysis.ipynb) notebook.


