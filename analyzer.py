import re
from models import LoginEvent
from models import AnalysisResults


LOG_PATTERN = r"for (\w+) from ([\d.]+)"


def analyze_logs(log_entries: list[str]) -> AnalysisResults:
    accepted_counter = 0
    failed_counter = 0
    events: list[LoginEvent] = []

    for line in log_entries:
        status = None

        if "Failed password" in line:
            failed_counter += 1
            status = "failed"

        elif "Accepted password" in line:
            accepted_counter += 1
            status = "accepted"

        if status:
            match = re.search(LOG_PATTERN, line)

            if match:
                user = match.group(1)
                ip_address = match.group(2)
                events.append(LoginEvent(username=user, ip=ip_address, status=status))

    return AnalysisResults(
        total=len(log_entries),
        failed=failed_counter,
        accepted=accepted_counter,
        events=events
    )
