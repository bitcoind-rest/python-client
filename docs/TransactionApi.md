# swagger_client.TransactionApi

All URIs are relative to *http://localhost:3000/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_tx**](TransactionApi.md#rest_tx) | **GET** /tx/{txHash} | Get transaction by hash.


# **rest_tx**
> Transaction rest_tx(tx_hash)

Get transaction by hash.

Given a transaction hash: returns a transaction in binary, hex-encoded binary, or JSON formats. For full TX query capability, one must enable the transaction index via txindex=1 command line / configuration option.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionApi()
tx_hash = 'tx_hash_example' # str | The transaction hash.

try:
    # Get transaction by hash.
    api_response = api_instance.rest_tx(tx_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->rest_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_hash** | **str**| The transaction hash. | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

