from analyzer import analyze_logs
from parser import load_logs
from report import print_report


logs = load_logs()
results = analyze_logs(logs)
print_report(results)