# elabjournal_client.UserApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get_current_user_id**](UserApi.md#user_get_current_user_id) | **GET** /api/v1/users/getCurrentUserInfo | Get the current user Info
[**user_get_current_user_plugin_setting**](UserApi.md#user_get_current_user_plugin_setting) | **GET** /api/v1/users/setting/plugin/{setting}/get | Get the current user plugin setting
[**user_get_current_user_setting**](UserApi.md#user_get_current_user_setting) | **GET** /api/v1/users/setting/{setting}/get | Get the current user setting
[**user_get_user_info**](UserApi.md#user_get_user_info) | **GET** /api/v1/users/{userID} | Get the information of a user
[**user_get_user_profile**](UserApi.md#user_get_user_profile) | **GET** /api/v1/users/{userID}/profile | Get the profile of a user
[**user_search_users**](UserApi.md#user_search_users) | **GET** /api/v1/users/search | Find users by email address
[**user_set_current_user_plugin_setting**](UserApi.md#user_set_current_user_plugin_setting) | **POST** /api/v1/users/setting/plugin/{setting}/set/{value} | Set the current user plugin setting
[**user_set_current_user_setting**](UserApi.md#user_set_current_user_setting) | **POST** /api/v1/users/setting/{setting}/set/{value} | Set the current user setting
[**user_settings_admin_create_user_setting**](UserApi.md#user_settings_admin_create_user_setting) | **POST** /api/v1/users/{userID}/settings | Create user setting by user id
[**user_settings_admin_delete_user_setting**](UserApi.md#user_settings_admin_delete_user_setting) | **DELETE** /api/v1/users/{userID}/settings/{userSettingsID} | Delete an user setting by user id
[**user_settings_admin_get_user_setting**](UserApi.md#user_settings_admin_get_user_setting) | **GET** /api/v1/users/{userID}/settings/{userSettingsID} | Get an user setting by user id
[**user_settings_admin_get_user_settings**](UserApi.md#user_settings_admin_get_user_settings) | **GET** /api/v1/users/{userID}/settings | Get user settings by user id
[**user_settings_admin_update_user_setting**](UserApi.md#user_settings_admin_update_user_setting) | **PUT** /api/v1/users/{userID}/settings/{userSettingsID} | Update an user setting by user id
[**user_settings_create_user_setting**](UserApi.md#user_settings_create_user_setting) | **POST** /api/v1/users/settings | Create a current user setting
[**user_settings_delete_user_setting**](UserApi.md#user_settings_delete_user_setting) | **DELETE** /api/v1/users/settings/{userSettingsID} | Delete a user setting for the logged in user
[**user_settings_get_user_setting**](UserApi.md#user_settings_get_user_setting) | **GET** /api/v1/users/settings/{userSettingID} | Get a current user setting
[**user_settings_get_user_settings**](UserApi.md#user_settings_get_user_settings) | **GET** /api/v1/users/settings | Get a current user settings
[**user_settings_update_user_setting**](UserApi.md#user_settings_update_user_setting) | **PUT** /api/v1/users/settings/{userSettingsID} | Update a current user setting
[**user_update_user_profile**](UserApi.md#user_update_user_profile) | **PATCH** /api/v1/users/{userID}/profile | Update user information


# **user_get_current_user_id**
> UserInfo user_get_current_user_id(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the current user Info

          $expand values (separate with a comma for multiple expands):          * permissions

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the current user Info
    api_response = api_instance.user_get_current_user_id(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_current_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_current_user_plugin_setting**
> UserSettingDTO user_get_current_user_plugin_setting(setting, x_requested_with=x_requested_with)

Get the current user plugin setting

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
setting = 'setting_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the current user plugin setting
    api_response = api_instance.user_get_current_user_plugin_setting(setting, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_current_user_plugin_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**UserSettingDTO**](UserSettingDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_current_user_setting**
> UserSettingDTO user_get_current_user_setting(setting, x_requested_with=x_requested_with)

Get the current user setting

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
setting = 'setting_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the current user setting
    api_response = api_instance.user_get_current_user_setting(setting, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_current_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**UserSettingDTO**](UserSettingDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_user_info**
> UserDTO user_get_user_info(user_id, x_requested_with=x_requested_with)

Get the information of a user

Get the information of a user within your group

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the information of a user
    api_response = api_instance.user_get_user_info(user_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_user_profile**
> Profile user_get_user_profile(user_id, x_requested_with=x_requested_with)

Get the profile of a user

Get the profile of a user within your group.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the profile of a user
    api_response = api_instance.user_get_user_profile(user_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**Profile**](Profile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_search_users**
> list[UserSmall] user_search_users(email, x_requested_with=x_requested_with)

Find users by email address

Email address needs to be exact unless you have system admin privileges.   System administrators need to provide a minimum of 3 characters to search. A maximum of 250 records will be returned.  

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
email = 'email_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Find users by email address
    api_response = api_instance.user_search_users(email, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[UserSmall]**](UserSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_set_current_user_plugin_setting**
> bool user_set_current_user_plugin_setting(setting, value, x_requested_with=x_requested_with)

Set the current user plugin setting

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
setting = 'setting_example' # str | 
value = 'value_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Set the current user plugin setting
    api_response = api_instance.user_set_current_user_plugin_setting(setting, value, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_set_current_user_plugin_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | **str**|  | 
 **value** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_set_current_user_setting**
> bool user_set_current_user_setting(setting, value, x_requested_with=x_requested_with)

Set the current user setting

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
setting = 'setting_example' # str | 
value = 'value_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Set the current user setting
    api_response = api_instance.user_set_current_user_setting(setting, value, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_set_current_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | **str**|  | 
 **value** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_admin_create_user_setting**
> user_settings_admin_create_user_setting(user_id, dto, x_requested_with=x_requested_with)

Create user setting by user id

This call creates an user setting for a specified user. This call can only be used by Elab admins

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
dto = elabjournal_client.UserSettingNew() # UserSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create user setting by user id
    api_instance.user_settings_admin_create_user_setting(user_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_admin_create_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **dto** | [**UserSettingNew**](UserSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_admin_delete_user_setting**
> user_settings_admin_delete_user_setting(user_id, user_settings_id, x_requested_with=x_requested_with)

Delete an user setting by user id

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
user_settings_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete an user setting by user id
    api_instance.user_settings_admin_delete_user_setting(user_id, user_settings_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_admin_delete_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **user_settings_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_admin_get_user_setting**
> user_settings_admin_get_user_setting(user_id, user_settings_id, x_requested_with=x_requested_with)

Get an user setting by user id

This call fetches user settings of specified users. This call can only be used by Elab admins.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
user_settings_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an user setting by user id
    api_instance.user_settings_admin_get_user_setting(user_id, user_settings_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_admin_get_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **user_settings_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_admin_get_user_settings**
> user_settings_admin_get_user_settings(user_id, expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)

Get user settings by user id

This call gets all user settings of a specified user. The results can be filtered on a single key or multiple keys. To filter on multiple keys the keys have to be provided in the following way: 'key1,key2,key3'. This call can only be used by Elab admins

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
keys = 'keys_example' # str | Filter by user settings keys (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get user settings by user id
    api_instance.user_settings_admin_get_user_settings(user_id, expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_admin_get_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **keys** | **str**| Filter by user settings keys | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_admin_update_user_setting**
> user_settings_admin_update_user_setting(user_id, user_settings_id, dto, x_requested_with=x_requested_with)

Update an user setting by user id

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
user_settings_id = 56 # int | 
dto = elabjournal_client.UserSettingNew() # UserSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update an user setting by user id
    api_instance.user_settings_admin_update_user_setting(user_id, user_settings_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_admin_update_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **user_settings_id** | **int**|  | 
 **dto** | [**UserSettingNew**](UserSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_create_user_setting**
> user_settings_create_user_setting(dto, x_requested_with=x_requested_with)

Create a current user setting

This call creates a current user setting.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
dto = elabjournal_client.UserSettingNew() # UserSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a current user setting
    api_instance.user_settings_create_user_setting(dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_create_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**UserSettingNew**](UserSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_delete_user_setting**
> user_settings_delete_user_setting(user_settings_id, x_requested_with=x_requested_with)

Delete a user setting for the logged in user

This call deletes a user setting for the logged in user.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_settings_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a user setting for the logged in user
    api_instance.user_settings_delete_user_setting(user_settings_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_delete_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_settings_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_get_user_setting**
> user_settings_get_user_setting(user_setting_id, x_requested_with=x_requested_with)

Get a current user setting

This call gets a current user setting.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a current user setting
    api_instance.user_settings_get_user_setting(user_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_get_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_get_user_settings**
> user_settings_get_user_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)

Get a current user settings

This call gets all current user settings. The results can be filtered on a single key or multiple keys. To filter on multiple keys the keys have to be provided in the following way: 'key1,key2,key3'.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
keys = 'keys_example' # str | Filter by user settings keys (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a current user settings
    api_instance.user_settings_get_user_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_get_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **keys** | **str**| Filter by user settings keys | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_update_user_setting**
> user_settings_update_user_setting(user_settings_id, dto, x_requested_with=x_requested_with)

Update a current user setting

This call updates a current user setting.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_settings_id = 56 # int | 
dto = elabjournal_client.UserSettingNew() # UserSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a current user setting
    api_instance.user_settings_update_user_setting(user_settings_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_settings_update_user_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_settings_id** | **int**|  | 
 **dto** | [**UserSettingNew**](UserSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_user_profile**
> user_update_user_profile(user_id, delta, x_requested_with=x_requested_with)

Update user information

UserID needs to be a existing UserID in the database. Delta has an example value of the fields that can be changed.

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
api_instance = elabjournal_client.UserApi(elabjournal_client.ApiClient(configuration))
user_id = 56 # int | 
delta = elabjournal_client.ProfileUpdate() # ProfileUpdate | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update user information
    api_instance.user_update_user_profile(user_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling UserApi->user_update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **delta** | [**ProfileUpdate**](ProfileUpdate.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

