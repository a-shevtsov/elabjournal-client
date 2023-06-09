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


class OAuthResponse(object):
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
        'token_type': 'str',
        'id_token': 'str',
        'access_token': 'str',
        'refresh_token': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'token_type': 'tokenType',
        'id_token': 'idToken',
        'access_token': 'access_token',
        'refresh_token': 'refresh_token',
        'expires_in': 'expires_in'
    }

    def __init__(self, token_type=None, id_token=None, access_token=None, refresh_token=None, expires_in=None, _configuration=None):  # noqa: E501
        """OAuthResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token_type = None
        self._id_token = None
        self._access_token = None
        self._refresh_token = None
        self._expires_in = None
        self.discriminator = None

        if token_type is not None:
            self.token_type = token_type
        if id_token is not None:
            self.id_token = id_token
        if access_token is not None:
            self.access_token = access_token
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if expires_in is not None:
            self.expires_in = expires_in

    @property
    def token_type(self):
        """Gets the token_type of this OAuthResponse.  # noqa: E501


        :return: The token_type of this OAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this OAuthResponse.


        :param token_type: The token_type of this OAuthResponse.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def id_token(self):
        """Gets the id_token of this OAuthResponse.  # noqa: E501


        :return: The id_token of this OAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this OAuthResponse.


        :param id_token: The id_token of this OAuthResponse.  # noqa: E501
        :type: str
        """

        self._id_token = id_token

    @property
    def access_token(self):
        """Gets the access_token of this OAuthResponse.  # noqa: E501


        :return: The access_token of this OAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OAuthResponse.


        :param access_token: The access_token of this OAuthResponse.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this OAuthResponse.  # noqa: E501


        :return: The refresh_token of this OAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this OAuthResponse.


        :param refresh_token: The refresh_token of this OAuthResponse.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def expires_in(self):
        """Gets the expires_in of this OAuthResponse.  # noqa: E501


        :return: The expires_in of this OAuthResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this OAuthResponse.


        :param expires_in: The expires_in of this OAuthResponse.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

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
        if issubclass(OAuthResponse, dict):
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
        if not isinstance(other, OAuthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuthResponse):
            return True

        return self.to_dict() != other.to_dict()
