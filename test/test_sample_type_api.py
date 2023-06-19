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
from elabjournal_client.api.sample_type_api import SampleTypeApi  # noqa: E501
from elabjournal_client.rest import ApiException


class TestSampleTypeApi(unittest.TestCase):
    """SampleTypeApi unit test stubs"""

    def setUp(self):
        self.api = elabjournal_client.api.sample_type_api.SampleTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sample_type_create_sample_type(self):
        """Test case for sample_type_create_sample_type

        Create a new sample type  # noqa: E501
        """
        pass

    def test_sample_type_create_sample_type_meta(self):
        """Test case for sample_type_create_sample_type_meta

        Create a new sample type's meta field  # noqa: E501
        """
        pass

    def test_sample_type_delete_sample_type(self):
        """Test case for sample_type_delete_sample_type

        Delete a sample type  # noqa: E501
        """
        pass

    def test_sample_type_delete_sample_type_meta(self):
        """Test case for sample_type_delete_sample_type_meta

        Delete a sample type's meta field  # noqa: E501
        """
        pass

    def test_sample_type_get_sample_type_by_id(self):
        """Test case for sample_type_get_sample_type_by_id

        Get a sample type by id  # noqa: E501
        """
        pass

    def test_sample_type_get_sample_type_meta(self):
        """Test case for sample_type_get_sample_type_meta

        Get a sample type's meta field by id  # noqa: E501
        """
        pass

    def test_sample_type_get_sample_type_meta_defaults(self):
        """Test case for sample_type_get_sample_type_meta_defaults

        Get a sample type meta field's default options  # noqa: E501
        """
        pass

    def test_sample_type_get_sample_type_metas(self):
        """Test case for sample_type_get_sample_type_metas

        Get all of a sample type's meta fields  # noqa: E501
        """
        pass

    def test_sample_type_get_sample_type_metas_for_all_sample_types(self):
        """Test case for sample_type_get_sample_type_metas_for_all_sample_types

        Get all meta fields from all sample types  # noqa: E501
        """
        pass

    def test_sample_type_get_sample_types(self):
        """Test case for sample_type_get_sample_types

        Get sample types  # noqa: E501
        """
        pass

    def test_sample_type_get_sample_types_for_names(self):
        """Test case for sample_type_get_sample_types_for_names

        Get a list of sample types for multiple names  # noqa: E501
        """
        pass

    def test_sample_type_patch_sample_type(self):
        """Test case for sample_type_patch_sample_type

        Update a sample type's properties  # noqa: E501
        """
        pass

    def test_sample_type_patch_sample_type_meta(self):
        """Test case for sample_type_patch_sample_type_meta

        Update a sample type meta field's properties  # noqa: E501
        """
        pass

    def test_sample_type_put_sample_type_meta(self):
        """Test case for sample_type_put_sample_type_meta

        Create or update a sample type's meta field  # noqa: E501
        """
        pass

    def test_sample_type_put_sample_type_meta_defaults(self):
        """Test case for sample_type_put_sample_type_meta_defaults

        Update, Remove and Create a sample type meta field's default options  # noqa: E501
        """
        pass

    def test_sample_type_restore_sample_type(self):
        """Test case for sample_type_restore_sample_type

        Restore the given sampleType from archive  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
