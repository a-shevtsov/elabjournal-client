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


class StorageValidationNew(object):
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
        'validation_date': 'datetime',
        'expiration_date': 'datetime',
        'is_active': 'bool',
        'meta_file_name': 'str',
        'meta_file_ids': 'list[int]'
    }

    attribute_map = {
        'validation_date': 'validationDate',
        'expiration_date': 'expirationDate',
        'is_active': 'IsActive',
        'meta_file_name': 'metaFileName',
        'meta_file_ids': 'metaFileIDs'
    }

    def __init__(self, validation_date=None, expiration_date=None, is_active=None, meta_file_name=None, meta_file_ids=None, _configuration=None):  # noqa: E501
        """StorageValidationNew - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._validation_date = None
        self._expiration_date = None
        self._is_active = None
        self._meta_file_name = None
        self._meta_file_ids = None
        self.discriminator = None

        self.validation_date = validation_date
        self.expiration_date = expiration_date
        if is_active is not None:
            self.is_active = is_active
        if meta_file_name is not None:
            self.meta_file_name = meta_file_name
        if meta_file_ids is not None:
            self.meta_file_ids = meta_file_ids

    @property
    def validation_date(self):
        """Gets the validation_date of this StorageValidationNew.  # noqa: E501


        :return: The validation_date of this StorageValidationNew.  # noqa: E501
        :rtype: datetime
        """
        return self._validation_date

    @validation_date.setter
    def validation_date(self, validation_date):
        """Sets the validation_date of this StorageValidationNew.


        :param validation_date: The validation_date of this StorageValidationNew.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and validation_date is None:
            raise ValueError("Invalid value for `validation_date`, must not be `None`")  # noqa: E501

        self._validation_date = validation_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this StorageValidationNew.  # noqa: E501


        :return: The expiration_date of this StorageValidationNew.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this StorageValidationNew.


        :param expiration_date: The expiration_date of this StorageValidationNew.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def is_active(self):
        """Gets the is_active of this StorageValidationNew.  # noqa: E501


        :return: The is_active of this StorageValidationNew.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this StorageValidationNew.


        :param is_active: The is_active of this StorageValidationNew.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def meta_file_name(self):
        """Gets the meta_file_name of this StorageValidationNew.  # noqa: E501


        :return: The meta_file_name of this StorageValidationNew.  # noqa: E501
        :rtype: str
        """
        return self._meta_file_name

    @meta_file_name.setter
    def meta_file_name(self, meta_file_name):
        """Sets the meta_file_name of this StorageValidationNew.


        :param meta_file_name: The meta_file_name of this StorageValidationNew.  # noqa: E501
        :type: str
        """

        self._meta_file_name = meta_file_name

    @property
    def meta_file_ids(self):
        """Gets the meta_file_ids of this StorageValidationNew.  # noqa: E501


        :return: The meta_file_ids of this StorageValidationNew.  # noqa: E501
        :rtype: list[int]
        """
        return self._meta_file_ids

    @meta_file_ids.setter
    def meta_file_ids(self, meta_file_ids):
        """Sets the meta_file_ids of this StorageValidationNew.


        :param meta_file_ids: The meta_file_ids of this StorageValidationNew.  # noqa: E501
        :type: list[int]
        """

        self._meta_file_ids = meta_file_ids

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
        if issubclass(StorageValidationNew, dict):
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
        if not isinstance(other, StorageValidationNew):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageValidationNew):
            return True

        return self.to_dict() != other.to_dict()
