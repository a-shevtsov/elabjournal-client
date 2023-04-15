# swagger_client.OrganisationsApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisation_search_organisations**](OrganisationsApi.md#organisation_search_organisations) | **GET** /api/v1/organisations/search | Find organisation by name
[**organisation_settings_create_active_group_setting**](OrganisationsApi.md#organisation_settings_create_active_group_setting) | **POST** /api/v1/organisations/active/settings | Create an active institute setting
[**organisation_settings_create_institute_setting**](OrganisationsApi.md#organisation_settings_create_institute_setting) | **POST** /api/v1/organisations/{instituteID}/settings | Create a institute setting
[**organisation_settings_delete_institute_setting**](OrganisationsApi.md#organisation_settings_delete_institute_setting) | **DELETE** /api/v1/organisations/{instituteID}/settings/{instituteSettingID} | Delete an institute setting
[**organisation_settings_delete_institute_setting_for_current_institute**](OrganisationsApi.md#organisation_settings_delete_institute_setting_for_current_institute) | **DELETE** /api/v1/organisations/active/settings/{instituteSettingID} | Delete an active institute setting
[**organisation_settings_get_active_institute_setting**](OrganisationsApi.md#organisation_settings_get_active_institute_setting) | **GET** /api/v1/organisations/active/settings/{instituteSettingId} | Get an active institute setting
[**organisation_settings_get_active_institute_settings**](OrganisationsApi.md#organisation_settings_get_active_institute_settings) | **GET** /api/v1/organisations/active/settings | Get active institute settings
[**organisation_settings_get_institute_setting**](OrganisationsApi.md#organisation_settings_get_institute_setting) | **GET** /api/v1/organisations/{instituteID}/settings/{instituteSettingID} | Get an institute setting
[**organisation_settings_get_institute_settings**](OrganisationsApi.md#organisation_settings_get_institute_settings) | **GET** /api/v1/organisations/{instituteID}/settings | Get institute settings
[**organisation_settings_update_active_institute_setting**](OrganisationsApi.md#organisation_settings_update_active_institute_setting) | **PUT** /api/v1/organisations/active/settings/{instituteSettingID} | Update an active institute setting
[**organisation_settings_update_institute_setting**](OrganisationsApi.md#organisation_settings_update_institute_setting) | **PUT** /api/v1/organisations/{instituteID}/settings/{instituteSettingsID} | Update an institute setting


# **organisation_search_organisations**
> list[Institute] organisation_search_organisations(name, x_requested_with=x_requested_with)

Find organisation by name

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Find organisation by name
    api_response = api_instance.organisation_search_organisations(name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_search_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[Institute]**](Institute.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_create_active_group_setting**
> organisation_settings_create_active_group_setting(dto, x_requested_with=x_requested_with)

Create an active institute setting

This call creates an active institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
dto = swagger_client.InstituteSettingNew() # InstituteSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create an active institute setting
    api_instance.organisation_settings_create_active_group_setting(dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_create_active_group_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**InstituteSettingNew**](InstituteSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_create_institute_setting**
> organisation_settings_create_institute_setting(institute_id, dto, x_requested_with=x_requested_with)

Create a institute setting

This call creates a institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
institute_id = 56 # int | 
dto = swagger_client.InstituteSettingNew() # InstituteSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a institute setting
    api_instance.organisation_settings_create_institute_setting(institute_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_create_institute_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institute_id** | **int**|  | 
 **dto** | [**InstituteSettingNew**](InstituteSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_delete_institute_setting**
> organisation_settings_delete_institute_setting(institute_id, institute_setting_id, x_requested_with=x_requested_with)

Delete an institute setting

This call deletes an institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
institute_id = 56 # int | 
institute_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete an institute setting
    api_instance.organisation_settings_delete_institute_setting(institute_id, institute_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_delete_institute_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institute_id** | **int**|  | 
 **institute_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_delete_institute_setting_for_current_institute**
> organisation_settings_delete_institute_setting_for_current_institute(institute_setting_id, x_requested_with=x_requested_with)

Delete an active institute setting

This call deletes an active institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
institute_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete an active institute setting
    api_instance.organisation_settings_delete_institute_setting_for_current_institute(institute_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_delete_institute_setting_for_current_institute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institute_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_get_active_institute_setting**
> organisation_settings_get_active_institute_setting(institute_setting_id, x_requested_with=x_requested_with)

Get an active institute setting

This call fetches an active institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
institute_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an active institute setting
    api_instance.organisation_settings_get_active_institute_setting(institute_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_get_active_institute_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institute_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_get_active_institute_settings**
> organisation_settings_get_active_institute_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)

Get active institute settings

This call fetches institute group settings. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
keys = 'keys_example' # str | Filter by group institute keys (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get active institute settings
    api_instance.organisation_settings_get_active_institute_settings(expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_get_active_institute_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **keys** | **str**| Filter by group institute keys | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_get_institute_setting**
> organisation_settings_get_institute_setting(institute_id, institute_setting_id, x_requested_with=x_requested_with)

Get an institute setting

This call fetches an institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
institute_id = 56 # int | 
institute_setting_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an institute setting
    api_instance.organisation_settings_get_institute_setting(institute_id, institute_setting_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_get_institute_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institute_id** | **int**|  | 
 **institute_setting_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_get_institute_settings**
> organisation_settings_get_institute_settings(group_id, institute_id, expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)

Get institute settings

This call fetches all institute settings. The results can be filtered on a single key or multiple keys. To filter on multiple keys the keys have to be provided in the following way: 'key1,key2,key3'.Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
group_id = 56 # int | 
institute_id = 'institute_id_example' # str | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
keys = 'keys_example' # str | Filter by institute settings keys (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get institute settings
    api_instance.organisation_settings_get_institute_settings(group_id, institute_id, expand=expand, view_id=view_id, view_columns=view_columns, keys=keys, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_get_institute_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **institute_id** | **str**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **keys** | **str**| Filter by institute settings keys | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_update_active_institute_setting**
> organisation_settings_update_active_institute_setting(institute_setting_id, dto, x_requested_with=x_requested_with)

Update an active institute setting

This call updates an active institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
institute_setting_id = 56 # int | 
dto = swagger_client.InstituteSettingNew() # InstituteSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update an active institute setting
    api_instance.organisation_settings_update_active_institute_setting(institute_setting_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_update_active_institute_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institute_setting_id** | **int**|  | 
 **dto** | [**InstituteSettingNew**](InstituteSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_settings_update_institute_setting**
> organisation_settings_update_institute_setting(institute_id, institute_settings_id, dto, x_requested_with=x_requested_with)

Update an institute setting

This call updates an institute setting. Elab admins or organisation admins can only use this call.

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
api_instance = swagger_client.OrganisationsApi(swagger_client.ApiClient(configuration))
institute_id = 56 # int | 
institute_settings_id = 56 # int | 
dto = swagger_client.InstituteSettingNew() # InstituteSettingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update an institute setting
    api_instance.organisation_settings_update_institute_setting(institute_id, institute_settings_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisation_settings_update_institute_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institute_id** | **int**|  | 
 **institute_settings_id** | **int**|  | 
 **dto** | [**InstituteSettingNew**](InstituteSettingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

