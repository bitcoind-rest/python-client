# coding: utf-8

"""
    Bitcoind

    The REST API can be enabled with the `-rest` option. The interface runs on the same port as the JSON-RPC interface, by default port `8332` for **mainnet**, port `18332` for **testnet**, and port `18443` for **regtest**.  # noqa: E501

    OpenAPI spec version: 0.16
    Contact: johan@lepetitbloc.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MemoryPool(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'size': 'int',
        'bytes': 'int',
        'usage': 'int',
        'maxmempool': 'int',
        'mempoolminfee': 'float',
        'minrelaytxfee': 'float'
    }

    attribute_map = {
        'size': 'size',
        'bytes': 'bytes',
        'usage': 'usage',
        'maxmempool': 'maxmempool',
        'mempoolminfee': 'mempoolminfee',
        'minrelaytxfee': 'minrelaytxfee'
    }

    def __init__(self, size=None, bytes=None, usage=None, maxmempool=None, mempoolminfee=None, minrelaytxfee=None):  # noqa: E501
        """MemoryPool - a model defined in Swagger"""  # noqa: E501

        self._size = None
        self._bytes = None
        self._usage = None
        self._maxmempool = None
        self._mempoolminfee = None
        self._minrelaytxfee = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if bytes is not None:
            self.bytes = bytes
        if usage is not None:
            self.usage = usage
        if maxmempool is not None:
            self.maxmempool = maxmempool
        if mempoolminfee is not None:
            self.mempoolminfee = mempoolminfee
        if minrelaytxfee is not None:
            self.minrelaytxfee = minrelaytxfee

    @property
    def size(self):
        """Gets the size of this MemoryPool.  # noqa: E501

        the number of transactions in the TX mempool  # noqa: E501

        :return: The size of this MemoryPool.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MemoryPool.

        the number of transactions in the TX mempool  # noqa: E501

        :param size: The size of this MemoryPool.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def bytes(self):
        """Gets the bytes of this MemoryPool.  # noqa: E501

        size of the TX mempool in bytes  # noqa: E501

        :return: The bytes of this MemoryPool.  # noqa: E501
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this MemoryPool.

        size of the TX mempool in bytes  # noqa: E501

        :param bytes: The bytes of this MemoryPool.  # noqa: E501
        :type: int
        """

        self._bytes = bytes

    @property
    def usage(self):
        """Gets the usage of this MemoryPool.  # noqa: E501

        total TX mempool memory usage  # noqa: E501

        :return: The usage of this MemoryPool.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this MemoryPool.

        total TX mempool memory usage  # noqa: E501

        :param usage: The usage of this MemoryPool.  # noqa: E501
        :type: int
        """

        self._usage = usage

    @property
    def maxmempool(self):
        """Gets the maxmempool of this MemoryPool.  # noqa: E501

        maximum memory usage for the mempool in bytes  # noqa: E501

        :return: The maxmempool of this MemoryPool.  # noqa: E501
        :rtype: int
        """
        return self._maxmempool

    @maxmempool.setter
    def maxmempool(self, maxmempool):
        """Sets the maxmempool of this MemoryPool.

        maximum memory usage for the mempool in bytes  # noqa: E501

        :param maxmempool: The maxmempool of this MemoryPool.  # noqa: E501
        :type: int
        """

        self._maxmempool = maxmempool

    @property
    def mempoolminfee(self):
        """Gets the mempoolminfee of this MemoryPool.  # noqa: E501

        minimum feerate (BTC per KB) for tx to be accepted  # noqa: E501

        :return: The mempoolminfee of this MemoryPool.  # noqa: E501
        :rtype: float
        """
        return self._mempoolminfee

    @mempoolminfee.setter
    def mempoolminfee(self, mempoolminfee):
        """Sets the mempoolminfee of this MemoryPool.

        minimum feerate (BTC per KB) for tx to be accepted  # noqa: E501

        :param mempoolminfee: The mempoolminfee of this MemoryPool.  # noqa: E501
        :type: float
        """

        self._mempoolminfee = mempoolminfee

    @property
    def minrelaytxfee(self):
        """Gets the minrelaytxfee of this MemoryPool.  # noqa: E501


        :return: The minrelaytxfee of this MemoryPool.  # noqa: E501
        :rtype: float
        """
        return self._minrelaytxfee

    @minrelaytxfee.setter
    def minrelaytxfee(self, minrelaytxfee):
        """Sets the minrelaytxfee of this MemoryPool.


        :param minrelaytxfee: The minrelaytxfee of this MemoryPool.  # noqa: E501
        :type: float
        """

        self._minrelaytxfee = minrelaytxfee

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MemoryPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
