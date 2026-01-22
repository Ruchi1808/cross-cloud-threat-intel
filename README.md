# 🌐 Cross-Cloud Threat Intelligence Aggregator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Cloud](https://img.shields.io/badge/Cloud-AWS%20|%20Azure%20|%20GCP-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Overview
The **Cross-Cloud Threat Intelligence Aggregator** is a Python-based cybersecurity project that correlates threat intelligence feeds with activity logs from AWS, Azure, and GCP to detect malicious behavior and prioritize risks.

This project simulates a **real-world SOC workflow**, demonstrating log analysis, IOC correlation, and risk assessment.

---

## 🎯 Problem Statement
Organizations operate across multiple cloud platforms, but security teams struggle to correlate threat intelligence with cloud activity efficiently, leading to delayed detection and poor prioritization.

---

## 💡 Solution
This project provides:
- Unified threat intelligence ingestion
- Cross-cloud log correlation
- IOC enrichment
- Risk-based prioritization

---

## 🏗️ Architecture
```
Threat Intelligence Feed
|
Cloud Logs (AWS | Azure | GCP)
|
IOC Correlation Engine
|
Risk Scoring Engine
|
Enriched IOC Dataset & Risk Report
```
---

## ⚙️ Features
- Threat feed ingestion (CSV)
- AWS, Azure, GCP log analysis (simulated)
- IOC correlation using Pandas
- Risk score calculation
- Security reporting

---

## 🛠️ Technologies Used
- Python 3
- Pandas
- Requests
- AWS S3 (simulated)
- Azure Blob Storage (simulated)
- GCP Cloud Storage (simulated)

---

## 📂 Project Structure
```
cross-cloud-threat-intel/
├── data/
│ ├── threat_feed.csv
│ ├── aws_logs.csv
│ ├── azure_logs.csv
│ └── gcp_logs.csv
│
├── src/
│ ├── ingest.py
│ ├── correlate.py
│ ├── risk.py
│ └── main.py
│
├── output/
│ ├── enriched_iocs.csv
│ └── risk_report.txt
│
├── requirements.txt
└── README.md
```
---


## 🚀 How to Run the Project
```bash
pip install -r requirements.txt
python src/main.py
```
📊 Output
```
enriched_iocs.csv
Correlated IOCs with severity, confidence, and risk score.

risk_report.txt
Human-readable report highlighting high-risk threats.
```
---
🔐 Use Cases
```
SOC Analyst threat triage

Cloud security monitoring

Threat intelligence correlation

Cybersecurity learning & portfolio demonstration
```
---
👩‍💻 Author
```
Ruchi Kumari Singh
Cybersecurity Enthusiast | Cloud Security | SOC Operations
```
---










