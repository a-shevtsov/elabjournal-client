# swagger_client.BarcodeApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcode_get_barcode_result**](BarcodeApi.md#barcode_get_barcode_result) | **GET** /api/v1/barcode/{barcode} | Get the object type of a barcode and its associated id


# **barcode_get_barcode_result**
> BarcodeResult barcode_get_barcode_result(barcode, x_requested_with=x_requested_with)

Get the object type of a barcode and its associated id

Searches for the provided barcode and returns its type (SAMPLE/STORAGELAYER/SAMPLESERIES) and the id of its associated object. You can use the GET API call for the specific type to retrieve the full object.    Note: if the barcode parameter has a dot (e.g. \"my.barcode\") then you MUST add a / to the end of this call (e.g. \".../barcode/my.barcode/\").    In case of an unrecognized barcode the type property will be set to UNKNOWN.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BarcodeApi(swagger_client.ApiClient(configuration))
barcode = 'barcode_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the object type of a barcode and its associated id
    api_response = api_instance.barcode_get_barcode_result(barcode, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->barcode_get_barcode_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**BarcodeResult**](BarcodeResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

