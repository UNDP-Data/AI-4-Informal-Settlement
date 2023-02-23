# AI-4-Informal-Settlement
The UNDP requires high resolution maps and granular statistics - on informal settlement or slums to develop programming opportunities in livelihoods, health, service, infrastructure, urban planning, disaster preparedness, and climate change adaption/mitigation. This information is important for the UNDP to successfully conductprograms to support the poor segment of population. However, most cities in Low and Middle Income Countries do not have reliable and timely high-resolution maps and granular statistics to plan intervention and monitor progress of poverty alleviation programs. 

This project is a proof of concept to comprehensively map informal urban settlements using Artificial Intelligence-based toolchain applied to Earth Observation Data.The project relies on low cost solutions focusing on Freely available Sentinel-2 and open-source tool  to map informal settlements and slums. 

## Getting Started 
### Installation
The work required on free and open-source software and packages for geospatial proessig and analysis. These packages can be install with the attached AI4IS_env.yaml file. In addition Python, the following packages are needed. 
- Gdal 
- Rasterio
- Sklearn
- Geopandas
- XGBoost
- Sklearn

### Datasets
The workflow takes in Raster dataset. Mask layer that represent label and the input satellite image. It is strucutred in the (image, mask) pair. the image is typically a georeferenced earth observation photograph (satellite or aerial).

### Preprocessing 
```
create_mask_layer.py : Use for creating the mask layer from from groundthruth. it takes shapefile or geojson and the corresponding raster data
prepare_spfea.py : Use to prepare image features for modeling 
```

### Model
Several model were carried out in this project. The gradient boosting folder contains XGBOOST workflow. The DeepLearning folder contain the implemented GIM model and Fully Convolutionl Nueral (FCN) Network model.
```
modeling.ipynb : pipeline for gradient boosting model. Found the gradient bossting folder
FCN_model.ipynb : pipeline for FCN model 
gim_cv : pipeline for GIM model. it starts from training to inference.
gim_inference : code for making inference from trained models. 
```
