from core.request_handler import RequestHandler
from models.scan_result import ScanResult
from utils.check_registry import registered_checks

class Scanner:

    def __init__(self, url):
        self.url = url
        self.checks = []
        self.request_handler = RequestHandler()

    def add_check(self, check):
        self.checks.append(check)

    def run(self):
        
        scan_result = ScanResult()
        
        response = self.request_handler.fetch(self.url)

        for check in self.checks:
            result = check.run(response)
            scan_result.total_checks += 1
            if result:
                scan_result.add_vulnerability(result)
        
        scan_result.calculate_score()

        return scan_result
    
    def load_checks(self):

        for check_class in registered_checks:

            try:
                check = check_class(self.url)
            except TypeError:
                check = check_class()
            self.add_check(check)