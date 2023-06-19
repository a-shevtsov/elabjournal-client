# elabjournal_client.QuantityApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quantity_get_quantity_types**](QuantityApi.md#quantity_get_quantity_types) | **GET** /api/v1/quantityType | Get quantity types
[**quantity_get_quantity_types_by_id**](QuantityApi.md#quantity_get_quantity_types_by_id) | **GET** /api/v1/quantityType/{quantityId} | Get quantity types by id


# **quantity_get_quantity_types**
> PagedOfQuantity quantity_get_quantity_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, unit_name=unit_name, x_requested_with=x_requested_with)

Get quantity types

This endpoint returns all the different quantity types

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
api_instance = elabjournal_client.QuantityApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
unit_name = 'unit_name_example' # str | Filter based on the unit name (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get quantity types
    api_response = api_instance.quantity_get_quantity_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, unit_name=unit_name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuantityApi->quantity_get_quantity_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **unit_name** | **str**| Filter based on the unit name | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfQuantity**](PagedOfQuantity.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quantity_get_quantity_types_by_id**
> Quantity quantity_get_quantity_types_by_id(quantity_id, x_requested_with=x_requested_with)

Get quantity types by id

Get quantity types by the quantity id

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
api_instance = elabjournal_client.QuantityApi(elabjournal_client.ApiClient(configuration))
quantity_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get quantity types by id
    api_response = api_instance.quantity_get_quantity_types_by_id(quantity_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuantityApi->quantity_get_quantity_types_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**Quantity**](Quantity.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

