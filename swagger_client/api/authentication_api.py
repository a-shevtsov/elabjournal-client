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


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authentication_auth_user(self, body, **kwargs):  # noqa: E501
        """Authenticate and obtain an API token for a user.  # noqa: E501

          Supplying only a username and password in the body is sufficient for most users.    Example:  ```  {    \"username\": \"demo@elabjournal.com\",    \"password\": \"abc123\"  }  ```    You can use the resulting token property in the api_key field above to access all other API calls.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_auth_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthRequest body: (required)
        :param str x_requested_with: 
        :return: AuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_auth_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_auth_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def authentication_auth_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Authenticate and obtain an API token for a user.  # noqa: E501

          Supplying only a username and password in the body is sufficient for most users.    Example:  ```  {    \"username\": \"demo@elabjournal.com\",    \"password\": \"abc123\"  }  ```    You can use the resulting token property in the api_key field above to access all other API calls.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_auth_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthRequest body: (required)
        :param str x_requested_with: 
        :return: AuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_auth_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `authentication_auth_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'text/html', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/auth/user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_check_app_version(self, **kwargs):  # noqa: E501
        """authentication_check_app_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_check_app_version(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str x_requested_with: 
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_check_app_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.authentication_check_app_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def authentication_check_app_version_with_http_info(self, **kwargs):  # noqa: E501
        """authentication_check_app_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_check_app_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str x_requested_with: 
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand', 'view_id', 'view_columns', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_check_app_version" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'view_id' in params:
            query_params.append(('$viewID', params['view_id']))  # noqa: E501
        if 'view_columns' in params:
            query_params.append(('$viewColumns', params['view_columns']))  # noqa: E501

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
            '/api/v1/auth/checkAppVersion', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_exchange_token(self, body, **kwargs):  # noqa: E501
        """Obtain an API token for a user, based on a request token generated while using the Add-On authentication flow for 3rd party systems.  # noqa: E501

            Example:  ```  {    \"requestToken\": \"abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc1\"  }  ```    You can use the resulting apiToken property in the api_key field above to access all other API calls.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_exchange_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthRequestToken body: (required)
        :param str x_requested_with: 
        :return: AuthRequestTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_exchange_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.authentication_exchange_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def authentication_exchange_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Obtain an API token for a user, based on a request token generated while using the Add-On authentication flow for 3rd party systems.  # noqa: E501

            Example:  ```  {    \"requestToken\": \"abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc1\"  }  ```    You can use the resulting apiToken property in the api_key field above to access all other API calls.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_exchange_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthRequestToken body: (required)
        :param str x_requested_with: 
        :return: AuthRequestTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_exchange_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `authentication_exchange_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'text/html', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/auth/user/exchangeToken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthRequestTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def authentication_user_info(self, **kwargs):  # noqa: E501
        """Get authentication details that you're currently using  # noqa: E501

        In most cases set the body to:  ```  {}  ```    Add the following body to the request to receive a \"domain\" field in the response that points to the correct endpoint in case the user is located on another eLab deployment:  ```  {    \"domain\": \"my.current.domain\"  }  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_user_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str field: A specific field to request
        :param str x_requested_with: 
        :return: AuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authentication_user_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.authentication_user_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def authentication_user_info_with_http_info(self, **kwargs):  # noqa: E501
        """Get authentication details that you're currently using  # noqa: E501

        In most cases set the body to:  ```  {}  ```    Add the following body to the request to receive a \"domain\" field in the response that points to the correct endpoint in case the user is located on another eLab deployment:  ```  {    \"domain\": \"my.current.domain\"  }  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authentication_user_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str field: A specific field to request
        :param str x_requested_with: 
        :return: AuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand', 'view_id', 'view_columns', 'field', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authentication_user_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'view_id' in params:
            query_params.append(('$viewID', params['view_id']))  # noqa: E501
        if 'view_columns' in params:
            query_params.append(('$viewColumns', params['view_columns']))  # noqa: E501
        if 'field' in params:
            query_params.append(('field', params['field']))  # noqa: E501

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
            '/api/v1/auth/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
