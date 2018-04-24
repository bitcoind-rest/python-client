# swagger_client.ChainApi

All URIs are relative to *http://localhost:3000/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_chaininfo**](ChainApi.md#rest_chaininfo) | **GET** /chaininfo.json | Returns various state info regarding block chain processing.


# **rest_chaininfo**
> ChainInfo rest_chaininfo()

Returns various state info regarding block chain processing.

Returns various state info regarding block chain processing. Only supports JSON as output format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChainApi()

try:
    # Returns various state info regarding block chain processing.
    api_response = api_instance.rest_chaininfo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainApi->rest_chaininfo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ChainInfo**](ChainInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

