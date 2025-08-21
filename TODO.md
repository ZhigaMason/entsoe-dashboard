# Data Collection

- [ ] Data injestion
    - Write a script to get daily data from [transperancy](https://transparency.entsoe.eu/) (daily load, generation wind & solar by country)
    - Containerize & Deploy
- [ ] Historical Data
    - Decide on CSV vs Parquet (Databricks uses parquet)
    - Download
    - Setup storage (ChatGPT advocated for *Azure Blob Storage*, *Azure Storage Account* is required everywhere)
    - Decide whether to save model and data on the same resource

# Processing

- [ ] Explore dataset
- [ ] Explore time dependant features (moving averages, std, meadian etc)
- [ ] Write a script
- [ ] Containerize & Deploy

# Model

- [ ] Setup Azure ML Workspace
- [ ] Train model (hp search)
- [ ] Deploy

# Dashboard

- [ ] How tf plotly dash works
- [ ] Write a dash board (geo data, series data, predictions)
- [ ] Deploy

# Documentation

- [ ] Documentation ¯\\\_(ツ)\_/¯
