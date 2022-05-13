# Overview

Simple stack of Airflow, Feast, FastAPI

## Getting started

Poetry is used to manage dependencies. Let's get our feature store stood up and features materialized into our Redis online_store for low latency retrieval.

<!-- ```bash
    make setup
``` -->

```bash
  docker compose up redis -d
  poetry install
  cd feature_repo
  poetry run feast apply
  poetry run python3 -m training
  CURRENT_TIME=$(date -u +"%Y-%m-%dT%H:%M:%S")
  poetry run feast materialize-incremental $CURRENT_TIME
```
