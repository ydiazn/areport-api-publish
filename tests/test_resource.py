from unittest import TestCase
from unittest.mock import Mock, patch

from wrapi.resource import Resource


class ResourceTest(TestCase):
    def test_simple_get(self):
        expected_response = Mock()
        client = Mock()
        client.dispatch.return_value = expected_response
        map_data = {'another_param': 5}
        mapping = Mock(return_value=map_data)
        resource_path = '/report'
        params = {'some_param': 5}

        resource = Resource(client, 'get', resource_path, mapping)
        response = resource(**params)

        mapping.assert_called_once_with(**params)
        client.dispatch.get.called_once_with(resource_path, 'get', **map_data)
        self.assertEqual(response, expected_response)

    def test_simple_get(self):
        expected_response = Mock()
        client = Mock()
        client.dispatch.return_value = expected_response
        resource_path = '/report/{}'
        resource_url = '/report/5'
        kwargs = {'some_param': 'some'}
        mapping = Mock(return_value=kwargs)

        resource = Resource(client, 'get', resource_path, mapping)
        response = resource(25, **kwargs)

        client.dispatch.get.called_once_with(resource_url, 'get', **kwargs)
        self.assertEqual(response, expected_response)
