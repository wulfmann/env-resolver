import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="env_resolver",
    version="0.1.0",
    author="Joe Snell | wulfmann",
    author_email="joepsnell@gmail.com",
    description="A utility for resolving ssm parameters and secretsmanager secrets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wulfmann/parameter-resolver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['boto3']
)
