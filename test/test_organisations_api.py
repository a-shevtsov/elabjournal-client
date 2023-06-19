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
from elabjournal_client.api.organisations_api import OrganisationsApi  # noqa: E501
from elabjournal_client.rest import ApiException


class TestOrganisationsApi(unittest.TestCase):
    """OrganisationsApi unit test stubs"""

    def setUp(self):
        self.api = elabjournal_client.api.organisations_api.OrganisationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_organisation_search_organisations(self):
        """Test case for organisation_search_organisations

        Find organisation by name  # noqa: E501
        """
        pass

    def test_organisation_settings_create_active_group_setting(self):
        """Test case for organisation_settings_create_active_group_setting

        Create an active institute setting  # noqa: E501
        """
        pass

    def test_organisation_settings_create_institute_setting(self):
        """Test case for organisation_settings_create_institute_setting

        Create a institute setting  # noqa: E501
        """
        pass

    def test_organisation_settings_delete_institute_setting(self):
        """Test case for organisation_settings_delete_institute_setting

        Delete an institute setting  # noqa: E501
        """
        pass

    def test_organisation_settings_delete_institute_setting_for_current_institute(self):
        """Test case for organisation_settings_delete_institute_setting_for_current_institute

        Delete an active institute setting  # noqa: E501
        """
        pass

    def test_organisation_settings_get_active_institute_setting(self):
        """Test case for organisation_settings_get_active_institute_setting

        Get an active institute setting  # noqa: E501
        """
        pass

    def test_organisation_settings_get_active_institute_settings(self):
        """Test case for organisation_settings_get_active_institute_settings

        Get active institute settings  # noqa: E501
        """
        pass

    def test_organisation_settings_get_institute_setting(self):
        """Test case for organisation_settings_get_institute_setting

        Get an institute setting  # noqa: E501
        """
        pass

    def test_organisation_settings_get_institute_settings(self):
        """Test case for organisation_settings_get_institute_settings

        Get institute settings  # noqa: E501
        """
        pass

    def test_organisation_settings_update_active_institute_setting(self):
        """Test case for organisation_settings_update_active_institute_setting

        Update an active institute setting  # noqa: E501
        """
        pass

    def test_organisation_settings_update_institute_setting(self):
        """Test case for organisation_settings_update_institute_setting

        Update an institute setting  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
