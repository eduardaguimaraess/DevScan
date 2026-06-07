from checks.base_check import BaseCheck
from models.vulnerability import Vulnerability
from decorators.execution_logger import execution_logger
from decorators.register_check import register_check

@register_check
class HTTPSCheck(BaseCheck):

    def __init__(self, url):
        self.url = url
        self.name = "HTTPS Check"
        self.category = "Transport Security"
        
    @execution_logger   
    def run(self, response):

        if self.url.startswith("https://"):
            return None

        return Vulnerability(
            title="HTTPS Not Enabled",
            severity="HIGH",
            description="The website is not using HTTPS encryption.",
            recommendation="Enable HTTPS to protect data transmission."
        )