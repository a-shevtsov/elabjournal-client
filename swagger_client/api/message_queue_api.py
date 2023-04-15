# coding: utf-8

"""
    eLabNext REST API

    ## Authentication    To authenticate use the `POST /api/v1/auth/user` call below in the Authentication tab with a username and password. This will return an API token as property `token`.    All API calls, with the exception of authentication, need this API token in the header as `Authorization: [API token]`. Omitting this header or supplying an invalid API token results in an error 401 Not Authorized.    Example: `Authorization: eec0727eaf6f7b127aaec1ec33c21caf`    To use this with the **Try it out** buttons, fill in the **api_key** field above with the API token.    ## Request Bodies    The API uses JSON with character set UTF-8 for request and response bodies.    In any call that utilizes request bodies you must supply the header `Content-Type: application/json; charset=utf-8`.    ## Response Codes    Status Code | Name | Meaning  ----------- | ---- | -------  200 | OK | Success. (JSON) content is included in the body.  204 | No Content | Success and no body content. This status is always returned when a call does not produce content.  400 | Bad Request | Bad/missing parameters or JSON input.  401 | Not Authorized | Authentication header is missing or the supplied API token is invalid.  403 | Forbidden | The user associated with the API token has no permission for the requested operation.  404 | Not Found | The resource specified in the request does not exist.  405 | Method Not Allowed | The API call was made with an unsupported HTTP method. (e.g. GET instead of POST.)  409 | Conflict | A POST or PUT operation failed because it conflicts with existing data.  500 | Internal Server Error | A generic error occurred on the server. The response's `message` property contains a description of the error.        # noqa: E501

    OpenAPI spec version: v1
    Contact: enquiries@elabnext.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MessageQueueApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def message_queue_message_queue_deliver(self, topic, payload, **kwargs):  # noqa: E501
        """Deliver a new message  # noqa: E501

          This endpoint adds a message to the message queue    parameters:        - topic (required): String used as an address to send/retrieve messages, i.e. myAddonRootVar/function1/myTopic/. The same topic must be provided to retrieve the message.  - payload (required): this is the message you want to send, e.g. \"test message\".  - token (optional): Any string that will act as a key. If given, the exact same string must be provided during the GET retrieve call to gain access to the message.  - lifetime (optional): The time the message is available in seconds. Default is 8 hours, 7 days is the maximum (adjustable for dedicated installations).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.message_queue_message_queue_deliver(topic, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic: (required)
        :param str payload: (required)
        :param str token:
        :param int lifetime:
        :param str x_requested_with: 
        :return: MessageQueueDeliveryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.message_queue_message_queue_deliver_with_http_info(topic, payload, **kwargs)  # noqa: E501
        else:
            (data) = self.message_queue_message_queue_deliver_with_http_info(topic, payload, **kwargs)  # noqa: E501
            return data

    def message_queue_message_queue_deliver_with_http_info(self, topic, payload, **kwargs):  # noqa: E501
        """Deliver a new message  # noqa: E501

          This endpoint adds a message to the message queue    parameters:        - topic (required): String used as an address to send/retrieve messages, i.e. myAddonRootVar/function1/myTopic/. The same topic must be provided to retrieve the message.  - payload (required): this is the message you want to send, e.g. \"test message\".  - token (optional): Any string that will act as a key. If given, the exact same string must be provided during the GET retrieve call to gain access to the message.  - lifetime (optional): The time the message is available in seconds. Default is 8 hours, 7 days is the maximum (adjustable for dedicated installations).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.message_queue_message_queue_deliver_with_http_info(topic, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic: (required)
        :param str payload: (required)
        :param str token:
        :param int lifetime:
        :param str x_requested_with: 
        :return: MessageQueueDeliveryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topic', 'payload', 'token', 'lifetime', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method message_queue_message_queue_deliver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topic' is set
        if self.api_client.client_side_validation and ('topic' not in params or
                                                       params['topic'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `topic` when calling `message_queue_message_queue_deliver`")  # noqa: E501
        # verify the required parameter 'payload' is set
        if self.api_client.client_side_validation and ('payload' not in params or
                                                       params['payload'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payload` when calling `message_queue_message_queue_deliver`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'topic' in params:
            query_params.append(('topic', params['topic']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'lifetime' in params:
            query_params.append(('lifetime', params['lifetime']))  # noqa: E501

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'text/html', 'application/hl7-v2', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/messagequeue/deliver', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageQueueDeliveryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def message_queue_message_queue_retrieve(self, topic, **kwargs):  # noqa: E501
        """Retrieve a new message from the queue  # noqa: E501

          This endpoint retrieves a message from the message queue    parameters:        - topic (required): String used as an address to send/retrieve messages, i.e. myAddonRootVar/function1/myTopic/. The same topic must be provided as during sending of the message.  - token (optional): String that unlocks the message. The exact same string must be provided during the POST deliver call to gain access to the message.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.message_queue_message_queue_retrieve(topic, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic: (required)
        :param str token:
        :param bool keep_at_server:
        :param str x_requested_with: 
        :return: list[MessageQueueMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.message_queue_message_queue_retrieve_with_http_info(topic, **kwargs)  # noqa: E501
        else:
            (data) = self.message_queue_message_queue_retrieve_with_http_info(topic, **kwargs)  # noqa: E501
            return data

    def message_queue_message_queue_retrieve_with_http_info(self, topic, **kwargs):  # noqa: E501
        """Retrieve a new message from the queue  # noqa: E501

          This endpoint retrieves a message from the message queue    parameters:        - topic (required): String used as an address to send/retrieve messages, i.e. myAddonRootVar/function1/myTopic/. The same topic must be provided as during sending of the message.  - token (optional): String that unlocks the message. The exact same string must be provided during the POST deliver call to gain access to the message.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.message_queue_message_queue_retrieve_with_http_info(topic, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic: (required)
        :param str token:
        :param bool keep_at_server:
        :param str x_requested_with: 
        :return: list[MessageQueueMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topic', 'token', 'keep_at_server', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method message_queue_message_queue_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topic' is set
        if self.api_client.client_side_validation and ('topic' not in params or
                                                       params['topic'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `topic` when calling `message_queue_message_queue_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'topic' in params:
            query_params.append(('topic', params['topic']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'keep_at_server' in params:
            query_params.append(('keepAtServer', params['keep_at_server']))  # noqa: E501

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/messagequeue/retrieve', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MessageQueueMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)