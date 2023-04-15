# swagger_client.SystemApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_get_controller_capabilities**](SystemApi.md#system_get_controller_capabilities) | **GET** /api/v1/system/capabilities | Get all capabilities
[**system_get_current_elab_version**](SystemApi.md#system_get_current_elab_version) | **GET** /api/v1/system/version | Get the current Elab version
[**system_get_system_time_zones**](SystemApi.md#system_get_system_time_zones) | **GET** /api/v1/system/timezones | Get system timezones
[**system_settings_create_system_setting**](SystemApi.md#system_settings_create_system_setting) | **POST** /api/v1/systemsettings | Create a system setting
[**system_settings_delete_system_setting**](SystemApi.md#system_settings_delete_system_setting) | **DELETE** /api/v1/systemsettings | Delete a system setting
[**system_settings_delete_system_setting_v2**](SystemApi.md#system_settings_delete_system_setting_v2) | **DELETE** /api/v1/systemsettings/{systemSettingID} | Delete a system setting
[**system_settings_get_system_setting**](SystemApi.md#system_settings_get_system_setting) | **GET** /api/v1/systemsettings/setting | Get system setting
[**system_settings_get_system_setting_v2**](SystemApi.md#system_settings_get_system_setting_v2) | **GET** /api/v1/systemsettings/{systemSettingID} | Get system setting by id
[**system_settings_get_system_settings**](SystemApi.md#system_settings_get_system_settings) | **GET** /api/v1/systemsettings | Get system settings
[**system_settings_put_system_settings**](SystemApi.md#system_settings_put_system_settings) | **PUT** /api/v1/systemsettings/bulk | Create or update a list of system setting
[**system_settings_update_system_setting**](SystemApi.md#system_settings_update_system_setting) | **PUT** /api/v1/systemsettings | Update a system setting
[**system_settings_update_system_setting_v2**](SystemApi.md#system_settings_update_system_setting_v2) | **PUT** /api/v1/systemsettings/{systemSettingID} | Update a system setting by id


# **system_get_controller_capabilities**
> system_get_controller_capabilities(x_requested_with=x_requested_with)

Get all capabilities

Gets a deduplicated list of all the capabilities present in the application

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all capabilities
    api_instance.system_get_controller_capabilities(x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_controller_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_current_elab_version**
> VersionInfo system_get_current_elab_version(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the current Elab version

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the current Elab version
    api_response = api_instance.system_get_current_elab_version(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_current_elab_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_system_time_zones**
> system_get_system_time_zones(x_requested_with=x_requested_with)

Get system timezones

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get system timezones
    api_instance.system_get_system_time_zones(x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_system_time_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_create_system_setting**
> SystemSetting system_settings_create_system_setting(setting, x_requested_with=x_requested_with)

Create a system setting

This call creates a system setting. This call can only be used by admins.

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
setting = swagger_client.SystemSettingNew() # SystemSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a system setting
    api_response = api_instance.system_settings_create_system_setting(setting, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_create_system_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | [**SystemSettingNew**](SystemSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_delete_system_setting**
> system_settings_delete_system_setting(expand=expand, view_id=view_id, view_columns=view_columns, key=key, x_requested_with=x_requested_with)

Delete a system setting

This call deletes a system setting.

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
key = 'key_example' # str | Delete the system setting key (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a system setting
    api_instance.system_settings_delete_system_setting(expand=expand, view_id=view_id, view_columns=view_columns, key=key, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_delete_system_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **key** | **str**| Delete the system setting key | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_delete_system_setting_v2**
> system_settings_delete_system_setting_v2(system_setting_id, x_requested_with=x_requested_with)

Delete a system setting

This call deletes a system setting. This call can only be used by admins.

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
system_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a system setting
    api_instance.system_settings_delete_system_setting_v2(system_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_delete_system_setting_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_get_system_setting**
> SystemSetting system_settings_get_system_setting(expand=expand, view_id=view_id, view_columns=view_columns, key=key, x_requested_with=x_requested_with)

Get system setting

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
key = 'key_example' # str | Filter by system settings key (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get system setting
    api_response = api_instance.system_settings_get_system_setting(expand=expand, view_id=view_id, view_columns=view_columns, key=key, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_get_system_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **key** | **str**| Filter by system settings key | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_get_system_setting_v2**
> system_settings_get_system_setting_v2(system_setting_id, x_requested_with=x_requested_with)

Get system setting by id

This call gets a system setting by id. This call can only be used by admins.

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
system_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get system setting by id
    api_instance.system_settings_get_system_setting_v2(system_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_get_system_setting_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_get_system_settings**
> system_settings_get_system_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)

Get system settings

This call gets all system settings. The results can be filtered on a single key or multiple keys. To filter on multiple keys the keys have to be provided in the following way: 'key1,key2,key3'. This call can only be used by admins.

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
keys = 'keys_example' # str | Filter by system settings keys (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get system settings
    api_instance.system_settings_get_system_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_get_system_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **keys** | **str**| Filter by system settings keys | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_put_system_settings**
> system_settings_put_system_settings(settings, x_requested_with=x_requested_with)

Create or update a list of system setting

This call updates multiple system settings. This call can only be used by admins.

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
settings = [swagger_client.SystemSettingNew()] # list[SystemSettingNew] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create or update a list of system setting
    api_instance.system_settings_put_system_settings(settings, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_put_system_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**list[SystemSettingNew]**](SystemSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_update_system_setting**
> system_settings_update_system_setting(setting, x_requested_with=x_requested_with)

Update a system setting

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
setting = swagger_client.SystemSettingNew() # SystemSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a system setting
    api_instance.system_settings_update_system_setting(setting, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_update_system_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | [**SystemSettingNew**](SystemSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_update_system_setting_v2**
> system_settings_update_system_setting_v2(system_setting_id, setting, x_requested_with=x_requested_with)

Update a system setting by id

This call updates a system setting. This call can only be used by admins.

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
system_setting_id = 56 # int | 
setting = swagger_client.SystemSettingNew() # SystemSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a system setting by id
    api_instance.system_settings_update_system_setting_v2(system_setting_id, setting, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SystemApi->system_settings_update_system_setting_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_setting_id** | **int**|  | 
 **setting** | [**SystemSettingNew**](SystemSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

