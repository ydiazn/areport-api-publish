from unittest import TestCase
from unittest.mock import Mock, patch

from wrapi import client, exceptions


class RequestsClient(TestCase):
    def test_dispatch(self):
        base_url = 'http://api.com'
        resource_path = '/report'
        full_url = f'{base_url}{resource_path}'
        kwargs = {'some_parram': 5}
        session = Mock()
        expected_response = Mock()
        session.get.return_value = expected_response

        client_obj = client.RequestsClient(base_url, session)
        response = client_obj.dispatch(resource_path, 'get', **kwargs)

        self.assertEqual(response, expected_response)
        session.get.called_once_with(full_url, **kwargs)

    def test_unsupported_method(self):
        session = Mock()
        session.unknow_method = Mock(
            side_effect=exceptions.UsupportedMethodException)

        client_obj = client.RequestsClient('http://api.com', session)

        with self.assertRaises(exceptions.UsupportedMethodException):
            client_obj.dispatch('/resource', 'unknow_method')
