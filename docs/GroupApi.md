# swagger_client.GroupApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_get_active_group_for_user**](GroupApi.md#group_get_active_group_for_user) | **GET** /api/v1/groups/active | Get your currently active group
[**group_get_groups_for_user**](GroupApi.md#group_get_groups_for_user) | **GET** /api/v1/groups | Get all groups that you have joined
[**group_get_members_for_group**](GroupApi.md#group_get_members_for_group) | **GET** /api/v1/groups/members | Get members of groups that you have joined. You need to have View User permission to use this call. If no role is specified, the user is blocked and has no permissions within the group.
[**group_search_groups**](GroupApi.md#group_search_groups) | **GET** /api/v1/groups/search | Search groups by searchterms
[**group_set_active_group_for_user**](GroupApi.md#group_set_active_group_for_user) | **PUT** /api/v1/groups/active | Change your currently active group
[**group_settings_create_active_group_setting**](GroupApi.md#group_settings_create_active_group_setting) | **POST** /api/v1/groups/active/settings | Create an active group setting
[**group_settings_create_group_setting**](GroupApi.md#group_settings_create_group_setting) | **POST** /api/v1/groups/{groupID}/settings | Create a group setting
[**group_settings_delete_active_group_setting**](GroupApi.md#group_settings_delete_active_group_setting) | **DELETE** /api/v1/groups/active/settings/{groupSettingID} | Delete an active group setting
[**group_settings_delete_group_setting**](GroupApi.md#group_settings_delete_group_setting) | **DELETE** /api/v1/groups/{groupID}/settings/{groupSettingID} | Delete a group setting
[**group_settings_get_active_group_setting**](GroupApi.md#group_settings_get_active_group_setting) | **GET** /api/v1/groups/active/settings/{groupSettingID} | Get an active group setting
[**group_settings_get_active_group_settings**](GroupApi.md#group_settings_get_active_group_settings) | **GET** /api/v1/groups/active/settings | Get all settings for the currently active group.
[**group_settings_get_group_setting**](GroupApi.md#group_settings_get_group_setting) | **GET** /api/v1/groups/{groupID}/settings/{groupSettingsID} | Get a group setting
[**group_settings_get_group_settings**](GroupApi.md#group_settings_get_group_settings) | **GET** /api/v1/groups/{groupID}/settings | Get group settings
[**group_settings_update_active_group_setting**](GroupApi.md#group_settings_update_active_group_setting) | **PUT** /api/v1/groups/active/settings/{groupSettingID} | Update an active group setting
[**group_settings_update_group_setting**](GroupApi.md#group_settings_update_group_setting) | **PUT** /api/v1/groups/{groupID}/settings/{groupSettingID} | Update a group setting


# **group_get_active_group_for_user**
> GroupLarge group_get_active_group_for_user(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get your currently active group

The active group determines what other API calls return and what access you have. For example, GET /samples will only return the samples in your currently active group.    Use PUT /groups/active to switch to another group.    $expand values(separate with comma for multiple expands):  * roles  * subgroups  

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get your currently active group
    api_response = api_instance.group_get_active_group_for_user(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_get_active_group_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**GroupLarge**](GroupLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_get_groups_for_user**
> PagedOfGroup group_get_groups_for_user(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all groups that you have joined

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all groups that you have joined
    api_response = api_instance.group_get_groups_for_user(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_get_groups_for_user: %s\n" % e)
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

[**PagedOfGroup**](PagedOfGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_get_members_for_group**
> list[UserInfo] group_get_members_for_group(group_id, x_requested_with=x_requested_with)

Get members of groups that you have joined. You need to have View User permission to use this call. If no role is specified, the user is blocked and has no permissions within the group.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get members of groups that you have joined. You need to have View User permission to use this call. If no role is specified, the user is blocked and has no permissions within the group.
    api_response = api_instance.group_get_members_for_group(group_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_get_members_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[UserInfo]**](UserInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_search_groups**
> list[Group] group_search_groups(name, x_requested_with=x_requested_with)

Search groups by searchterms

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Search groups by searchterms
    api_response = api_instance.group_search_groups(name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_search_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[Group]**](Group.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_set_active_group_for_user**
> group_set_active_group_for_user(group_id, x_requested_with=x_requested_with)

Change your currently active group

The active group determines what other API calls return and what access you have. For example, GET /samples will only return the samples in your currently active group.    When a group has the policy `TwoFactorAuthRequired` enabled and you haven't set up two-factor authentication in your user account then this call will result in a status 409 (Conflict).  

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Change your currently active group
    api_instance.group_set_active_group_for_user(group_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_set_active_group_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_create_active_group_setting**
> group_settings_create_active_group_setting(dto, x_requested_with=x_requested_with)

Create an active group setting

This call creates an active group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
dto = swagger_client.GroupSettingNew() # GroupSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create an active group setting
    api_instance.group_settings_create_active_group_setting(dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_create_active_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**GroupSettingNew**](GroupSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_create_group_setting**
> group_settings_create_group_setting(group_id, dto, x_requested_with=x_requested_with)

Create a group setting

This call creates a group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
dto = swagger_client.GroupSettingNew() # GroupSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a group setting
    api_instance.group_settings_create_group_setting(group_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_create_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **dto** | [**GroupSettingNew**](GroupSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_delete_active_group_setting**
> group_settings_delete_active_group_setting(group_setting_id, x_requested_with=x_requested_with)

Delete an active group setting

This call deletes an active group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete an active group setting
    api_instance.group_settings_delete_active_group_setting(group_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_delete_active_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_delete_group_setting**
> group_settings_delete_group_setting(group_id, group_setting_id, x_requested_with=x_requested_with)

Delete a group setting

This call deletes a group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
group_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a group setting
    api_instance.group_settings_delete_group_setting(group_id, group_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_delete_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **group_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_get_active_group_setting**
> group_settings_get_active_group_setting(group_setting_id, x_requested_with=x_requested_with)

Get an active group setting

This call fetches an active group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an active group setting
    api_instance.group_settings_get_active_group_setting(group_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_get_active_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_get_active_group_settings**
> group_settings_get_active_group_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)

Get all settings for the currently active group.

This call fetches active group settings.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
keys = 'keys_example' # str | Filter by group settings keys (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all settings for the currently active group.
    api_instance.group_settings_get_active_group_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_get_active_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **keys** | **str**| Filter by group settings keys | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_get_group_setting**
> group_settings_get_group_setting(group_id, group_settings_id, x_requested_with=x_requested_with)

Get a group setting

This call fetches a single group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
group_settings_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a group setting
    api_instance.group_settings_get_group_setting(group_id, group_settings_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_get_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **group_settings_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_get_group_settings**
> group_settings_get_group_settings(group_id, expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)

Get group settings

This call gets all group settings. The results can be filtered on a single key or multiple keys. To filter on multiple keys the keys have to be provided in the following way: 'key1,key2,key3'.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
keys = 'keys_example' # str | Filter by group settings keys (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get group settings
    api_instance.group_settings_get_group_settings(group_id, expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_get_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **keys** | **str**| Filter by group settings keys | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_update_active_group_setting**
> group_settings_update_active_group_setting(group_setting_id, dto, x_requested_with=x_requested_with)

Update an active group setting

This call updates an active group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_setting_id = 56 # int | 
dto = swagger_client.GroupSettingNew() # GroupSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update an active group setting
    api_instance.group_settings_update_active_group_setting(group_setting_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_update_active_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_setting_id** | **int**|  | 
 **dto** | [**GroupSettingNew**](GroupSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_update_group_setting**
> group_settings_update_group_setting(group_id, group_setting_id, dto, x_requested_with=x_requested_with)

Update a group setting

This call updates a group setting.

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
group_setting_id = 56 # int | 
dto = swagger_client.GroupSettingNew() # GroupSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a group setting
    api_instance.group_settings_update_group_setting(group_id, group_setting_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling GroupApi->group_settings_update_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **group_setting_id** | **int**|  | 
 **dto** | [**GroupSettingNew**](GroupSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

