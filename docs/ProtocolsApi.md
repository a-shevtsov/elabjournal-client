# elabjournal_client.ProtocolsApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocol_log_get_protocol_logs**](ProtocolsApi.md#protocol_log_get_protocol_logs) | **GET** /api/v1/protocols/{protID}/logs | Get log records for a protocol
[**protocol_saml_sign_saml_sign_protocol**](ProtocolsApi.md#protocol_saml_sign_saml_sign_protocol) | **POST** /api/v1/protocols/{protID}/sign/saml | Sign a protocol using SAML authentication
[**protocol_saml_sign_saml_witness_sign_protocol**](ProtocolsApi.md#protocol_saml_sign_saml_witness_sign_protocol) | **POST** /api/v1/protocols/{protID}/witness/sign/saml | Witness sign a protocol using SAML authentication
[**protocol_sign_decline_protocol**](ProtocolsApi.md#protocol_sign_decline_protocol) | **POST** /api/v1/protocols/{protID}/witness/decline | Decline a protocol sign request
[**protocol_sign_get_declined_witness_signatures**](ProtocolsApi.md#protocol_sign_get_declined_witness_signatures) | **GET** /api/v1/protocols/signatures/declined | Retrieve declined witness signatures
[**protocol_sign_get_pending_witness_signatures**](ProtocolsApi.md#protocol_sign_get_pending_witness_signatures) | **GET** /api/v1/protocols/signatures/pending | Retrieve pending witness signatures
[**protocol_sign_get_witnesses_candidates**](ProtocolsApi.md#protocol_sign_get_witnesses_candidates) | **GET** /api/v1/protocols/{protID}/witnessCandidates | Retrieve list of possible sign witnesses for this protocol
[**protocol_sign_re_assign_witness**](ProtocolsApi.md#protocol_sign_re_assign_witness) | **POST** /api/v1/protocols/{protID}/sign/reassignWitness | Reassign a witness
[**protocol_sign_sign_protocol**](ProtocolsApi.md#protocol_sign_sign_protocol) | **POST** /api/v1/protocols/{protID}/sign | Sign a protocol
[**protocol_sign_witness_sign_protocol**](ProtocolsApi.md#protocol_sign_witness_sign_protocol) | **POST** /api/v1/protocols/{protID}/witness/sign | Witness sign a protocol
[**protocols_add_protocol_category**](ProtocolsApi.md#protocols_add_protocol_category) | **POST** /api/v1/protocols/categories | Add protocol category
[**protocols_archive_protocol_category**](ProtocolsApi.md#protocols_archive_protocol_category) | **DELETE** /api/v1/protocols/categories | Archive protocol category
[**protocols_get_categories**](ProtocolsApi.md#protocols_get_categories) | **GET** /api/v1/protocols/categories | Get available protocol categories
[**protocols_get_protocol_by_id**](ProtocolsApi.md#protocols_get_protocol_by_id) | **GET** /api/v1/protocols/{protID} | Get a protocol by id
[**protocols_get_protocol_by_protocol_version_id**](ProtocolsApi.md#protocols_get_protocol_by_protocol_version_id) | **GET** /api/v1/protocols/version/{protVersionID} | Get a protocol by its version id
[**protocols_get_protocol_digest**](ProtocolsApi.md#protocols_get_protocol_digest) | **GET** /api/v1/protocols/digest | Get protocol digest
[**protocols_get_protocol_file**](ProtocolsApi.md#protocols_get_protocol_file) | **GET** /api/v1/protocols/file/{fileID} | Get protocol file
[**protocols_get_protocol_list**](ProtocolsApi.md#protocols_get_protocol_list) | **GET** /api/v1/protocols | Get protocols


# **protocol_log_get_protocol_logs**
> PagedOfProtocolLog protocol_log_get_protocol_logs(prot_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get log records for a protocol

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get log records for a protocol
    api_response = api_instance.protocol_log_get_protocol_logs(prot_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_log_get_protocol_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfProtocolLog**](PagedOfProtocolLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_saml_sign_saml_sign_protocol**
> protocol_saml_sign_saml_sign_protocol(prot_id, witness_user_id, x_requested_with=x_requested_with)

Sign a protocol using SAML authentication

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
witness_user_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Sign a protocol using SAML authentication
    api_instance.protocol_saml_sign_saml_sign_protocol(prot_id, witness_user_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_saml_sign_saml_sign_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **witness_user_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_saml_sign_saml_witness_sign_protocol**
> protocol_saml_sign_saml_witness_sign_protocol(prot_id, x_requested_with=x_requested_with)

Witness sign a protocol using SAML authentication

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Witness sign a protocol using SAML authentication
    api_instance.protocol_saml_sign_saml_witness_sign_protocol(prot_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_saml_sign_saml_witness_sign_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_sign_decline_protocol**
> protocol_sign_decline_protocol(prot_id, reason, x_requested_with=x_requested_with)

Decline a protocol sign request

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
reason = 'reason_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Decline a protocol sign request
    api_instance.protocol_sign_decline_protocol(prot_id, reason, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_sign_decline_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **reason** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/hl7-v2, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_sign_get_declined_witness_signatures**
> PagedOfDeclinedSignatureDTO protocol_sign_get_declined_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Retrieve declined witness signatures

Retrieve all declined witness signatures for the current user.

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve declined witness signatures
    api_response = api_instance.protocol_sign_get_declined_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_sign_get_declined_witness_signatures: %s\n" % e)
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

[**PagedOfDeclinedSignatureDTO**](PagedOfDeclinedSignatureDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_sign_get_pending_witness_signatures**
> PagedOfPendingSignatureDTO protocol_sign_get_pending_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Retrieve pending witness signatures

Retrieve all pending witness signatures for the current user.

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve pending witness signatures
    api_response = api_instance.protocol_sign_get_pending_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_sign_get_pending_witness_signatures: %s\n" % e)
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

[**PagedOfPendingSignatureDTO**](PagedOfPendingSignatureDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_sign_get_witnesses_candidates**
> PagedOfProtocolWitnessDTO protocol_sign_get_witnesses_candidates(prot_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Retrieve list of possible sign witnesses for this protocol

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve list of possible sign witnesses for this protocol
    api_response = api_instance.protocol_sign_get_witnesses_candidates(prot_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_sign_get_witnesses_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfProtocolWitnessDTO**](PagedOfProtocolWitnessDTO.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_sign_re_assign_witness**
> protocol_sign_re_assign_witness(prot_id, witness_user_id, x_requested_with=x_requested_with)

Reassign a witness

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
witness_user_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Reassign a witness
    api_instance.protocol_sign_re_assign_witness(prot_id, witness_user_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_sign_re_assign_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **witness_user_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_sign_sign_protocol**
> protocol_sign_sign_protocol(prot_id, protocol_sign_credentials_dto, x_requested_with=x_requested_with)

Sign a protocol

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
protocol_sign_credentials_dto = elabjournal_client.SignProtocolCredentialsDTO() # SignProtocolCredentialsDTO | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Sign a protocol
    api_instance.protocol_sign_sign_protocol(prot_id, protocol_sign_credentials_dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_sign_sign_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **protocol_sign_credentials_dto** | [**SignProtocolCredentialsDTO**](SignProtocolCredentialsDTO.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocol_sign_witness_sign_protocol**
> protocol_sign_witness_sign_protocol(prot_id, protocol_sign_credentials_dto, x_requested_with=x_requested_with)

Witness sign a protocol

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
protocol_sign_credentials_dto = elabjournal_client.SignProtocolCredentialsDTO() # SignProtocolCredentialsDTO | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Witness sign a protocol
    api_instance.protocol_sign_witness_sign_protocol(prot_id, protocol_sign_credentials_dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocol_sign_witness_sign_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **protocol_sign_credentials_dto** | [**SignProtocolCredentialsDTO**](SignProtocolCredentialsDTO.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_add_protocol_category**
> protocols_add_protocol_category(dto, x_requested_with=x_requested_with)

Add protocol category

This call adds a protocol category. System admins are able to add public categories by using groupID: 0. Group admins are able to add group specific protocol categories with this call.

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
dto = elabjournal_client.ProtocolCategoryNew() # ProtocolCategoryNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add protocol category
    api_instance.protocols_add_protocol_category(dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_add_protocol_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**ProtocolCategoryNew**](ProtocolCategoryNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_archive_protocol_category**
> protocols_archive_protocol_category(protocol_category_id, x_requested_with=x_requested_with)

Archive protocol category

This call archives a protocol category. Warning: it is possible to remove categories that are linked to protocols. Be careful when archiving categories.

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
protocol_category_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Archive protocol category
    api_instance.protocols_archive_protocol_category(protocol_category_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_archive_protocol_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_category_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_categories**
> list[ProtocolCategory] protocols_get_categories(expand=expand, view_id=view_id, view_columns=view_columns, archived=archived, public=public, x_requested_with=x_requested_with)

Get available protocol categories

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
archived = 'archived_example' # str | Filter by archived categories (optional)
public = 'public_example' # str | Filter on public protocol categories (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get available protocol categories
    api_response = api_instance.protocols_get_categories(expand=expand, view_id=view_id, view_columns=view_columns, archived=archived, public=public, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **archived** | **str**| Filter by archived categories | [optional] 
 **public** | **str**| Filter on public protocol categories | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[ProtocolCategory]**](ProtocolCategory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_protocol_by_id**
> ProtocolEntry protocols_get_protocol_by_id(prot_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a protocol by id

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a protocol by id
    api_response = api_instance.protocols_get_protocol_by_id(prot_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_protocol_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ProtocolEntry**](ProtocolEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_protocol_by_protocol_version_id**
> ProtocolEntry protocols_get_protocol_by_protocol_version_id(prot_version_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a protocol by its version id

$expand values (separate with a comma for multiple expands):  * signingStatus

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
prot_version_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a protocol by its version id
    api_response = api_instance.protocols_get_protocol_by_protocol_version_id(prot_version_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_protocol_by_protocol_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prot_version_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ProtocolEntry**](ProtocolEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_protocol_digest**
> list[ProtocolDigest] protocols_get_protocol_digest(expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)

Get protocol digest

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
scope = 'scope_example' # str | user/group/userAndGroup/public/all (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get protocol digest
    api_response = api_instance.protocols_get_protocol_digest(expand=expand, view_id=view_id, view_columns=view_columns, scope=scope, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_protocol_digest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **scope** | **str**| user/group/userAndGroup/public/all | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[ProtocolDigest]**](ProtocolDigest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_protocol_file**
> object protocols_get_protocol_file(file_id, expand=expand, view_id=view_id, view_columns=view_columns, max_width=max_width, x_requested_with=x_requested_with)

Get protocol file

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
file_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
max_width = 'max_width_example' # str | The maximum width of an image (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get protocol file
    api_response = api_instance.protocols_get_protocol_file(file_id, expand=expand, view_id=view_id, view_columns=view_columns, max_width=max_width, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_protocol_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **max_width** | **str**| The maximum width of an image | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_protocol_list**
> list[ProtocolEntry] protocols_get_protocol_list(expand=expand, view_id=view_id, view_columns=view_columns, group_ids=group_ids, scope=scope, search=search, x_requested_with=x_requested_with)

Get protocols

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
api_instance = elabjournal_client.ProtocolsApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
group_ids = 'group_ids_example' # str | Comma-separated list of groups to include if scope is group or userAndGroup (optional)
scope = 'scope_example' # str | user/group/userAndGroup/public/all (optional)
search = 'search_example' # str | Search protocols by name or contents (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get protocols
    api_response = api_instance.protocols_get_protocol_list(expand=expand, view_id=view_id, view_columns=view_columns, group_ids=group_ids, scope=scope, search=search, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_protocol_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **group_ids** | **str**| Comma-separated list of groups to include if scope is group or userAndGroup | [optional] 
 **scope** | **str**| user/group/userAndGroup/public/all | [optional] 
 **search** | **str**| Search protocols by name or contents | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[ProtocolEntry]**](ProtocolEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

