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


class StorageMeta(object):
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
        'storage_meta_id': 'int',
        'meta_type': 'str',
        'name': 'str',
        'value': 'str',
        'meta_file_id': 'int',
        'order': 'int'
    }

    attribute_map = {
        'storage_meta_id': 'storageMetaID',
        'meta_type': 'metaType',
        'name': 'name',
        'value': 'value',
        'meta_file_id': 'metaFileID',
        'order': 'order'
    }

    def __init__(self, storage_meta_id=None, meta_type=None, name=None, value=None, meta_file_id=None, order=None, _configuration=None):  # noqa: E501
        """StorageMeta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._storage_meta_id = None
        self._meta_type = None
        self._name = None
        self._value = None
        self._meta_file_id = None
        self._order = None
        self.discriminator = None

        if storage_meta_id is not None:
            self.storage_meta_id = storage_meta_id
        if meta_type is not None:
            self.meta_type = meta_type
        self.name = name
        if value is not None:
            self.value = value
        if meta_file_id is not None:
            self.meta_file_id = meta_file_id
        if order is not None:
            self.order = order

    @property
    def storage_meta_id(self):
        """Gets the storage_meta_id of this StorageMeta.  # noqa: E501


        :return: The storage_meta_id of this StorageMeta.  # noqa: E501
        :rtype: int
        """
        return self._storage_meta_id

    @storage_meta_id.setter
    def storage_meta_id(self, storage_meta_id):
        """Sets the storage_meta_id of this StorageMeta.


        :param storage_meta_id: The storage_meta_id of this StorageMeta.  # noqa: E501
        :type: int
        """

        self._storage_meta_id = storage_meta_id

    @property
    def meta_type(self):
        """Gets the meta_type of this StorageMeta.  # noqa: E501


        :return: The meta_type of this StorageMeta.  # noqa: E501
        :rtype: str
        """
        return self._meta_type

    @meta_type.setter
    def meta_type(self, meta_type):
        """Sets the meta_type of this StorageMeta.


        :param meta_type: The meta_type of this StorageMeta.  # noqa: E501
        :type: str
        """
        allowed_values = ["TEXT", "FILE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                meta_type not in allowed_values):
            raise ValueError(
                "Invalid value for `meta_type` ({0}), must be one of {1}"  # noqa: E501
                .format(meta_type, allowed_values)
            )

        self._meta_type = meta_type

    @property
    def name(self):
        """Gets the name of this StorageMeta.  # noqa: E501


        :return: The name of this StorageMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageMeta.


        :param name: The name of this StorageMeta.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this StorageMeta.  # noqa: E501


        :return: The value of this StorageMeta.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StorageMeta.


        :param value: The value of this StorageMeta.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def meta_file_id(self):
        """Gets the meta_file_id of this StorageMeta.  # noqa: E501


        :return: The meta_file_id of this StorageMeta.  # noqa: E501
        :rtype: int
        """
        return self._meta_file_id

    @meta_file_id.setter
    def meta_file_id(self, meta_file_id):
        """Sets the meta_file_id of this StorageMeta.


        :param meta_file_id: The meta_file_id of this StorageMeta.  # noqa: E501
        :type: int
        """

        self._meta_file_id = meta_file_id

    @property
    def order(self):
        """Gets the order of this StorageMeta.  # noqa: E501


        :return: The order of this StorageMeta.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this StorageMeta.


        :param order: The order of this StorageMeta.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if issubclass(StorageMeta, dict):
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
        if not isinstance(other, StorageMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageMeta):
            return True

        return self.to_dict() != other.to_dict()
