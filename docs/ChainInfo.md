# ChainInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** | Current network name as defined in BIP70 (main, test, regtest) | [optional] 
**blocks** | **int** | The current number of blocks processed in the server | [optional] 
**headers** | **int** | The current number of headers we have validated | [optional] 
**bestblockhash** | **str** | The hash of the currently best block | [optional] 
**difficulty** | **int** | The current difficulty | [optional] 
**mediantime** | **int** | The median time of the 11 blocks before the most recent block on the blockchain | [optional] 
**verificationprogress** | **int** | Estimate of verification progress [0..1] | [optional] 
**initialblockdownload** | **bool** |  | [optional] 
**chainwork** | **str** | Total amount of work in active chain, in hexadecimal | [optional] 
**size_on_disk** | **int** |  | [optional] 
**pruned** | **bool** | If the blocks are subject to pruning | [optional] 
**softforks** | [**list[BIP]**](BIP.md) | status of softforks in progress | [optional] 
**bip9_softforks** | [**ChainInfoBip9Softforks**](ChainInfoBip9Softforks.md) |  | [optional] 
**warnings** | **str** | An eventual warning on the current build status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


