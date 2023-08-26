from pathlib import Path
from typing import Any

class Resource:
    def __init__(self, client, method, resource, mapping):
        self.client = client
        self.method = method
        self.resource = resource
        self.mapping = mapping

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        url = self.resource.format(*args)
        kwargs = self.mapping(**kwds)

        return self.client.dispatch(url, self.method, **kwargs)
