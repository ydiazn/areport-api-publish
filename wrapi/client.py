from . import exceptions


class RequestsClient:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    def dispatch(self, url, method, **kwargs):
        try:
            method_func = getattr(self.session, method)
        except AttributeError:
            raise exceptions.UsupportedMethodException

        return method_func(url, **kwargs)
