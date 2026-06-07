from colorama import Fore, Style, init

init(autoreset=True)


class ConsoleReport:

    def display(self, scan_result):

        print(Fore.CYAN + "\n=== DEVSCAN REPORT ===\n")

        print(Fore.YELLOW +
              f"Security Score: {scan_result.security_score}/100")

        print(Fore.YELLOW +
              f"Total Checks: {scan_result.total_checks}\n")

        if not scan_result.vulnerabilities:

            print(Fore.GREEN + "[OK] No vulnerabilities found.")
            return

        for vulnerability in scan_result.vulnerabilities:

            color = Fore.WHITE

            if vulnerability.severity == "HIGH":
                color = Fore.RED

            elif vulnerability.severity == "MEDIUM":
                color = Fore.YELLOW

            elif vulnerability.severity == "LOW":
                color = Fore.BLUE

            print(
                color +
                f"[{vulnerability.severity}] {vulnerability.title}"
            )

            print(
                Style.RESET_ALL +
                f"Description: {vulnerability.description}"
            )

            print(
                f"Recommendation: {vulnerability.recommendation}"
            )

            print()