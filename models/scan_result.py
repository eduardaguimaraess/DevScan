class ScanResult:

    def __init__(self):

        self.vulnerabilities = []
        self.total_checks = 0
        self.security_score = 100

    def add_vulnerability(self, vulnerability):

        self.vulnerabilities.append(vulnerability)

    def calculate_score(self):

        for vulnerability in self.vulnerabilities:

            if vulnerability.severity == "HIGH":
                self.security_score -= 30

            elif vulnerability.severity == "MEDIUM":
                self.security_score -= 15

            elif vulnerability.severity == "LOW":
                self.security_score -= 5

        if self.security_score < 0:
            self.security_score = 0