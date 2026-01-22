def correlate_iocs(logs, threats):
    """
    Match cloud log IPs with threat intelligence IOCs
    """
    return logs.merge(
        threats,
        left_on="source_ip",
        right_on="ioc",
        how="inner"
    )
