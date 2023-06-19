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
from elabjournal_client.api.experiment_api import ExperimentApi  # noqa: E501
from elabjournal_client.rest import ApiException


class TestExperimentApi(unittest.TestCase):
    """ExperimentApi unit test stubs"""

    def setUp(self):
        self.api = elabjournal_client.api.experiment_api.ExperimentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_experiment_assign_witness(self):
        """Test case for experiment_assign_witness

        Assign a witness for an experiment signature  # noqa: E501
        """
        pass

    def test_experiment_create_experiment(self):
        """Test case for experiment_create_experiment

        Create a new experiment  # noqa: E501
        """
        pass

    def test_experiment_create_saml_pre_sign_request(self):
        """Test case for experiment_create_saml_pre_sign_request

        Assign a witness for an experiment signature using SAML authentication  # noqa: E501
        """
        pass

    def test_experiment_create_saml_pre_sign_request_deprecated(self):
        """Test case for experiment_create_saml_pre_sign_request_deprecated

        Setup a new request to pre sign an experiment using SAML authentication  # noqa: E501
        """
        pass

    def test_experiment_create_saml_sign(self):
        """Test case for experiment_create_saml_sign

        Sign an experiment using SAML authentication  # noqa: E501
        """
        pass

    def test_experiment_create_saml_sign_request(self):
        """Test case for experiment_create_saml_sign_request

        Setup a new request to sign an experiment using SAML authentication  # noqa: E501
        """
        pass

    def test_experiment_decline_experiment(self):
        """Test case for experiment_decline_experiment

        Decline an experiment of a user which requested a witness.  # noqa: E501
        """
        pass

    def test_experiment_fetch_collaborators_for_experiment(self):
        """Test case for experiment_fetch_collaborators_for_experiment

        Retrieve collaborators for given experimentID  # noqa: E501
        """
        pass

    def test_experiment_get_all_experiment_templates(self):
        """Test case for experiment_get_all_experiment_templates

        Get experiment templates  # noqa: E501
        """
        pass

    def test_experiment_get_declined_witness_signatures(self):
        """Test case for experiment_get_declined_witness_signatures

        Retrieve declined witness signatures  # noqa: E501
        """
        pass

    def test_experiment_get_experiment_by_id(self):
        """Test case for experiment_get_experiment_by_id

        Get an experiment by id  # noqa: E501
        """
        pass

    def test_experiment_get_experiment_template_groups(self):
        """Test case for experiment_get_experiment_template_groups

        Get experiment template groups  # noqa: E501
        """
        pass

    def test_experiment_get_experiment_templates_by_group_id(self):
        """Test case for experiment_get_experiment_templates_by_group_id

        Get experiment templates by templateCategoryID  # noqa: E501
        """
        pass

    def test_experiment_get_experiments(self):
        """Test case for experiment_get_experiments

        Get experiments  # noqa: E501
        """
        pass

    def test_experiment_get_pending_witness_signatures(self):
        """Test case for experiment_get_pending_witness_signatures

        Retrieve pending witness signatures  # noqa: E501
        """
        pass

    def test_experiment_sign_experiment(self):
        """Test case for experiment_sign_experiment

        Sign an experiment  # noqa: E501
        """
        pass

    def test_experiment_update_witness(self):
        """Test case for experiment_update_witness

        Update the witness for an experiment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
