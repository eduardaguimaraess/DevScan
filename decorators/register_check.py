from utils.check_registry import registered_checks

def register_check(cls):

    registered_checks.append(cls)

    return cls