# swagger_client.MeasurementUnitApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measurement_unit_get_storage_types**](MeasurementUnitApi.md#measurement_unit_get_storage_types) | **GET** /api/v1/measurementUnits | Get all measurement units defined by eLab


# **measurement_unit_get_storage_types**
> list[MeasurementUnit] measurement_unit_get_storage_types(expand=expand, view_id=view_id, view_columns=view_columns, unit_short=unit_short, unit_name=unit_name, quantity_name=quantity_name, x_requested_with=x_requested_with)

Get all measurement units defined by eLab

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
api_instance = swagger_client.MeasurementUnitApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
unit_short = 'unit_short_example' # str | Filter by the abbreviation of the unit (\"kg\", \"μl\", etc.) (optional)
unit_name = 'unit_name_example' # str | Filter by the name of the unit (\"milligram\", \"microliter\", etc.) (optional)
quantity_name = 'quantity_name_example' # str | Filter by the unit's type (\"Mass\", \"Volume\", etc.) (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all measurement units defined by eLab
    api_response = api_instance.measurement_unit_get_storage_types(expand=expand, view_id=view_id, view_columns=view_columns, unit_short=unit_short, unit_name=unit_name, quantity_name=quantity_name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeasurementUnitApi->measurement_unit_get_storage_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **unit_short** | **str**| Filter by the abbreviation of the unit (\&quot;kg\&quot;, \&quot;μl\&quot;, etc.) | [optional] 
 **unit_name** | **str**| Filter by the name of the unit (\&quot;milligram\&quot;, \&quot;microliter\&quot;, etc.) | [optional] 
 **quantity_name** | **str**| Filter by the unit&#39;s type (\&quot;Mass\&quot;, \&quot;Volume\&quot;, etc.) | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[MeasurementUnit]**](MeasurementUnit.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

