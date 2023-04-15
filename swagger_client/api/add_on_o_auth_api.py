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


class AddOnOAuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def o_auth2_create_configuration(self, sdk_plugin_id, o_auth_configuration, **kwargs):  # noqa: E501
        """Create new oAuthConfiguration  # noqa: E501

        Creates a OAuth 2.0 configuration to be used by a addon installed via the eLab Marketplace. You can choose to encrypt the client secret in the database aswel with the `isEncoded` property. If your eLab installation is also serving as host for public addons you can choose to distribute the OAuth 2.0 configuration when addons are synced. If `isPublic` is enabled the `clientSecret` will be encrypted by default.   Example: ```json {   'sdkPluginID': 123,    'description': 'config for my addon',    'authorizationURI': 'https://example.com/authEndpoint',   'tokenRequestURI': 'https://example.com/tokenRequestEndpoint',   'refreshURI': 'https://example.com/tokenRefreshEndpoint',   'clientID': '123456',   'clientSecret': '123456',   'isEncoded': true,    'isPublic': true }```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_create_configuration(sdk_plugin_id, o_auth_configuration, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param OAuthConfiguration o_auth_configuration: (required)
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_auth2_create_configuration_with_http_info(sdk_plugin_id, o_auth_configuration, **kwargs)  # noqa: E501
        else:
            (data) = self.o_auth2_create_configuration_with_http_info(sdk_plugin_id, o_auth_configuration, **kwargs)  # noqa: E501
            return data

    def o_auth2_create_configuration_with_http_info(self, sdk_plugin_id, o_auth_configuration, **kwargs):  # noqa: E501
        """Create new oAuthConfiguration  # noqa: E501

        Creates a OAuth 2.0 configuration to be used by a addon installed via the eLab Marketplace. You can choose to encrypt the client secret in the database aswel with the `isEncoded` property. If your eLab installation is also serving as host for public addons you can choose to distribute the OAuth 2.0 configuration when addons are synced. If `isPublic` is enabled the `clientSecret` will be encrypted by default.   Example: ```json {   'sdkPluginID': 123,    'description': 'config for my addon',    'authorizationURI': 'https://example.com/authEndpoint',   'tokenRequestURI': 'https://example.com/tokenRequestEndpoint',   'refreshURI': 'https://example.com/tokenRefreshEndpoint',   'clientID': '123456',   'clientSecret': '123456',   'isEncoded': true,    'isPublic': true }```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_create_configuration_with_http_info(sdk_plugin_id, o_auth_configuration, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param OAuthConfiguration o_auth_configuration: (required)
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sdk_plugin_id', 'o_auth_configuration', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_auth2_create_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sdk_plugin_id' is set
        if self.api_client.client_side_validation and ('sdk_plugin_id' not in params or
                                                       params['sdk_plugin_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sdk_plugin_id` when calling `o_auth2_create_configuration`")  # noqa: E501
        # verify the required parameter 'o_auth_configuration' is set
        if self.api_client.client_side_validation and ('o_auth_configuration' not in params or
                                                       params['o_auth_configuration'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `o_auth_configuration` when calling `o_auth2_create_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sdk_plugin_id' in params:
            path_params['sdkPluginID'] = params['sdk_plugin_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'o_auth_configuration' in params:
            body_params = params['o_auth_configuration']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'text/html', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/addons/{sdkPluginID}/oauthConfig', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_auth2_get_access_token(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Retrieve access token by sdkPluginID  # noqa: E501

        Retrieve the access token for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_get_access_token(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str scope: Filter by scope
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_auth2_get_access_token_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_auth2_get_access_token_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
            return data

    def o_auth2_get_access_token_with_http_info(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Retrieve access token by sdkPluginID  # noqa: E501

        Retrieve the access token for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_get_access_token_with_http_info(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str scope: Filter by scope
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sdk_plugin_id', 'expand', 'view_id', 'view_columns', 'scope', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_auth2_get_access_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sdk_plugin_id' is set
        if self.api_client.client_side_validation and ('sdk_plugin_id' not in params or
                                                       params['sdk_plugin_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sdk_plugin_id` when calling `o_auth2_get_access_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sdk_plugin_id' in params:
            path_params['sdkPluginID'] = params['sdk_plugin_id']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'view_id' in params:
            query_params.append(('$viewID', params['view_id']))  # noqa: E501
        if 'view_columns' in params:
            query_params.append(('$viewColumns', params['view_columns']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'text/html', 'application/hl7-v2'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/addons/{sdkPluginID}/oauthConfig/getAccessToken', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_auth2_get_authentication_uri(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Retrieve authentication URI by sdkPluginID  # noqa: E501

        Retrieve the OAuth 2.0 request URL for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_get_authentication_uri(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_auth2_get_authentication_uri_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_auth2_get_authentication_uri_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
            return data

    def o_auth2_get_authentication_uri_with_http_info(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Retrieve authentication URI by sdkPluginID  # noqa: E501

        Retrieve the OAuth 2.0 request URL for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_get_authentication_uri_with_http_info(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sdk_plugin_id', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_auth2_get_authentication_uri" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sdk_plugin_id' is set
        if self.api_client.client_side_validation and ('sdk_plugin_id' not in params or
                                                       params['sdk_plugin_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sdk_plugin_id` when calling `o_auth2_get_authentication_uri`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sdk_plugin_id' in params:
            path_params['sdkPluginID'] = params['sdk_plugin_id']  # noqa: E501

        query_params = []

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
            '/api/v1/addons/{sdkPluginID}/oauthConfig/getAuthUrl', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_auth2_get_oauth_configuration(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Retrieve OAuth configuration by sdkPluginID  # noqa: E501

        Retrieve the OAuth 2.0 config  for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_get_oauth_configuration(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_auth2_get_oauth_configuration_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_auth2_get_oauth_configuration_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
            return data

    def o_auth2_get_oauth_configuration_with_http_info(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Retrieve OAuth configuration by sdkPluginID  # noqa: E501

        Retrieve the OAuth 2.0 config  for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_get_oauth_configuration_with_http_info(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sdk_plugin_id', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_auth2_get_oauth_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sdk_plugin_id' is set
        if self.api_client.client_side_validation and ('sdk_plugin_id' not in params or
                                                       params['sdk_plugin_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sdk_plugin_id` when calling `o_auth2_get_oauth_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sdk_plugin_id' in params:
            path_params['sdkPluginID'] = params['sdk_plugin_id']  # noqa: E501

        query_params = []

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
            '/api/v1/addons/{sdkPluginID}/oauthConfig', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_auth2_refresh_access_and_refresh_token(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Refresh access and refresh token  # noqa: E501

        Refresh the access and refresh token for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_refresh_access_and_refresh_token(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str scope: Filter by scope
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_auth2_refresh_access_and_refresh_token_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_auth2_refresh_access_and_refresh_token_with_http_info(sdk_plugin_id, **kwargs)  # noqa: E501
            return data

    def o_auth2_refresh_access_and_refresh_token_with_http_info(self, sdk_plugin_id, **kwargs):  # noqa: E501
        """Refresh access and refresh token  # noqa: E501

        Refresh the access and refresh token for the given sdkPluginID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_refresh_access_and_refresh_token_with_http_info(sdk_plugin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str scope: Filter by scope
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sdk_plugin_id', 'expand', 'view_id', 'view_columns', 'scope', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_auth2_refresh_access_and_refresh_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sdk_plugin_id' is set
        if self.api_client.client_side_validation and ('sdk_plugin_id' not in params or
                                                       params['sdk_plugin_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sdk_plugin_id` when calling `o_auth2_refresh_access_and_refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sdk_plugin_id' in params:
            path_params['sdkPluginID'] = params['sdk_plugin_id']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'view_id' in params:
            query_params.append(('$viewID', params['view_id']))  # noqa: E501
        if 'view_columns' in params:
            query_params.append(('$viewColumns', params['view_columns']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/addons/{sdkPluginID}/oauthConfig/refreshAccessAndRefreshToken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_auth2_set_access_and_refresh_token(self, sdk_plugin_id, token_request, **kwargs):  # noqa: E501
        """Request access and refresh token by temporary code  # noqa: E501

        Request a access and refresh token with a short lived `code` property.   Example: ```json {   'code': '123456' }```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_set_access_and_refresh_token(sdk_plugin_id, token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param TokenRequest token_request: (required)
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str scope: Filter by scope
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_auth2_set_access_and_refresh_token_with_http_info(sdk_plugin_id, token_request, **kwargs)  # noqa: E501
        else:
            (data) = self.o_auth2_set_access_and_refresh_token_with_http_info(sdk_plugin_id, token_request, **kwargs)  # noqa: E501
            return data

    def o_auth2_set_access_and_refresh_token_with_http_info(self, sdk_plugin_id, token_request, **kwargs):  # noqa: E501
        """Request access and refresh token by temporary code  # noqa: E501

        Request a access and refresh token with a short lived `code` property.   Example: ```json {   'code': '123456' }```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_auth2_set_access_and_refresh_token_with_http_info(sdk_plugin_id, token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sdk_plugin_id: (required)
        :param TokenRequest token_request: (required)
        :param str expand: Expand an ID field to an object
        :param str view_id: Specify a viewID to customize the result
        :param str view_columns: Specify viewColumns to extend the result
        :param str scope: Filter by scope
        :param str x_requested_with: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sdk_plugin_id', 'token_request', 'expand', 'view_id', 'view_columns', 'scope', 'x_requested_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_auth2_set_access_and_refresh_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sdk_plugin_id' is set
        if self.api_client.client_side_validation and ('sdk_plugin_id' not in params or
                                                       params['sdk_plugin_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sdk_plugin_id` when calling `o_auth2_set_access_and_refresh_token`")  # noqa: E501
        # verify the required parameter 'token_request' is set
        if self.api_client.client_side_validation and ('token_request' not in params or
                                                       params['token_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token_request` when calling `o_auth2_set_access_and_refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sdk_plugin_id' in params:
            path_params['sdkPluginID'] = params['sdk_plugin_id']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'view_id' in params:
            query_params.append(('$viewID', params['view_id']))  # noqa: E501
        if 'view_columns' in params:
            query_params.append(('$viewColumns', params['view_columns']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501

        header_params = {}
        if 'x_requested_with' in params:
            header_params['X-Requested-With'] = params['x_requested_with']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'token_request' in params:
            body_params = params['token_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'text/html', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/addons/{sdkPluginID}/oauthConfig/setAccessAndRefreshToken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)