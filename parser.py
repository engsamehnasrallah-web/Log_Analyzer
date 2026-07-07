import os

def load_logs(log_file_path: str = "sample_logs/auth.log") -> list[str]:
    if not os.path.exists(log_file_path):
        raise FileNotFoundError("Error: Log file not found.")

    with open(log_file_path, "r", encoding="utf-8") as file:
        return file.readlines()