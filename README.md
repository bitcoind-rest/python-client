# swagger-client
The REST API can be enabled with the `-rest` option. The interface runs on the same port as the JSON-RPC interface, by default port `8332` for **mainnet**, port `18332` for **testnet**, and port `18443` for **regtest**.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.16
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.BlockApi()
block_hash = 'block_hash_example' # str | the block hash

try:
    # Get block by hash.
    api_response = api_instance.rest_block_extended(block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->rest_block_extended: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:3000/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BlockApi* | [**rest_block_extended**](docs/BlockApi.md#rest_block_extended) | **GET** /block/{blockHash} | Get block by hash.
*BlockApi* | [**rest_block_notxdetails**](docs/BlockApi.md#rest_block_notxdetails) | **GET** /block/notxdetails/{blockHash}.{format} | Get block by hash.
*ChainApi* | [**rest_chaininfo**](docs/ChainApi.md#rest_chaininfo) | **GET** /chaininfo.json | Returns various state info regarding block chain processing.
*MemoryPoolApi* | [**rest_getutxos**](docs/MemoryPoolApi.md#rest_getutxos) | **GET** /getutxos/checkmempool/{txHash}-{txOutput}.{format} | Returns Unspent Transaction (TX) Outputs
*MemoryPoolApi* | [**rest_headers**](docs/MemoryPoolApi.md#rest_headers) | **GET** /headers/{headerCount}/{blockHash}.{format} | Returns headers.
*MemoryPoolApi* | [**rest_mempool_contents**](docs/MemoryPoolApi.md#rest_mempool_contents) | **GET** /mempool/contents.json | Returns transactions in the TX mempool.
*MemoryPoolApi* | [**rest_mempool_info**](docs/MemoryPoolApi.md#rest_mempool_info) | **GET** /mempool/info.json | Returns various information about the TX mempool.
*TransactionApi* | [**rest_tx**](docs/TransactionApi.md#rest_tx) | **GET** /tx/{txHash} | Get transaction by hash.


## Documentation For Models

 - [BIP](docs/BIP.md)
 - [BIP9](docs/BIP9.md)
 - [BIPReject](docs/BIPReject.md)
 - [Block](docs/Block.md)
 - [ChainInfo](docs/ChainInfo.md)
 - [ChainInfoBip9Softforks](docs/ChainInfoBip9Softforks.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponseDefault](docs/InlineResponseDefault.md)
 - [MemoryPool](docs/MemoryPool.md)
 - [ScriptPubKey](docs/ScriptPubKey.md)
 - [Transaction](docs/Transaction.md)
 - [UTxO](docs/UTxO.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

johan@lepetitbloc.net

