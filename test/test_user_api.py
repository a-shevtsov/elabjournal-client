# coding: utf-8

"""
    eLabNext REST API

    ## Authentication    To authenticate use the `POST /api/v1/auth/user` call below in the Authentication tab with a username and password. This will return an API token as property `token`.    All API calls, with the exception of authentication, need this API token in the header as `Authorization: [API token]`. Omitting this header or supplying an invalid API token results in an error 401 Not Authorized.    Example: `Authorization: eec0727eaf6f7b127aaec1ec33c21caf`    To use this with the **Try it out** buttons, fill in the **api_key** field above with the API token.    ## Request Bodies    The API uses JSON with character set UTF-8 for request and response bodies.    In any call that utilizes request bodies you must supply the header `Content-Type: application/json; charset=utf-8`.    ## Response Codes    Status Code | Name | Meaning  ----------- | ---- | -------  200 | OK | Success. (JSON) content is included in the body.  204 | No Content | Success and no body content. This status is always returned when a call does not produce content.  400 | Bad Request | Bad/missing parameters or JSON input.  401 | Not Authorized | Authentication header is missing or the supplied API token is invalid.  403 | Forbidden | The user associated with the API token has no permission for the requested operation.  404 | Not Found | The resource specified in the request does not exist.  405 | Method Not Allowed | The API call was made with an unsupported HTTP method. (e.g. GET instead of POST.)  409 | Conflict | A POST or PUT operation failed because it conflicts with existing data.  500 | Internal Server Error | A generic error occurred on the server. The response's `message` property contains a description of the error.        # noqa: E501

    OpenAPI spec version: v1
    Contact: enquiries@elabnext.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.user_api import UserApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_get_current_user_id(self):
        """Test case for user_get_current_user_id

        Get the current user Info  # noqa: E501
        """
        pass

    def test_user_get_current_user_plugin_setting(self):
        """Test case for user_get_current_user_plugin_setting

        Get the current user plugin setting  # noqa: E501
        """
        pass

    def test_user_get_current_user_setting(self):
        """Test case for user_get_current_user_setting

        Get the current user setting  # noqa: E501
        """
        pass

    def test_user_get_user_info(self):
        """Test case for user_get_user_info

        Get the information of a user  # noqa: E501
        """
        pass

    def test_user_get_user_profile(self):
        """Test case for user_get_user_profile

        Get the profile of a user  # noqa: E501
        """
        pass

    def test_user_search_users(self):
        """Test case for user_search_users

        Find users by email address  # noqa: E501
        """
        pass

    def test_user_set_current_user_plugin_setting(self):
        """Test case for user_set_current_user_plugin_setting

        Set the current user plugin setting  # noqa: E501
        """
        pass

    def test_user_set_current_user_setting(self):
        """Test case for user_set_current_user_setting

        Set the current user setting  # noqa: E501
        """
        pass

    def test_user_settings_admin_create_user_setting(self):
        """Test case for user_settings_admin_create_user_setting

        Create user setting by user id  # noqa: E501
        """
        pass

    def test_user_settings_admin_delete_user_setting(self):
        """Test case for user_settings_admin_delete_user_setting

        Delete an user setting by user id  # noqa: E501
        """
        pass

    def test_user_settings_admin_get_user_setting(self):
        """Test case for user_settings_admin_get_user_setting

        Get an user setting by user id  # noqa: E501
        """
        pass

    def test_user_settings_admin_get_user_settings(self):
        """Test case for user_settings_admin_get_user_settings

        Get user settings by user id  # noqa: E501
        """
        pass

    def test_user_settings_admin_update_user_setting(self):
        """Test case for user_settings_admin_update_user_setting

        Update an user setting by user id  # noqa: E501
        """
        pass

    def test_user_settings_create_user_setting(self):
        """Test case for user_settings_create_user_setting

        Create a current user setting  # noqa: E501
        """
        pass

    def test_user_settings_delete_user_setting(self):
        """Test case for user_settings_delete_user_setting

        Delete a user setting for the logged in user  # noqa: E501
        """
        pass

    def test_user_settings_get_user_setting(self):
        """Test case for user_settings_get_user_setting

        Get a current user setting  # noqa: E501
        """
        pass

    def test_user_settings_get_user_settings(self):
        """Test case for user_settings_get_user_settings

        Get a current user settings  # noqa: E501
        """
        pass

    def test_user_settings_update_user_setting(self):
        """Test case for user_settings_update_user_setting

        Update a current user setting  # noqa: E501
        """
        pass

    def test_user_update_user_profile(self):
        """Test case for user_update_user_profile

        Update user information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()