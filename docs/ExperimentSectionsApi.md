# elabjournal_client.ExperimentSectionsApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment_section_add_section_samples**](ExperimentSectionsApi.md#experiment_section_add_section_samples) | **PUT** /api/v1/experiments/sections/{expJournalID}/samples | Add samples to a SAMPLESIN or SAMPLESOUT section
[**experiment_section_archive_section**](ExperimentSectionsApi.md#experiment_section_archive_section) | **DELETE** /api/v1/experiments/sections/{expJournalID} | Archives an experiment section
[**experiment_section_change_section_position**](ExperimentSectionsApi.md#experiment_section_change_section_position) | **PUT** /api/v1/experiments/sections/{expJournalID}/position | Changes the position of the section within the experiment
[**experiment_section_copy_experiment_section**](ExperimentSectionsApi.md#experiment_section_copy_experiment_section) | **POST** /api/v1/experiments/sections/{expJournalID}/copy | Copies experiment section
[**experiment_section_create_blank_oos_file**](ExperimentSectionsApi.md#experiment_section_create_blank_oos_file) | **POST** /api/v1/experiments/sections/{expJournalID}/oos/file | Create a blank OOS file of a given type
[**experiment_section_create_section**](ExperimentSectionsApi.md#experiment_section_create_section) | **POST** /api/v1/experiments/{experimentID}/sections | Create a new, empty section in an experiment
[**experiment_section_create_section_meta**](ExperimentSectionsApi.md#experiment_section_create_section_meta) | **POST** /api/v1/experiments/sections/{expJournalID}/meta | Create or update meta data in a section
[**experiment_section_create_section_meta2**](ExperimentSectionsApi.md#experiment_section_create_section_meta2) | **PUT** /api/v1/experiments/sections/{expJournalID}/meta | Create or update meta data in a section
[**experiment_section_delete_section_file**](ExperimentSectionsApi.md#experiment_section_delete_section_file) | **DELETE** /api/v1/experiments/sections/{expJournalID}/files/{experimentFileID} | Remove a file from a FILE or CUSTOM section
[**experiment_section_delete_section_files**](ExperimentSectionsApi.md#experiment_section_delete_section_files) | **DELETE** /api/v1/experiments/sections/{expJournalID}/files | Remove multiple files from a FILE or CUSTOM section
[**experiment_section_delete_section_image**](ExperimentSectionsApi.md#experiment_section_delete_section_image) | **DELETE** /api/v1/experiments/sections/{expJournalID}/images/{experimentFileID} | Remove an image from an IMAGE or CUSTOM section
[**experiment_section_delete_section_images**](ExperimentSectionsApi.md#experiment_section_delete_section_images) | **DELETE** /api/v1/experiments/sections/{expJournalID}/images | Remove multiple images from an IMAGE or CUSTOM section
[**experiment_section_delete_section_samples**](ExperimentSectionsApi.md#experiment_section_delete_section_samples) | **DELETE** /api/v1/experiments/sections/{expJournalID}/samples | Remove samples from a SAMPLESIN or SAMPLESOUT section
[**experiment_section_download_marvin_js_image**](ExperimentSectionsApi.md#experiment_section_download_marvin_js_image) | **GET** /api/v1/experiments/sections/{expJournalID}/marvinjs/image | Download the image of a MARVINJS section
[**experiment_section_download_section_canvas_image**](ExperimentSectionsApi.md#experiment_section_download_section_canvas_image) | **GET** /api/v1/experiments/sections/{expJournalID}/canvas | Download the canvas image from a CANVAS section
[**experiment_section_download_section_excel_file**](ExperimentSectionsApi.md#experiment_section_download_section_excel_file) | **GET** /api/v1/experiments/sections/{expJournalID}/excel | Download the excel file from an EXCEL section
[**experiment_section_download_section_excel_preview**](ExperimentSectionsApi.md#experiment_section_download_section_excel_preview) | **GET** /api/v1/experiments/sections/{expJournalID}/excel/preview | Download the preview image from an EXCEL section
[**experiment_section_download_section_file**](ExperimentSectionsApi.md#experiment_section_download_section_file) | **GET** /api/v1/experiments/sections/{expJournalID}/files/{experimentFileID} | Download a file from a FILE or CUSTOM section
[**experiment_section_download_section_image**](ExperimentSectionsApi.md#experiment_section_download_section_image) | **GET** /api/v1/experiments/sections/{expJournalID}/images/{experimentFileID} | Download an image from an IMAGE or CUSTOM section
[**experiment_section_download_section_oos_preview**](ExperimentSectionsApi.md#experiment_section_download_section_oos_preview) | **GET** /api/v1/experiments/sections/{expJournalID}/oos/preview | Download the preview image from an OOS section
[**experiment_section_generate_access_token**](ExperimentSectionsApi.md#experiment_section_generate_access_token) | **POST** /api/v1/experiments/sections/{expJournalID}/oos/access-token | Generate an access token for use in oos integration
[**experiment_section_get_custom_section_info**](ExperimentSectionsApi.md#experiment_section_get_custom_section_info) | **GET** /api/v1/experiments/sections/{expJournalID}/customSectionInfo | Get the custom section information of a CUSTOM section
[**experiment_section_get_excel_section_oos_link**](ExperimentSectionsApi.md#experiment_section_get_excel_section_oos_link) | **GET** /api/v1/experiments/sections/{expJournalID}/excel/oos | Get the URL to the OOS server for editing an EXCEL section
[**experiment_section_get_experiment_section**](ExperimentSectionsApi.md#experiment_section_get_experiment_section) | **GET** /api/v1/experiments/sections/{expJournalID} | Gets an experiment section
[**experiment_section_get_experiment_sections**](ExperimentSectionsApi.md#experiment_section_get_experiment_sections) | **GET** /api/v1/experiments/{experimentID}/sections | Get experiment sections
[**experiment_section_get_latest_oos_file_id**](ExperimentSectionsApi.md#experiment_section_get_latest_oos_file_id) | **POST** /api/v1/experiments/sections/{expJournalID}/oos/getlatestfileid | Get latest oos file id
[**experiment_section_get_marvin_js_image_as_data_url**](ExperimentSectionsApi.md#experiment_section_get_marvin_js_image_as_data_url) | **GET** /api/v1/experiments/sections/{expJournalID}/marvinjs/image/dataURL | Get the image of a MARVINJS section as a data URL
[**experiment_section_get_marvin_js_reaction_table_content**](ExperimentSectionsApi.md#experiment_section_get_marvin_js_reaction_table_content) | **GET** /api/v1/experiments/sections/{expJournalID}/marvinjs/reaction | Get the marvin js reaction from an experiment section ID
[**experiment_section_get_marvin_js_structure_data**](ExperimentSectionsApi.md#experiment_section_get_marvin_js_structure_data) | **GET** /api/v1/experiments/sections/{expJournalID}/marvinjs/smiles | Get the marvin js structure data from an experiment section ID
[**experiment_section_get_oos_link**](ExperimentSectionsApi.md#experiment_section_get_oos_link) | **GET** /api/v1/experiments/sections/{expJournalID}/oos/url | Get the URL to the OOS server
[**experiment_section_get_section_content**](ExperimentSectionsApi.md#experiment_section_get_section_content) | **GET** /api/v1/experiments/sections/{expJournalID}/content | Get the content from a text section
[**experiment_section_get_section_content_as_html**](ExperimentSectionsApi.md#experiment_section_get_section_content_as_html) | **GET** /api/v1/experiments/sections/{expJournalID}/html | Get a full HTML page from a section
[**experiment_section_get_section_data_table**](ExperimentSectionsApi.md#experiment_section_get_section_data_table) | **GET** /api/v1/experiments/sections/{expJournalID}/datatable | Get the content from a DATATABLE section
[**experiment_section_get_section_file_list**](ExperimentSectionsApi.md#experiment_section_get_section_file_list) | **GET** /api/v1/experiments/sections/{expJournalID}/files | Get file list of a FILE or CUSTOM section
[**experiment_section_get_section_image_list**](ExperimentSectionsApi.md#experiment_section_get_section_image_list) | **GET** /api/v1/experiments/sections/{expJournalID}/images | Get image list of an IMAGE or CUSTOM section
[**experiment_section_get_section_lock_info**](ExperimentSectionsApi.md#experiment_section_get_section_lock_info) | **GET** /api/v1/experiments/sections/{expJournalID}/lock | Check if a text section has been locked
[**experiment_section_get_section_meta**](ExperimentSectionsApi.md#experiment_section_get_section_meta) | **GET** /api/v1/experiments/sections/{expJournalID}/meta | Get all meta data in a section
[**experiment_section_get_section_meta_by_name**](ExperimentSectionsApi.md#experiment_section_get_section_meta_by_name) | **GET** /api/v1/experiments/sections/{expJournalID}/meta/{name} | Get meta data from a section by name
[**experiment_section_get_section_samples**](ExperimentSectionsApi.md#experiment_section_get_section_samples) | **GET** /api/v1/experiments/sections/{expJournalID}/samples | Get sample list from a SAMPLESIN or SAMPLESOUT section
[**experiment_section_is_empty_file_check**](ExperimentSectionsApi.md#experiment_section_is_empty_file_check) | **GET** /api/v1/experiments/sections/{expJournalID}/oos/isemptyfile | Check if the file is empty
[**experiment_section_lock_section**](ExperimentSectionsApi.md#experiment_section_lock_section) | **PUT** /api/v1/experiments/sections/{expJournalID}/lock | Try to lock a text section
[**experiment_section_post_marvin_js_reaction_table_content**](ExperimentSectionsApi.md#experiment_section_post_marvin_js_reaction_table_content) | **POST** /api/v1/experiments/sections/{expJournalID}/marvinjs/reaction | Post the marvin js reaction to an experiment section ID
[**experiment_section_put_section_content**](ExperimentSectionsApi.md#experiment_section_put_section_content) | **PUT** /api/v1/experiments/sections/{expJournalID}/content | Update the content of a text section
[**experiment_section_put_section_content_html**](ExperimentSectionsApi.md#experiment_section_put_section_content_html) | **PUT** /api/v1/experiments/sections/{expJournalID}/html | Update a text section&#39;s HTML content
[**experiment_section_put_section_data_table**](ExperimentSectionsApi.md#experiment_section_put_section_data_table) | **PUT** /api/v1/experiments/sections/{expJournalID}/datatable | Update the content of a DATATABLE section
[**experiment_section_restore_oos_file**](ExperimentSectionsApi.md#experiment_section_restore_oos_file) | **PUT** /api/v1/experiments/sections/{expJournalID}/oos/restore/{fileID} | Restore OOS section to selected file and retake screenshot
[**experiment_section_restore_section**](ExperimentSectionsApi.md#experiment_section_restore_section) | **POST** /api/v1/experiments/sections/{expJournalID}/restore | Restores an archived experiment section
[**experiment_section_unlock_section**](ExperimentSectionsApi.md#experiment_section_unlock_section) | **DELETE** /api/v1/experiments/sections/{expJournalID}/lock | Try to unlock a text section
[**experiment_section_update_experiment_section**](ExperimentSectionsApi.md#experiment_section_update_experiment_section) | **PATCH** /api/v1/experiments/sections/{expJournalID} | Updates an experiment section&#39;s general properties
[**experiment_section_update_section_image_description**](ExperimentSectionsApi.md#experiment_section_update_section_image_description) | **PUT** /api/v1/experiments/sections/{expJournalID}/images/{experimentFileID}/description | Updates the description of an image in an IMAGE or CUSTOM section
[**experiment_section_update_section_image_position**](ExperimentSectionsApi.md#experiment_section_update_section_image_position) | **PUT** /api/v1/experiments/sections/{expJournalID}/images/{experimentFileID}/position | Updates the position of an image in an IMAGE or CUSTOM section
[**experiment_section_upload_section_canvas_image**](ExperimentSectionsApi.md#experiment_section_upload_section_canvas_image) | **PUT** /api/v1/experiments/sections/{expJournalID}/canvas | Upload an image to a CANVAS section
[**experiment_section_upload_section_excel_file**](ExperimentSectionsApi.md#experiment_section_upload_section_excel_file) | **PUT** /api/v1/experiments/sections/{expJournalID}/excel | Upload an Excel file to an EXCEL section
[**experiment_section_upload_section_file**](ExperimentSectionsApi.md#experiment_section_upload_section_file) | **POST** /api/v1/experiments/sections/{expJournalID}/files | Upload a file to a FILE or CUSTOM section
[**experiment_section_upload_section_image**](ExperimentSectionsApi.md#experiment_section_upload_section_image) | **POST** /api/v1/experiments/sections/{expJournalID}/images | Upload an image file to an IMAGE or CUSTOM section


# **experiment_section_add_section_samples**
> experiment_section_add_section_samples(exp_journal_id, sample_ids, x_requested_with=x_requested_with)

Add samples to a SAMPLESIN or SAMPLESOUT section

This call will also add archived samples.    The request body of this call should contain a JSON array with the sample IDs.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
sample_ids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add samples to a SAMPLESIN or SAMPLESOUT section
    api_instance.experiment_section_add_section_samples(exp_journal_id, sample_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_add_section_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_archive_section**
> experiment_section_archive_section(exp_journal_id, x_requested_with=x_requested_with)

Archives an experiment section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Archives an experiment section
    api_instance.experiment_section_archive_section(exp_journal_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_archive_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_change_section_position**
> experiment_section_change_section_position(exp_journal_id, position, x_requested_with=x_requested_with)

Changes the position of the section within the experiment

The position is a 0-based integer where 0 is the top position within the experiment.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
position = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Changes the position of the section within the experiment
    api_instance.experiment_section_change_section_position(exp_journal_id, position, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_change_section_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **position** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_copy_experiment_section**
> experiment_section_copy_experiment_section(exp_journal_id, expand=expand, view_id=view_id, view_columns=view_columns, section_header=section_header, experiment_id=experiment_id, x_requested_with=x_requested_with)

Copies experiment section

This call copies a section of an experiment. The default experimentID is the ID of the experiment in which the section resides, to copy a section into another experiment provide the optional experimentID.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
section_header = 'section_header_example' # str | The header of the copied section, if left blank the header will be the original with 'Copy of' added in front of it. (optional)
experiment_id = 'experiment_id_example' # str | The experiment where this section should be copied to, leave blank for the provided sections experiment ID. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Copies experiment section
    api_instance.experiment_section_copy_experiment_section(exp_journal_id, expand=expand, view_id=view_id, view_columns=view_columns, section_header=section_header, experiment_id=experiment_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_copy_experiment_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **section_header** | **str**| The header of the copied section, if left blank the header will be the original with &#39;Copy of&#39; added in front of it. | [optional] 
 **experiment_id** | **str**| The experiment where this section should be copied to, leave blank for the provided sections experiment ID. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_create_blank_oos_file**
> int experiment_section_create_blank_oos_file(exp_journal_id, oos_section, x_requested_with=x_requested_with)

Create a blank OOS file of a given type

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
oos_section = elabjournal_client.OosSection() # OosSection | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a blank OOS file of a given type
    api_response = api_instance.experiment_section_create_blank_oos_file(exp_journal_id, oos_section, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_create_blank_oos_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **oos_section** | [**OosSection**](OosSection.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_create_section**
> int experiment_section_create_section(experiment_id, section, x_requested_with=x_requested_with)

Create a new, empty section in an experiment

Use the `order` property to specify the position of the new section within the experiment. This is a a 0-based integer where 0 is the top position within the experiment. If you omit this property the section is appended at the bottom.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_id = 56 # int | 
section = elabjournal_client.ExpJournalNew() # ExpJournalNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new, empty section in an experiment
    api_response = api_instance.experiment_section_create_section(experiment_id, section, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_create_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **section** | [**ExpJournalNew**](ExpJournalNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_create_section_meta**
> object experiment_section_create_section_meta(exp_journal_id, section_meta, x_requested_with=x_requested_with)

Create or update meta data in a section

This call will add the meta data if the name of the meta doesn't exist yet. If the name exists the associated meta data will be updated.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
section_meta = elabjournal_client.ExpJournalMetaNew() # ExpJournalMetaNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create or update meta data in a section
    api_response = api_instance.experiment_section_create_section_meta(exp_journal_id, section_meta, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_create_section_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **section_meta** | [**ExpJournalMetaNew**](ExpJournalMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_create_section_meta2**
> ExpJournalMeta experiment_section_create_section_meta2(exp_journal_id, section_meta, x_requested_with=x_requested_with)

Create or update meta data in a section

This call will add the meta data if the name of the meta doesn't exist yet. If the name exists the associated meta data will be updated.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
section_meta = elabjournal_client.ExpJournalMetaNew() # ExpJournalMetaNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create or update meta data in a section
    api_response = api_instance.experiment_section_create_section_meta2(exp_journal_id, section_meta, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_create_section_meta2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **section_meta** | [**ExpJournalMetaNew**](ExpJournalMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ExpJournalMeta**](ExpJournalMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_delete_section_file**
> experiment_section_delete_section_file(experiment_file_id, exp_journal_id, x_requested_with=x_requested_with)

Remove a file from a FILE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove a file from a FILE or CUSTOM section
    api_instance.experiment_section_delete_section_file(experiment_file_id, exp_journal_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_delete_section_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_delete_section_files**
> experiment_section_delete_section_files(exp_journal_id, experiment_file_ids, x_requested_with=x_requested_with)

Remove multiple files from a FILE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_file_ids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove multiple files from a FILE or CUSTOM section
    api_instance.experiment_section_delete_section_files(exp_journal_id, experiment_file_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_delete_section_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_file_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_delete_section_image**
> experiment_section_delete_section_image(experiment_file_id, exp_journal_id, x_requested_with=x_requested_with)

Remove an image from an IMAGE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove an image from an IMAGE or CUSTOM section
    api_instance.experiment_section_delete_section_image(experiment_file_id, exp_journal_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_delete_section_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_delete_section_images**
> experiment_section_delete_section_images(exp_journal_id, experiment_file_ids, x_requested_with=x_requested_with)

Remove multiple images from an IMAGE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
experiment_file_ids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove multiple images from an IMAGE or CUSTOM section
    api_instance.experiment_section_delete_section_images(exp_journal_id, experiment_file_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_delete_section_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **experiment_file_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_delete_section_samples**
> experiment_section_delete_section_samples(exp_journal_id, sample_ids, archive_samples=archive_samples, x_requested_with=x_requested_with)

Remove samples from a SAMPLESIN or SAMPLESOUT section

The request body of this call should contain a JSON array with the sample IDs which should be removed from the section.    You can add the boolean query parameter `archiveSamples` to this call to archive the samples as well.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
sample_ids = [elabjournal_client.list[int]()] # list[int] | 
archive_samples = true # bool |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove samples from a SAMPLESIN or SAMPLESOUT section
    api_instance.experiment_section_delete_section_samples(exp_journal_id, sample_ids, archive_samples=archive_samples, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_delete_section_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **sample_ids** | **list[int]**|  | 
 **archive_samples** | **bool**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_download_marvin_js_image**
> object experiment_section_download_marvin_js_image(exp_journal_id, x_requested_with=x_requested_with)

Download the image of a MARVINJS section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the image of a MARVINJS section
    api_response = api_instance.experiment_section_download_marvin_js_image(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_download_marvin_js_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_download_section_canvas_image**
> object experiment_section_download_section_canvas_image(exp_journal_id, max_width=max_width, x_requested_with=x_requested_with)

Download the canvas image from a CANVAS section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
max_width = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the canvas image from a CANVAS section
    api_response = api_instance.experiment_section_download_section_canvas_image(exp_journal_id, max_width=max_width, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_download_section_canvas_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **max_width** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_download_section_excel_file**
> object experiment_section_download_section_excel_file(exp_journal_id, x_requested_with=x_requested_with)

Download the excel file from an EXCEL section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the excel file from an EXCEL section
    api_response = api_instance.experiment_section_download_section_excel_file(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_download_section_excel_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_download_section_excel_preview**
> object experiment_section_download_section_excel_preview(exp_journal_id, x_requested_with=x_requested_with)

Download the preview image from an EXCEL section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the preview image from an EXCEL section
    api_response = api_instance.experiment_section_download_section_excel_preview(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_download_section_excel_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_download_section_file**
> object experiment_section_download_section_file(experiment_file_id, exp_journal_id, x_requested_with=x_requested_with)

Download a file from a FILE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download a file from a FILE or CUSTOM section
    api_response = api_instance.experiment_section_download_section_file(experiment_file_id, exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_download_section_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_download_section_image**
> object experiment_section_download_section_image(experiment_file_id, exp_journal_id, max_width=max_width, x_requested_with=x_requested_with)

Download an image from an IMAGE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
max_width = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download an image from an IMAGE or CUSTOM section
    api_response = api_instance.experiment_section_download_section_image(experiment_file_id, exp_journal_id, max_width=max_width, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_download_section_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **max_width** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_download_section_oos_preview**
> object experiment_section_download_section_oos_preview(exp_journal_id, oos_extension, x_requested_with=x_requested_with)

Download the preview image from an OOS section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
oos_extension = 'oos_extension_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download the preview image from an OOS section
    api_response = api_instance.experiment_section_download_section_oos_preview(exp_journal_id, oos_extension, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_download_section_oos_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **oos_extension** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_generate_access_token**
> str experiment_section_generate_access_token(exp_journal_id, x_requested_with=x_requested_with)

Generate an access token for use in oos integration

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Generate an access token for use in oos integration
    api_response = api_instance.experiment_section_generate_access_token(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_generate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_custom_section_info**
> object experiment_section_get_custom_section_info(exp_journal_id, x_requested_with=x_requested_with)

Get the custom section information of a CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the custom section information of a CUSTOM section
    api_response = api_instance.experiment_section_get_custom_section_info(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_custom_section_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_excel_section_oos_link**
> OOSLink experiment_section_get_excel_section_oos_link(exp_journal_id, x_requested_with=x_requested_with)

Get the URL to the OOS server for editing an EXCEL section

The link returned in the `url` property enables you to show an Excel editor for the specified section in a web browser.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the URL to the OOS server for editing an EXCEL section
    api_response = api_instance.experiment_section_get_excel_section_oos_link(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_excel_section_oos_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**OOSLink**](OOSLink.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_experiment_section**
> ExpJournalLarge experiment_section_get_experiment_section(exp_journal_id, x_requested_with=x_requested_with)

Gets an experiment section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Gets an experiment section
    api_response = api_instance.experiment_section_get_experiment_section(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_experiment_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ExpJournalLarge**](ExpJournalLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_experiment_sections**
> PagedOfExpJournalLarge experiment_section_get_experiment_sections(experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, archived=archived, x_requested_with=x_requested_with)

Get experiment sections

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
archived = 'archived_example' # str | Filter by archived or non-archived sections. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get experiment sections
    api_response = api_instance.experiment_section_get_experiment_sections(experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, archived=archived, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_experiment_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **archived** | **str**| Filter by archived or non-archived sections. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExpJournalLarge**](PagedOfExpJournalLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_latest_oos_file_id**
> OosLatestFileIDAndAccessToken experiment_section_get_latest_oos_file_id(exp_journal_id, oos_latest_file_id, x_requested_with=x_requested_with)

Get latest oos file id

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
oos_latest_file_id = elabjournal_client.OosLatestFileID() # OosLatestFileID | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get latest oos file id
    api_response = api_instance.experiment_section_get_latest_oos_file_id(exp_journal_id, oos_latest_file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_latest_oos_file_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **oos_latest_file_id** | [**OosLatestFileID**](OosLatestFileID.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**OosLatestFileIDAndAccessToken**](OosLatestFileIDAndAccessToken.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_marvin_js_image_as_data_url**
> object experiment_section_get_marvin_js_image_as_data_url(exp_journal_id, x_requested_with=x_requested_with)

Get the image of a MARVINJS section as a data URL

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the image of a MARVINJS section as a data URL
    api_response = api_instance.experiment_section_get_marvin_js_image_as_data_url(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_marvin_js_image_as_data_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_marvin_js_reaction_table_content**
> list[ExpReactionTableData] experiment_section_get_marvin_js_reaction_table_content(exp_journal_id, x_requested_with=x_requested_with)

Get the marvin js reaction from an experiment section ID

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the marvin js reaction from an experiment section ID
    api_response = api_instance.experiment_section_get_marvin_js_reaction_table_content(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_marvin_js_reaction_table_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[ExpReactionTableData]**](ExpReactionTableData.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_marvin_js_structure_data**
> SmilesInfo experiment_section_get_marvin_js_structure_data(exp_journal_id, x_requested_with=x_requested_with)

Get the marvin js structure data from an experiment section ID

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the marvin js structure data from an experiment section ID
    api_response = api_instance.experiment_section_get_marvin_js_structure_data(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_marvin_js_structure_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SmilesInfo**](SmilesInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_oos_link**
> experiment_section_get_oos_link(exp_journal_id, oostype, x_requested_with=x_requested_with)

Get the URL to the OOS server

This endpoint retrieves the URLs for accessing content on the OOS server from MS word, MS excel and       MS powerpoint experiment sections. The office online addon is required to use this endpoint. 

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
oostype = 'oostype_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the URL to the OOS server
    api_instance.experiment_section_get_oos_link(exp_journal_id, oostype, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_oos_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **oostype** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_section_content**
> ExpJournalContentAndMeta experiment_section_get_section_content(exp_journal_id, x_requested_with=x_requested_with)

Get the content from a text section

This call will also return the section's meta data. A PROCEDURE section contains meta data containing the protocol's version ID and its variable values.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the content from a text section
    api_response = api_instance.experiment_section_get_section_content(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ExpJournalContentAndMeta**](ExpJournalContentAndMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_section_content_as_html**
> object experiment_section_get_section_content_as_html(exp_journal_id, x_requested_with=x_requested_with)

Get a full HTML page from a section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a full HTML page from a section
    api_response = api_instance.experiment_section_get_section_content_as_html(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_content_as_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_section_data_table**
> list[list[str]] experiment_section_get_section_data_table(exp_journal_id, x_requested_with=x_requested_with)

Get the content from a DATATABLE section

The contents of the data table is returned in the following format:  ```  [      [\"cell A1 contents\", \"cell B1 contents\"],      [\"cell A2 contents\", \"cell B2 contents\"],      [\"cell A3 contents\", \"cell B3 contents\"]  ]  ```    Note that all values are returned as strings, including numbers.    Empty cells will have a value of \"\", e.g. `[[\"\", \"\", \"123\"]]` will show nothing in cells A1 and B1 and `123` in cell C1.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the content from a DATATABLE section
    api_response = api_instance.experiment_section_get_section_data_table(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[list[str]]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_section_file_list**
> PagedOfExperimentFile experiment_section_get_section_file_list(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get file list of a FILE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get file list of a FILE or CUSTOM section
    api_response = api_instance.experiment_section_get_section_file_list(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
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

# **experiment_section_get_section_image_list**
> PagedOfExperimentImage experiment_section_get_section_image_list(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get image list of an IMAGE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get image list of an IMAGE or CUSTOM section
    api_response = api_instance.experiment_section_get_section_image_list(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_image_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
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

# **experiment_section_get_section_lock_info**
> ExpJournalLockInfo experiment_section_get_section_lock_info(exp_journal_id, ignore_own_lock=ignore_own_lock, x_requested_with=x_requested_with)

Check if a text section has been locked

If the section is locked this call will return which user has the lock. If the section isn't locked it will only return the property `hasLock` with a value of `false`.    You can specify the query parameter `ignoreOwnLock` which, when set to true, reports no lock if you own the lock.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
ignore_own_lock = true # bool |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check if a text section has been locked
    api_response = api_instance.experiment_section_get_section_lock_info(exp_journal_id, ignore_own_lock=ignore_own_lock, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_lock_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **ignore_own_lock** | **bool**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ExpJournalLockInfo**](ExpJournalLockInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_section_meta**
> PagedOfExpJournalMeta experiment_section_get_section_meta(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all meta data in a section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all meta data in a section
    api_response = api_instance.experiment_section_get_section_meta(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExpJournalMeta**](PagedOfExpJournalMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_section_meta_by_name**
> ExpJournalMeta experiment_section_get_section_meta_by_name(exp_journal_id, name, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get meta data from a section by name

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
name = 'name_example' # str | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get meta data from a section by name
    api_response = api_instance.experiment_section_get_section_meta_by_name(exp_journal_id, name, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_meta_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **name** | **str**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ExpJournalMeta**](ExpJournalMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_get_section_samples**
> PagedOfSampleLarge experiment_section_get_section_samples(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get sample list from a SAMPLESIN or SAMPLESOUT section

This call will also fetch archived samples.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get sample list from a SAMPLESIN or SAMPLESOUT section
    api_response = api_instance.experiment_section_get_section_samples(exp_journal_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_get_section_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
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

# **experiment_section_is_empty_file_check**
> bool experiment_section_is_empty_file_check(exp_journal_id, oos_section_type=oos_section_type, x_requested_with=x_requested_with)

Check if the file is empty

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
oos_section_type = 'oos_section_type_example' # str |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check if the file is empty
    api_response = api_instance.experiment_section_is_empty_file_check(exp_journal_id, oos_section_type=oos_section_type, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_is_empty_file_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **oos_section_type** | **str**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_lock_section**
> experiment_section_lock_section(exp_journal_id, x_requested_with=x_requested_with)

Try to lock a text section

Use this call to prevent overwrites of text sections by other users. The lock is valid for 2 minutes but you can extend it by periodically using this call.    This call will only lock sections of types PARAGRAPH, PROCEDURE, COMMENT and NOTES.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Try to lock a text section
    api_instance.experiment_section_lock_section(exp_journal_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_lock_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_post_marvin_js_reaction_table_content**
> bool experiment_section_post_marvin_js_reaction_table_content(exp_journal_id, reaction_data_dto, x_requested_with=x_requested_with)

Post the marvin js reaction to an experiment section ID

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
reaction_data_dto = elabjournal_client.MarvinJSReactionDataDTO() # MarvinJSReactionDataDTO | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Post the marvin js reaction to an experiment section ID
    api_response = api_instance.experiment_section_post_marvin_js_reaction_table_content(exp_journal_id, reaction_data_dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_post_marvin_js_reaction_table_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **reaction_data_dto** | [**MarvinJSReactionDataDTO**](MarvinJSReactionDataDTO.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_put_section_content**
> experiment_section_put_section_content(exp_journal_id, data, x_requested_with=x_requested_with)

Update the content of a text section

You can add meta data to this call. In case of PROCEDURE sections you have to add the protocol's version ID and the values of its variables as meta data. Example:    ```  {      \"contents\": \"[protocol HTML]\"      \"meta\": [          {              \"name\": \"protVersionID\",              \"val\": \"2344\"          },          {              \"name\": \"version\",              \"val\": \"1\"          },          {              \"name\": \"protVar_7869\",              \"val\": \"100\"          },          {              \"name\": \"protVar_7871\",              \"val\": \"0.3\"          }      ]  }  ```  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
data = elabjournal_client.ExpJournalContentAndMeta() # ExpJournalContentAndMeta | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update the content of a text section
    api_instance.experiment_section_put_section_content(exp_journal_id, data, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_put_section_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **data** | [**ExpJournalContentAndMeta**](ExpJournalContentAndMeta.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_put_section_content_html**
> experiment_section_put_section_content_html(exp_journal_id, html, x_requested_with=x_requested_with)

Update a text section's HTML content

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
html = 'html_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a text section's HTML content
    api_instance.experiment_section_put_section_content_html(exp_journal_id, html, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_put_section_content_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **html** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/hl7-v2, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_put_section_data_table**
> experiment_section_put_section_data_table(exp_journal_id, table, x_requested_with=x_requested_with)

Update the content of a DATATABLE section

Supply the contents of the data table in the body with the following format:  ```  [      [\"cell A1 contents\", \"cell B1 contents\"],      [\"cell A2 contents\", \"cell B2 contents\"],      [\"cell A3 contents\", \"cell B3 contents\"]  ]  ```    Note that all cell values must be strings, even if they're numeric.    The number of columns must always be equal per row. For example, if you have three rows and three columns then you must supply the values for cells A1..C1, A2..C2 and A3..C3, even if some of those cells are empty.    You can make empty cells by supplying a value of \"\", e.g. `[[\"\", \"\", \"123\"]]` will create a table with one row and three columns where cells A1 and B1 are empty and C3 contains `123`.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
table = [elabjournal_client.list[list[str]]()] # list[list[str]] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update the content of a DATATABLE section
    api_instance.experiment_section_put_section_data_table(exp_journal_id, table, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_put_section_data_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **table** | **list[list[str]]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_restore_oos_file**
> str experiment_section_restore_oos_file(exp_journal_id, file_id, x_requested_with=x_requested_with)

Restore OOS section to selected file and retake screenshot

Put previous version of oos file back and recreate a screenshot.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
file_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Restore OOS section to selected file and retake screenshot
    api_response = api_instance.experiment_section_restore_oos_file(exp_journal_id, file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_restore_oos_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **file_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_restore_section**
> experiment_section_restore_section(exp_journal_id, x_requested_with=x_requested_with)

Restores an archived experiment section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Restores an archived experiment section
    api_instance.experiment_section_restore_section(exp_journal_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_restore_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_unlock_section**
> experiment_section_unlock_section(exp_journal_id, x_requested_with=x_requested_with)

Try to unlock a text section

Releases a lock on a section that you requested earlier with the PUT call. Note that you can only release your own locks.    If there was no lock on the specified section then this call will also return success.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Try to unlock a text section
    api_instance.experiment_section_unlock_section(exp_journal_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_unlock_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_update_experiment_section**
> experiment_section_update_experiment_section(exp_journal_id, dto, x_requested_with=x_requested_with)

Updates an experiment section's general properties

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
dto = elabjournal_client.ExpJournalUpdate() # ExpJournalUpdate | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Updates an experiment section's general properties
    api_instance.experiment_section_update_experiment_section(exp_journal_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_update_experiment_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **dto** | [**ExpJournalUpdate**](ExpJournalUpdate.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_update_section_image_description**
> experiment_section_update_section_image_description(experiment_file_id, exp_journal_id, description, x_requested_with=x_requested_with)

Updates the description of an image in an IMAGE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
description = 'description_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Updates the description of an image in an IMAGE or CUSTOM section
    api_instance.experiment_section_update_section_image_description(experiment_file_id, exp_journal_id, description, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_update_section_image_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **description** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/hl7-v2, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_update_section_image_position**
> experiment_section_update_section_image_position(experiment_file_id, exp_journal_id, position, x_requested_with=x_requested_with)

Updates the position of an image in an IMAGE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
experiment_file_id = 56 # int | 
exp_journal_id = 56 # int | 
position = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Updates the position of an image in an IMAGE or CUSTOM section
    api_instance.experiment_section_update_section_image_position(experiment_file_id, exp_journal_id, position, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_update_section_image_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_file_id** | **int**|  | 
 **exp_journal_id** | **int**|  | 
 **position** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_upload_section_canvas_image**
> int experiment_section_upload_section_canvas_image(exp_journal_id, x_requested_with=x_requested_with)

Upload an image to a CANVAS section

This call only accepts PNG files. Use MIME type `image/png`.    Additionally, the uploaded image **must** have a width of 825 pixels.  

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload an image to a CANVAS section
    api_response = api_instance.experiment_section_upload_section_canvas_image(exp_journal_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_upload_section_canvas_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_upload_section_excel_file**
> experiment_section_upload_section_excel_file(exp_journal_id, x_requested_with=x_requested_with)

Upload an Excel file to an EXCEL section

Only `.xlsx` files may be uploaded. The old Excel format `.xls` isn't supported. CUSTOM Office sections are not yet supported.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload an Excel file to an EXCEL section
    api_instance.experiment_section_upload_section_excel_file(exp_journal_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_upload_section_excel_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_upload_section_file**
> int experiment_section_upload_section_file(exp_journal_id, file_name=file_name, x_requested_with=x_requested_with)

Upload a file to a FILE or CUSTOM section

Office (Excel, Word and Powerpoint) / Excel sections are currently not supported.

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
file_name = 'file_name_example' # str |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload a file to a FILE or CUSTOM section
    api_response = api_instance.experiment_section_upload_section_file(exp_journal_id, file_name=file_name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_upload_section_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **file_name** | **str**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_section_upload_section_image**
> int experiment_section_upload_section_image(exp_journal_id, file_name=file_name, description=description, position=position, x_requested_with=x_requested_with)

Upload an image file to an IMAGE or CUSTOM section

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
api_instance = elabjournal_client.ExperimentSectionsApi(elabjournal_client.ApiClient(configuration))
exp_journal_id = 56 # int | 
file_name = 'file_name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
position = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload an image file to an IMAGE or CUSTOM section
    api_response = api_instance.experiment_section_upload_section_image(exp_journal_id, file_name=file_name, description=description, position=position, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentSectionsApi->experiment_section_upload_section_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_journal_id** | **int**|  | 
 **file_name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **position** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

