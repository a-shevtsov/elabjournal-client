# elabjournal_client.OAuth2Api

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth2_redirect_build_redirect_url**](OAuth2Api.md#o_auth2_redirect_build_redirect_url) | **GET** /api/v1/oauth2/redirect | OAuth2 redirect URI
[**o_auth2_redirect_handle_oauth2_request_from_remote**](OAuth2Api.md#o_auth2_redirect_handle_oauth2_request_from_remote) | **POST** /api/v1/oauth2/proxy | 


# **o_auth2_redirect_build_redirect_url**
> o_auth2_redirect_build_redirect_url(state, code, x_requested_with=x_requested_with)

OAuth2 redirect URI

Redirect url to be used within OAuth 2.0 applications. This endpoint understants `state` and `code` parameters which will be passed down to the endpoint that is encryped in the the `state` param.

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
api_instance = elabjournal_client.OAuth2Api(elabjournal_client.ApiClient(configuration))
state = 'state_example' # str | 
code = 'code_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # OAuth2 redirect URI
    api_instance.o_auth2_redirect_build_redirect_url(state, code, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling OAuth2Api->o_auth2_redirect_build_redirect_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **code** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth2_redirect_handle_oauth2_request_from_remote**
> OAuthResponse o_auth2_redirect_handle_oauth2_request_from_remote(o_auth_proxy_request, x_requested_with=x_requested_with)



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
api_instance = elabjournal_client.OAuth2Api(elabjournal_client.ApiClient(configuration))
o_auth_proxy_request = elabjournal_client.OAuthProxyRequest() # OAuthProxyRequest | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    api_response = api_instance.o_auth2_redirect_handle_oauth2_request_from_remote(o_auth_proxy_request, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuth2Api->o_auth2_redirect_handle_oauth2_request_from_remote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_proxy_request** | [**OAuthProxyRequest**](OAuthProxyRequest.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**OAuthResponse**](OAuthResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

