from datetime import datetime, timezone

def format_timestamp(epoch_ts):
    return datetime.fromtimestamp(epoch_ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
