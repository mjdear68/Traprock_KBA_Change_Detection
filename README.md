# BirdLife Australia Traprock Key Biodiversity Area (KBA), Change Detection

## Objective
To quantify the changes in land cover in the Traprock KBA, QLD.

## Method
Landsat 8 satellite data was obtained from Digital Earth Australia's Open Data Cube for one date in each of June and December for 2013-2015 and 2021-2023. Each $30m×30m=900m^2$ plot in the study area was represented by one pixel in the dataset. The dates in each period were summarised to provide the per-pixel mean and standard deviation for the period. The last dates in the two periods formed the bi-temporal pair for the change detection. Various composite and NDVI images of the study area and its surrounds were plotted and reviewed. Land cover classifications were developed using NDVI thresholds and K-means classification, from which class change matrices and class change maps were produced. 

## Usage
1. Clone the repository to the [Digital Earth Australia (DEA) Sandbox](https://app.sandbox.dea.ga.gov.au/hub/login?next=%2Fhub%2F)
2. (Recommended) Clone the repository locally to perfom the analysis steps.
3. Update relevant parameters in the [global_prameters.py]() file.
4. Complete all relevant steps in the [DEA Data Preparation](./nbk/dea_data_prep.ipynb) notebook. Some steps are optional, depending on the objectives of the study.
5. Complete the steps in the [Exploratory Data Analysis](./nbk/eda.ipynb) notebook and review the potential change classes for the study site.
6. Complete relevant steps in the [Class Data Preparation](./nbk/class_data_prep.ipynb) notebook to create any necessary classification variables.
7. Complete the [Post-classification Analysis](./nbk/post_class_analysis.ipynb) notebook.


