# swagger_client.AddOnOAuthApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth2_create_configuration**](AddOnOAuthApi.md#o_auth2_create_configuration) | **POST** /api/v1/addons/{sdkPluginID}/oauthConfig | Create new oAuthConfiguration
[**o_auth2_get_access_token**](AddOnOAuthApi.md#o_auth2_get_access_token) | **GET** /api/v1/addons/{sdkPluginID}/oauthConfig/getAccessToken | Retrieve access token by sdkPluginID
[**o_auth2_get_authentication_uri**](AddOnOAuthApi.md#o_auth2_get_authentication_uri) | **GET** /api/v1/addons/{sdkPluginID}/oauthConfig/getAuthUrl | Retrieve authentication URI by sdkPluginID
[**o_auth2_get_oauth_configuration**](AddOnOAuthApi.md#o_auth2_get_oauth_configuration) | **GET** /api/v1/addons/{sdkPluginID}/oauthConfig | Retrieve OAuth configuration by sdkPluginID
[**o_auth2_refresh_access_and_refresh_token**](AddOnOAuthApi.md#o_auth2_refresh_access_and_refresh_token) | **POST** /api/v1/addons/{sdkPluginID}/oauthConfig/refreshAccessAndRefreshToken | Refresh access and refresh token
[**o_auth2_set_access_and_refresh_token**](AddOnOAuthApi.md#o_auth2_set_access_and_refresh_token) | **POST** /api/v1/addons/{sdkPluginID}/oauthConfig/setAccessAndRefreshToken | Request access and refresh token by temporary code


# **o_auth2_create_configuration**
> o_auth2_create_configuration(sdk_plugin_id, o_auth_configuration, x_requested_with=x_requested_with)

Create new oAuthConfiguration

Creates a OAuth 2.0 configuration to be used by a addon installed via the eLab Marketplace. You can choose to encrypt the client secret in the database aswel with the `isEncoded` property. If your eLab installation is also serving as host for public addons you can choose to distribute the OAuth 2.0 configuration when addons are synced. If `isPublic` is enabled the `clientSecret` will be encrypted by default.   Example: ```json {   'sdkPluginID': 123,    'description': 'config for my addon',    'authorizationURI': 'https://example.com/authEndpoint',   'tokenRequestURI': 'https://example.com/tokenRequestEndpoint',   'refreshURI': 'https://example.com/tokenRefreshEndpoint',   'clientID': '123456',   'clientSecret': '123456',   'isEncoded': true,    'isPublic': true }```

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
api_instance = swagger_client.AddOnOAuthApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
o_auth_configuration = swagger_client.OAuthConfiguration() # OAuthConfiguration | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create new oAuthConfiguration
    api_instance.o_auth2_create_configuration(sdk_plugin_id, o_auth_configuration, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnOAuthApi->o_auth2_create_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **o_auth_configuration** | [**OAuthConfiguration**](OAuthConfiguration.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth2_get_access_token**
> o_auth2_get_access_token(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)

Retrieve access token by sdkPluginID

Retrieve the access token for the given sdkPluginID

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
api_instance = swagger_client.AddOnOAuthApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
scope = 'scope_example' # str | Filter by scope (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve access token by sdkPluginID
    api_instance.o_auth2_get_access_token(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnOAuthApi->o_auth2_get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **scope** | **str**| Filter by scope | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth2_get_authentication_uri**
> o_auth2_get_authentication_uri(sdk_plugin_id, x_requested_with=x_requested_with)

Retrieve authentication URI by sdkPluginID

Retrieve the OAuth 2.0 request URL for the given sdkPluginID

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
api_instance = swagger_client.AddOnOAuthApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve authentication URI by sdkPluginID
    api_instance.o_auth2_get_authentication_uri(sdk_plugin_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnOAuthApi->o_auth2_get_authentication_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth2_get_oauth_configuration**
> o_auth2_get_oauth_configuration(sdk_plugin_id, x_requested_with=x_requested_with)

Retrieve OAuth configuration by sdkPluginID

Retrieve the OAuth 2.0 config  for the given sdkPluginID

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
api_instance = swagger_client.AddOnOAuthApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve OAuth configuration by sdkPluginID
    api_instance.o_auth2_get_oauth_configuration(sdk_plugin_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnOAuthApi->o_auth2_get_oauth_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth2_refresh_access_and_refresh_token**
> o_auth2_refresh_access_and_refresh_token(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)

Refresh access and refresh token

Refresh the access and refresh token for the given sdkPluginID

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
api_instance = swagger_client.AddOnOAuthApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
scope = 'scope_example' # str | Filter by scope (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Refresh access and refresh token
    api_instance.o_auth2_refresh_access_and_refresh_token(sdk_plugin_id, expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnOAuthApi->o_auth2_refresh_access_and_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **scope** | **str**| Filter by scope | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth2_set_access_and_refresh_token**
> o_auth2_set_access_and_refresh_token(sdk_plugin_id, token_request, expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)

Request access and refresh token by temporary code

Request a access and refresh token with a short lived `code` property.   Example: ```json {   'code': '123456' }```

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
api_instance = swagger_client.AddOnOAuthApi(swagger_client.ApiClient(configuration))
sdk_plugin_id = 56 # int | 
token_request = swagger_client.TokenRequest() # TokenRequest | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
scope = 'scope_example' # str | Filter by scope (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Request access and refresh token by temporary code
    api_instance.o_auth2_set_access_and_refresh_token(sdk_plugin_id, token_request, expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling AddOnOAuthApi->o_auth2_set_access_and_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_plugin_id** | **int**|  | 
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **scope** | **str**| Filter by scope | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

