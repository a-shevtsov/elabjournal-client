# elabjournal_client.AuthenticationApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_auth_user**](AuthenticationApi.md#authentication_auth_user) | **POST** /api/v1/auth/user | Authenticate and obtain an API token for a user.
[**authentication_check_app_version**](AuthenticationApi.md#authentication_check_app_version) | **GET** /api/v1/auth/checkAppVersion | 
[**authentication_exchange_token**](AuthenticationApi.md#authentication_exchange_token) | **POST** /api/v1/auth/user/exchangeToken | Obtain an API token for a user, based on a request token generated while using the Add-On authentication flow for 3rd party systems.
[**authentication_user_info**](AuthenticationApi.md#authentication_user_info) | **GET** /api/v1/auth/user | Get authentication details that you&#39;re currently using


# **authentication_auth_user**
> AuthResponse authentication_auth_user(body, x_requested_with=x_requested_with)

Authenticate and obtain an API token for a user.

  Supplying only a username and password in the body is sufficient for most users.    Example:  ```  {    \"username\": \"demo@elabjournal.com\",    \"password\": \"abc123\"  }  ```    You can use the resulting token property in the api_key field above to access all other API calls.  

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
api_instance = elabjournal_client.AuthenticationApi(elabjournal_client.ApiClient(configuration))
body = elabjournal_client.AuthRequest() # AuthRequest | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Authenticate and obtain an API token for a user.
    api_response = api_instance.authentication_auth_user(body, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_auth_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthRequest**](AuthRequest.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_check_app_version**
> object authentication_check_app_version(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)



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
api_instance = elabjournal_client.AuthenticationApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.authentication_check_app_version(expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_check_app_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **authentication_exchange_token**
> AuthRequestTokenResponse authentication_exchange_token(body, x_requested_with=x_requested_with)

Obtain an API token for a user, based on a request token generated while using the Add-On authentication flow for 3rd party systems.

    Example:  ```  {    \"requestToken\": \"abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc1\"  }  ```    You can use the resulting apiToken property in the api_key field above to access all other API calls.  

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
api_instance = elabjournal_client.AuthenticationApi(elabjournal_client.ApiClient(configuration))
body = elabjournal_client.AuthRequestToken() # AuthRequestToken | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Obtain an API token for a user, based on a request token generated while using the Add-On authentication flow for 3rd party systems.
    api_response = api_instance.authentication_exchange_token(body, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_exchange_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthRequestToken**](AuthRequestToken.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AuthRequestTokenResponse**](AuthRequestTokenResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_user_info**
> AuthResponse authentication_user_info(expand=expand, view_id=view_id, view_columns=view_columns, field=field, x_requested_with=x_requested_with)

Get authentication details that you're currently using

In most cases set the body to:  ```  {}  ```    Add the following body to the request to receive a \"domain\" field in the response that points to the correct endpoint in case the user is located on another eLab deployment:  ```  {    \"domain\": \"my.current.domain\"  }  ```

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
api_instance = elabjournal_client.AuthenticationApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
field = 'field_example' # str | A specific field to request (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get authentication details that you're currently using
    api_response = api_instance.authentication_user_info(expand=expand, view_id=view_id, view_columns=view_columns, field=field, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **field** | **str**| A specific field to request | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

