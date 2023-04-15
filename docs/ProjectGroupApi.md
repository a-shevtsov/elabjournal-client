# swagger_client.ProjectGroupApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_group_get_projectgroups_by_user_id**](ProjectGroupApi.md#project_group_get_projectgroups_by_user_id) | **GET** /api/v1/projectgroups | Get projectgroup for the specified user ID
[**project_group_set_projectgroup_manager**](ProjectGroupApi.md#project_group_set_projectgroup_manager) | **PUT** /api/v1/projectgroups/{projectGroupID}/manager | Set/Unset the specified user as project group manager


# **project_group_get_projectgroups_by_user_id**
> PagedOfProjectGroup project_group_get_projectgroups_by_user_id(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, user_id=user_id, archived=archived, is_manager=is_manager, sub_group_id=sub_group_id, x_requested_with=x_requested_with)

Get projectgroup for the specified user ID

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
api_instance = swagger_client.ProjectGroupApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
user_id = 'user_id_example' # str | User to retrieve the project group from, default userID is current logged in userID (optional)
archived = 'archived_example' # str | If you want to retrieve the archived group (default: false, so you only see non archived groups) (optional)
is_manager = 'is_manager_example' # str | Return only those projectgroups having user with given id as groupmanager (optional)
sub_group_id = 'sub_group_id_example' # str | Return only those projectgroups that belong to the subGroup with the given id as subGroupID (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get projectgroup for the specified user ID
    api_response = api_instance.project_group_get_projectgroups_by_user_id(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, user_id=user_id, archived=archived, is_manager=is_manager, sub_group_id=sub_group_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupApi->project_group_get_projectgroups_by_user_id: %s\n" % e)
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
 **user_id** | **str**| User to retrieve the project group from, default userID is current logged in userID | [optional] 
 **archived** | **str**| If you want to retrieve the archived group (default: false, so you only see non archived groups) | [optional] 
 **is_manager** | **str**| Return only those projectgroups having user with given id as groupmanager | [optional] 
 **sub_group_id** | **str**| Return only those projectgroups that belong to the subGroup with the given id as subGroupID | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfProjectGroup**](PagedOfProjectGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_group_set_projectgroup_manager**
> bool project_group_set_projectgroup_manager(project_group_id, project_group_member_dto, x_requested_with=x_requested_with)

Set/Unset the specified user as project group manager

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
api_instance = swagger_client.ProjectGroupApi(swagger_client.ApiClient(configuration))
project_group_id = 56 # int | 
project_group_member_dto = swagger_client.ProjectGroupMemberDTO() # ProjectGroupMemberDTO | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Set/Unset the specified user as project group manager
    api_response = api_instance.project_group_set_projectgroup_manager(project_group_id, project_group_member_dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupApi->project_group_set_projectgroup_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_group_id** | **int**|  | 
 **project_group_member_dto** | [**ProjectGroupMemberDTO**](ProjectGroupMemberDTO.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

