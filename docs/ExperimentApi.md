# swagger_client.ExperimentApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment_assign_witness**](ExperimentApi.md#experiment_assign_witness) | **POST** /api/v1/experiments/{experimentID}/sign/assignWitness | Assign a witness for an experiment signature
[**experiment_create_experiment**](ExperimentApi.md#experiment_create_experiment) | **POST** /api/v1/experiments | Create a new experiment
[**experiment_create_saml_pre_sign_request**](ExperimentApi.md#experiment_create_saml_pre_sign_request) | **POST** /api/v1/experiments/{experimentID}/sign/assignWitness/saml | Assign a witness for an experiment signature using SAML authentication
[**experiment_create_saml_pre_sign_request_deprecated**](ExperimentApi.md#experiment_create_saml_pre_sign_request_deprecated) | **POST** /api/v1/experiments/{experimentID}/presignrequest/saml/{witnessID} | Setup a new request to pre sign an experiment using SAML authentication
[**experiment_create_saml_sign**](ExperimentApi.md#experiment_create_saml_sign) | **POST** /api/v1/experiments/{experimentID}/sign/saml | Sign an experiment using SAML authentication
[**experiment_create_saml_sign_request**](ExperimentApi.md#experiment_create_saml_sign_request) | **POST** /api/v1/experiments/{experimentID}/signrequest/saml | Setup a new request to sign an experiment using SAML authentication
[**experiment_decline_experiment**](ExperimentApi.md#experiment_decline_experiment) | **POST** /api/v1/experiments/{experimentID}/sign/decline | Decline an experiment of a user which requested a witness.
[**experiment_fetch_collaborators_for_experiment**](ExperimentApi.md#experiment_fetch_collaborators_for_experiment) | **GET** /api/v1/experiments/{experimentID}/collaborators | Retrieve collaborators for given experimentID
[**experiment_get_all_experiment_templates**](ExperimentApi.md#experiment_get_all_experiment_templates) | **GET** /api/v1/experiments/templates | Get experiment templates
[**experiment_get_declined_witness_signatures**](ExperimentApi.md#experiment_get_declined_witness_signatures) | **GET** /api/v1/experiments/signatures/declined | Retrieve declined witness signatures
[**experiment_get_experiment_by_id**](ExperimentApi.md#experiment_get_experiment_by_id) | **GET** /api/v1/experiments/{experimentID} | Get an experiment by id
[**experiment_get_experiment_template_groups**](ExperimentApi.md#experiment_get_experiment_template_groups) | **GET** /api/v1/experiments/templateGroups | Get experiment template groups
[**experiment_get_experiment_templates_by_group_id**](ExperimentApi.md#experiment_get_experiment_templates_by_group_id) | **GET** /api/v1/experiments/templates/{expTemplateLabelID} | Get experiment templates by templateCategoryID
[**experiment_get_experiments**](ExperimentApi.md#experiment_get_experiments) | **GET** /api/v1/experiments | Get experiments
[**experiment_get_pending_witness_signatures**](ExperimentApi.md#experiment_get_pending_witness_signatures) | **GET** /api/v1/experiments/signatures/pending | Retrieve pending witness signatures
[**experiment_sign_experiment**](ExperimentApi.md#experiment_sign_experiment) | **POST** /api/v1/experiments/{experimentID}/sign | Sign an experiment
[**experiment_update_witness**](ExperimentApi.md#experiment_update_witness) | **POST** /api/v1/experiments/{experimentID}/sign/reassignWitness | Update the witness for an experiment


# **experiment_assign_witness**
> experiment_assign_witness(experiment_id, body, x_requested_with=x_requested_with)

Assign a witness for an experiment signature

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
body = swagger_client.AssignWitness() # AssignWitness | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Assign a witness for an experiment signature
    api_instance.experiment_assign_witness(experiment_id, body, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_assign_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **body** | [**AssignWitness**](AssignWitness.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_create_experiment**
> int experiment_create_experiment(experiment, x_requested_with=x_requested_with)

Create a new experiment

When autoCollaborate (optional) is true, the collaborators will be assigned to the experiment based on the                           setting of study or project. Default is false.    When templateID (optional) is 0, < 0, or left out, the experiment will be created without a template. Default is 0.    Status (optional) can be PENDING, PROGRESS, COMPLETED. Default is PENDING.  

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment = swagger_client.ExperimentNew() # ExperimentNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new experiment
    api_response = api_instance.experiment_create_experiment(experiment, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_create_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | [**ExperimentNew**](ExperimentNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_create_saml_pre_sign_request**
> experiment_create_saml_pre_sign_request(experiment_id, body, x_requested_with=x_requested_with)

Assign a witness for an experiment signature using SAML authentication

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
body = swagger_client.AssignWitness() # AssignWitness | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Assign a witness for an experiment signature using SAML authentication
    api_instance.experiment_create_saml_pre_sign_request(experiment_id, body, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_create_saml_pre_sign_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **body** | [**AssignWitness**](AssignWitness.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_create_saml_pre_sign_request_deprecated**
> experiment_create_saml_pre_sign_request_deprecated(experiment_id, witness_id, x_requested_with=x_requested_with)

Setup a new request to pre sign an experiment using SAML authentication

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
witness_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Setup a new request to pre sign an experiment using SAML authentication
    api_instance.experiment_create_saml_pre_sign_request_deprecated(experiment_id, witness_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_create_saml_pre_sign_request_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **witness_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_create_saml_sign**
> experiment_create_saml_sign(experiment_id, x_requested_with=x_requested_with)

Sign an experiment using SAML authentication

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Sign an experiment using SAML authentication
    api_instance.experiment_create_saml_sign(experiment_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_create_saml_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_create_saml_sign_request**
> experiment_create_saml_sign_request(experiment_id, x_requested_with=x_requested_with)

Setup a new request to sign an experiment using SAML authentication

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Setup a new request to sign an experiment using SAML authentication
    api_instance.experiment_create_saml_sign_request(experiment_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_create_saml_sign_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_decline_experiment**
> experiment_decline_experiment(experiment_id, reason, x_requested_with=x_requested_with)

Decline an experiment of a user which requested a witness.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
reason = 'reason_example' # str | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Decline an experiment of a user which requested a witness.
    api_instance.experiment_decline_experiment(experiment_id, reason, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_decline_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **reason** | **str**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_fetch_collaborators_for_experiment**
> PagedOfUserInfo experiment_fetch_collaborators_for_experiment(experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Retrieve collaborators for given experimentID

Retrieve all collaborators for the given experiment id.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve collaborators for given experimentID
    api_response = api_instance.experiment_fetch_collaborators_for_experiment(experiment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_fetch_collaborators_for_experiment: %s\n" % e)
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

[**PagedOfUserInfo**](PagedOfUserInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_get_all_experiment_templates**
> PagedOfExperimentTemplateLarge experiment_get_all_experiment_templates(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, creator_id=creator_id, x_requested_with=x_requested_with)

Get experiment templates

This call will fetch all templates within the group of the current user. The templates can be sorted on 'experimentID' and 'created'. Also the templates can be filtered on 'creatorID'

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
creator_id = 'creator_id_example' # str | Filter by creator (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get experiment templates
    api_response = api_instance.experiment_get_all_experiment_templates(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, creator_id=creator_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_get_all_experiment_templates: %s\n" % e)
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
 **creator_id** | **str**| Filter by creator | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExperimentTemplateLarge**](PagedOfExperimentTemplateLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_get_declined_witness_signatures**
> experiment_get_declined_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Retrieve declined witness signatures

Retrieve all declined witness signatures for the current user.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve declined witness signatures
    api_instance.experiment_get_declined_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_get_declined_witness_signatures: %s\n" % e)
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

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_get_experiment_by_id**
> ExperimentLarge experiment_get_experiment_by_id(experiment_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get an experiment by id

expand values  * signature  

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an experiment by id
    api_response = api_instance.experiment_get_experiment_by_id(experiment_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_get_experiment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**ExperimentLarge**](ExperimentLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_get_experiment_template_groups**
> PagedOfExperimentTemplateGroup experiment_get_experiment_template_groups(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get experiment template groups

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get experiment template groups
    api_response = api_instance.experiment_get_experiment_template_groups(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_get_experiment_template_groups: %s\n" % e)
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

[**PagedOfExperimentTemplateGroup**](PagedOfExperimentTemplateGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_get_experiment_templates_by_group_id**
> PagedOfExperimentTemplate experiment_get_experiment_templates_by_group_id(exp_template_label_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get experiment templates by templateCategoryID

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
exp_template_label_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get experiment templates by templateCategoryID
    api_response = api_instance.experiment_get_experiment_templates_by_group_id(exp_template_label_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_get_experiment_templates_by_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exp_template_label_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExperimentTemplate**](PagedOfExperimentTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_get_experiments**
> PagedOfExperimentLarge experiment_get_experiments(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, created_before=created_before, status_changed_before=status_changed_before, project_id=project_id, study_id=study_id, search_name=search_name, search=search, created_after=created_after, status_changed_after=status_changed_after, x_requested_with=x_requested_with)

Get experiments

expand values  * signature  

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
created_before = 'created_before_example' # str | Filters experiments on their created date (YYYY-MM-DDThh:mm:ss), you will only receive experiments created before the given date (optional)
status_changed_before = 'status_changed_before_example' # str | filter experiments on their statusChange date (YYYY-MM-DDThh:mm:ss), you will only receive experiments with a status change before the given date (optional)
project_id = 'project_id_example' # str | Filter by project (optional)
study_id = 'study_id_example' # str | Filter by study (optional)
search_name = 'search_name_example' # str | Search by experiment name (optional)
search = 'search_example' # str | Search experiments by name or contents (optional)
created_after = 'created_after_example' # str | Filters experiments on their created date (YYYY-MM-DDThh:mm:ss), you will only receive experiments created after the given date (optional)
status_changed_after = 'status_changed_after_example' # str | filter experiments on their statusChange date (YYYY-MM-DDThh:mm:ss), you will only receive experiments with a status change after the given date (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get experiments
    api_response = api_instance.experiment_get_experiments(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, created_before=created_before, status_changed_before=status_changed_before, project_id=project_id, study_id=study_id, search_name=search_name, search=search, created_after=created_after, status_changed_after=status_changed_after, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_get_experiments: %s\n" % e)
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
 **created_before** | **str**| Filters experiments on their created date (YYYY-MM-DDThh:mm:ss), you will only receive experiments created before the given date | [optional] 
 **status_changed_before** | **str**| filter experiments on their statusChange date (YYYY-MM-DDThh:mm:ss), you will only receive experiments with a status change before the given date | [optional] 
 **project_id** | **str**| Filter by project | [optional] 
 **study_id** | **str**| Filter by study | [optional] 
 **search_name** | **str**| Search by experiment name | [optional] 
 **search** | **str**| Search experiments by name or contents | [optional] 
 **created_after** | **str**| Filters experiments on their created date (YYYY-MM-DDThh:mm:ss), you will only receive experiments created after the given date | [optional] 
 **status_changed_after** | **str**| filter experiments on their statusChange date (YYYY-MM-DDThh:mm:ss), you will only receive experiments with a status change after the given date | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExperimentLarge**](PagedOfExperimentLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_get_pending_witness_signatures**
> experiment_get_pending_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Retrieve pending witness signatures

Retrieve all pending witness signatures for the current user.

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve pending witness signatures
    api_instance.experiment_get_pending_witness_signatures(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_get_pending_witness_signatures: %s\n" % e)
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

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_sign_experiment**
> experiment_sign_experiment(experiment_id, x_requested_with=x_requested_with)

Sign an experiment

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Sign an experiment
    api_instance.experiment_sign_experiment(experiment_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_sign_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment_update_witness**
> experiment_update_witness(experiment_id, experiment_witness, x_requested_with=x_requested_with)

Update the witness for an experiment

Update the existing witness for the given experiment

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
api_instance = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
experiment_id = 56 # int | 
experiment_witness = swagger_client.ReassignExperimentWitness() # ReassignExperimentWitness | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update the witness for an experiment
    api_instance.experiment_update_witness(experiment_id, experiment_witness, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiment_update_witness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **int**|  | 
 **experiment_witness** | [**ReassignExperimentWitness**](ReassignExperimentWitness.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

