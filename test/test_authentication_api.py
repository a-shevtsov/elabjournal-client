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

import elabjournal_client
from elabjournal_client.api.authentication_api import AuthenticationApi  # noqa: E501
from elabjournal_client.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = elabjournal_client.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authentication_auth_user(self):
        """Test case for authentication_auth_user

        Authenticate and obtain an API token for a user.  # noqa: E501
        """
        pass

    def test_authentication_check_app_version(self):
        """Test case for authentication_check_app_version

        """
        pass

    def test_authentication_exchange_token(self):
        """Test case for authentication_exchange_token

        Obtain an API token for a user, based on a request token generated while using the Add-On authentication flow for 3rd party systems.  # noqa: E501
        """
        pass

    def test_authentication_user_info(self):
        """Test case for authentication_user_info

        Get authentication details that you're currently using  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
