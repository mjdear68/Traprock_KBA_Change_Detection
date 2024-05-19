# Mudgee Region NSW, Change Detection 2004 to 2023

## Objective
To quantify the changes in land cover in the Mudgee region, NSW for the period Jan 2005 to Jan 2024.

## Method
Landsat satellite data was obtained from Digital Earth Australia's Open Data Cube for one date in each of September and December for 2004 and 2023. Each $100m×100m=1ha$ plot in the study area was represented by one pixel in the dataset. The two dates for each year were averaged to form RGB, NIR and NDVI datasets. True-colour (RGB) and NDVI images of the study area and its surrounds were plotted and reviewed. A land cover classification was developed using NDVI thresholds, from which class change matrices and a class change map were produced. 

## Usage
1. Clone the repository to the [Digital Earth Australia (DEA) Sandbox](https://app.sandbox.dea.ga.gov.au/hub/login?next=%2Fhub%2F)
2. Update relevant parameters in the [global_prameters.py]() file.
3. Complete all relevant steps in the [DEA Data Preparation](./nbk/dea_data_prep.ipynb) notebook. Some steps are optional, depending on the objectives of the study.
4. Complete the steps in the [Exploratory Data Analysis](./nbk/eda.ipynb) notebook and review the potential change classes for the study site.
5. Complete relevant steps in the [Class Data Preparation](./nbk/class_data_prep.ipynb) notebook to create any necessary classification variables.
6. Complete the [Post-classification Analysis](./nbk/post_class_analysis.ipynb) notebook.


