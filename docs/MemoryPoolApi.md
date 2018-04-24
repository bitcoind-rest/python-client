# swagger_client.MemoryPoolApi

All URIs are relative to *http://localhost:3000/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_getutxos**](MemoryPoolApi.md#rest_getutxos) | **GET** /getutxos/checkmempool/{txHash}-{txOutput}.{format} | Returns Unspent Transaction (TX) Outputs
[**rest_headers**](MemoryPoolApi.md#rest_headers) | **GET** /headers/{headerCount}/{blockHash}.{format} | Returns headers.
[**rest_mempool_contents**](MemoryPoolApi.md#rest_mempool_contents) | **GET** /mempool/contents.json | Returns transactions in the TX mempool.
[**rest_mempool_info**](MemoryPoolApi.md#rest_mempool_info) | **GET** /mempool/info.json | Returns various information about the TX mempool.


# **rest_getutxos**
> InlineResponse200 rest_getutxos(tx_hash, tx_output, format)

Returns Unspent Transaction (TX) Outputs

Only supports JSON as output format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemoryPoolApi()
tx_hash = 'tx_hash_example' # str | The transaction hash
tx_output = 'tx_output_example' # str | The transaction output
format = 'format_example' # str | The expected format

try:
    # Returns Unspent Transaction (TX) Outputs
    api_response = api_instance.rest_getutxos(tx_hash, tx_output, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoryPoolApi->rest_getutxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_hash** | **str**| The transaction hash | 
 **tx_output** | **str**| The transaction output | 
 **format** | **str**| The expected format | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_headers**
> str rest_headers(header_count, block_hash, format)

Returns headers.

Only supports BIN and HEX as output format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemoryPoolApi()
header_count = 56 # int | The header count
block_hash = 'block_hash_example' # str | The block hash
format = 'format_example' # str | The expected format

try:
    # Returns headers.
    api_response = api_instance.rest_headers(header_count, block_hash, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoryPoolApi->rest_headers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header_count** | **int**| The header count | 
 **block_hash** | **str**| The block hash | 
 **format** | **str**| The expected format | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_mempool_contents**
> InlineResponseDefault rest_mempool_contents()

Returns transactions in the TX mempool.

Only supports JSON as output format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemoryPoolApi()

try:
    # Returns transactions in the TX mempool.
    api_response = api_instance.rest_mempool_contents()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoryPoolApi->rest_mempool_contents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_mempool_info**
> MemoryPool rest_mempool_info()

Returns various information about the TX mempool.

Only supports JSON as output format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemoryPoolApi()

try:
    # Returns various information about the TX mempool.
    api_response = api_instance.rest_mempool_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoryPoolApi->rest_mempool_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MemoryPool**](MemoryPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

