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

from swagger_client.models.transaction import Transaction  # noqa: F401,E501


class Block(object):
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
        'hash': 'str',
        'confirmations': 'int',
        'strippedsize': 'int',
        'size': 'int',
        'weight': 'int',
        'height': 'int',
        'version': 'int',
        'version_hex': 'str',
        'merkleroot': 'str',
        'tx': 'list[Transaction]',
        'time': 'int',
        'mediantime': 'int',
        'nonce': 'int',
        'bits': 'str',
        'difficulty': 'float',
        'chainwork': 'str'
    }

    attribute_map = {
        'hash': 'hash',
        'confirmations': 'confirmations',
        'strippedsize': 'strippedsize',
        'size': 'size',
        'weight': 'weight',
        'height': 'height',
        'version': 'version',
        'version_hex': 'versionHex',
        'merkleroot': 'merkleroot',
        'tx': 'tx',
        'time': 'time',
        'mediantime': 'mediantime',
        'nonce': 'nonce',
        'bits': 'bits',
        'difficulty': 'difficulty',
        'chainwork': 'chainwork'
    }

    def __init__(self, hash=None, confirmations=None, strippedsize=None, size=None, weight=None, height=None, version=None, version_hex=None, merkleroot=None, tx=None, time=None, mediantime=None, nonce=None, bits=None, difficulty=None, chainwork=None):  # noqa: E501
        """Block - a model defined in Swagger"""  # noqa: E501

        self._hash = None
        self._confirmations = None
        self._strippedsize = None
        self._size = None
        self._weight = None
        self._height = None
        self._version = None
        self._version_hex = None
        self._merkleroot = None
        self._tx = None
        self._time = None
        self._mediantime = None
        self._nonce = None
        self._bits = None
        self._difficulty = None
        self._chainwork = None
        self.discriminator = None

        if hash is not None:
            self.hash = hash
        if confirmations is not None:
            self.confirmations = confirmations
        if strippedsize is not None:
            self.strippedsize = strippedsize
        if size is not None:
            self.size = size
        if weight is not None:
            self.weight = weight
        if height is not None:
            self.height = height
        if version is not None:
            self.version = version
        if version_hex is not None:
            self.version_hex = version_hex
        if merkleroot is not None:
            self.merkleroot = merkleroot
        if tx is not None:
            self.tx = tx
        if time is not None:
            self.time = time
        if mediantime is not None:
            self.mediantime = mediantime
        if nonce is not None:
            self.nonce = nonce
        if bits is not None:
            self.bits = bits
        if difficulty is not None:
            self.difficulty = difficulty
        if chainwork is not None:
            self.chainwork = chainwork

    @property
    def hash(self):
        """Gets the hash of this Block.  # noqa: E501

        The block hash  # noqa: E501

        :return: The hash of this Block.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Block.

        The block hash  # noqa: E501

        :param hash: The hash of this Block.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def confirmations(self):
        """Gets the confirmations of this Block.  # noqa: E501

        The number of confirmations  # noqa: E501

        :return: The confirmations of this Block.  # noqa: E501
        :rtype: int
        """
        return self._confirmations

    @confirmations.setter
    def confirmations(self, confirmations):
        """Sets the confirmations of this Block.

        The number of confirmations  # noqa: E501

        :param confirmations: The confirmations of this Block.  # noqa: E501
        :type: int
        """

        self._confirmations = confirmations

    @property
    def strippedsize(self):
        """Gets the strippedsize of this Block.  # noqa: E501

        The block stripped size  # noqa: E501

        :return: The strippedsize of this Block.  # noqa: E501
        :rtype: int
        """
        return self._strippedsize

    @strippedsize.setter
    def strippedsize(self, strippedsize):
        """Sets the strippedsize of this Block.

        The block stripped size  # noqa: E501

        :param strippedsize: The strippedsize of this Block.  # noqa: E501
        :type: int
        """

        self._strippedsize = strippedsize

    @property
    def size(self):
        """Gets the size of this Block.  # noqa: E501

        The block size  # noqa: E501

        :return: The size of this Block.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Block.

        The block size  # noqa: E501

        :param size: The size of this Block.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def weight(self):
        """Gets the weight of this Block.  # noqa: E501

        The block weight  # noqa: E501

        :return: The weight of this Block.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Block.

        The block weight  # noqa: E501

        :param weight: The weight of this Block.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def height(self):
        """Gets the height of this Block.  # noqa: E501

        The block height (or index)  # noqa: E501

        :return: The height of this Block.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Block.

        The block height (or index)  # noqa: E501

        :param height: The height of this Block.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def version(self):
        """Gets the version of this Block.  # noqa: E501

        The block version  # noqa: E501

        :return: The version of this Block.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Block.

        The block version  # noqa: E501

        :param version: The version of this Block.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def version_hex(self):
        """Gets the version_hex of this Block.  # noqa: E501

        The block version (in hex)  # noqa: E501

        :return: The version_hex of this Block.  # noqa: E501
        :rtype: str
        """
        return self._version_hex

    @version_hex.setter
    def version_hex(self, version_hex):
        """Sets the version_hex of this Block.

        The block version (in hex)  # noqa: E501

        :param version_hex: The version_hex of this Block.  # noqa: E501
        :type: str
        """

        self._version_hex = version_hex

    @property
    def merkleroot(self):
        """Gets the merkleroot of this Block.  # noqa: E501

        The block merkle root  # noqa: E501

        :return: The merkleroot of this Block.  # noqa: E501
        :rtype: str
        """
        return self._merkleroot

    @merkleroot.setter
    def merkleroot(self, merkleroot):
        """Sets the merkleroot of this Block.

        The block merkle root  # noqa: E501

        :param merkleroot: The merkleroot of this Block.  # noqa: E501
        :type: str
        """

        self._merkleroot = merkleroot

    @property
    def tx(self):
        """Gets the tx of this Block.  # noqa: E501

        The list of transactions in the block  # noqa: E501

        :return: The tx of this Block.  # noqa: E501
        :rtype: list[Transaction]
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """Sets the tx of this Block.

        The list of transactions in the block  # noqa: E501

        :param tx: The tx of this Block.  # noqa: E501
        :type: list[Transaction]
        """

        self._tx = tx

    @property
    def time(self):
        """Gets the time of this Block.  # noqa: E501

        The block time  # noqa: E501

        :return: The time of this Block.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Block.

        The block time  # noqa: E501

        :param time: The time of this Block.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def mediantime(self):
        """Gets the mediantime of this Block.  # noqa: E501

        The block median time  # noqa: E501

        :return: The mediantime of this Block.  # noqa: E501
        :rtype: int
        """
        return self._mediantime

    @mediantime.setter
    def mediantime(self, mediantime):
        """Sets the mediantime of this Block.

        The block median time  # noqa: E501

        :param mediantime: The mediantime of this Block.  # noqa: E501
        :type: int
        """

        self._mediantime = mediantime

    @property
    def nonce(self):
        """Gets the nonce of this Block.  # noqa: E501

        The block nonce  # noqa: E501

        :return: The nonce of this Block.  # noqa: E501
        :rtype: int
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this Block.

        The block nonce  # noqa: E501

        :param nonce: The nonce of this Block.  # noqa: E501
        :type: int
        """

        self._nonce = nonce

    @property
    def bits(self):
        """Gets the bits of this Block.  # noqa: E501


        :return: The bits of this Block.  # noqa: E501
        :rtype: str
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this Block.


        :param bits: The bits of this Block.  # noqa: E501
        :type: str
        """

        self._bits = bits

    @property
    def difficulty(self):
        """Gets the difficulty of this Block.  # noqa: E501


        :return: The difficulty of this Block.  # noqa: E501
        :rtype: float
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        """Sets the difficulty of this Block.


        :param difficulty: The difficulty of this Block.  # noqa: E501
        :type: float
        """

        self._difficulty = difficulty

    @property
    def chainwork(self):
        """Gets the chainwork of this Block.  # noqa: E501


        :return: The chainwork of this Block.  # noqa: E501
        :rtype: str
        """
        return self._chainwork

    @chainwork.setter
    def chainwork(self, chainwork):
        """Sets the chainwork of this Block.


        :param chainwork: The chainwork of this Block.  # noqa: E501
        :type: str
        """

        self._chainwork = chainwork

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
        if not isinstance(other, Block):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other