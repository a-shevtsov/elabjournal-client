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


class AuthResponse(object):
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
        'token': 'str',
        'user': 'AuthInfo',
        'federated_login': 'bool',
        'two_factor_auth_login': 'bool'
    }

    attribute_map = {
        'token': 'token',
        'user': 'user',
        'federated_login': 'federatedLogin',
        'two_factor_auth_login': 'twoFactorAuthLogin'
    }

    def __init__(self, token=None, user=None, federated_login=None, two_factor_auth_login=None, _configuration=None):  # noqa: E501
        """AuthResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token = None
        self._user = None
        self._federated_login = None
        self._two_factor_auth_login = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if user is not None:
            self.user = user
        if federated_login is not None:
            self.federated_login = federated_login
        if two_factor_auth_login is not None:
            self.two_factor_auth_login = two_factor_auth_login

    @property
    def token(self):
        """Gets the token of this AuthResponse.  # noqa: E501


        :return: The token of this AuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AuthResponse.


        :param token: The token of this AuthResponse.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def user(self):
        """Gets the user of this AuthResponse.  # noqa: E501


        :return: The user of this AuthResponse.  # noqa: E501
        :rtype: AuthInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AuthResponse.


        :param user: The user of this AuthResponse.  # noqa: E501
        :type: AuthInfo
        """

        self._user = user

    @property
    def federated_login(self):
        """Gets the federated_login of this AuthResponse.  # noqa: E501


        :return: The federated_login of this AuthResponse.  # noqa: E501
        :rtype: bool
        """
        return self._federated_login

    @federated_login.setter
    def federated_login(self, federated_login):
        """Sets the federated_login of this AuthResponse.


        :param federated_login: The federated_login of this AuthResponse.  # noqa: E501
        :type: bool
        """

        self._federated_login = federated_login

    @property
    def two_factor_auth_login(self):
        """Gets the two_factor_auth_login of this AuthResponse.  # noqa: E501


        :return: The two_factor_auth_login of this AuthResponse.  # noqa: E501
        :rtype: bool
        """
        return self._two_factor_auth_login

    @two_factor_auth_login.setter
    def two_factor_auth_login(self, two_factor_auth_login):
        """Sets the two_factor_auth_login of this AuthResponse.


        :param two_factor_auth_login: The two_factor_auth_login of this AuthResponse.  # noqa: E501
        :type: bool
        """

        self._two_factor_auth_login = two_factor_auth_login

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
        if issubclass(AuthResponse, dict):
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
        if not isinstance(other, AuthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthResponse):
            return True

        return self.to_dict() != other.to_dict()
