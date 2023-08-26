from . import exceptions


class ApiWrapper:
    def __init__(self, connection, resources):
        self.connection = connection
        self.resources = resources

    def __getattr__(self, name):
        try:
            return self.resources[name]
        except KeyError:
            raise AttributeError(f'ApiWrapper object has no attribute {name}')
