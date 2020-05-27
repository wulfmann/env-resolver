import os, json
from unittest.mock import patch, call
from unittest import TestCase

from env_resolver.main import resolve

class MainTest(TestCase):

    def setUp(self):
        self.original_env = os.environ
        os.environ = {}

    def tearDown(self):
        os.environ = self.original_env


    @patch('boto3.client')
    def test_ssm_resolve(self, mock_client):
        mock_client.return_value.get_parameters.side_effect = [
            {
                'Parameters': [
                    {
                        'Name': 'test.one',
                        'Value': 'value_one'
                    },
                    {
                        'Name': 'test.two',
                        'Value': 'value_two'
                    }
                ]
            }
        ]

        os.environ = {
            'TEST_ONE': 'test.one',
            'TEST_TWO': 'test.two'
        }

        result = resolve('ssm', os.environ)

        assert {'TEST_ONE': 'value_one', 'TEST_TWO': 'value_two'} == result

        assert [
            call('ssm'),
            call().get_parameters(
                Names=[
                    'test.one',
                    'test.two'
                ],
                WithDecryption=True
            )
        ] == mock_client.mock_calls

    @patch('boto3.client')
    def test_secretsmanager_resolve(self, mock_client):
        mock_client.return_value.get_secret_value.side_effect = [
            {
                'SecretString': json.dumps({
                    'TEST_ONE': 'value_one',
                    'TEST_TWO': 'value_two'
                })
            }
        ]

        secret = { 'secret_id': 'secret/one' }

        result = resolve('secretsmanager', secret)

        assert {'TEST_ONE': 'value_one', 'TEST_TWO': 'value_two'} == result

        assert [
            call('secretsmanager'),
            call().get_secret_value(
                SecretId='secret/one'
            )
        ] == mock_client.mock_calls

    @patch('boto3.client')
    def test_secretsmanager_resolve_with_version_id(self, mock_client):
        mock_client.return_value.get_secret_value.side_effect = [
            {
                'SecretString': json.dumps({
                    'TEST_ONE': 'value_one',
                    'TEST_TWO': 'value_two'
                })
            }
        ]

        secret = {
            'secret_id': 'secret/one',
            'version_id': '1'
        }

        result = resolve('secretsmanager', secret)

        assert {'TEST_ONE': 'value_one', 'TEST_TWO': 'value_two'} == result

        assert [
            call('secretsmanager'),
            call().get_secret_value(
                SecretId='secret/one',
                VersionId='1'
            )
        ] == mock_client.mock_calls

    @patch('boto3.client')
    def test_secretsmanager_resolve_with_non_json_value(self, mock_client):
        mock_client.return_value.get_secret_value.side_effect = [
            {
                'SecretString': 'non-json-value'
            }
        ]

        secret = {
            'secret_id': 'secret/one',
            'json_value': False
        }

        result = resolve('secretsmanager', secret)

        assert 'non-json-value' == result

        assert [
            call('secretsmanager'),
            call().get_secret_value(
                SecretId='secret/one'
            )
        ] == mock_client.mock_calls
