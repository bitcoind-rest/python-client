# coding: utf-8

"""
    Bitcoind

    The REST API can be enabled with the `-rest` option. The interface runs on the same port as the JSON-RPC interface, by default port `8332` for **mainnet**, port `18332` for **testnet**, and port `18443` for **regtest**.  # noqa: E501

    OpenAPI spec version: 0.16
    Contact: johan@lepetitbloc.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Bitcoind",
    author_email="johan@lepetitbloc.net",
    url="",
    keywords=["Swagger", "Bitcoind"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The REST API can be enabled with the &#x60;-rest&#x60; option. The interface runs on the same port as the JSON-RPC interface, by default port &#x60;8332&#x60; for **mainnet**, port &#x60;18332&#x60; for **testnet**, and port &#x60;18443&#x60; for **regtest**.  # noqa: E501
    """
)
