# Cross-Cloud Threat Intelligence Aggregator

## Overview
This project demonstrates how threat intelligence feeds can be correlated with activity logs from multiple cloud platforms to detect malicious behavior.

## Use Case
Security teams often struggle to correlate threat intelligence across AWS, Azure, and GCP environments. This project provides a unified approach to identify malicious IPs and prioritize risks.

## Architecture
- Threat intelligence ingestion (CSV-based)
- Cloud log ingestion (AWS CloudTrail, Azure Activity Logs, GCP Audit Logs – simulated)
- IOC correlation using Python and Pandas
- Risk scoring based on severity and confidence
- Enriched IOC and risk reporting

## Technologies Used
- Python 3
- Pandas
- Requests
- AWS S3 (simulated)
- Azure Blob Storage (simulated)
- GCP Cloud Storage (simulated)

## How to Run
```bash
pip install -r requirements.txt
python src/main.py
