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
from swagger_client.api.task_management_api import TaskManagementApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTaskManagementApi(unittest.TestCase):
    """TaskManagementApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.task_management_api.TaskManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_task_bulk_update_status(self):
        """Test case for task_bulk_update_status

        Update multiple task statuses  # noqa: E501
        """
        pass

    def test_task_create_task(self):
        """Test case for task_create_task

        Create a task  # noqa: E501
        """
        pass

    def test_task_create_task_experiment_link(self):
        """Test case for task_create_task_experiment_link

        Setup an experiment link  # noqa: E501
        """
        pass

    def test_task_create_task_protocol_link(self):
        """Test case for task_create_task_protocol_link

        Setup a protocol link  # noqa: E501
        """
        pass

    def test_task_create_task_sample_link(self):
        """Test case for task_create_task_sample_link

        Setup a sample link  # noqa: E501
        """
        pass

    def test_task_delete_task(self):
        """Test case for task_delete_task

        Delete a task  # noqa: E501
        """
        pass

    def test_task_delete_tasks(self):
        """Test case for task_delete_tasks

        Delete multiple tasks  # noqa: E501
        """
        pass

    def test_task_get_all(self):
        """Test case for task_get_all

        List all tasks for current logged in user  # noqa: E501
        """
        pass

    def test_task_get_linked_experiments(self):
        """Test case for task_get_linked_experiments

        Get the linked experiments of a task  # noqa: E501
        """
        pass

    def test_task_get_linked_protocols(self):
        """Test case for task_get_linked_protocols

        Get the linked protocols of a task  # noqa: E501
        """
        pass

    def test_task_get_linked_samples(self):
        """Test case for task_get_linked_samples

        Get the linked samples of a task  # noqa: E501
        """
        pass

    def test_task_get_single(self):
        """Test case for task_get_single

        Get single task  # noqa: E501
        """
        pass

    def test_task_update_task(self):
        """Test case for task_update_task

        Update a task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()