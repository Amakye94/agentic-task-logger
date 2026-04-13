import datetime

def process_event(event: str):
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "event": event,
        "priority": "low" if event == "button_click" else "high",
        "agent_comment": "User interaction recorded"
    }