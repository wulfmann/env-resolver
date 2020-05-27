# ENV Resolver (Node)

![](https://github.com/wulfmann/env-resolver/workflows/Node%20CI/badge.svg)

This is a small utility to resolve [SSM Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) and [Secretsmanager Secrets](https://aws.amazon.com/secrets-manager/) and conditionally set them in the environment.

This is helpful for services like [AWS Batch](https://aws.amazon.com/batch/) or [AWS Lambda](https://aws.amazon.com/lambda/) where there is not a way natively to pass secret values.

## Install

```bash
npm install env-resolver
```

This package assumes that you already depend on [aws-cdk](https://github.com/aws/aws-cdk) and have it installed as a dependency of your project. If you are using this package in [AWS Lambda](https://aws.amazon.com/lambda/), `aws-cdk` will already be available.
