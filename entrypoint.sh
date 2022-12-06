#!/usr/bin/env bash

# Launch our mlflow tracking server
set -e
# set -x

mlflow server \
  --backend-store-uri=${MLFLOW_BACKEND_STORE_PATH} \
  --artifacts-destination=${MLFLOW_ARTIFACT_PATH} \
  --serve-artifacts \
  --host 0.0.0.0 \
  --port ${PORT}
