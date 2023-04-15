# swagger_client.AddOnLicensesApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addon_license_create_addon_license_type**](AddOnLicensesApi.md#addon_license_create_addon_license_type) | **POST** /api/v1/addons/licenses/types/{licenseType}/link/{rootVar} | Create license type for add-on with given rootVar
[**addon_license_delete_addon_license_type**](AddOnLicensesApi.md#addon_license_delete_addon_license_type) | **DELETE** /api/v1/addons/licenses/types/{licenseType}/link/{rootVar} | Delete link between license type and rootVar
[**addon_license_get_expired_licenses**](AddOnLicensesApi.md#addon_license_get_expired_licenses) | **GET** /api/v1/addons/licenses/expired | Retrieve all expired add-on licenses
[**addon_license_get_license**](AddOnLicensesApi.md#addon_license_get_license) | **GET** /api/v1/addons/licenses/{rootVar} | Retrieve license for add-on with given rootVar
[**addon_license_get_license_type**](AddOnLicensesApi.md#addon_license_get_license_type) | **GET** /api/v1/addons/licenses/types/{rootVar} | Retrieve license type for add-on with given rootVar
[**addon_license_get_license_types**](AddOnLicensesApi.md#addon_license_get_license_types) | **GET** /api/v1/addons/licenses/types | Retrieve all license types
[**addon_license_get_licenses**](AddOnLicensesApi.md#addon_license_get_licenses) | **GET** /api/v1/addons/licenses | Retrieve all add-on licenses
[**addon_license_purchase_license**](AddOnLicensesApi.md#addon_license_purchase_license) | **POST** /api/v1/addons/licenses/{rootVar}/request | Purchase license for add-on with given rootVar
[**addon_license_start_trial**](AddOnLicensesApi.md#addon_license_start_trial) | **POST** /api/v1/addons/licenses/{rootVar}/trial | Start a trial for add-on with given rootVar
[**addon_license_update_addon_license_type**](AddOnLicensesApi.md#addon_license_update_addon_license_type) | **PUT** /api/v1/addons/licenses/types/{licenseType}/link/{rootVar} | Update license type for add-on with given rootVar


# **addon_license_create_addon_license_type**
> AddonLicenseType addon_license_create_addon_license_type(license_type, root_var, x_requested_with=x_requested_with)

Create license type for add-on with given rootVar

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
license_type = 'license_type_example' # str | 
root_var = 'root_var_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create license type for add-on with given rootVar
    api_response = api_instance.addon_license_create_addon_license_type(license_type, root_var, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_create_addon_license_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_type** | **str**|  | 
 **root_var** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonLicenseType**](AddonLicenseType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_delete_addon_license_type**
> bool addon_license_delete_addon_license_type(license_type, root_var, x_requested_with=x_requested_with)

Delete link between license type and rootVar

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
license_type = 'license_type_example' # str | 
root_var = 'root_var_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete link between license type and rootVar
    api_response = api_instance.addon_license_delete_addon_license_type(license_type, root_var, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_delete_addon_license_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_type** | **str**|  | 
 **root_var** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_get_expired_licenses**
> list[AddonLicense] addon_license_get_expired_licenses(x_requested_with=x_requested_with)

Retrieve all expired add-on licenses

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve all expired add-on licenses
    api_response = api_instance.addon_license_get_expired_licenses(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_get_expired_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[AddonLicense]**](AddonLicense.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_get_license**
> AddonLicense addon_license_get_license(root_var, scope=scope, x_requested_with=x_requested_with)

Retrieve license for add-on with given rootVar

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
root_var = 'root_var_example' # str | 
scope = 'scope_example' # str |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve license for add-on with given rootVar
    api_response = api_instance.addon_license_get_license(root_var, scope=scope, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_get_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_var** | **str**|  | 
 **scope** | **str**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonLicense**](AddonLicense.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_get_license_type**
> AddonLicenseType addon_license_get_license_type(root_var, x_requested_with=x_requested_with)

Retrieve license type for add-on with given rootVar

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
root_var = 'root_var_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve license type for add-on with given rootVar
    api_response = api_instance.addon_license_get_license_type(root_var, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_get_license_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_var** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonLicenseType**](AddonLicenseType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_get_license_types**
> list[AddonLicenseType] addon_license_get_license_types(x_requested_with=x_requested_with)

Retrieve all license types

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve all license types
    api_response = api_instance.addon_license_get_license_types(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_get_license_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[AddonLicenseType]**](AddonLicenseType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_get_licenses**
> list[AddonLicense] addon_license_get_licenses(x_requested_with=x_requested_with)

Retrieve all add-on licenses

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve all add-on licenses
    api_response = api_instance.addon_license_get_licenses(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_get_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[AddonLicense]**](AddonLicense.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_purchase_license**
> bool addon_license_purchase_license(root_var, body, x_requested_with=x_requested_with)

Purchase license for add-on with given rootVar

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
root_var = 'root_var_example' # str | 
body = NULL # object | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Purchase license for add-on with given rootVar
    api_response = api_instance.addon_license_purchase_license(root_var, body, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_purchase_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_var** | **str**|  | 
 **body** | **object**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_start_trial**
> bool addon_license_start_trial(root_var, x_requested_with=x_requested_with)

Start a trial for add-on with given rootVar

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
root_var = 'root_var_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Start a trial for add-on with given rootVar
    api_response = api_instance.addon_license_start_trial(root_var, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_start_trial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_var** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_license_update_addon_license_type**
> AddonLicenseType addon_license_update_addon_license_type(license_type, root_var, x_requested_with=x_requested_with)

Update license type for add-on with given rootVar

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
api_instance = swagger_client.AddOnLicensesApi(swagger_client.ApiClient(configuration))
license_type = 'license_type_example' # str | 
root_var = 'root_var_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update license type for add-on with given rootVar
    api_response = api_instance.addon_license_update_addon_license_type(license_type, root_var, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnLicensesApi->addon_license_update_addon_license_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_type** | **str**|  | 
 **root_var** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**AddonLicenseType**](AddonLicenseType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

