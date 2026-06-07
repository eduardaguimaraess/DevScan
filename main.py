from core.scanner import Scanner
from checks.https_check import HTTPSCheck
from reports.console_report import ConsoleReport
from checks.headers_check import HeadersCheck
from checks.server_check import ServerCheck
from checks.forms_check import FormsCheck
from reports.json_report import JSONReport
import argparse

parser = argparse.ArgumentParser(
    description="DevScan - Web Vulnerability Scanner"
)

parser.add_argument(
    "--url",
    required=True,
    help="Target URL"
)

parser.add_argument(
    "--json",
    action="store_true",
    help="Generate JSON report"
)

args = parser.parse_args()

url = args.url

scanner = Scanner(url)

scanner.load_checks()

results = scanner.run()

report = ConsoleReport()
report.display(results)

if args.json:

    json_report = JSONReport()
    json_report.generate(results)