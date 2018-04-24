# swagger_client.BlockApi

All URIs are relative to *http://localhost:3000/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_block_extended**](BlockApi.md#rest_block_extended) | **GET** /block/{blockHash} | Get block by hash.
[**rest_block_notxdetails**](BlockApi.md#rest_block_notxdetails) | **GET** /block/notxdetails/{blockHash}.{format} | Get block by hash.


# **rest_block_extended**
> Block rest_block_extended(block_hash)

Get block by hash.

Given a block hash: returns a block, in binary, hex-encoded binary or JSON formats. The HTTP request and response are both handled entirely in-memory, thus making maximum memory usage at least 2.66MB (1 MB max block, plus hex encoding) per request. With the /notxdetails/ option JSON response will only contain the transaction hash instead of the complete transaction details. The option only affects the JSON response.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**| the block hash | 

### Return type

[**Block**](Block.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_block_notxdetails**
> Block rest_block_notxdetails(block_hash, format)

Get block by hash.

Given a block hash: returns a block, in binary, hex-encoded binary or JSON formats. The HTTP request and response are both handled entirely in-memory, thus making maximum memory usage at least 2.66MB (1 MB max block, plus hex encoding) per request. With the /notxdetails/ option JSON response will only contain the transaction hash instead of the complete transaction details. The option only affects the JSON response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
block_hash = 'block_hash_example' # str | The block hash
format = 'format_example' # str | The expected format

try:
    # Get block by hash.
    api_response = api_instance.rest_block_notxdetails(block_hash, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->rest_block_notxdetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**| The block hash | 
 **format** | **str**| The expected format | 

### Return type

[**Block**](Block.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

