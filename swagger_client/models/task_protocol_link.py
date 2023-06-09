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


class TaskProtocolLink(object):
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
        'task_protocol_id': 'int',
        'protocol': 'Protocol',
        'task_id': 'int',
        'prot_id': 'int'
    }

    attribute_map = {
        'task_protocol_id': 'taskProtocolId',
        'protocol': 'protocol',
        'task_id': 'taskID',
        'prot_id': 'protID'
    }

    def __init__(self, task_protocol_id=None, protocol=None, task_id=None, prot_id=None, _configuration=None):  # noqa: E501
        """TaskProtocolLink - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._task_protocol_id = None
        self._protocol = None
        self._task_id = None
        self._prot_id = None
        self.discriminator = None

        if task_protocol_id is not None:
            self.task_protocol_id = task_protocol_id
        if protocol is not None:
            self.protocol = protocol
        if task_id is not None:
            self.task_id = task_id
        if prot_id is not None:
            self.prot_id = prot_id

    @property
    def task_protocol_id(self):
        """Gets the task_protocol_id of this TaskProtocolLink.  # noqa: E501


        :return: The task_protocol_id of this TaskProtocolLink.  # noqa: E501
        :rtype: int
        """
        return self._task_protocol_id

    @task_protocol_id.setter
    def task_protocol_id(self, task_protocol_id):
        """Sets the task_protocol_id of this TaskProtocolLink.


        :param task_protocol_id: The task_protocol_id of this TaskProtocolLink.  # noqa: E501
        :type: int
        """

        self._task_protocol_id = task_protocol_id

    @property
    def protocol(self):
        """Gets the protocol of this TaskProtocolLink.  # noqa: E501


        :return: The protocol of this TaskProtocolLink.  # noqa: E501
        :rtype: Protocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TaskProtocolLink.


        :param protocol: The protocol of this TaskProtocolLink.  # noqa: E501
        :type: Protocol
        """

        self._protocol = protocol

    @property
    def task_id(self):
        """Gets the task_id of this TaskProtocolLink.  # noqa: E501


        :return: The task_id of this TaskProtocolLink.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskProtocolLink.


        :param task_id: The task_id of this TaskProtocolLink.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

    @property
    def prot_id(self):
        """Gets the prot_id of this TaskProtocolLink.  # noqa: E501


        :return: The prot_id of this TaskProtocolLink.  # noqa: E501
        :rtype: int
        """
        return self._prot_id

    @prot_id.setter
    def prot_id(self, prot_id):
        """Sets the prot_id of this TaskProtocolLink.


        :param prot_id: The prot_id of this TaskProtocolLink.  # noqa: E501
        :type: int
        """

        self._prot_id = prot_id

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
        if issubclass(TaskProtocolLink, dict):
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
        if not isinstance(other, TaskProtocolLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskProtocolLink):
            return True

        return self.to_dict() != other.to_dict()
