from checks.base_check import BaseCheck
from models.vulnerability import Vulnerability
from decorators.execution_logger import execution_logger
from decorators.register_check import register_check

@register_check
class ServerCheck(BaseCheck):

    def __init__(self):
        self.name = "Server Check"
        self.category = "Information Disclosure"

    @execution_logger
    def run(self, response):

        if response is None:
            return None

        exposed_headers = []

        if "Server" in response.headers:
            exposed_headers.append(
                f"Server: {response.headers['Server']}"
            )

        if "X-Powered-By" in response.headers:
            exposed_headers.append(
                f"X-Powered-By: {response.headers['X-Powered-By']}"
            )

        if exposed_headers:

            return Vulnerability(
                title="Server Information Exposure",
                severity="LOW",
                description=f"Exposed technologies: {', '.join(exposed_headers)}",
                recommendation="Hide server and framework version headers."
            )

        return None