from dataclasses import dataclass

@dataclass
class LoginEvent:
    username: str
    ip: str
    status: str

@dataclass
class AnalysisResults:
    total: int
    failed: int
    accepted: int
    events: list[LoginEvent]