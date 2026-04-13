def analyze(log):
    if log["priority"] == "low":
        return "Normal usage"
    return "Attention needed"