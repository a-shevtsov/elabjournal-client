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


class AuthInfo(object):
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
        'user_id': 'int',
        'username': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'institute_id': 'int',
        'primary_group_id': 'int',
        'primary_sub_group_id': 'int',
        'domain': 'str'
    }

    attribute_map = {
        'user_id': 'userID',
        'username': 'username',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'institute_id': 'instituteID',
        'primary_group_id': 'primaryGroupID',
        'primary_sub_group_id': 'primarySubGroupID',
        'domain': 'domain'
    }

    def __init__(self, user_id=None, username=None, email=None, first_name=None, last_name=None, institute_id=None, primary_group_id=None, primary_sub_group_id=None, domain=None, _configuration=None):  # noqa: E501
        """AuthInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._username = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._institute_id = None
        self._primary_group_id = None
        self._primary_sub_group_id = None
        self._domain = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if institute_id is not None:
            self.institute_id = institute_id
        if primary_group_id is not None:
            self.primary_group_id = primary_group_id
        if primary_sub_group_id is not None:
            self.primary_sub_group_id = primary_sub_group_id
        if domain is not None:
            self.domain = domain

    @property
    def user_id(self):
        """Gets the user_id of this AuthInfo.  # noqa: E501


        :return: The user_id of this AuthInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuthInfo.


        :param user_id: The user_id of this AuthInfo.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this AuthInfo.  # noqa: E501


        :return: The username of this AuthInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthInfo.


        :param username: The username of this AuthInfo.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this AuthInfo.  # noqa: E501


        :return: The email of this AuthInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuthInfo.


        :param email: The email of this AuthInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this AuthInfo.  # noqa: E501


        :return: The first_name of this AuthInfo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AuthInfo.


        :param first_name: The first_name of this AuthInfo.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this AuthInfo.  # noqa: E501


        :return: The last_name of this AuthInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AuthInfo.


        :param last_name: The last_name of this AuthInfo.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def institute_id(self):
        """Gets the institute_id of this AuthInfo.  # noqa: E501


        :return: The institute_id of this AuthInfo.  # noqa: E501
        :rtype: int
        """
        return self._institute_id

    @institute_id.setter
    def institute_id(self, institute_id):
        """Sets the institute_id of this AuthInfo.


        :param institute_id: The institute_id of this AuthInfo.  # noqa: E501
        :type: int
        """

        self._institute_id = institute_id

    @property
    def primary_group_id(self):
        """Gets the primary_group_id of this AuthInfo.  # noqa: E501


        :return: The primary_group_id of this AuthInfo.  # noqa: E501
        :rtype: int
        """
        return self._primary_group_id

    @primary_group_id.setter
    def primary_group_id(self, primary_group_id):
        """Sets the primary_group_id of this AuthInfo.


        :param primary_group_id: The primary_group_id of this AuthInfo.  # noqa: E501
        :type: int
        """

        self._primary_group_id = primary_group_id

    @property
    def primary_sub_group_id(self):
        """Gets the primary_sub_group_id of this AuthInfo.  # noqa: E501


        :return: The primary_sub_group_id of this AuthInfo.  # noqa: E501
        :rtype: int
        """
        return self._primary_sub_group_id

    @primary_sub_group_id.setter
    def primary_sub_group_id(self, primary_sub_group_id):
        """Sets the primary_sub_group_id of this AuthInfo.


        :param primary_sub_group_id: The primary_sub_group_id of this AuthInfo.  # noqa: E501
        :type: int
        """

        self._primary_sub_group_id = primary_sub_group_id

    @property
    def domain(self):
        """Gets the domain of this AuthInfo.  # noqa: E501


        :return: The domain of this AuthInfo.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AuthInfo.


        :param domain: The domain of this AuthInfo.  # noqa: E501
        :type: str
        """

        self._domain = domain

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
        if issubclass(AuthInfo, dict):
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
        if not isinstance(other, AuthInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthInfo):
            return True

        return self.to_dict() != other.to_dict()
