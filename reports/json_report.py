import json


class JSONReport:

    def generate(self, scan_result):

        data = {
            "security_score": scan_result.security_score,
            "total_checks": scan_result.total_checks,
            "vulnerabilities": []
        }

        for vulnerability in scan_result.vulnerabilities:

            data["vulnerabilities"].append({
                "title": vulnerability.title,
                "severity": vulnerability.severity,
                "description": vulnerability.description,
                "recommendation": vulnerability.recommendation
            })

        with open("report.json", "w") as file:

            json.dump(data, file, indent=4)