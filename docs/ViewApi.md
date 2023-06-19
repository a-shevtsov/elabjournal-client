# elabjournal_client.ViewApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**view_create_view**](ViewApi.md#view_create_view) | **POST** /api/v1/views | 
[**view_delete_view**](ViewApi.md#view_delete_view) | **DELETE** /api/v1/views/{viewID} | 
[**view_get_view**](ViewApi.md#view_get_view) | **GET** /api/v1/views/{viewID} | 
[**view_get_views**](ViewApi.md#view_get_views) | **GET** /api/v1/views | 
[**view_update_view**](ViewApi.md#view_update_view) | **PUT** /api/v1/views/{viewID} | 


# **view_create_view**
> int view_create_view(view, x_requested_with=x_requested_with)



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
api_instance = elabjournal_client.ViewApi(elabjournal_client.ApiClient(configuration))
view = elabjournal_client.View() # View | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.view_create_view(view, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_create_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | [**View**](View.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_delete_view**
> view_delete_view(view_id, x_requested_with=x_requested_with)



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
api_instance = elabjournal_client.ViewApi(elabjournal_client.ApiClient(configuration))
view_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_instance.view_delete_view(view_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ViewApi->view_delete_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_get_view**
> View view_get_view(view_id, expand=expand, view_id2=view_id2, view_columns=view_columns, x_requested_with=x_requested_with)



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
api_instance = elabjournal_client.ViewApi(elabjournal_client.ApiClient(configuration))
view_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id2 = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.view_get_view(view_id, expand=expand, view_id2=view_id2, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id2** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**View**](View.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_get_views**
> PagedOfView view_get_views(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)



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
api_instance = elabjournal_client.ViewApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.view_get_views(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_get_views: %s\n" % e)
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
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfView**](PagedOfView.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_update_view**
> View view_update_view(view_id, view, x_requested_with=x_requested_with)



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
api_instance = elabjournal_client.ViewApi(elabjournal_client.ApiClient(configuration))
view_id = 56 # int | 
view = elabjournal_client.View() # View | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.view_update_view(view_id, view, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->view_update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**|  | 
 **view** | [**View**](View.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**View**](View.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

