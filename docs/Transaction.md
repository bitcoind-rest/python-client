# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The transaction amount in BTC | [optional] 
**fee** | **float** | The amount of the fee in BTC. This is negative and only available for the send category of transactions. | [optional] 
**confirmations** | **int** | The number of confirmations | [optional] 
**blockhash** | **str** | The block hash | [optional] 
**blockindex** | **int** | The index of the transaction in the block that includes it | [optional] 
**blocktime** | **int** | The time in seconds since epoch (1 Jan 1970 GMT) | [optional] 
**txid** | **str** | The transaction id | [optional] 
**txhash** | **str** | The transaction hash | [optional] 
**version** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**vsize** | **int** |  | [optional] 
**locktime** | **int** |  | [optional] 
**time** | **int** | The transaction time in seconds since epoch (1 Jan 1970 GMT) | [optional] 
**timereceived** | **int** | The time received in seconds since epoch (1 Jan 1970 GMT) | [optional] 
**bip125_replaceable** | **str** | Whether this transaction could be replaced due to BIP125 (replace-by-fee); may be unknown for unconfirmed transactions not in the mempool | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


