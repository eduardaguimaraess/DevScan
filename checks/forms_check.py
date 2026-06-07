from bs4 import BeautifulSoup
from checks.base_check import BaseCheck
from models.vulnerability import Vulnerability
from decorators.execution_logger import execution_logger
from decorators.register_check import register_check

@register_check
class FormsCheck(BaseCheck):

    def __init__(self):
        self.name = "Forms Check"
        self.category = "Form Security"

    @execution_logger
    def run(self, response):

        if response is None:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")

        if not forms:
            return None

        vulnerabilities = []

        for form in forms:

            method = form.get("method", "GET").upper()
            action = form.get("action", "")

            if method == "GET":

                vulnerabilities.append(
                    "Form using GET method"
                )

            if action.startswith("http://"):

                vulnerabilities.append(
                    "Form submitting over insecure HTTP"
                )

        if vulnerabilities:

            return Vulnerability(
                title="Insecure Forms Detected",
                severity="MEDIUM",
                description=", ".join(vulnerabilities),
                recommendation="Use POST methods and HTTPS forms."
            )

        return None