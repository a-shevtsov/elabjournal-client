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


class MarketPlacePermission(object):
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
        'can_install_for_group': 'bool',
        'can_install_for_user': 'bool',
        'can_delete_for_group': 'bool',
        'can_delete_for_user': 'bool'
    }

    attribute_map = {
        'can_install_for_group': 'canInstallForGroup',
        'can_install_for_user': 'canInstallForUser',
        'can_delete_for_group': 'canDeleteForGroup',
        'can_delete_for_user': 'canDeleteForUser'
    }

    def __init__(self, can_install_for_group=None, can_install_for_user=None, can_delete_for_group=None, can_delete_for_user=None, _configuration=None):  # noqa: E501
        """MarketPlacePermission - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_install_for_group = None
        self._can_install_for_user = None
        self._can_delete_for_group = None
        self._can_delete_for_user = None
        self.discriminator = None

        if can_install_for_group is not None:
            self.can_install_for_group = can_install_for_group
        if can_install_for_user is not None:
            self.can_install_for_user = can_install_for_user
        if can_delete_for_group is not None:
            self.can_delete_for_group = can_delete_for_group
        if can_delete_for_user is not None:
            self.can_delete_for_user = can_delete_for_user

    @property
    def can_install_for_group(self):
        """Gets the can_install_for_group of this MarketPlacePermission.  # noqa: E501


        :return: The can_install_for_group of this MarketPlacePermission.  # noqa: E501
        :rtype: bool
        """
        return self._can_install_for_group

    @can_install_for_group.setter
    def can_install_for_group(self, can_install_for_group):
        """Sets the can_install_for_group of this MarketPlacePermission.


        :param can_install_for_group: The can_install_for_group of this MarketPlacePermission.  # noqa: E501
        :type: bool
        """

        self._can_install_for_group = can_install_for_group

    @property
    def can_install_for_user(self):
        """Gets the can_install_for_user of this MarketPlacePermission.  # noqa: E501


        :return: The can_install_for_user of this MarketPlacePermission.  # noqa: E501
        :rtype: bool
        """
        return self._can_install_for_user

    @can_install_for_user.setter
    def can_install_for_user(self, can_install_for_user):
        """Sets the can_install_for_user of this MarketPlacePermission.


        :param can_install_for_user: The can_install_for_user of this MarketPlacePermission.  # noqa: E501
        :type: bool
        """

        self._can_install_for_user = can_install_for_user

    @property
    def can_delete_for_group(self):
        """Gets the can_delete_for_group of this MarketPlacePermission.  # noqa: E501


        :return: The can_delete_for_group of this MarketPlacePermission.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_for_group

    @can_delete_for_group.setter
    def can_delete_for_group(self, can_delete_for_group):
        """Sets the can_delete_for_group of this MarketPlacePermission.


        :param can_delete_for_group: The can_delete_for_group of this MarketPlacePermission.  # noqa: E501
        :type: bool
        """

        self._can_delete_for_group = can_delete_for_group

    @property
    def can_delete_for_user(self):
        """Gets the can_delete_for_user of this MarketPlacePermission.  # noqa: E501


        :return: The can_delete_for_user of this MarketPlacePermission.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_for_user

    @can_delete_for_user.setter
    def can_delete_for_user(self, can_delete_for_user):
        """Sets the can_delete_for_user of this MarketPlacePermission.


        :param can_delete_for_user: The can_delete_for_user of this MarketPlacePermission.  # noqa: E501
        :type: bool
        """

        self._can_delete_for_user = can_delete_for_user

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
        if issubclass(MarketPlacePermission, dict):
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
        if not isinstance(other, MarketPlacePermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketPlacePermission):
            return True

        return self.to_dict() != other.to_dict()
