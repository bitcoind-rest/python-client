# coding: utf-8

"""
    Bitcoind

    The REST API can be enabled with the `-rest` option. The interface runs on the same port as the JSON-RPC interface, by default port `8332` for **mainnet**, port `18332` for **testnet**, and port `18443` for **regtest**.  # noqa: E501

    OpenAPI spec version: 0.16
    Contact: johan@lepetitbloc.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.u_tx_o import UTxO  # noqa: E501
from swagger_client.rest import ApiException


class TestUTxO(unittest.TestCase):
    """UTxO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUTxO(self):
        """Test UTxO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.u_tx_o.UTxO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
