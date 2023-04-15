# swagger_client.OfficeOnlineApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_os_get_user_locale**](OfficeOnlineApi.md#o_os_get_user_locale) | **GET** /api/v1/oos/locale | Get the OOS locale for the current user
[**o_os_get_version**](OfficeOnlineApi.md#o_os_get_version) | **GET** /api/v1/oos/version | Lookup version of office online server


# **o_os_get_user_locale**
> str o_os_get_user_locale(x_requested_with=x_requested_with)

Get the OOS locale for the current user

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
api_instance = swagger_client.OfficeOnlineApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the OOS locale for the current user
    api_response = api_instance.o_os_get_user_locale(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficeOnlineApi->o_os_get_user_locale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_os_get_version**
> str o_os_get_version(x_requested_with=x_requested_with)

Lookup version of office online server

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
api_instance = swagger_client.OfficeOnlineApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Lookup version of office online server
    api_response = api_instance.o_os_get_version(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficeOnlineApi->o_os_get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

