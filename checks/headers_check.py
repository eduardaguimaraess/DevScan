from checks.base_check import BaseCheck
from models.vulnerability import Vulnerability
from decorators.execution_logger import execution_logger
from decorators.register_check import register_check

@register_check
class HeadersCheck(BaseCheck):

    def __init__(self):
        self.name = "Headers Check"
        self.category = "Headers Security"

    @execution_logger
    def run(self, response):

        if response is None:
            return Vulnerability(
                title="Connection Error",
                severity="HIGH",
                description="Failed to connect to the target website.",
                recommendation="Check if the website is online."
            )

        required_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "Strict-Transport-Security"
        ]

        missing_headers = []

        for header in required_headers:

            if header not in response.headers:
                missing_headers.append(header)

        if missing_headers:

            return Vulnerability(
                title="Missing Security Headers",
                severity="MEDIUM",
                description=f"Missing headers: {', '.join(missing_headers)}",
                recommendation="Configure the missing security headers."
            )

        return None