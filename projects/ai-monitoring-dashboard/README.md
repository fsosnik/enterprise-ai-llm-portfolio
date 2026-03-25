# AI Monitoring Dashboard (MLOps)

## Overview
This project simulates an **MLOps Monitoring script** designed to track the health of an AI model deployed in production. It generates mock traffic data, evaluates metrics such as Model Accuracy and Data Drift (simulated using standard deviation and mean shifts), and aggregates this into a console dashboard summary.

*Note: In an enterprise setting, this logic would run on a schedule (e.g., Airflow or CRON), writing metrics to Prometheus/Grafana or Datadog. Here, it simply outputs a report to the console to showcase understanding of production ML lifecycle concepts like Data Drift.*

## Stack
- **Python 3.9+**
- **Numpy** and **Pandas** (Data generation and statistical analysis)

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python main.py
   ```
