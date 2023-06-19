# elabjournal_client.ExperimentSectionsDeprecatedCallsApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment_section_deprecated_download_marvin_js_image**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_download_marvin_js_image) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/marvinjs | Download a marvinJS image
[**experiment_section_deprecated_download_marvin_js_image_base64**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_download_marvin_js_image_base64) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/marvinjs/base64 | Download a marvinJS image in Base64 format
[**experiment_section_deprecated_download_section_canvas_image**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_download_section_canvas_image) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/canvas | Download the canvas image from a CANVAS section
[**experiment_section_deprecated_download_section_excel_file**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_download_section_excel_file) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/excel | Download the excel file from an EXCEL section
[**experiment_section_deprecated_download_section_excel_preview**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_download_section_excel_preview) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/excelPreview | Download the preview image from an EXCEL section
[**experiment_section_deprecated_download_section_file**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_download_section_file) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/files/{experimentFileID} | Download a file from a FILES section
[**experiment_section_deprecated_download_section_image**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_download_section_image) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/images/{experimentFileID} | Download an image from an IMAGE section
[**experiment_section_deprecated_get_section_content**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_get_section_content) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/content | Get the content from a text section
[**experiment_section_deprecated_get_section_content_as_html**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_get_section_content_as_html) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/html | Get a full HTML page from a section
[**experiment_section_deprecated_get_section_file_list**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_get_section_file_list) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/files | Get file list of a FILE section
[**experiment_section_deprecated_get_section_image_list**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_get_section_image_list) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/images | Get image list of an IMAGE section
[**experiment_section_deprecated_get_section_samples**](ExperimentSectionsDeprecatedCallsApi.md#experiment_section_deprecated_get_section_samples) | **GET** /api/v1/experiments/{experimentID}/sections/{expJournalID}/samples | Get sample list from a SAMPLESIN or SAMPLESOUT section


# **experiment_section_deprecated_download_marvin_js_image**
> object experiment_section_deprecated_download_marvin_js_image(exp_journal_id, experiment_id, x_requested_with=x_requested_with)

Download a marvinJS image

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/marvinjs/image``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download a marvinJS image
    api_response = api_instance.experiment_section_deprecated_download_marvin_js_image(exp_journal_id, experiment_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_download_marvin_js_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_download_marvin_js_image_base64**
> object experiment_section_deprecated_download_marvin_js_image_base64(exp_journal_id, experiment_id, x_requested_with=x_requested_with)

Download a marvinJS image in Base64 format

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/marvinjs/image/dataURL``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download a marvinJS image in Base64 format
    api_response = api_instance.experiment_section_deprecated_download_marvin_js_image_base64(exp_journal_id, experiment_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_download_marvin_js_image_base64: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_download_section_canvas_image**
> object experiment_section_deprecated_download_section_canvas_image(exp_journal_id, experiment_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Download the canvas image from a CANVAS section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/canvas``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the canvas image from a CANVAS section
    api_response = api_instance.experiment_section_deprecated_download_section_canvas_image(exp_journal_id, experiment_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_download_section_canvas_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
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

# **experiment_section_deprecated_download_section_excel_file**
> object experiment_section_deprecated_download_section_excel_file(exp_journal_id, experiment_id, x_requested_with=x_requested_with)

Download the excel file from an EXCEL section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/excel``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the excel file from an EXCEL section
    api_response = api_instance.experiment_section_deprecated_download_section_excel_file(exp_journal_id, experiment_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_download_section_excel_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_download_section_excel_preview**
> object experiment_section_deprecated_download_section_excel_preview(exp_journal_id, experiment_id, x_requested_with=x_requested_with)

Download the preview image from an EXCEL section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/excel/preview``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the preview image from an EXCEL section
    api_response = api_instance.experiment_section_deprecated_download_section_excel_preview(exp_journal_id, experiment_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_download_section_excel_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_download_section_file**
> object experiment_section_deprecated_download_section_file(experiment_file_id, exp_journal_id, experiment_id, x_requested_with=x_requested_with)

Download a file from a FILES section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/files/{experimentFileID:int}``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download a file from a FILES section
    api_response = api_instance.experiment_section_deprecated_download_section_file(experiment_file_id, exp_journal_id, experiment_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_download_section_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_download_section_image**
> object experiment_section_deprecated_download_section_image(experiment_file_id, exp_journal_id, experiment_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Download an image from an IMAGE section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/images/{experimentFileID:int}``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download an image from an IMAGE section
    api_response = api_instance.experiment_section_deprecated_download_section_image(experiment_file_id, exp_journal_id, experiment_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_download_section_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
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

# **experiment_section_deprecated_get_section_content**
> ExpJournalContentBase experiment_section_deprecated_get_section_content(exp_journal_id, experiment_id, x_requested_with=x_requested_with)

Get the content from a text section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/content``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the content from a text section
    api_response = api_instance.experiment_section_deprecated_get_section_content(exp_journal_id, experiment_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_get_section_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ExpJournalContentBase**](ExpJournalContentBase.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_get_section_content_as_html**
> object experiment_section_deprecated_get_section_content_as_html(exp_journal_id, experiment_id, x_requested_with=x_requested_with)

Get a full HTML page from a section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/html``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a full HTML page from a section
    api_response = api_instance.experiment_section_deprecated_get_section_content_as_html(exp_journal_id, experiment_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_get_section_content_as_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_get_section_file_list**
> PagedOfExperimentFile experiment_section_deprecated_get_section_file_list(exp_journal_id, experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get file list of a FILE section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/files``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get file list of a FILE section
    api_response = api_instance.experiment_section_deprecated_get_section_file_list(exp_journal_id, experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_get_section_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExperimentFile**](PagedOfExperimentFile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_get_section_image_list**
> PagedOfExperimentImage experiment_section_deprecated_get_section_image_list(exp_journal_id, experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get image list of an IMAGE section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/images``  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get image list of an IMAGE section
    api_response = api_instance.experiment_section_deprecated_get_section_image_list(exp_journal_id, experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_get_section_image_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExperimentImage**](PagedOfExperimentImage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_deprecated_get_section_samples**
> PagedOfSampleLarge experiment_section_deprecated_get_section_samples(exp_journal_id, experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get sample list from a SAMPLESIN or SAMPLESOUT section

**Deprecated.** Please use ``GET /api/v1/experiments/sections/{expJournalID}/samples``    This call will also fetch archived samples.  

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
api_instance = elabjournal_client.ExperimentSectionsDeprecatedCallsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get sample list from a SAMPLESIN or SAMPLESOUT section
    api_response = api_instance.experiment_section_deprecated_get_section_samples(exp_journal_id, experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsDeprecatedCallsApi->experiment_section_deprecated_get_section_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLarge**](PagedOfSampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

