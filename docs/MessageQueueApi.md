# elabjournal_client.MessageQueueApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_queue_message_queue_deliver**](MessageQueueApi.md#message_queue_message_queue_deliver) | **POST** /api/v1/messagequeue/deliver | Deliver a new message
[**message_queue_message_queue_retrieve**](MessageQueueApi.md#message_queue_message_queue_retrieve) | **GET** /api/v1/messagequeue/retrieve | Retrieve a new message from the queue


# **message_queue_message_queue_deliver**
> MessageQueueDeliveryResponse message_queue_message_queue_deliver(topic, payload, token=token, lifetime=lifetime, x_requested_with=x_requested_with)

Deliver a new message

  This endpoint adds a message to the message queue    parameters:        - topic (required): String used as an address to send/retrieve messages, i.e. myAddonRootVar/function1/myTopic/. The same topic must be provided to retrieve the message.  - payload (required): this is the message you want to send, e.g. \"test message\".  - token (optional): Any string that will act as a key. If given, the exact same string must be provided during the GET retrieve call to gain access to the message.  - lifetime (optional): The time the message is available in seconds. Default is 8 hours, 7 days is the maximum (adjustable for dedicated installations).  

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
api_instance = elabjournal_client.MessageQueueApi(elabjournal_client.ApiClient(configuration))
topic = 'topic_example' # str | 
payload = 'payload_example' # str | 
token = 'token_example' # str |  (optional)
lifetime = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Deliver a new message
    api_response = api_instance.message_queue_message_queue_deliver(topic, payload, token=token, lifetime=lifetime, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageQueueApi->message_queue_message_queue_deliver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **payload** | **str**|  | 
 **token** | **str**|  | [optional] 
 **lifetime** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**MessageQueueDeliveryResponse**](MessageQueueDeliveryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/hl7-v2, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_queue_message_queue_retrieve**
> list[MessageQueueMessage] message_queue_message_queue_retrieve(topic, token=token, keep_at_server=keep_at_server, x_requested_with=x_requested_with)

Retrieve a new message from the queue

  This endpoint retrieves a message from the message queue    parameters:        - topic (required): String used as an address to send/retrieve messages, i.e. myAddonRootVar/function1/myTopic/. The same topic must be provided as during sending of the message.  - token (optional): String that unlocks the message. The exact same string must be provided during the POST deliver call to gain access to the message.  

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
api_instance = elabjournal_client.MessageQueueApi(elabjournal_client.ApiClient(configuration))
topic = 'topic_example' # str | 
token = 'token_example' # str |  (optional)
keep_at_server = true # bool |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Retrieve a new message from the queue
    api_response = api_instance.message_queue_message_queue_retrieve(topic, token=token, keep_at_server=keep_at_server, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageQueueApi->message_queue_message_queue_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **token** | **str**|  | [optional] 
 **keep_at_server** | **bool**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[MessageQueueMessage]**](MessageQueueMessage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

