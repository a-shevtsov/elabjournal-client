# elabjournal_client.SampleTypeApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sample_type_create_sample_type**](SampleTypeApi.md#sample_type_create_sample_type) | **POST** /api/v1/sampleTypes | Create a new sample type
[**sample_type_create_sample_type_meta**](SampleTypeApi.md#sample_type_create_sample_type_meta) | **POST** /api/v1/sampleTypes/{sampleTypeID}/meta | Create a new sample type&#39;s meta field
[**sample_type_delete_sample_type**](SampleTypeApi.md#sample_type_delete_sample_type) | **DELETE** /api/v1/sampleTypes/{sampleTypeID} | Delete a sample type
[**sample_type_delete_sample_type_meta**](SampleTypeApi.md#sample_type_delete_sample_type_meta) | **DELETE** /api/v1/sampleTypes/{sampleTypeID}/meta/{sampleTypeMetaID} | Delete a sample type&#39;s meta field
[**sample_type_get_sample_type_by_id**](SampleTypeApi.md#sample_type_get_sample_type_by_id) | **GET** /api/v1/sampleTypes/{sampleTypeID} | Get a sample type by id
[**sample_type_get_sample_type_meta**](SampleTypeApi.md#sample_type_get_sample_type_meta) | **GET** /api/v1/sampleTypes/{sampleTypeID}/meta/{sampleTypeMetaID} | Get a sample type&#39;s meta field by id
[**sample_type_get_sample_type_meta_defaults**](SampleTypeApi.md#sample_type_get_sample_type_meta_defaults) | **GET** /api/v1/sampleTypes/{sampleTypeID}/meta/{sampleTypeMetaID}/defaults | Get a sample type meta field&#39;s default options
[**sample_type_get_sample_type_metas**](SampleTypeApi.md#sample_type_get_sample_type_metas) | **GET** /api/v1/sampleTypes/{sampleTypeId}/meta | Get all of a sample type&#39;s meta fields
[**sample_type_get_sample_type_metas_for_all_sample_types**](SampleTypeApi.md#sample_type_get_sample_type_metas_for_all_sample_types) | **GET** /api/v1/sampleTypes/meta | Get all meta fields from all sample types
[**sample_type_get_sample_types**](SampleTypeApi.md#sample_type_get_sample_types) | **GET** /api/v1/sampleTypes | Get sample types
[**sample_type_get_sample_types_for_names**](SampleTypeApi.md#sample_type_get_sample_types_for_names) | **GET** /api/v1/sampleTypes/forNames | Get a list of sample types for multiple names
[**sample_type_patch_sample_type**](SampleTypeApi.md#sample_type_patch_sample_type) | **PATCH** /api/v1/sampleTypes/{sampleTypeID} | Update a sample type&#39;s properties
[**sample_type_patch_sample_type_meta**](SampleTypeApi.md#sample_type_patch_sample_type_meta) | **PATCH** /api/v1/sampleTypes/{sampleTypeID}/meta/{sampleTypeMetaID} | Update a sample type meta field&#39;s properties
[**sample_type_put_sample_type_meta**](SampleTypeApi.md#sample_type_put_sample_type_meta) | **PUT** /api/v1/sampleTypes/{sampleTypeID}/meta | Create or update a sample type&#39;s meta field
[**sample_type_put_sample_type_meta_defaults**](SampleTypeApi.md#sample_type_put_sample_type_meta_defaults) | **PUT** /api/v1/sampleTypes/{sampleTypeID}/meta/{sampleTypeMetaID}/defaults | Update, Remove and Create a sample type meta field&#39;s default options
[**sample_type_restore_sample_type**](SampleTypeApi.md#sample_type_restore_sample_type) | **POST** /api/v1/sampleTypes/{sampleTypeID}/restore | Restore the given sampleType from archive


# **sample_type_create_sample_type**
> int sample_type_create_sample_type(sample_type, x_requested_with=x_requested_with)

Create a new sample type

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type = elabjournal_client.SampleTypeNew() # SampleTypeNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new sample type
    api_response = api_instance.sample_type_create_sample_type(sample_type, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_create_sample_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type** | [**SampleTypeNew**](SampleTypeNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_create_sample_type_meta**
> int sample_type_create_sample_type_meta(sample_type_id, dto, x_requested_with=x_requested_with)

Create a new sample type's meta field

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
dto = elabjournal_client.SampleTypeMetaNew() # SampleTypeMetaNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new sample type's meta field
    api_response = api_instance.sample_type_create_sample_type_meta(sample_type_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_create_sample_type_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **dto** | [**SampleTypeMetaNew**](SampleTypeMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_delete_sample_type**
> sample_type_delete_sample_type(sample_type_id, x_requested_with=x_requested_with)

Delete a sample type

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a sample type
    api_instance.sample_type_delete_sample_type(sample_type_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_delete_sample_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_delete_sample_type_meta**
> sample_type_delete_sample_type_meta(sample_type_id, sample_type_meta_id, x_requested_with=x_requested_with)

Delete a sample type's meta field

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
sample_type_meta_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a sample type's meta field
    api_instance.sample_type_delete_sample_type_meta(sample_type_id, sample_type_meta_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_delete_sample_type_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **sample_type_meta_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_get_sample_type_by_id**
> SampleType sample_type_get_sample_type_by_id(sample_type_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample type by id

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample type by id
    api_response = api_instance.sample_type_get_sample_type_by_id(sample_type_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_get_sample_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleType**](SampleType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_get_sample_type_meta**
> SampleTypeMetaLarge sample_type_get_sample_type_meta(sample_type_id, sample_type_meta_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample type's meta field by id

$expand values (separate with comma for multiple expands):  * sampleTypeSection  

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
sample_type_meta_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample type's meta field by id
    api_response = api_instance.sample_type_get_sample_type_meta(sample_type_id, sample_type_meta_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_get_sample_type_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **sample_type_meta_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleTypeMetaLarge**](SampleTypeMetaLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_get_sample_type_meta_defaults**
> PagedOfSampleTypeMetaDefault sample_type_get_sample_type_meta_defaults(sample_type_id, sample_type_meta_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample type meta field's default options

The default options are only present for field types RADIO, COMBO and CHECKBOX. These are the same as the \"optionValues\" field in the sample type calls, but this call also includes their database IDs

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
sample_type_meta_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample type meta field's default options
    api_response = api_instance.sample_type_get_sample_type_meta_defaults(sample_type_id, sample_type_meta_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_get_sample_type_meta_defaults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **sample_type_meta_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleTypeMetaDefault**](PagedOfSampleTypeMetaDefault.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_get_sample_type_metas**
> PagedOfSampleTypeMetaLarge sample_type_get_sample_type_metas(sample_type_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all of a sample type's meta fields

$expand values (separate with comma for multiple expands):  * sampleTypeSection  

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all of a sample type's meta fields
    api_response = api_instance.sample_type_get_sample_type_metas(sample_type_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_get_sample_type_metas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleTypeMetaLarge**](PagedOfSampleTypeMetaLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_get_sample_type_metas_for_all_sample_types**
> PagedOfSampleTypeMetaLarge sample_type_get_sample_type_metas_for_all_sample_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all meta fields from all sample types

$expand values (separate with comma for multiple expands):  * sampleTypeSection  

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all meta fields from all sample types
    api_response = api_instance.sample_type_get_sample_type_metas_for_all_sample_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_get_sample_type_metas_for_all_sample_types: %s\n" % e)
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

[**PagedOfSampleTypeMetaLarge**](PagedOfSampleTypeMetaLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_get_sample_types**
> PagedOfSampleTypeLarge sample_type_get_sample_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, name=name, archived=archived, x_requested_with=x_requested_with)

Get sample types

If the archived parameter isn't set, archived=false is automatically implied.  $expand values (separate with comma for multiple expands):  * sampleTypeNumbering  

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
name = 'name_example' # str | Filter by sample type name (optional)
archived = 'archived_example' # str | Filter by archived or non-archived sample types. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get sample types
    api_response = api_instance.sample_type_get_sample_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, name=name, archived=archived, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_get_sample_types: %s\n" % e)
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
 **name** | **str**| Filter by sample type name | [optional] 
 **archived** | **str**| Filter by archived or non-archived sample types. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleTypeLarge**](PagedOfSampleTypeLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_get_sample_types_for_names**
> PagedOfSampleType sample_type_get_sample_types_for_names(names, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, archived=archived, x_requested_with=x_requested_with)

Get a list of sample types for multiple names

If the archived parameter isn't set, archived=false is automatically implied.  

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
names = ['names_example'] # list[str] | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
archived = 'archived_example' # str | Filter by archived or non-archived sample types. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of sample types for multiple names
    api_response = api_instance.sample_type_get_sample_types_for_names(names, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, archived=archived, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_get_sample_types_for_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **archived** | **str**| Filter by archived or non-archived sample types. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleType**](PagedOfSampleType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_patch_sample_type**
> sample_type_patch_sample_type(sample_type_id, delta, x_requested_with=x_requested_with)

Update a sample type's properties

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
delta = elabjournal_client.SampleTypeNew() # SampleTypeNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a sample type's properties
    api_instance.sample_type_patch_sample_type(sample_type_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_patch_sample_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **delta** | [**SampleTypeNew**](SampleTypeNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_patch_sample_type_meta**
> sample_type_patch_sample_type_meta(sample_type_id, sample_type_meta_id, delta, x_requested_with=x_requested_with)

Update a sample type meta field's properties

Only pass the properties within your delta that needs to be changed.

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
sample_type_meta_id = 56 # int | 
delta = elabjournal_client.SampleTypeMetaUpdateDto() # SampleTypeMetaUpdateDto | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a sample type meta field's properties
    api_instance.sample_type_patch_sample_type_meta(sample_type_id, sample_type_meta_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_patch_sample_type_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **sample_type_meta_id** | **int**|  | 
 **delta** | [**SampleTypeMetaUpdateDto**](SampleTypeMetaUpdateDto.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_put_sample_type_meta**
> int sample_type_put_sample_type_meta(sample_type_id, dto, x_requested_with=x_requested_with)

Create or update a sample type's meta field

This call will check if a sample type meta field with the specified key already exists. If so it overwrites that meta field; otherwise it creates a new meta field.    Note: the sampleTypeMetaID will always be newly created, even on an overwrite. Don't use this call to update an existing combo, checkbox or radio field that has existing samples if you don't want to get the mapping disconnected.  

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
dto = elabjournal_client.SampleTypeMetaNew() # SampleTypeMetaNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create or update a sample type's meta field
    api_response = api_instance.sample_type_put_sample_type_meta(sample_type_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_put_sample_type_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **dto** | [**SampleTypeMetaNew**](SampleTypeMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_put_sample_type_meta_defaults**
> PagedOfSampleTypeMetaDefault sample_type_put_sample_type_meta_defaults(sample_type_id, sample_type_meta_id, option_list, x_requested_with=x_requested_with)

Update, Remove and Create a sample type meta field's default options

The default options are only present for field types RADIO, COMBO and CHECKBOX. Ommit the sampleTypeMetaDefaultsID or set to 0 to create a new option value. Be sure to include the options that you need to keep, as the complete option values object will be replaced.

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
sample_type_meta_id = 56 # int | 
option_list = [elabjournal_client.SampleTypeMetaOptionFieldDto()] # list[SampleTypeMetaOptionFieldDto] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update, Remove and Create a sample type meta field's default options
    api_response = api_instance.sample_type_put_sample_type_meta_defaults(sample_type_id, sample_type_meta_id, option_list, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_put_sample_type_meta_defaults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **sample_type_meta_id** | **int**|  | 
 **option_list** | [**list[SampleTypeMetaOptionFieldDto]**](SampleTypeMetaOptionFieldDto.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleTypeMetaDefault**](PagedOfSampleTypeMetaDefault.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_type_restore_sample_type**
> sample_type_restore_sample_type(sample_type_id, x_requested_with=x_requested_with)

Restore the given sampleType from archive

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
api_instance = elabjournal_client.SampleTypeApi(elabjournal_client.ApiClient(configuration))
sample_type_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Restore the given sampleType from archive
    api_instance.sample_type_restore_sample_type(sample_type_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleTypeApi->sample_type_restore_sample_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_type_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

