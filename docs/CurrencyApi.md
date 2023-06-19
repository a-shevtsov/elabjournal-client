# elabjournal_client.CurrencyApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_get_all_currency_iso3_letter_codes**](CurrencyApi.md#currency_get_all_currency_iso3_letter_codes) | **GET** /api/v1/currencies/iso3lettercodes | Get the list of currencies available in elab
[**currency_get_all_currency_letter_codes_with_symbols**](CurrencyApi.md#currency_get_all_currency_letter_codes_with_symbols) | **GET** /api/v1/currencies/currency-symbol-pairs | Get the list of currencie symbols available in elab


# **currency_get_all_currency_iso3_letter_codes**
> list[str] currency_get_all_currency_iso3_letter_codes(x_requested_with=x_requested_with)

Get the list of currencies available in elab

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.CurrencyApi(elabjournal_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the list of currencies available in elab
    api_response = api_instance.currency_get_all_currency_iso3_letter_codes(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->currency_get_all_currency_iso3_letter_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_get_all_currency_letter_codes_with_symbols**
> dict(str, str) currency_get_all_currency_letter_codes_with_symbols(x_requested_with=x_requested_with)

Get the list of currencie symbols available in elab

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.CurrencyApi(elabjournal_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the list of currencie symbols available in elab
    api_response = api_instance.currency_get_all_currency_letter_codes_with_symbols(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->currency_get_all_currency_letter_codes_with_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**dict(str, str)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

