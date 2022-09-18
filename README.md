# Project 1 - Fangting Ma

[![Python application test with Github Actions](https://github.com/nogibjj/scafford/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/scafford/actions/workflows/main.yml)

## INTRODUCTION

It is my 706 Project 1. I use a dataset about asteroids in the outer space from [Kaggle](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects?select=neo_v2.csv). Users can know some details about those objects and their hazardousness to the Earth through FastAPI and CLI.

## IMPLEMENTATION

I created this new repo on github for my project 1, set virtual environment on codespaces. Then I wrote Makefile and requirements.txt, and also a simple test py file to test the proper work of my scaffold. I also set up GitHub Actions. I also built container for it.

I downloaded the dataset about the nearest earth objects from kaggle, uploaded it onto Databricks, created table UI of it. I connected the databricks to Codespaces, built a CLI with Click and also implemented FastAPI.

## HOW TO USE: CLI

<code>
  <html>
    <head>
        databricks clusters list --output JSON | jq
        databricks fs ls dbfs:/
        databricks jobs list --output JSON | jq
    </head>
    <head>
      chmod +x query_sql_db.py
      ./query_sql_db.py cli-query --query "SELECT * FROM neo_v2_csv LIMIT 5"
    </head>
  </html>
</code>

## HOW TO USE: FastAPI

```
      python fast_api.py
```

Then go to the browser and open the webpage. You can play on the url, or can use swagger.
