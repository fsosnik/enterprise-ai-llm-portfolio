import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def simulate_production_metrics(days=7):
    """
    Simulates production AI metrics over the given number of days.
    Introduces 'drift' starting on day 4.
    """
    dates = [datetime.now() - timedelta(days=i) for i in range(days)]
    dates.reverse()
    
    records = []
    
    for i, date in enumerate(dates):
        # Base healthy behavior
        accuracy = np.random.normal(loc=0.92, scale=0.02)
        latency_ms = np.random.normal(loc=150, scale=20)
        feature_mean = np.random.normal(loc=5.0, scale=0.5)
        
        # Simulate Data Drift and Accuracy Degradation after day 3
        if i >= 3:
            feature_mean += 2.0  # Distribution shift
            accuracy -= 0.15     # Performance drops due to drift
            
        records.append({
            "Date": date.strftime("%Y-%m-%d"),
            "Accuracy": min(max(accuracy, 0.0), 1.0),
            "Avg_Latency_ms": round(max(latency_ms, 50), 2),
            "Input_Feature_X_Mean": round(feature_mean, 2)
        })
        
    return pd.DataFrame(records)

def run_monitoring_checks(df: pd.DataFrame):
    """
    Evaluates the metrics dataframe to detect degradation.
    """
    alerts = []
    
    latest_acc = df.iloc[-1]["Accuracy"]
    baseline_acc = df.iloc[0]["Accuracy"]
    
    # 1. Check Accuracy Threshold
    if latest_acc < 0.80:
        alerts.append(f"[CRITICAL] Model Accuracy dropped below 0.80. Current: {latest_acc:.2f}")
        
    # 2. Check Input Drift (Comparing first 3 days vs last 3 days)
    if len(df) >= 6:
        baseline_feature = df.iloc[:3]["Input_Feature_X_Mean"].mean()
        recent_feature = df.iloc[-3:]["Input_Feature_X_Mean"].mean()
        shift_percentage = abs((recent_feature - baseline_feature) / baseline_feature) * 100
        
        if shift_percentage > 20.0:
            alerts.append(f"[WARNING] Feature 'X' has drifted by {shift_percentage:.1f}%. Models may need retraining.")

    return alerts

def print_dashboard(df, alerts):
    print("="*50)
    print(f"      AI MODEL MONITORING DASHBOARD - {datetime.now().strftime('%Y-%m-%d')} ")
    print("="*50)
    print("\\n[Last 7 Days Metrics]:")
    print(df.to_string(index=False))
    
    print("\\n" + "="*50)
    print("                 SYSTEM STATUS")
    print("="*50)
    if not alerts:
        print("✅ ALL SYSTEMS NOMINAL. No drift or degradation detected.")
    else:
        for alert in alerts:
            print(f"🚨 {alert}")
    print("="*50)

if __name__ == "__main__":
    # 1. Collect mock data
    metrics_df = simulate_production_metrics()
    
    # 2. Analyze data
    system_alerts = run_monitoring_checks(metrics_df)
    
    # 3. Render Dashboard
    print_dashboard(metrics_df, system_alerts)
