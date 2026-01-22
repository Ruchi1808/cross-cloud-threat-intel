import pandas as pd

def load_threat_feed():
    """Load threat intelligence feed"""
    return pd.read_csv("../data/threat_feed.csv")

def load_cloud_logs():
    """Load AWS, Azure, and GCP logs"""
    aws = pd.read_csv("../data/aws_logs.csv")
    azure = pd.read_csv("../data/azure_logs.csv")
    gcp = pd.read_csv("../data/gcp_logs.csv")

    return pd.concat([aws, azure, gcp], ignore_index=True)
