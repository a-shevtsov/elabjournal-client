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


class AssignedWitnesses(object):
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
        'witness_user_id': 'int',
        'requested': 'datetime',
        'witnessed': 'datetime',
        'decline_reason': 'str'
    }

    attribute_map = {
        'witness_user_id': 'witnessUserID',
        'requested': 'requested',
        'witnessed': 'witnessed',
        'decline_reason': 'declineReason'
    }

    def __init__(self, witness_user_id=None, requested=None, witnessed=None, decline_reason=None, _configuration=None):  # noqa: E501
        """AssignedWitnesses - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._witness_user_id = None
        self._requested = None
        self._witnessed = None
        self._decline_reason = None
        self.discriminator = None

        if witness_user_id is not None:
            self.witness_user_id = witness_user_id
        if requested is not None:
            self.requested = requested
        if witnessed is not None:
            self.witnessed = witnessed
        if decline_reason is not None:
            self.decline_reason = decline_reason

    @property
    def witness_user_id(self):
        """Gets the witness_user_id of this AssignedWitnesses.  # noqa: E501


        :return: The witness_user_id of this AssignedWitnesses.  # noqa: E501
        :rtype: int
        """
        return self._witness_user_id

    @witness_user_id.setter
    def witness_user_id(self, witness_user_id):
        """Sets the witness_user_id of this AssignedWitnesses.


        :param witness_user_id: The witness_user_id of this AssignedWitnesses.  # noqa: E501
        :type: int
        """

        self._witness_user_id = witness_user_id

    @property
    def requested(self):
        """Gets the requested of this AssignedWitnesses.  # noqa: E501


        :return: The requested of this AssignedWitnesses.  # noqa: E501
        :rtype: datetime
        """
        return self._requested

    @requested.setter
    def requested(self, requested):
        """Sets the requested of this AssignedWitnesses.


        :param requested: The requested of this AssignedWitnesses.  # noqa: E501
        :type: datetime
        """

        self._requested = requested

    @property
    def witnessed(self):
        """Gets the witnessed of this AssignedWitnesses.  # noqa: E501


        :return: The witnessed of this AssignedWitnesses.  # noqa: E501
        :rtype: datetime
        """
        return self._witnessed

    @witnessed.setter
    def witnessed(self, witnessed):
        """Sets the witnessed of this AssignedWitnesses.


        :param witnessed: The witnessed of this AssignedWitnesses.  # noqa: E501
        :type: datetime
        """

        self._witnessed = witnessed

    @property
    def decline_reason(self):
        """Gets the decline_reason of this AssignedWitnesses.  # noqa: E501


        :return: The decline_reason of this AssignedWitnesses.  # noqa: E501
        :rtype: str
        """
        return self._decline_reason

    @decline_reason.setter
    def decline_reason(self, decline_reason):
        """Sets the decline_reason of this AssignedWitnesses.


        :param decline_reason: The decline_reason of this AssignedWitnesses.  # noqa: E501
        :type: str
        """

        self._decline_reason = decline_reason

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
        if issubclass(AssignedWitnesses, dict):
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
        if not isinstance(other, AssignedWitnesses):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignedWitnesses):
            return True

        return self.to_dict() != other.to_dict()
