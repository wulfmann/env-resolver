# ENV Resolver (Python)

![](https://github.com/wulfmann/env-resolver/workflows/Python%20CI/badge.svg)

This is a small utility to resolve [SSM Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) and [Secretsmanager Secrets](https://aws.amazon.com/secrets-manager/) and conditionally set them in the environment.

This is helpful for services like [AWS Batch](https://aws.amazon.com/batch/) or [AWS Lambda](https://aws.amazon.com/lambda/) where there is not a way natively to pass secret values.

## Install

```bash
pip install env-resolver
```

This package assumes that you already depend on [boto3](https://github.com/boto/boto3) and have it installed as a dependency of your project. If you are using this package in [AWS Lambda](https://aws.amazon.com/lambda/), `boto3` will already be available.

## Quick Start

### Parameter Store

```python
from parameter_resolver import resolve

# assuming you've created two parameters:
# ssm/parameter/env-one = val-one
# ssm/parameter/env-two = val-two

parameters = {
    'ENV_ONE': 'ssm/parameter/env-one',
    'ENV_TWO': 'ssm/parameter/env-two'
}

print(resolve('ssm', parameters))

# Outputs:
# {
#     'ENV_ONE': 'val-one',
#     'ENV_TWO': 'val-two'
# }
```

### Secrets Manager

```python
from parameter_resolver import resolve

# assuming you've created the following secret:
# secret/secret-one =
# {
#     'ENV_ONE': 'val-one',
#     'ENV_TWO': 'val-two'
# }

secret = {
    'secret_id': 'secret/secret-one'
}

print(resolve('secretsmanager', secret))

# Outputs:
# {
#     'ENV_ONE': 'val-one',
#     'ENV_TWO': 'val-two'
# }
```

## Usage

```text
resolve(parameter_type, parameter_value, set_environment_variables=True)
```

These are the possible values for `parameter_type`:

* ssm
* secretsmanager

## Options

The `set_environment_variables` options allows you to choose whether or not to set the new `key-value` pairs in the environment.

### SSM

For a parameter store parameter, `resolve` expects the `parameter_value` to be a dictionary of `KEY`: `PARAMETER_NAME`.

### Secretsmanager

For a secretsmanager secret, `resolve` expects the `parameter_value` to be a dictionary with the following possible values:

```python
secret = {
    'secret_id': 'string',
    'version_id': 'string', # optional
    'json_value': 'boolean' # option, default=True
}
```

## Contributing

PR's are welcome!

This project uses [Poetry](https://python-poetry.org/) for dependency / environment management.

### Install Dependencies

```bash
poetry install
```

### Tests

```bash
poetry run pytest
```
