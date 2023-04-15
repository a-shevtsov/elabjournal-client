# swagger_client.AddOnsApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addon_approve_addon**](AddOnsApi.md#addon_approve_addon) | **PUT** /api/v1/addons/{sdkPluginID}/approve | Approve an addon for installation by end users.
[**addon_delete_addon**](AddOnsApi.md#addon_delete_addon) | **DELETE** /api/v1/addons/{sdkPluginID} | Delete the specified installed add-on.
[**addon_delete_media_from_addon**](AddOnsApi.md#addon_delete_media_from_addon) | **DELETE** /api/v1/addons/{sdkPluginID}/media/{mediaID} | Delete given media for the specified add-on.
[**addon_disable_addon**](AddOnsApi.md#addon_disable_addon) | **PUT** /api/v1/addons/{sdkPluginID}/disable/{scope} | Disable the specified add-on for the given scope.
[**addon_enable_addon**](AddOnsApi.md#addon_enable_addon) | **PUT** /api/v1/addons/{sdkPluginID}/enable/{scope} | Enable the specified add-on for the given scope.
[**addon_get_addon**](AddOnsApi.md#addon_get_addon) | **GET** /api/v1/addons/{sdkPluginID} | Get an available addon by ID for internal use
[**addon_get_addon_config**](AddOnsApi.md#addon_get_addon_config) | **GET** /api/v1/addons/{sdkPluginID}/configuration | Get the configuration details for the specified add-on.
[**addon_get_available_addons**](AddOnsApi.md#addon_get_available_addons) | **GET** /api/v1/addons/available | Retrieve list of addons for use in marketplace.
[**addon_get_available_addons_grouped_by_version**](AddOnsApi.md#addon_get_available_addons_grouped_by_version) | **GET** /api/v1/addons/available/grouped | Get all available addons grouped by rootVar and included lower versioned add-ons.
[**addon_get_available_upgrades_count**](AddOnsApi.md#addon_get_available_upgrades_count) | **GET** /api/v1/addons/availableUpgradesCount | Get the amount of available addon upgrades
[**addon_get_groups_for_installed_addon**](AddOnsApi.md#addon_get_groups_for_installed_addon) | **GET** /api/v1/addons/{sdkPluginID}/group | Get a list of groups which have the specified add-on installed
[**addon_get_installed_addon**](AddOnsApi.md#addon_get_installed_addon) | **GET** /api/v1/addons/installed/{sdkPluginID} | Get the specified installed add-on.
[**addon_get_installed_addons**](AddOnsApi.md#addon_get_installed_addons) | **GET** /api/v1/addons/installed | List installed add-ons
[**addon_get_institures_for_installed_addon**](AddOnsApi.md#addon_get_institures_for_installed_addon) | **GET** /api/v1/addons/{sdkPluginID}/institute | Get a list of institutes which have the specified add-on installed
[**addon_get_users_for_installed_addon**](AddOnsApi.md#addon_get_users_for_installed_addon) | **GET** /api/v1/addons/{sdkPluginID}/user | Get a list of users which have the specified add-on installed
[**addon_install_addon**](AddOnsApi.md#addon_install_addon) | **POST** /api/v1/addons/install | Install the specified add-on for a given scope.
[**addon_publish_addon**](AddOnsApi.md#addon_publish_addon) | **POST** /api/v1/addons/publish | Publish a new add-on.
[**addon_save_addon_config**](AddOnsApi.md#addon_save_addon_config) | **PUT** /api/v1/addons/configuration | Set the configuration for the specified add-on.
[**addon_sync_addons**](AddOnsApi.md#addon_sync_addons) | **GET** /api/v1/addons/sync | Synchronise the local addons with ones located in the remote sources
[**addon_target_create_target_group**](AddOnsApi.md#addon_target_create_target_group) | **POST** /api/v1/addons/{sdkPluginID}/target/groups | Add new target group
[**addon_target_create_target_organisation**](AddOnsApi.md#addon_target_create_target_organisation) | **POST** /api/v1/addons/{sdkPluginID}/target/organisations | Add new target organisation
[**addon_target_create_target_user**](AddOnsApi.md#addon_target_create_target_user) | **POST** /api/v1/addons/{sdkPluginID}/target/users | Add new target user
[**addon_target_create_targets**](AddOnsApi.md#addon_target_create_targets) | **POST** /api/v1/addons/{sdkPluginID}/target | Create targets for addons (users, organisations and/or groups
[**addon_target_get_groups_outside_target**](AddOnsApi.md#addon_target_get_groups_outside_target) | **GET** /api/v1/addons/{sdkPluginID}/target/validateTarget/group | Get groups for addons that have the add-on installed but do not fall within the specified target
[**addon_target_get_target_groups**](AddOnsApi.md#addon_target_get_target_groups) | **GET** /api/v1/addons/{sdkPluginID}/target/groups | List all target groups for specified addon
[**addon_target_get_target_organisations**](AddOnsApi.md#addon_target_get_target_organisations) | **GET** /api/v1/addons/{sdkPluginID}/target/organisations | List all target organisations for specified addon
[**addon_target_get_target_users**](AddOnsApi.md#addon_target_get_target_users) | **GET** /api/v1/addons/{sdkPluginID}/target/users | List all target users for specified addon
[**addon_target_get_targets**](AddOnsApi.md#addon_target_get_targets) | **GET** /api/v1/addons/{sdkPluginID}/target | Get targets for addons (users, organisations and/or groups
[**addon_target_get_users_outside_target**](AddOnsApi.md#addon_target_get_users_outside_target) | **GET** /api/v1/addons/{sdkPluginID}/target/validateTarget/user | 
[**addon_target_remove_target_group**](AddOnsApi.md#addon_target_remove_target_group) | **DELETE** /api/v1/addons/{sdkPluginID}/target/groups/{groupID} | Remove group target from addon
[**addon_target_remove_target_organisation**](AddOnsApi.md#addon_target_remove_target_organisation) | **DELETE** /api/v1/addons/{sdkPluginID}/target/organisations/{organisationID} | Remove organisation target from addon
[**addon_target_remove_target_user**](AddOnsApi.md#addon_target_remove_target_user) | **DELETE** /api/v1/addons/{sdkPluginID}/target/users/{userID} | Remove user target from addon
[**addon_target_update_targets**](AddOnsApi.md#addon_target_update_targets) | **PUT** /api/v1/addons/{sdkPluginID}/target | Update targets for addons (users, organisations and/or groups
[**addon_uninstall_addon**](AddOnsApi.md#addon_uninstall_addon) | **POST** /api/v1/addons/uninstall | Uninstall the specified add-on for a given scope.
[**addon_update_addon**](AddOnsApi.md#addon_update_addon) | **PUT** /api/v1/addons/publish | Update existing add-on contents.
[**addon_update_all**](AddOnsApi.md#addon_update_all) | **POST** /api/v1/addons/{sdkPluginID}/updateall | Update all other installed versions of this addon to this version
[**addon_upload_media**](AddOnsApi.md#addon_upload_media) | **POST** /api/v1/addons/{sdkPluginID}/media | Add media to the specified add-on.
[**bundle_create_bundle**](AddOnsApi.md#bundle_create_bundle) | **POST** /api/v1/addons/bundles | 
[**bundle_delete_bundle**](AddOnsApi.md#bundle_delete_bundle) | **DELETE** /api/v1/addons/bundles/{BundleID} | 
[**bundle_get_bundles**](AddOnsApi.md#bundle_get_bundles) | **GET** /api/v1/addons/bundles | 
[**bundle_install_bundle**](AddOnsApi.md#bundle_install_bundle) | **POST** /api/v1/addons/bundles/install | 
[**bundle_update_bundle**](AddOnsApi.md#bundle_update_bundle) | **PUT** /api/v1/addons/bundles/{BundleID} | 
[**category_create_category**](AddOnsApi.md#category_create_category) | **POST** /api/v1/addons/categories | 
[**category_delete_category**](AddOnsApi.md#category_delete_category) | **DELETE** /api/v1/addons/categories/{categoryID} | 
[**category_get_categories**](AddOnsApi.md#category_get_categories) | **GET** /api/v1/addons/categories | 
[**category_update_category**](AddOnsApi.md#category_update_category) | **PUT** /api/v1/addons/categories/{categoryID} | 
[**foreign_source_create_foreign_source**](AddOnsApi.md#foreign_source_create_foreign_source) | **POST** /api/v1/addons/sources | Create a new registered source
[**foreign_source_delete_foreign_source**](AddOnsApi.md#foreign_source_delete_foreign_source) | **DELETE** /api/v1/addons/sources/{id} | Remove a registered source
[**foreign_source_get_foreign_source**](AddOnsApi.md#foreign_source_get_foreign_source) | **GET** /api/v1/addons/sources/{id} | Get a specific source
[**foreign_source_get_foreign_sources**](AddOnsApi.md#foreign_source_get_foreign_sources) | **GET** /api/v1/addons/sources | Get a list of registered sources
[**foreign_source_update_foreign_source**](AddOnsApi.md#foreign_source_update_foreign_source) | **PUT** /api/v1/addons/sources/{id} | Update a source
[**permission_get_permissions**](AddOnsApi.md#permission_get_permissions) | **GET** /api/v1/addons/permissions | 
[**sample_type_meta_get_addon_sample_meta**](AddOnsApi.md#sample_type_meta_get_addon_sample_meta) | **GET** /api/v1/addons/sampleTypeMeta | 


# **addon_approve_addon**
> bool addon_approve_addon(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, approve_previous_versions=approve_previous_versions, x_requested_with=x_requested_with)

Approve an addon for installation by end users.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
approve_previous_versions = 'approve_previous_versions_example' # str | Optional: Also approve the previous versions of the add-on (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Approve an addon for installation by end users.
    api_response = api_instance.addon_approve_addon(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, approve_previous_versions=approve_previous_versions, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_approve_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **approve_previous_versions** | **str**| Optional: Also approve the previous versions of the add-on | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_delete_addon**
> bool addon_delete_addon(sdk_plugin_id, x_requested_with=x_requested_with)

Delete the specified installed add-on.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete the specified installed add-on.
    api_response = api_instance.addon_delete_addon(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_delete_addon: %s\n" % e)
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

# **addon_delete_media_from_addon**
> bool addon_delete_media_from_addon(sdk_plugin_id, media_id, x_requested_with=x_requested_with)

Delete given media for the specified add-on.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
media_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete given media for the specified add-on.
    api_response = api_instance.addon_delete_media_from_addon(sdk_plugin_id, media_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_delete_media_from_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **media_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_disable_addon**
> addon_disable_addon(sdk_plugin_id, scope, x_requested_with=x_requested_with)

Disable the specified add-on for the given scope.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
scope = 'scope_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Disable the specified add-on for the given scope.
    api_instance.addon_disable_addon(sdk_plugin_id, scope, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_disable_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **scope** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_enable_addon**
> addon_enable_addon(sdk_plugin_id, scope, x_requested_with=x_requested_with)

Enable the specified add-on for the given scope.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
scope = 'scope_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Enable the specified add-on for the given scope.
    api_instance.addon_enable_addon(sdk_plugin_id, scope, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_enable_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **scope** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_addon**
> PluginDetailed addon_get_addon(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get an available addon by ID for internal use

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an available addon by ID for internal use
    api_response = api_instance.addon_get_addon(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_addon: %s\n" % e)
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

[**PluginDetailed**](PluginDetailed.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_addon_config**
> str addon_get_addon_config(sdk_plugin_id, x_requested_with=x_requested_with)

Get the configuration details for the specified add-on.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the configuration details for the specified add-on.
    api_response = api_instance.addon_get_addon_config(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_addon_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_available_addons**
> PagedOfPluginSmall addon_get_available_addons(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Retrieve list of addons for use in marketplace.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve list of addons for use in marketplace.
    api_response = api_instance.addon_get_available_addons(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_available_addons: %s\n" % e)
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

[**PagedOfPluginSmall**](PagedOfPluginSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_available_addons_grouped_by_version**
> PagedOfPluginSmallVersionGroup addon_get_available_addons_grouped_by_version(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, root_var=root_var, scopes=scopes, x_requested_with=x_requested_with)

Get all available addons grouped by rootVar and included lower versioned add-ons.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
root_var = 'root_var_example' # str | Filter by addon identifier (optional)
scopes = 'scopes_example' # str | Filter by scope (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all available addons grouped by rootVar and included lower versioned add-ons.
    api_response = api_instance.addon_get_available_addons_grouped_by_version(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, root_var=root_var, scopes=scopes, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_available_addons_grouped_by_version: %s\n" % e)
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
 **root_var** | **str**| Filter by addon identifier | [optional] 
 **scopes** | **str**| Filter by scope | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfPluginSmallVersionGroup**](PagedOfPluginSmallVersionGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_available_upgrades_count**
> int addon_get_available_upgrades_count(x_requested_with=x_requested_with)

Get the amount of available addon upgrades

This call gets the amount of available addon upgrades in the marketplace.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the amount of available addon upgrades
    api_response = api_instance.addon_get_available_upgrades_count(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_available_upgrades_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_groups_for_installed_addon**
> list[GroupSmall] addon_get_groups_for_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)

Get a list of groups which have the specified add-on installed

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of groups which have the specified add-on installed
    api_response = api_instance.addon_get_groups_for_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_groups_for_installed_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[GroupSmall]**](GroupSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_installed_addon**
> InstalledAddon addon_get_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)

Get the specified installed add-on.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the specified installed add-on.
    api_response = api_instance.addon_get_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_installed_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**InstalledAddon**](InstalledAddon.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_installed_addons**
> PagedOfInstalledAddon addon_get_installed_addons(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, root_var=root_var, category=category, x_requested_with=x_requested_with)

List installed add-ons

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
root_var = 'root_var_example' # str | Filter by list of rootVars (optional)
category = 'category_example' # str | Filter by category identifiers (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # List installed add-ons
    api_response = api_instance.addon_get_installed_addons(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, root_var=root_var, category=category, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_installed_addons: %s\n" % e)
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
 **root_var** | **str**| Filter by list of rootVars | [optional] 
 **category** | **str**| Filter by category identifiers | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfInstalledAddon**](PagedOfInstalledAddon.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_institures_for_installed_addon**
> list[OrganisationSmall] addon_get_institures_for_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)

Get a list of institutes which have the specified add-on installed

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of institutes which have the specified add-on installed
    api_response = api_instance.addon_get_institures_for_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_institures_for_installed_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[OrganisationSmall]**](OrganisationSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_get_users_for_installed_addon**
> list[UserSmall] addon_get_users_for_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)

Get a list of users which have the specified add-on installed

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of users which have the specified add-on installed
    api_response = api_instance.addon_get_users_for_installed_addon(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_get_users_for_installed_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[UserSmall]**](UserSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_install_addon**
> int addon_install_addon(addon, x_requested_with=x_requested_with)

Install the specified add-on for a given scope.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
addon = swagger_client.ScopedAddon() # ScopedAddon | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Install the specified add-on for a given scope.
    api_response = api_instance.addon_install_addon(addon, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_install_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon** | [**ScopedAddon**](ScopedAddon.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_publish_addon**
> PluginSmall addon_publish_addon(addon, x_requested_with=x_requested_with)

Publish a new add-on.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
addon = swagger_client.AddonPublish() # AddonPublish | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Publish a new add-on.
    api_response = api_instance.addon_publish_addon(addon, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_publish_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon** | [**AddonPublish**](AddonPublish.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PluginSmall**](PluginSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_save_addon_config**
> addon_save_addon_config(config, x_requested_with=x_requested_with)

Set the configuration for the specified add-on.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
config = swagger_client.AddonConfiguration() # AddonConfiguration | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Set the configuration for the specified add-on.
    api_instance.addon_save_addon_config(config, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_save_addon_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**AddonConfiguration**](AddonConfiguration.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_sync_addons**
> list[PluginDetailed] addon_sync_addons(x_requested_with=x_requested_with)

Synchronise the local addons with ones located in the remote sources

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Synchronise the local addons with ones located in the remote sources
    api_response = api_instance.addon_sync_addons(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_sync_addons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[PluginDetailed]**](PluginDetailed.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_create_target_group**
> SDKTargetGroupMap addon_target_create_target_group(sdk_plugin_id, target_group, x_requested_with=x_requested_with)

Add new target group

Create new target group to display/install this adddon.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
target_group = swagger_client.TargetGroup() # TargetGroup | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add new target group
    api_response = api_instance.addon_target_create_target_group(sdk_plugin_id, target_group, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_create_target_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **target_group** | [**TargetGroup**](TargetGroup.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SDKTargetGroupMap**](SDKTargetGroupMap.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_create_target_organisation**
> SDKTargetOrganisationMap addon_target_create_target_organisation(sdk_plugin_id, target_organisation, x_requested_with=x_requested_with)

Add new target organisation

Create new target organisation to display/install this adddon.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
target_organisation = swagger_client.TargetOrganisation() # TargetOrganisation | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add new target organisation
    api_response = api_instance.addon_target_create_target_organisation(sdk_plugin_id, target_organisation, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_create_target_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **target_organisation** | [**TargetOrganisation**](TargetOrganisation.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SDKTargetOrganisationMap**](SDKTargetOrganisationMap.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_create_target_user**
> SDKTargetUserMap addon_target_create_target_user(sdk_plugin_id, target_user, x_requested_with=x_requested_with)

Add new target user

Create new target user to display/install this adddon.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
target_user = swagger_client.TargetUser() # TargetUser | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add new target user
    api_response = api_instance.addon_target_create_target_user(sdk_plugin_id, target_user, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_create_target_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **target_user** | [**TargetUser**](TargetUser.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SDKTargetUserMap**](SDKTargetUserMap.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_create_targets**
> addon_target_create_targets(sdk_plugin_id, targets, x_requested_with=x_requested_with)

Create targets for addons (users, organisations and/or groups

Create targets for addons (users, organisations and/or groups

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
targets = swagger_client.MixedTargets() # MixedTargets | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create targets for addons (users, organisations and/or groups
    api_instance.addon_target_create_targets(sdk_plugin_id, targets, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_create_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **targets** | [**MixedTargets**](MixedTargets.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_get_groups_outside_target**
> list[GroupSmall] addon_target_get_groups_outside_target(sdk_plugin_id, x_requested_with=x_requested_with)

Get groups for addons that have the add-on installed but do not fall within the specified target

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get groups for addons that have the add-on installed but do not fall within the specified target
    api_response = api_instance.addon_target_get_groups_outside_target(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_get_groups_outside_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[GroupSmall]**](GroupSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_get_target_groups**
> list[GroupSmall] addon_target_get_target_groups(sdk_plugin_id, x_requested_with=x_requested_with)

List all target groups for specified addon

Lists the targets groups that are allowed to see display/install this addon.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # List all target groups for specified addon
    api_response = api_instance.addon_target_get_target_groups(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_get_target_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[GroupSmall]**](GroupSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_get_target_organisations**
> list[OrganisationSmall] addon_target_get_target_organisations(sdk_plugin_id, x_requested_with=x_requested_with)

List all target organisations for specified addon

Lists the targets organisations that are allowed to see display/install this addon.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # List all target organisations for specified addon
    api_response = api_instance.addon_target_get_target_organisations(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_get_target_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[OrganisationSmall]**](OrganisationSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_get_target_users**
> list[UserSmall] addon_target_get_target_users(sdk_plugin_id, x_requested_with=x_requested_with)

List all target users for specified addon

Lists the targets users that are allowed to see display/install this addon.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # List all target users for specified addon
    api_response = api_instance.addon_target_get_target_users(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_get_target_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[UserSmall]**](UserSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_get_targets**
> MixedTargets addon_target_get_targets(sdk_plugin_id, x_requested_with=x_requested_with)

Get targets for addons (users, organisations and/or groups

Get targets for addons (users, organisations and/or groups

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get targets for addons (users, organisations and/or groups
    api_response = api_instance.addon_target_get_targets(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_get_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**MixedTargets**](MixedTargets.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_get_users_outside_target**
> list[UserSmall] addon_target_get_users_outside_target(sdk_plugin_id, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.addon_target_get_users_outside_target(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_get_users_outside_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[UserSmall]**](UserSmall.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_remove_target_group**
> addon_target_remove_target_group(sdk_plugin_id, group_id, x_requested_with=x_requested_with)

Remove group target from addon

Remove group from list of groups that can install/display this addon

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
group_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove group target from addon
    api_instance.addon_target_remove_target_group(sdk_plugin_id, group_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_remove_target_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **group_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_remove_target_organisation**
> addon_target_remove_target_organisation(sdk_plugin_id, organisation_id, x_requested_with=x_requested_with)

Remove organisation target from addon

Remove organisation from list of organisations that can install/display this addon

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
organisation_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove organisation target from addon
    api_instance.addon_target_remove_target_organisation(sdk_plugin_id, organisation_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_remove_target_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **organisation_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_remove_target_user**
> addon_target_remove_target_user(sdk_plugin_id, user_id, x_requested_with=x_requested_with)

Remove user target from addon

Remove user from list of users that can install/display this addon

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
user_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove user target from addon
    api_instance.addon_target_remove_target_user(sdk_plugin_id, user_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_remove_target_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **user_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_target_update_targets**
> addon_target_update_targets(sdk_plugin_id, targets, x_requested_with=x_requested_with)

Update targets for addons (users, organisations and/or groups

Update targets for addons (users, organisations and/or groups

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
targets = swagger_client.MixedTargets() # MixedTargets | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update targets for addons (users, organisations and/or groups
    api_instance.addon_target_update_targets(sdk_plugin_id, targets, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_target_update_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **targets** | [**MixedTargets**](MixedTargets.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_uninstall_addon**
> bool addon_uninstall_addon(addon, x_requested_with=x_requested_with)

Uninstall the specified add-on for a given scope.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
addon = swagger_client.ScopedAddon() # ScopedAddon | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Uninstall the specified add-on for a given scope.
    api_response = api_instance.addon_uninstall_addon(addon, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_uninstall_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon** | [**ScopedAddon**](ScopedAddon.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_update_addon**
> PluginDetailed addon_update_addon(addon, x_requested_with=x_requested_with)

Update existing add-on contents.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
addon = swagger_client.AddonPublish() # AddonPublish | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update existing add-on contents.
    api_response = api_instance.addon_update_addon(addon, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_update_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon** | [**AddonPublish**](AddonPublish.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PluginDetailed**](PluginDetailed.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_update_all**
> dict(str, int) addon_update_all(sdk_plugin_id, x_requested_with=x_requested_with)

Update all other installed versions of this addon to this version

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update all other installed versions of this addon to this version
    api_response = api_instance.addon_update_all(sdk_plugin_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_update_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**dict(str, int)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_upload_media**
> int addon_upload_media(sdk_plugin_id, parameters, x_requested_with=x_requested_with)

Add media to the specified add-on.

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
parameters = swagger_client.MediaFile() # MediaFile | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add media to the specified add-on.
    api_response = api_instance.addon_upload_media(sdk_plugin_id, parameters, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->addon_upload_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **parameters** | [**MediaFile**](MediaFile.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_create_bundle**
> AddonBundle bundle_create_bundle(create_bundle, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
create_bundle = swagger_client.AddonBundleDTO() # AddonBundleDTO | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.bundle_create_bundle(create_bundle, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->bundle_create_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bundle** | [**AddonBundleDTO**](AddonBundleDTO.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonBundle**](AddonBundle.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_delete_bundle**
> AddonBundle bundle_delete_bundle(bundle_id, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
bundle_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.bundle_delete_bundle(bundle_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->bundle_delete_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonBundle**](AddonBundle.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_get_bundles**
> list[AddonBundle] bundle_get_bundles(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.bundle_get_bundles(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->bundle_get_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[AddonBundle]**](AddonBundle.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_install_bundle**
> list[object] bundle_install_bundle(bundle, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
bundle = swagger_client.ScopedBundle() # ScopedBundle | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.bundle_install_bundle(bundle, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->bundle_install_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | [**ScopedBundle**](ScopedBundle.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[object]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_update_bundle**
> AddonBundle bundle_update_bundle(create_bundle, bundle_id, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
create_bundle = swagger_client.AddonBundleDTO() # AddonBundleDTO | 
bundle_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.bundle_update_bundle(create_bundle, bundle_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->bundle_update_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bundle** | [**AddonBundleDTO**](AddonBundleDTO.md)|  | 
 **bundle_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonBundle**](AddonBundle.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_create_category**
> AddonCategory category_create_category(create_category, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
create_category = swagger_client.CategoryDTO() # CategoryDTO | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.category_create_category(create_category, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->category_create_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_category** | [**CategoryDTO**](CategoryDTO.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonCategory**](AddonCategory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_delete_category**
> AddonCategory category_delete_category(category_id, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
category_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.category_delete_category(category_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->category_delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonCategory**](AddonCategory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_get_categories**
> list[AddonCategory] category_get_categories(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.category_get_categories(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->category_get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[AddonCategory]**](AddonCategory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **category_update_category**
> AddonCategory category_update_category(create_category, category_id, x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
create_category = swagger_client.CategoryDTO() # CategoryDTO | 
category_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.category_update_category(create_category, category_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->category_update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_category** | [**CategoryDTO**](CategoryDTO.md)|  | 
 **category_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonCategory**](AddonCategory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **foreign_source_create_foreign_source**
> ForeignSource foreign_source_create_foreign_source(source, x_requested_with=x_requested_with)

Create a new registered source

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
source = swagger_client.ForeignSource() # ForeignSource | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new registered source
    api_response = api_instance.foreign_source_create_foreign_source(source, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->foreign_source_create_foreign_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**ForeignSource**](ForeignSource.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ForeignSource**](ForeignSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **foreign_source_delete_foreign_source**
> int foreign_source_delete_foreign_source(id, x_requested_with=x_requested_with)

Remove a registered source

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove a registered source
    api_response = api_instance.foreign_source_delete_foreign_source(id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->foreign_source_delete_foreign_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **foreign_source_get_foreign_source**
> ForeignSource foreign_source_get_foreign_source(id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a specific source

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a specific source
    api_response = api_instance.foreign_source_get_foreign_source(id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->foreign_source_get_foreign_source: %s\n" % e)
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

[**ForeignSource**](ForeignSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **foreign_source_get_foreign_sources**
> list[ForeignSource] foreign_source_get_foreign_sources(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a list of registered sources

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of registered sources
    api_response = api_instance.foreign_source_get_foreign_sources(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->foreign_source_get_foreign_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[ForeignSource]**](ForeignSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **foreign_source_update_foreign_source**
> ForeignSource foreign_source_update_foreign_source(id, source, x_requested_with=x_requested_with)

Update a source

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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
source = swagger_client.ForeignSource() # ForeignSource | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a source
    api_response = api_instance.foreign_source_update_foreign_source(id, source, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->foreign_source_update_foreign_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **source** | [**ForeignSource**](ForeignSource.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ForeignSource**](ForeignSource.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_get_permissions**
> MarketPlacePermission permission_get_permissions(x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.permission_get_permissions(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->permission_get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**MarketPlacePermission**](MarketPlacePermission.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_meta_get_addon_sample_meta**
> list[AddonSampleTypeMeta] sample_type_meta_get_addon_sample_meta(x_requested_with=x_requested_with)



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
api_instance = swagger_client.AddOnsApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.sample_type_meta_get_addon_sample_meta(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->sample_type_meta_get_addon_sample_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[AddonSampleTypeMeta]**](AddonSampleTypeMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

