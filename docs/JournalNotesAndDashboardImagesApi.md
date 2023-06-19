# elabjournal_client.JournalNotesAndDashboardImagesApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**note_create_note**](JournalNotesAndDashboardImagesApi.md#note_create_note) | **POST** /api/v1/notes | Create a new note
[**note_delete_note**](JournalNotesAndDashboardImagesApi.md#note_delete_note) | **DELETE** /api/v1/notes/{noteID} | Deletes a note
[**note_delete_note_image**](JournalNotesAndDashboardImagesApi.md#note_delete_note_image) | **DELETE** /api/v1/noteImages/{noteImageID} | Deletes a note image
[**note_delete_note_images**](JournalNotesAndDashboardImagesApi.md#note_delete_note_images) | **DELETE** /api/v1/noteImages | Deletes several note images
[**note_delete_notes**](JournalNotesAndDashboardImagesApi.md#note_delete_notes) | **DELETE** /api/v1/notes | Deletes several notes
[**note_download_note_image**](JournalNotesAndDashboardImagesApi.md#note_download_note_image) | **GET** /api/v1/noteImages/{noteImageID} | Download a note image by id
[**note_get_note_by_id**](JournalNotesAndDashboardImagesApi.md#note_get_note_by_id) | **GET** /api/v1/notes/{noteID} | Gets a note by id
[**note_get_note_digest**](JournalNotesAndDashboardImagesApi.md#note_get_note_digest) | **GET** /api/v1/notes/digest | Get a digest of all your notes
[**note_get_note_image_digest**](JournalNotesAndDashboardImagesApi.md#note_get_note_image_digest) | **GET** /api/v1/noteImages/digest | Get a digest of your note images
[**note_get_notes**](JournalNotesAndDashboardImagesApi.md#note_get_notes) | **GET** /api/v1/notes | Gets your notes
[**note_patch_note**](JournalNotesAndDashboardImagesApi.md#note_patch_note) | **PATCH** /api/v1/notes/{noteID} | Updates a note&#39;s properties
[**note_upload_note_image**](JournalNotesAndDashboardImagesApi.md#note_upload_note_image) | **POST** /api/v1/noteImages | Upload a note image


# **note_create_note**
> int note_create_note(dto, x_requested_with=x_requested_with)

Create a new note

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
dto = elabjournal_client.NoteNew() # NoteNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new note
    api_response = api_instance.note_create_note(dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_create_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**NoteNew**](NoteNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_delete_note**
> note_delete_note(note_id, x_requested_with=x_requested_with)

Deletes a note

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
note_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Deletes a note
    api_instance.note_delete_note(note_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_delete_note_image**
> note_delete_note_image(note_image_id, x_requested_with=x_requested_with)

Deletes a note image

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
note_image_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Deletes a note image
    api_instance.note_delete_note_image(note_image_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_delete_note_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_image_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_delete_note_images**
> note_delete_note_images(expand=expand, view_id=view_id, view_columns=view_columns, note_image_ids=note_image_ids, x_requested_with=x_requested_with)

Deletes several note images

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
note_image_ids = 'note_image_ids_example' # str | An array of noteImageIDs to delete (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Deletes several note images
    api_instance.note_delete_note_images(expand=expand, view_id=view_id, view_columns=view_columns, note_image_ids=note_image_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_delete_note_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **note_image_ids** | **str**| An array of noteImageIDs to delete | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_delete_notes**
> note_delete_notes(expand=expand, view_id=view_id, view_columns=view_columns, note_ids=note_ids, x_requested_with=x_requested_with)

Deletes several notes

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
note_ids = 'note_ids_example' # str | An array of noteIDs to delete (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Deletes several notes
    api_instance.note_delete_notes(expand=expand, view_id=view_id, view_columns=view_columns, note_ids=note_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_delete_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **note_ids** | **str**| An array of noteIDs to delete | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_download_note_image**
> object note_download_note_image(note_image_id, expand=expand, view_id=view_id, view_columns=view_columns, max_width=max_width, x_requested_with=x_requested_with)

Download a note image by id

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
note_image_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
max_width = 'max_width_example' # str | The maximum pixel width of the image. If the original image is larger it will be scaled down. If set to 0 or omitted the original image is returned. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Download a note image by id
    api_response = api_instance.note_download_note_image(note_image_id, expand=expand, view_id=view_id, view_columns=view_columns, max_width=max_width, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_download_note_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_image_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **max_width** | **str**| The maximum pixel width of the image. If the original image is larger it will be scaled down. If set to 0 or omitted the original image is returned. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_get_note_by_id**
> Note note_get_note_by_id(note_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Gets a note by id

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
note_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Gets a note by id
    api_response = api_instance.note_get_note_by_id(note_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_get_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**Note**](Note.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_get_note_digest**
> PagedOfNoteDigest note_get_note_digest(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a digest of all your notes

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a digest of all your notes
    api_response = api_instance.note_get_note_digest(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_get_note_digest: %s\n" % e)
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

[**PagedOfNoteDigest**](PagedOfNoteDigest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_get_note_image_digest**
> PagedOfNoteImageDigest note_get_note_image_digest(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a digest of your note images

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a digest of your note images
    api_response = api_instance.note_get_note_image_digest(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_get_note_image_digest: %s\n" % e)
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

[**PagedOfNoteImageDigest**](PagedOfNoteImageDigest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_get_notes**
> PagedOfNote note_get_notes(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, note_ids=note_ids, title=title, x_requested_with=x_requested_with)

Gets your notes

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
note_ids = 'note_ids_example' # str | Filter by an array of noteIDs (optional)
title = 'title_example' # str | Filter by note title (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Gets your notes
    api_response = api_instance.note_get_notes(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, note_ids=note_ids, title=title, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_get_notes: %s\n" % e)
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
 **note_ids** | **str**| Filter by an array of noteIDs | [optional] 
 **title** | **str**| Filter by note title | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfNote**](PagedOfNote.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_patch_note**
> note_patch_note(note_id, dto, x_requested_with=x_requested_with)

Updates a note's properties

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
note_id = 56 # int | 
dto = elabjournal_client.NoteUpdate() # NoteUpdate | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Updates a note's properties
    api_instance.note_patch_note(note_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_patch_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**|  | 
 **dto** | [**NoteUpdate**](NoteUpdate.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_upload_note_image**
> int note_upload_note_image(file_name, x_requested_with=x_requested_with)

Upload a note image

  This call expects inline binary image data for a single file. Multipart content is **not** supported.    The Content-Type header is required and must be set to the correct image MIME type. For example: `Content-Type: image/jpeg`    The URI parameter 'fileName' is required and must contain a correct extension for the image. For example: `?fileName=My%20Image.jpg`    The maximum file size is determined by eLab's 'files:maxFileSize' system setting. By default this is set to 50 MB.    For uploading large image files, consider streaming the HTTP request using [Chunked Transfer Encoding](https://en.wikipedia.org/wiki/Chunked_transfer_encoding) if your HTTP client library supports it.      

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
api_instance = elabjournal_client.JournalNotesAndDashboardImagesApi(elabjournal_client.ApiClient(configuration))
file_name = 'file_name_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Upload a note image
    api_response = api_instance.note_upload_note_image(file_name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalNotesAndDashboardImagesApi->note_upload_note_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

