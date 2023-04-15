# swagger_client.ProjectApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_create_project**](ProjectApi.md#project_create_project) | **POST** /api/v1/projects | Create a new project
[**project_get_projects**](ProjectApi.md#project_get_projects) | **GET** /api/v1/projects | Get projects


# **project_create_project**
> project_create_project(data, x_requested_with=x_requested_with)

Create a new project

Creates a project in elabjournal and provide labels as well as meta data to the project. The only hard requirement is that a project musthave a name, both labels and metadata are optional additions. If metadata is provided, the name field is a required paramater. Options for metadata types is either FILE or TEXT.   Example: ```json { 'name': 'mytestproject',  'longname': 'mytestprojectlong', 'description': 'my test description', 'notes': 'my test notes', 'label': [  'label1',  'label2',  ], 'projectMeta': [   {   'name': 'testmeta',   'value': 'test meta value',   'metatype': 'TEXT',   }  ] }```

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
data = swagger_client.CreateProjectData() # CreateProjectData | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new project
    api_instance.project_create_project(data, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ProjectApi->project_create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateProjectData**](CreateProjectData.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_get_projects**
> PagedOfProjectLarge project_get_projects(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, search_name=search_name, project_id=project_id, search=search, x_requested_with=x_requested_with)

Get projects

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
search_name = 'search_name_example' # str | Search by project name or internal ID (optional)
project_id = 'project_id_example' # str | Filter by project (optional)
search = 'search_example' # str | Search experiments by name or contents (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get projects
    api_response = api_instance.project_get_projects(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, search_name=search_name, project_id=project_id, search=search, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project_get_projects: %s\n" % e)
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
 **search_name** | **str**| Search by project name or internal ID | [optional] 
 **project_id** | **str**| Filter by project | [optional] 
 **search** | **str**| Search experiments by name or contents | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfProjectLarge**](PagedOfProjectLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

