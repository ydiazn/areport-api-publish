from unittest import TestCase
from unittest.mock import Mock


from wrapi.wrapper import ApiWrapper


class ResourceTest(TestCase):
    def test_call(self):
        expected_response = Mock()
        client = Mock()
        resource = Mock(return_value=expected_response)
        kwargs = {'some_parram': 5}

        api = ApiWrapper(client, {
            'create_report': resource
        })

        response = api.create_report(**kwargs)

        resource.called_once_with(**kwargs)
        self.assertEqual(expected_response, response)

    def test_resource_unavailablecall(self):
        client = Mock()
        api = ApiWrapper(client, {})

        with self.assertRaises(AttributeError):
            api.create_report()
