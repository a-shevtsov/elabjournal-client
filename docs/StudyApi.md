# elabjournal_client.StudyApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**study_create_saml_sign_request**](StudyApi.md#study_create_saml_sign_request) | **POST** /api/v1/studies/{studyID}/signrequest/saml | Request to sign a study using SAML authentication
[**study_create_study**](StudyApi.md#study_create_study) | **POST** /api/v1/studies | Create a study
[**study_get_studies**](StudyApi.md#study_get_studies) | **GET** /api/v1/studies | Get studies


# **study_create_saml_sign_request**
> study_create_saml_sign_request(study_id, experimentids, x_requested_with=x_requested_with)

Request to sign a study using SAML authentication

This endpoint creates a new request to sign a study. Only to be used with SAML.

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
api_instance = elabjournal_client.StudyApi(elabjournal_client.ApiClient(configuration))
study_id = 56 # int | 
experimentids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Request to sign a study using SAML authentication
    api_instance.study_create_saml_sign_request(study_id, experimentids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StudyApi->study_create_saml_sign_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**|  | 
 **experimentids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_create_study**
> Study study_create_study(new_study, x_requested_with=x_requested_with)

Create a study

This endpoint creates a new study associated with a given project but does not provide the additional functionality of adding collaborators or adding meta fields. A valid projectID is needed to create a study with this endpoint which can be retrieved by quering the `/api/v1/project` GET endpoint. The approve field options are 'NOTREQUIRED' or 'BYSTUDYMANAGER'

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
api_instance = elabjournal_client.StudyApi(elabjournal_client.ApiClient(configuration))
new_study = elabjournal_client.StudyLimited() # StudyLimited | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a study
    api_response = api_instance.study_create_study(new_study, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudyApi->study_create_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_study** | [**StudyLimited**](StudyLimited.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**Study**](Study.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_studies**
> PagedOfStudyLarge study_get_studies(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, search_name=search_name, study_id=study_id, project_id=project_id, search=search, x_requested_with=x_requested_with)

Get studies

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
api_instance = elabjournal_client.StudyApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
search_name = 'search_name_example' # str | Search by study name (optional)
study_id = 'study_id_example' # str | Filter by studyID (optional)
project_id = 'project_id_example' # str | Filter by project (optional)
search = 'search_example' # str | Search experiments by name or contents (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get studies
    api_response = api_instance.study_get_studies(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, search_name=search_name, study_id=study_id, project_id=project_id, search=search, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudyApi->study_get_studies: %s\n" % e)
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
 **search_name** | **str**| Search by study name | [optional] 
 **study_id** | **str**| Filter by studyID | [optional] 
 **project_id** | **str**| Filter by project | [optional] 
 **search** | **str**| Search experiments by name or contents | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStudyLarge**](PagedOfStudyLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

