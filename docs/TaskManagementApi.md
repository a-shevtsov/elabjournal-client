# elabjournal_client.TaskManagementApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_bulk_update_status**](TaskManagementApi.md#task_bulk_update_status) | **PATCH** /api/v1/tasks/bulk | Update multiple task statuses
[**task_create_task**](TaskManagementApi.md#task_create_task) | **POST** /api/v1/tasks | Create a task
[**task_create_task_experiment_link**](TaskManagementApi.md#task_create_task_experiment_link) | **POST** /api/v1/tasks/{taskID}/links/experiment/{targetExperimentID} | Setup an experiment link
[**task_create_task_protocol_link**](TaskManagementApi.md#task_create_task_protocol_link) | **POST** /api/v1/tasks/{taskID}/links/protocol/{targetProtocolID} | Setup a protocol link
[**task_create_task_sample_link**](TaskManagementApi.md#task_create_task_sample_link) | **POST** /api/v1/tasks/{taskID}/links/sample/{targetSampleID} | Setup a sample link
[**task_delete_task**](TaskManagementApi.md#task_delete_task) | **DELETE** /api/v1/tasks/{taskID} | Delete a task
[**task_delete_tasks**](TaskManagementApi.md#task_delete_tasks) | **DELETE** /api/v1/tasks/bulk | Delete multiple tasks
[**task_get_all**](TaskManagementApi.md#task_get_all) | **GET** /api/v1/tasks | List all tasks for current logged in user
[**task_get_linked_experiments**](TaskManagementApi.md#task_get_linked_experiments) | **GET** /api/v1/tasks/{taskID}/links/experiment | Get the linked experiments of a task
[**task_get_linked_protocols**](TaskManagementApi.md#task_get_linked_protocols) | **GET** /api/v1/tasks/{taskID}/links/protocol | Get the linked protocols of a task
[**task_get_linked_samples**](TaskManagementApi.md#task_get_linked_samples) | **GET** /api/v1/tasks/{taskID}/links/sample | Get the linked samples of a task
[**task_get_single**](TaskManagementApi.md#task_get_single) | **GET** /api/v1/tasks/{taskID} | Get single task
[**task_update_task**](TaskManagementApi.md#task_update_task) | **PATCH** /api/v1/tasks/{taskID} | Update a task


# **task_bulk_update_status**
> task_bulk_update_status(bulk_status_update, x_requested_with=x_requested_with)

Update multiple task statuses

Updates multiple task statuses. The valid statuses are: 'ASSIGNED', 'PROGRESS', 'COMPLETED'.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
bulk_status_update = elabjournal_client.TaskBulkStatusUpdate() # TaskBulkStatusUpdate | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update multiple task statuses
    api_instance.task_bulk_update_status(bulk_status_update, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_bulk_update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_status_update** | [**TaskBulkStatusUpdate**](TaskBulkStatusUpdate.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_create_task**
> task_create_task(task, x_requested_with=x_requested_with)

Create a task

Creates a task. The required fields are 'assigneeID' and 'status'. If the assigneeID is 0 the assigneeID willbe changed to the current user id. Also the task can only be assigned to an user in the same group as the current user.The valid statuses are: 'ASSIGNED', 'PROGRESS', 'COMPLETED'.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task = elabjournal_client.TaskNew() # TaskNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a task
    api_instance.task_create_task(task, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**TaskNew**](TaskNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_create_task_experiment_link**
> task_create_task_experiment_link(task_id, target_experiment_id, x_requested_with=x_requested_with)

Setup an experiment link

Creates a link between an experiment and a task.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
target_experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Setup an experiment link
    api_instance.task_create_task_experiment_link(task_id, target_experiment_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_create_task_experiment_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **target_experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_create_task_protocol_link**
> task_create_task_protocol_link(task_id, target_protocol_id, x_requested_with=x_requested_with)

Setup a protocol link

Creates a link between a protocol and a task

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
target_protocol_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Setup a protocol link
    api_instance.task_create_task_protocol_link(task_id, target_protocol_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_create_task_protocol_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **target_protocol_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_create_task_sample_link**
> task_create_task_sample_link(task_id, target_sample_id, x_requested_with=x_requested_with)

Setup a sample link

Creates a link between a sample and a task.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
target_sample_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Setup a sample link
    api_instance.task_create_task_sample_link(task_id, target_sample_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_create_task_sample_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **target_sample_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_delete_task**
> task_delete_task(task_id, x_requested_with=x_requested_with)

Delete a task

Deletes a task which is created by or assigned to the current user

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a task
    api_instance.task_delete_task(task_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_delete_tasks**
> task_delete_tasks(task_ids, x_requested_with=x_requested_with)

Delete multiple tasks

Deletes multiple tasks which are created by or assigned to the current user

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_ids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete multiple tasks
    api_instance.task_delete_tasks(task_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_delete_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_get_all**
> task_get_all(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, status=status, assignee=assignee, before_date=before_date, after_date=after_date, x_requested_with=x_requested_with)

List all tasks for current logged in user

Gets all the tasks for the current user. The list of task objects will consist of tasks that are created by or assigned to the           current user in descending order based on the created date.     $expand values (separate with comma for multiple expands):  * experiments  * samples  * protocols          

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
status = 'status_example' # str | Filter by status (optional)
assignee = 'assignee_example' # str | Filter by assignee (optional)
before_date = 'before_date_example' # str | Filter by due date before (optional)
after_date = 'after_date_example' # str | Filter by due date after (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # List all tasks for current logged in user
    api_instance.task_get_all(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, status=status, assignee=assignee, before_date=before_date, after_date=after_date, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_get_all: %s\n" % e)
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
 **status** | **str**| Filter by status | [optional] 
 **assignee** | **str**| Filter by assignee | [optional] 
 **before_date** | **str**| Filter by due date before | [optional] 
 **after_date** | **str**| Filter by due date after | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_get_linked_experiments**
> task_get_linked_experiments(task_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the linked experiments of a task

Fetches a link between an experiment and a task.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the linked experiments of a task
    api_instance.task_get_linked_experiments(task_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_get_linked_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_get_linked_protocols**
> task_get_linked_protocols(task_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the linked protocols of a task

Fetches all linked protocols of that task.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the linked protocols of a task
    api_instance.task_get_linked_protocols(task_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_get_linked_protocols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_get_linked_samples**
> task_get_linked_samples(task_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the linked samples of a task

Fetches a link between an sample and a task.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the linked samples of a task
    api_instance.task_get_linked_samples(task_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_get_linked_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_get_single**
> task_get_single(task_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get single task

Gets a single task which is created by or assigned to the current user

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get single task
    api_instance.task_get_single(task_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_get_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_update_task**
> task_update_task(task_id, task, x_requested_with=x_requested_with)

Update a task

Updates a task. The required fields are 'assigneeID' and 'status'. If the assigneeID is 0 the assigneeID will be changed to the current user id. Also the task can only be assigned to an user in the same group as the current user.The valid statuses are: 'ASSIGNED', 'PROGRESS', 'COMPLETED'.

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
api_instance = elabjournal_client.TaskManagementApi(elabjournal_client.ApiClient(configuration))
task_id = 56 # int | 
task = elabjournal_client.TaskUpdate() # TaskUpdate | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a task
    api_instance.task_update_task(task_id, task, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling TaskManagementApi->task_update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task** | [**TaskUpdate**](TaskUpdate.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

