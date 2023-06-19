# elabjournal_client.FileAndMetaFileStorageApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_convert_from_tiff_to_png_data_string**](FileAndMetaFileStorageApi.md#file_convert_from_tiff_to_png_data_string) | **GET** /api/v1/files/{fileID}/convertFromTiffToPngDataString | Get a tiff file by file id from your current group, and converts it to a png data string
[**file_delete_file_by_id**](FileAndMetaFileStorageApi.md#file_delete_file_by_id) | **DELETE** /api/v1/files/{fileID} | Delete a file by id from your current group
[**file_get_all_files**](FileAndMetaFileStorageApi.md#file_get_all_files) | **GET** /api/v1/files | List files
[**file_get_file_by_id**](FileAndMetaFileStorageApi.md#file_get_file_by_id) | **GET** /api/v1/files/{fileID} | Get a file by file id from your current group
[**file_get_file_by_id_for_group**](FileAndMetaFileStorageApi.md#file_get_file_by_id_for_group) | **GET** /api/v1/groups/{groupID}/files/{fileID} | Get a file by group and file id
[**file_get_latest_file_by_id**](FileAndMetaFileStorageApi.md#file_get_latest_file_by_id) | **GET** /api/v1/files/latest/{fileID} | Get a file by file id from your current group
[**file_get_meta_file_by_id**](FileAndMetaFileStorageApi.md#file_get_meta_file_by_id) | **GET** /api/v1/metaFiles/{metaFileID} | Get a meta file by file id from your current group
[**file_get_meta_file_by_id_for_group**](FileAndMetaFileStorageApi.md#file_get_meta_file_by_id_for_group) | **GET** /api/v1/groups/{groupID}/metaFiles/{metaFileID} | Get a meta file by group and file id
[**file_upload**](FileAndMetaFileStorageApi.md#file_upload) | **POST** /api/v1/files | Upload files to the server
[**file_upload_meta_file**](FileAndMetaFileStorageApi.md#file_upload_meta_file) | **POST** /api/v1/metaFiles | Upload metafiles to the server
[**file_upload_workstation_file**](FileAndMetaFileStorageApi.md#file_upload_workstation_file) | **POST** /api/v1/workstationFiles | Upload files to a staging area


# **file_convert_from_tiff_to_png_data_string**
> str file_convert_from_tiff_to_png_data_string(file_id, expand=expand, view_id=view_id, view_columns=view_columns, new_width=new_width, x_requested_with=x_requested_with)

Get a tiff file by file id from your current group, and converts it to a png data string

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
file_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
new_width = 'new_width_example' # str | New width for redimension. default 0 = no redimension (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a tiff file by file id from your current group, and converts it to a png data string
    api_response = api_instance.file_convert_from_tiff_to_png_data_string(file_id, expand=expand, view_id=view_id, view_columns=view_columns, new_width=new_width, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_convert_from_tiff_to_png_data_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **new_width** | **str**| New width for redimension. default 0 &#x3D; no redimension | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/hl7-v2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_delete_file_by_id**
> object file_delete_file_by_id(file_id, x_requested_with=x_requested_with)

Delete a file by id from your current group

Deletes a file from the file storage. The file will still be available for download if linked to a sample.

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
file_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a file by id from your current group
    api_response = api_instance.file_delete_file_by_id(file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_delete_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_all_files**
> PagedOfFileInStorageLarge file_get_all_files(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, file_name=file_name, group_id=group_id, folder_id=folder_id, user_id=user_id, search=search, x_requested_with=x_requested_with)

List files

Gets file IDs and other data associated with stored files from your group.  Results can be filtered on file name, folderID and groupID. The file name must be an exact match.   The groupID parameter can be used to extract all records with a specific valid group number.   If left blank, the current active group will be used        $expand values (separate with comma for multiple expands):      * location  

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
file_name = 'file_name_example' # str | Filter files by name (optional)
group_id = 'group_id_example' # str | Filter files by a group you are a member of (optional)
folder_id = 'folder_id_example' # str | Filter files by folder ID (optional)
user_id = 'user_id_example' # str | Filter files by userID (optional)
search = 'search_example' # str | Search by (partial) filename. (Minimum search 3 characters) (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # List files
    api_response = api_instance.file_get_all_files(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, file_name=file_name, group_id=group_id, folder_id=folder_id, user_id=user_id, search=search, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_get_all_files: %s\n" % e)
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
 **file_name** | **str**| Filter files by name | [optional] 
 **group_id** | **str**| Filter files by a group you are a member of | [optional] 
 **folder_id** | **str**| Filter files by folder ID | [optional] 
 **user_id** | **str**| Filter files by userID | [optional] 
 **search** | **str**| Search by (partial) filename. (Minimum search 3 characters) | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfFileInStorageLarge**](PagedOfFileInStorageLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_file_by_id**
> object file_get_file_by_id(file_id, x_requested_with=x_requested_with)

Get a file by file id from your current group

This call returns the version of the file associated with the fileID passed as parameter.  

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
file_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a file by file id from your current group
    api_response = api_instance.file_get_file_by_id(file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_get_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_file_by_id_for_group**
> object file_get_file_by_id_for_group(group_id, file_id, x_requested_with=x_requested_with)

Get a file by group and file id

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
group_id = 56 # int | 
file_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a file by group and file id
    api_response = api_instance.file_get_file_by_id_for_group(group_id, file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_get_file_by_id_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **file_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_latest_file_by_id**
> object file_get_latest_file_by_id(file_id, x_requested_with=x_requested_with)

Get a file by file id from your current group

This call returns the latest version of the file within its lineage, regardless of the actual fileID passed as parameter.  

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
file_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a file by file id from your current group
    api_response = api_instance.file_get_latest_file_by_id(file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_get_latest_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_meta_file_by_id**
> object file_get_meta_file_by_id(meta_file_id, x_requested_with=x_requested_with)

Get a meta file by file id from your current group

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
meta_file_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a meta file by file id from your current group
    api_response = api_instance.file_get_meta_file_by_id(meta_file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_get_meta_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_file_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_get_meta_file_by_id_for_group**
> object file_get_meta_file_by_id_for_group(group_id, meta_file_id, x_requested_with=x_requested_with)

Get a meta file by group and file id

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
group_id = 56 # int | 
meta_file_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a meta file by group and file id
    api_response = api_instance.file_get_meta_file_by_id_for_group(group_id, meta_file_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_get_meta_file_by_id_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **meta_file_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_upload**
> FileInStorage file_upload(file_name, url=url, folder_id=folder_id, x_requested_with=x_requested_with)

Upload files to the server

Files can be a maximum size of 250 mb. Currently only supports local storage. A valid URL (e.g. https://www.abc.com/myfile.jpg, not www.abc.com/myfile.jpg) can be given as a optional parameter which will be used to fetch a file from the URL provided instead of uploading a file directly from local machine. On Elabjournal file storage browser your files will appear in the outside of a folder unless the folderID is provided.Swagger cannot be used for testing file uploads, please use another external tool (e.g. Postman).  Example url local file: https://www.elabjournal.com/api/v1/files?fileName=testfile.jpg   Example url remote file: https://www.elabjournal.com/api/v1/files?fileName=testfile.jpg&url=https://picsum.photos/200

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
file_name = 'file_name_example' # str | 
url = 'url_example' # str |  (optional)
folder_id = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload files to the server
    api_response = api_instance.file_upload(file_name, url=url, folder_id=folder_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **url** | **str**|  | [optional] 
 **folder_id** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**FileInStorage**](FileInStorage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_upload_meta_file**
> MetaFile file_upload_meta_file(file_name, description=description, url=url, x_requested_with=x_requested_with)

Upload metafiles to the server

Files can be a maximum size of 250 mb. Currently only supports local storage. A valid URL (e.g. https://www.abc.com/myfile.jpg, not wwww.abc.com/myfile.jpg) can be given as a optional parameter which will be used to fetch a file from the URL provided instead of uploading a file directly from local machine. Note that Swagger cannot be used for testing file uploads, please use another external tool (e.g. Postman).  

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
file_name = 'file_name_example' # str | 
description = 'description_example' # str |  (optional)
url = 'url_example' # str |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload metafiles to the server
    api_response = api_instance.file_upload_meta_file(file_name, description=description, url=url, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_upload_meta_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **description** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**MetaFile**](MetaFile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_upload_workstation_file**
> CreateWorkstationFileDto file_upload_workstation_file(file_name, total_chunks, chunk, chunk_hash, file_identifier, x_requested_with=x_requested_with)

Upload files to a staging area

Files uploaded with this API call will be stored in a general experiment storage space accessible throughout the application and can be later transferred to either an experiment or moved into the file storage.

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
api_instance = elabjournal_client.FileAndMetaFileStorageApi(elabjournal_client.ApiClient(configuration))
file_name = 'file_name_example' # str | 
total_chunks = 56 # int | 
chunk = 56 # int | 
chunk_hash = 'chunk_hash_example' # str | 
file_identifier = 'file_identifier_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload files to a staging area
    api_response = api_instance.file_upload_workstation_file(file_name, total_chunks, chunk, chunk_hash, file_identifier, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAndMetaFileStorageApi->file_upload_workstation_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **total_chunks** | **int**|  | 
 **chunk** | **int**|  | 
 **chunk_hash** | **str**|  | 
 **file_identifier** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**CreateWorkstationFileDto**](CreateWorkstationFileDto.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

