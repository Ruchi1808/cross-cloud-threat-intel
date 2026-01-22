# 🌐 Cross-Cloud Threat Intelligence Aggregator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Cloud](https://img.shields.io/badge/Cloud-AWS%20|%20Azure%20|%20GCP-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Overview
The **Cross-Cloud Threat Intelligence Aggregator** is a Python-based cybersecurity project that demonstrates how threat intelligence feeds can be correlated with activity logs from multiple cloud platforms to detect malicious behavior and prioritize risks.

This project simulates a **real-world SOC (Security Operations Center) workflow** by unifying threat data and cloud logs into a single detection and risk assessment pipeline.

---

## 🎯 Problem Statement
Organizations use multiple cloud platforms such as AWS, Azure, and GCP.  
Security teams often receive threat intelligence from various sources but lack a unified way to correlate it with cloud activity, leading to delayed detection and poor prioritization.

---

## 💡 Solution
This project provides:
- A unified pipeline to ingest threat intelligence
- Cross-cloud log correlation
- IOC enrichment
- Risk-based prioritization of security incidents

---

## 🏗️ Architecture
Threat Intelligence Feed (CSV)
|
v
Cloud Logs (AWS | Azure | GCP)
|
v
IOC Correlation Engine
|
v
Risk Scoring Engine
|
v
Enriched IOC Dataset & Risk Report


---

## ⚙️ Features
- Ingests threat intelligence feeds (IP & domain IOCs)
- Processes AWS, Azure, and GCP logs (simulated object storage)
- Correlates malicious indicators with cloud activity
- Calculates severity-based risk scores
- Generates enriched datasets and human-readable reports

---

## 🛠️ Technologies Used
- **Python 3**
- **Pandas**
- **Requests**
- **AWS S3** (simulated)
- **Azure Blob Storage** (simulated)
- **GCP Cloud Storage** (simulated)

---

## 📂 Project Structure
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

---

## 🚀 How to Run the Project
```bash
pip install -r requirements.txt
python src/main.py

📊 Output

enriched_iocs.csv
Contains correlated IOCs with severity, confidence, and risk score.

risk_report.txt
A readable report highlighting high-risk threats for prioritization.

🔐 Use Case

SOC Analyst threat triage

Cloud security monitoring

Threat intelligence correlation

Cybersecurity learning & portfolio demonstration

⚠️ Limitations

Cloud log ingestion is simulated (no live credentials used)

Supports IP-based IOC correlation

🔮 Future Enhancements

STIX/TAXII threat feed integration

Real cloud storage ingestion

Dashboard visualization

SIEM integration (Splunk / Sentinel)

👩‍💻 Author

Ruchi Kumari Singh
Cybersecurity Enthusiast | Cloud Security | SOC Operations
