# swagger_client.NotificationApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_delete**](NotificationApi.md#notification_delete) | **POST** /api/v1/notifications/delete | Set the deleted flag for a number of notifications
[**notification_get_notifications**](NotificationApi.md#notification_get_notifications) | **GET** /api/v1/notifications | Get notifications by a list of IDs
[**notification_get_notifications_digest**](NotificationApi.md#notification_get_notifications_digest) | **GET** /api/v1/notifications/digest | Get digest information for all notifications
[**notification_send_notification**](NotificationApi.md#notification_send_notification) | **POST** /api/v1/notifications/send | Send a notification
[**notification_set_read**](NotificationApi.md#notification_set_read) | **POST** /api/v1/notifications/setRead | Set the read flag for a number of notifications


# **notification_delete**
> notification_delete(notification_ids, x_requested_with=x_requested_with)

Set the deleted flag for a number of notifications

Supply the notification IDs to set to deleted in the body as an array of integers.    Example:  ```  [123, 456]  ```      

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Set the deleted flag for a number of notifications
    api_instance.notification_delete(notification_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_get_notifications**
> NotificationEntryList notification_get_notifications(notification_ids, x_requested_with=x_requested_with)

Get notifications by a list of IDs

The notificationsIDs array should be a comma-separated list (not line-separated!)

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_ids = [56] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get notifications by a list of IDs
    api_response = api_instance.notification_get_notifications(notification_ids, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_ids** | [**list[int]**](int.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**NotificationEntryList**](NotificationEntryList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_get_notifications_digest**
> NotificationDigestList notification_get_notifications_digest(x_requested_with=x_requested_with)

Get digest information for all notifications

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get digest information for all notifications
    api_response = api_instance.notification_get_notifications_digest(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_get_notifications_digest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**NotificationDigestList**](NotificationDigestList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_send_notification**
> notification_send_notification(notification, x_requested_with=x_requested_with)

Send a notification

Send a notification  - [int]userID, [string]message, [NotificationPriority]priority, [NotificationScope]scope, [int]senderUserID, [string]targetURL

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification = swagger_client.NotificationForUser() # NotificationForUser | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Send a notification
    api_instance.notification_send_notification(notification, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_send_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | [**NotificationForUser**](NotificationForUser.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_set_read**
> notification_set_read(notification_ids, x_requested_with=x_requested_with)

Set the read flag for a number of notifications

Supply the notification IDs to set to read in the body as an array of integers.    Example:  ```  [123, 456]  ```      

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Set the read flag for a number of notifications
    api_instance.notification_set_read(notification_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_set_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

