# coding: utf-8

"""
    eLabNext REST API

    ## Authentication    To authenticate use the `POST /api/v1/auth/user` call below in the Authentication tab with a username and password. This will return an API token as property `token`.    All API calls, with the exception of authentication, need this API token in the header as `Authorization: [API token]`. Omitting this header or supplying an invalid API token results in an error 401 Not Authorized.    Example: `Authorization: eec0727eaf6f7b127aaec1ec33c21caf`    To use this with the **Try it out** buttons, fill in the **api_key** field above with the API token.    ## Request Bodies    The API uses JSON with character set UTF-8 for request and response bodies.    In any call that utilizes request bodies you must supply the header `Content-Type: application/json; charset=utf-8`.    ## Response Codes    Status Code | Name | Meaning  ----------- | ---- | -------  200 | OK | Success. (JSON) content is included in the body.  204 | No Content | Success and no body content. This status is always returned when a call does not produce content.  400 | Bad Request | Bad/missing parameters or JSON input.  401 | Not Authorized | Authentication header is missing or the supplied API token is invalid.  403 | Forbidden | The user associated with the API token has no permission for the requested operation.  404 | Not Found | The resource specified in the request does not exist.  405 | Method Not Allowed | The API call was made with an unsupported HTTP method. (e.g. GET instead of POST.)  409 | Conflict | A POST or PUT operation failed because it conflicts with existing data.  500 | Internal Server Error | A generic error occurred on the server. The response's `message` property contains a description of the error.        # noqa: E501

    OpenAPI spec version: v1
    Contact: enquiries@elabnext.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class TaskLarge(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'creator': 'UserInfo',
        'assignee': 'UserInfo',
        'samples': 'list[Sample]',
        'experiments': 'list[Experiment]',
        'protocols': 'list[Protocol]',
        'creator_id': 'int',
        'task_id': 'int',
        'created': 'datetime',
        'updated': 'datetime',
        'assignee_id': 'int',
        'due': 'datetime',
        'title': 'str',
        'contents': 'str',
        'status': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'assignee': 'assignee',
        'samples': 'samples',
        'experiments': 'experiments',
        'protocols': 'protocols',
        'creator_id': 'creatorID',
        'task_id': 'taskID',
        'created': 'created',
        'updated': 'updated',
        'assignee_id': 'assigneeID',
        'due': 'due',
        'title': 'title',
        'contents': 'contents',
        'status': 'status'
    }

    def __init__(self, creator=None, assignee=None, samples=None, experiments=None, protocols=None, creator_id=None, task_id=None, created=None, updated=None, assignee_id=None, due=None, title=None, contents=None, status=None, _configuration=None):  # noqa: E501
        """TaskLarge - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creator = None
        self._assignee = None
        self._samples = None
        self._experiments = None
        self._protocols = None
        self._creator_id = None
        self._task_id = None
        self._created = None
        self._updated = None
        self._assignee_id = None
        self._due = None
        self._title = None
        self._contents = None
        self._status = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if assignee is not None:
            self.assignee = assignee
        if samples is not None:
            self.samples = samples
        if experiments is not None:
            self.experiments = experiments
        if protocols is not None:
            self.protocols = protocols
        if creator_id is not None:
            self.creator_id = creator_id
        if task_id is not None:
            self.task_id = task_id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if assignee_id is not None:
            self.assignee_id = assignee_id
        if due is not None:
            self.due = due
        if title is not None:
            self.title = title
        if contents is not None:
            self.contents = contents
        if status is not None:
            self.status = status

    @property
    def creator(self):
        """Gets the creator of this TaskLarge.  # noqa: E501


        :return: The creator of this TaskLarge.  # noqa: E501
        :rtype: UserInfo
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TaskLarge.


        :param creator: The creator of this TaskLarge.  # noqa: E501
        :type: UserInfo
        """

        self._creator = creator

    @property
    def assignee(self):
        """Gets the assignee of this TaskLarge.  # noqa: E501


        :return: The assignee of this TaskLarge.  # noqa: E501
        :rtype: UserInfo
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this TaskLarge.


        :param assignee: The assignee of this TaskLarge.  # noqa: E501
        :type: UserInfo
        """

        self._assignee = assignee

    @property
    def samples(self):
        """Gets the samples of this TaskLarge.  # noqa: E501


        :return: The samples of this TaskLarge.  # noqa: E501
        :rtype: list[Sample]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this TaskLarge.


        :param samples: The samples of this TaskLarge.  # noqa: E501
        :type: list[Sample]
        """

        self._samples = samples

    @property
    def experiments(self):
        """Gets the experiments of this TaskLarge.  # noqa: E501


        :return: The experiments of this TaskLarge.  # noqa: E501
        :rtype: list[Experiment]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this TaskLarge.


        :param experiments: The experiments of this TaskLarge.  # noqa: E501
        :type: list[Experiment]
        """

        self._experiments = experiments

    @property
    def protocols(self):
        """Gets the protocols of this TaskLarge.  # noqa: E501


        :return: The protocols of this TaskLarge.  # noqa: E501
        :rtype: list[Protocol]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this TaskLarge.


        :param protocols: The protocols of this TaskLarge.  # noqa: E501
        :type: list[Protocol]
        """

        self._protocols = protocols

    @property
    def creator_id(self):
        """Gets the creator_id of this TaskLarge.  # noqa: E501


        :return: The creator_id of this TaskLarge.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this TaskLarge.


        :param creator_id: The creator_id of this TaskLarge.  # noqa: E501
        :type: int
        """

        self._creator_id = creator_id

    @property
    def task_id(self):
        """Gets the task_id of this TaskLarge.  # noqa: E501


        :return: The task_id of this TaskLarge.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskLarge.


        :param task_id: The task_id of this TaskLarge.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

    @property
    def created(self):
        """Gets the created of this TaskLarge.  # noqa: E501


        :return: The created of this TaskLarge.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TaskLarge.


        :param created: The created of this TaskLarge.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this TaskLarge.  # noqa: E501


        :return: The updated of this TaskLarge.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this TaskLarge.


        :param updated: The updated of this TaskLarge.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def assignee_id(self):
        """Gets the assignee_id of this TaskLarge.  # noqa: E501


        :return: The assignee_id of this TaskLarge.  # noqa: E501
        :rtype: int
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        """Sets the assignee_id of this TaskLarge.


        :param assignee_id: The assignee_id of this TaskLarge.  # noqa: E501
        :type: int
        """

        self._assignee_id = assignee_id

    @property
    def due(self):
        """Gets the due of this TaskLarge.  # noqa: E501


        :return: The due of this TaskLarge.  # noqa: E501
        :rtype: datetime
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this TaskLarge.


        :param due: The due of this TaskLarge.  # noqa: E501
        :type: datetime
        """

        self._due = due

    @property
    def title(self):
        """Gets the title of this TaskLarge.  # noqa: E501


        :return: The title of this TaskLarge.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskLarge.


        :param title: The title of this TaskLarge.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def contents(self):
        """Gets the contents of this TaskLarge.  # noqa: E501


        :return: The contents of this TaskLarge.  # noqa: E501
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this TaskLarge.


        :param contents: The contents of this TaskLarge.  # noqa: E501
        :type: str
        """

        self._contents = contents

    @property
    def status(self):
        """Gets the status of this TaskLarge.  # noqa: E501


        :return: The status of this TaskLarge.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskLarge.


        :param status: The status of this TaskLarge.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASSIGNED", "PROGRESS", "COMPLETED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TaskLarge, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskLarge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskLarge):
            return True

        return self.to_dict() != other.to_dict()
