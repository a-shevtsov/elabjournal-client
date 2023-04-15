# swagger_client.ExperimentLinksApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment_link_get_linked_experiments**](ExperimentLinksApi.md#experiment_link_get_linked_experiments) | **GET** /api/v1/experiments/{experimentID}/links | Get all experiments linked to specified experiment.
[**experiment_link_set_linked_experiment**](ExperimentLinksApi.md#experiment_link_set_linked_experiment) | **POST** /api/v1/experiments/{experimentID}/links | Link an experiment to the specified experiment.
[**experiment_link_unlink_experiment**](ExperimentLinksApi.md#experiment_link_unlink_experiment) | **DELETE** /api/v1/experiments/{experimentID}/links | Unlink an experiment to the specified experiment.


# **experiment_link_get_linked_experiments**
> PagedOfExperiment experiment_link_get_linked_experiments(experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all experiments linked to specified experiment.

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
api_instance = swagger_client.ExperimentLinksApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all experiments linked to specified experiment.
    api_response = api_instance.experiment_link_get_linked_experiments(experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentLinksApi->experiment_link_get_linked_experiments: %s\n" % e)
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
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExperiment**](PagedOfExperiment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_link_set_linked_experiment**
> experiment_link_set_linked_experiment(experiment_id, target_experiment_ids, x_requested_with=x_requested_with)

Link an experiment to the specified experiment.

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
api_instance = swagger_client.ExperimentLinksApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
target_experiment_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Link an experiment to the specified experiment.
    api_instance.experiment_link_set_linked_experiment(experiment_id, target_experiment_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentLinksApi->experiment_link_set_linked_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **target_experiment_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_link_unlink_experiment**
> experiment_link_unlink_experiment(experiment_id, target_experiment_ids, x_requested_with=x_requested_with)

Unlink an experiment to the specified experiment.

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
api_instance = swagger_client.ExperimentLinksApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
target_experiment_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Unlink an experiment to the specified experiment.
    api_instance.experiment_link_unlink_experiment(experiment_id, target_experiment_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentLinksApi->experiment_link_unlink_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **target_experiment_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

