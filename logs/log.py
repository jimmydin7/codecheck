import datetime

def create_log(logtype, msg):
    current = datetime.datetime.now()
    if logtype == "error":
        return f"({current})[ERROR] - {msg}"
    elif logtype == "info":
        return f"({current})[INFO] - {msg}"
    elif logtype == "warning":
        return f"({current})[WARNING] - {msg}"
    else:
        return f"({current})[UNKNOWN] - {msg}"