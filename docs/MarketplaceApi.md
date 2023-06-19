# elabjournal_client.MarketplaceApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_place_get_addon**](MarketplaceApi.md#market_place_get_addon) | **GET** /api/v1/marketplace/addons/{sdkPluginID} | Get an available addon by ID.
[**market_place_get_addon_code**](MarketplaceApi.md#market_place_get_addon_code) | **GET** /api/v1/marketplace/addons/{sdkPluginID}/code | Get the script code of the specified available addon.
[**market_place_get_all_addons**](MarketplaceApi.md#market_place_get_all_addons) | **GET** /api/v1/marketplace/addons | Get all available addons.
[**market_place_has_addon_enabled**](MarketplaceApi.md#market_place_has_addon_enabled) | **GET** /api/v1/marketplace/addons/enabled | Check to see if current logged in user has addon with rootVar X enabled. If scope specified only installation for that scope will be checked, otherwise installation for any scope will be checked.
[**market_place_media_get_icon**](MarketplaceApi.md#market_place_media_get_icon) | **GET** /api/v1/marketplace/icon/{id} | Get icon by media ID.
[**market_place_media_get_image**](MarketplaceApi.md#market_place_media_get_image) | **GET** /api/v1/marketplace/image/{id} | Get image by media ID.
[**market_place_validate_dependencies**](MarketplaceApi.md#market_place_validate_dependencies) | **GET** /api/v1/marketplace/addons/{sdkPluginID}/validateDependencies | Check whether the required dependencies of the given addon are published.


# **market_place_get_addon**
> PluginDetailedExternal market_place_get_addon(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get an available addon by ID.

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
api_instance = elabjournal_client.MarketplaceApi(elabjournal_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an available addon by ID.
    api_response = api_instance.market_place_get_addon(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->market_place_get_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PluginDetailedExternal**](PluginDetailedExternal.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_place_get_addon_code**
> str market_place_get_addon_code(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the script code of the specified available addon.

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
api_instance = elabjournal_client.MarketplaceApi(elabjournal_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the script code of the specified available addon.
    api_response = api_instance.market_place_get_addon_code(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->market_place_get_addon_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_place_get_all_addons**
> PagedOfPluginSmallExternal market_place_get_all_addons(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, category=category, scopes=scopes, root_var=root_var, x_requested_with=x_requested_with)

Get all available addons.

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
api_instance = elabjournal_client.MarketplaceApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
category = 'category_example' # str | Filter by category identifiers (optional)
scopes = 'scopes_example' # str | Filter by scope (optional)
root_var = 'root_var_example' # str | Filter by addon identifier (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all available addons.
    api_response = api_instance.market_place_get_all_addons(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, category=category, scopes=scopes, root_var=root_var, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->market_place_get_all_addons: %s\n" % e)
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
 **category** | **str**| Filter by category identifiers | [optional] 
 **scopes** | **str**| Filter by scope | [optional] 
 **root_var** | **str**| Filter by addon identifier | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfPluginSmallExternal**](PagedOfPluginSmallExternal.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_place_has_addon_enabled**
> bool market_place_has_addon_enabled(root_var, scope=scope, x_requested_with=x_requested_with)

Check to see if current logged in user has addon with rootVar X enabled. If scope specified only installation for that scope will be checked, otherwise installation for any scope will be checked.

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
api_instance = elabjournal_client.MarketplaceApi(elabjournal_client.ApiClient(configuration))
root_var = 'root_var_example' # str | 
scope = 'scope_example' # str |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check to see if current logged in user has addon with rootVar X enabled. If scope specified only installation for that scope will be checked, otherwise installation for any scope will be checked.
    api_response = api_instance.market_place_has_addon_enabled(root_var, scope=scope, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->market_place_has_addon_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_var** | **str**|  | 
 **scope** | **str**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_place_media_get_icon**
> object market_place_media_get_icon(id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get icon by media ID.

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
api_instance = elabjournal_client.MarketplaceApi(elabjournal_client.ApiClient(configuration))
id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get icon by media ID.
    api_response = api_instance.market_place_media_get_icon(id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->market_place_media_get_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_place_media_get_image**
> object market_place_media_get_image(id, x_requested_with=x_requested_with)

Get image by media ID.

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
api_instance = elabjournal_client.MarketplaceApi(elabjournal_client.ApiClient(configuration))
id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get image by media ID.
    api_response = api_instance.market_place_media_get_image(id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->market_place_media_get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_place_validate_dependencies**
> bool market_place_validate_dependencies(sdk_plugin_id, x_requested_with=x_requested_with)

Check whether the required dependencies of the given addon are published.

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
api_instance = elabjournal_client.MarketplaceApi(elabjournal_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check whether the required dependencies of the given addon are published.
    api_response = api_instance.market_place_validate_dependencies(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->market_place_validate_dependencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

