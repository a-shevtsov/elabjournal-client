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


class StorageLayerDefinition(object):
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
        'storage_layer_definition_id': 'int',
        'storage_id': 'int',
        'deleted': 'bool',
        'is_grid': 'bool',
        'name': 'str',
        'level': 'int',
        'transposed': 'bool',
        'max_size': 'int',
        'icon': 'str',
        'dimension': 'StorageDimension'
    }

    attribute_map = {
        'storage_layer_definition_id': 'storageLayerDefinitionID',
        'storage_id': 'storageID',
        'deleted': 'deleted',
        'is_grid': 'isGrid',
        'name': 'name',
        'level': 'level',
        'transposed': 'transposed',
        'max_size': 'maxSize',
        'icon': 'icon',
        'dimension': 'dimension'
    }

    def __init__(self, storage_layer_definition_id=None, storage_id=None, deleted=None, is_grid=None, name=None, level=None, transposed=None, max_size=None, icon=None, dimension=None, _configuration=None):  # noqa: E501
        """StorageLayerDefinition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._storage_layer_definition_id = None
        self._storage_id = None
        self._deleted = None
        self._is_grid = None
        self._name = None
        self._level = None
        self._transposed = None
        self._max_size = None
        self._icon = None
        self._dimension = None
        self.discriminator = None

        if storage_layer_definition_id is not None:
            self.storage_layer_definition_id = storage_layer_definition_id
        if storage_id is not None:
            self.storage_id = storage_id
        if deleted is not None:
            self.deleted = deleted
        if is_grid is not None:
            self.is_grid = is_grid
        self.name = name
        self.level = level
        if transposed is not None:
            self.transposed = transposed
        if max_size is not None:
            self.max_size = max_size
        if icon is not None:
            self.icon = icon
        if dimension is not None:
            self.dimension = dimension

    @property
    def storage_layer_definition_id(self):
        """Gets the storage_layer_definition_id of this StorageLayerDefinition.  # noqa: E501


        :return: The storage_layer_definition_id of this StorageLayerDefinition.  # noqa: E501
        :rtype: int
        """
        return self._storage_layer_definition_id

    @storage_layer_definition_id.setter
    def storage_layer_definition_id(self, storage_layer_definition_id):
        """Sets the storage_layer_definition_id of this StorageLayerDefinition.


        :param storage_layer_definition_id: The storage_layer_definition_id of this StorageLayerDefinition.  # noqa: E501
        :type: int
        """

        self._storage_layer_definition_id = storage_layer_definition_id

    @property
    def storage_id(self):
        """Gets the storage_id of this StorageLayerDefinition.  # noqa: E501


        :return: The storage_id of this StorageLayerDefinition.  # noqa: E501
        :rtype: int
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this StorageLayerDefinition.


        :param storage_id: The storage_id of this StorageLayerDefinition.  # noqa: E501
        :type: int
        """

        self._storage_id = storage_id

    @property
    def deleted(self):
        """Gets the deleted of this StorageLayerDefinition.  # noqa: E501


        :return: The deleted of this StorageLayerDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this StorageLayerDefinition.


        :param deleted: The deleted of this StorageLayerDefinition.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def is_grid(self):
        """Gets the is_grid of this StorageLayerDefinition.  # noqa: E501


        :return: The is_grid of this StorageLayerDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_grid

    @is_grid.setter
    def is_grid(self, is_grid):
        """Sets the is_grid of this StorageLayerDefinition.


        :param is_grid: The is_grid of this StorageLayerDefinition.  # noqa: E501
        :type: bool
        """

        self._is_grid = is_grid

    @property
    def name(self):
        """Gets the name of this StorageLayerDefinition.  # noqa: E501


        :return: The name of this StorageLayerDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageLayerDefinition.


        :param name: The name of this StorageLayerDefinition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def level(self):
        """Gets the level of this StorageLayerDefinition.  # noqa: E501


        :return: The level of this StorageLayerDefinition.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this StorageLayerDefinition.


        :param level: The level of this StorageLayerDefinition.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                level is not None and level > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `level`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                level is not None and level < 1):  # noqa: E501
            raise ValueError("Invalid value for `level`, must be a value greater than or equal to `1`")  # noqa: E501

        self._level = level

    @property
    def transposed(self):
        """Gets the transposed of this StorageLayerDefinition.  # noqa: E501


        :return: The transposed of this StorageLayerDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._transposed

    @transposed.setter
    def transposed(self, transposed):
        """Sets the transposed of this StorageLayerDefinition.


        :param transposed: The transposed of this StorageLayerDefinition.  # noqa: E501
        :type: bool
        """

        self._transposed = transposed

    @property
    def max_size(self):
        """Gets the max_size of this StorageLayerDefinition.  # noqa: E501


        :return: The max_size of this StorageLayerDefinition.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this StorageLayerDefinition.


        :param max_size: The max_size of this StorageLayerDefinition.  # noqa: E501
        :type: int
        """

        self._max_size = max_size

    @property
    def icon(self):
        """Gets the icon of this StorageLayerDefinition.  # noqa: E501


        :return: The icon of this StorageLayerDefinition.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this StorageLayerDefinition.


        :param icon: The icon of this StorageLayerDefinition.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def dimension(self):
        """Gets the dimension of this StorageLayerDefinition.  # noqa: E501


        :return: The dimension of this StorageLayerDefinition.  # noqa: E501
        :rtype: StorageDimension
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this StorageLayerDefinition.


        :param dimension: The dimension of this StorageLayerDefinition.  # noqa: E501
        :type: StorageDimension
        """

        self._dimension = dimension

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
        if issubclass(StorageLayerDefinition, dict):
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
        if not isinstance(other, StorageLayerDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageLayerDefinition):
            return True

        return self.to_dict() != other.to_dict()
