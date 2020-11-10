# Idealista API analysis
This repository contains a POC for a housing pricing model based on the Idealista API. 

## Environment
The environment should be replicated in the following way: 
- Python dependencies are through [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)
- API keys should be passed through env variables `idealista_apikey` and `idealista_pass`
## Notebooks
The repository is estructured in the following ordered jobs:
- 01_DataExtraction.ipynb
- 02_EDA.ipynb
- 03_FeatureEngineering.ipynb           
- 04_SalePricePredictionModel.ipynb