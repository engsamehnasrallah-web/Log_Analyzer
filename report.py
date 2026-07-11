from models import AnalysisResults

def print_report(results: AnalysisResults) -> None:
    print("=" * 40)
    print("              SEC Log Analyzer")
    print("=" * 40)
    print()
    print("✓ Log file loaded successfully.")
    print(f"Total Log Entries       : {results.total}")
    print(f"Failed Login Attempts   : {results.failed}")
    print(f"Successful Logins       : {results.accepted}")

    events = results.events
    for event in events:
        print(f"User: {event.username}, IP Address: {event.ip}, Status: {event.status}")
