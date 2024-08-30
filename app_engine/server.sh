#!/bin/bash 

mlflow db upgrade "postgresql://data_scientist:05c4r@34.44.198.7/tracking"
mlflow server \
  --host 0.0.0.0 \
  --port 8080 \
  --backend-store-uri "postgresql://data_scientist:05c4r@34.44.198.7/tracking" \
  --artifacts-destination "gs://mlflow-artifacts-2024/mlruns"