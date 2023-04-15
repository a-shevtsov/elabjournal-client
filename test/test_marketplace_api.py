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
from swagger_client.api.marketplace_api import MarketplaceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMarketplaceApi(unittest.TestCase):
    """MarketplaceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.marketplace_api.MarketplaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_market_place_get_addon(self):
        """Test case for market_place_get_addon

        Get an available addon by ID.  # noqa: E501
        """
        pass

    def test_market_place_get_addon_code(self):
        """Test case for market_place_get_addon_code

        Get the script code of the specified available addon.  # noqa: E501
        """
        pass

    def test_market_place_get_all_addons(self):
        """Test case for market_place_get_all_addons

        Get all available addons.  # noqa: E501
        """
        pass

    def test_market_place_has_addon_enabled(self):
        """Test case for market_place_has_addon_enabled

        Check to see if current logged in user has addon with rootVar X enabled. If scope specified only installation for that scope will be checked, otherwise installation for any scope will be checked.  # noqa: E501
        """
        pass

    def test_market_place_media_get_icon(self):
        """Test case for market_place_media_get_icon

        Get icon by media ID.  # noqa: E501
        """
        pass

    def test_market_place_media_get_image(self):
        """Test case for market_place_media_get_image

        Get image by media ID.  # noqa: E501
        """
        pass

    def test_market_place_validate_dependencies(self):
        """Test case for market_place_validate_dependencies

        Check whether the required dependencies of the given addon are published.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()