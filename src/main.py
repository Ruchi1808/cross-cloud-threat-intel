from ingest import load_threat_feed, load_cloud_logs
from correlate import correlate_iocs
from risk import calculate_risk

# Load data
threats = load_threat_feed()
logs = load_cloud_logs()

# Correlate IOCs
matched = correlate_iocs(logs, threats)

# Calculate risk scores
matched["risk_score"] = matched.apply(calculate_risk, axis=1)

# Save enriched dataset
matched.to_csv("../output/enriched_iocs.csv", index=False)

# Generate risk report
with open("../output/risk_report.txt", "w") as f:
    for _, row in matched.iterrows():
        f.write(
            f"[{row['severity'].upper()}] IOC: {row['ioc']} | Risk Score: {row['risk_score']}\n"
        )

print("✔ Threat correlation and risk report generated successfully")
