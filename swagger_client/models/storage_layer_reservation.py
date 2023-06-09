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


class StorageLayerReservation(object):
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
        'storage_layer_reservation_id': 'int',
        'storage_layer_id': 'int',
        'created_by_user_id': 'int',
        'created': 'datetime',
        'reserved_for_name': 'str',
        'is_permanent': 'bool',
        'reservation_type': 'str',
        'start': 'datetime',
        'end': 'datetime',
        'reserved_for_id': 'int',
        'description': 'str'
    }

    attribute_map = {
        'storage_layer_reservation_id': 'storageLayerReservationID',
        'storage_layer_id': 'storageLayerID',
        'created_by_user_id': 'createdByUserID',
        'created': 'created',
        'reserved_for_name': 'reservedForName',
        'is_permanent': 'isPermanent',
        'reservation_type': 'reservationType',
        'start': 'start',
        'end': 'end',
        'reserved_for_id': 'reservedForID',
        'description': 'description'
    }

    def __init__(self, storage_layer_reservation_id=None, storage_layer_id=None, created_by_user_id=None, created=None, reserved_for_name=None, is_permanent=None, reservation_type=None, start=None, end=None, reserved_for_id=None, description=None, _configuration=None):  # noqa: E501
        """StorageLayerReservation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._storage_layer_reservation_id = None
        self._storage_layer_id = None
        self._created_by_user_id = None
        self._created = None
        self._reserved_for_name = None
        self._is_permanent = None
        self._reservation_type = None
        self._start = None
        self._end = None
        self._reserved_for_id = None
        self._description = None
        self.discriminator = None

        if storage_layer_reservation_id is not None:
            self.storage_layer_reservation_id = storage_layer_reservation_id
        if storage_layer_id is not None:
            self.storage_layer_id = storage_layer_id
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if created is not None:
            self.created = created
        if reserved_for_name is not None:
            self.reserved_for_name = reserved_for_name
        if is_permanent is not None:
            self.is_permanent = is_permanent
        self.reservation_type = reservation_type
        self.start = start
        if end is not None:
            self.end = end
        self.reserved_for_id = reserved_for_id
        if description is not None:
            self.description = description

    @property
    def storage_layer_reservation_id(self):
        """Gets the storage_layer_reservation_id of this StorageLayerReservation.  # noqa: E501


        :return: The storage_layer_reservation_id of this StorageLayerReservation.  # noqa: E501
        :rtype: int
        """
        return self._storage_layer_reservation_id

    @storage_layer_reservation_id.setter
    def storage_layer_reservation_id(self, storage_layer_reservation_id):
        """Sets the storage_layer_reservation_id of this StorageLayerReservation.


        :param storage_layer_reservation_id: The storage_layer_reservation_id of this StorageLayerReservation.  # noqa: E501
        :type: int
        """

        self._storage_layer_reservation_id = storage_layer_reservation_id

    @property
    def storage_layer_id(self):
        """Gets the storage_layer_id of this StorageLayerReservation.  # noqa: E501


        :return: The storage_layer_id of this StorageLayerReservation.  # noqa: E501
        :rtype: int
        """
        return self._storage_layer_id

    @storage_layer_id.setter
    def storage_layer_id(self, storage_layer_id):
        """Sets the storage_layer_id of this StorageLayerReservation.


        :param storage_layer_id: The storage_layer_id of this StorageLayerReservation.  # noqa: E501
        :type: int
        """

        self._storage_layer_id = storage_layer_id

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this StorageLayerReservation.  # noqa: E501


        :return: The created_by_user_id of this StorageLayerReservation.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this StorageLayerReservation.


        :param created_by_user_id: The created_by_user_id of this StorageLayerReservation.  # noqa: E501
        :type: int
        """

        self._created_by_user_id = created_by_user_id

    @property
    def created(self):
        """Gets the created of this StorageLayerReservation.  # noqa: E501


        :return: The created of this StorageLayerReservation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this StorageLayerReservation.


        :param created: The created of this StorageLayerReservation.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def reserved_for_name(self):
        """Gets the reserved_for_name of this StorageLayerReservation.  # noqa: E501


        :return: The reserved_for_name of this StorageLayerReservation.  # noqa: E501
        :rtype: str
        """
        return self._reserved_for_name

    @reserved_for_name.setter
    def reserved_for_name(self, reserved_for_name):
        """Sets the reserved_for_name of this StorageLayerReservation.


        :param reserved_for_name: The reserved_for_name of this StorageLayerReservation.  # noqa: E501
        :type: str
        """

        self._reserved_for_name = reserved_for_name

    @property
    def is_permanent(self):
        """Gets the is_permanent of this StorageLayerReservation.  # noqa: E501


        :return: The is_permanent of this StorageLayerReservation.  # noqa: E501
        :rtype: bool
        """
        return self._is_permanent

    @is_permanent.setter
    def is_permanent(self, is_permanent):
        """Sets the is_permanent of this StorageLayerReservation.


        :param is_permanent: The is_permanent of this StorageLayerReservation.  # noqa: E501
        :type: bool
        """

        self._is_permanent = is_permanent

    @property
    def reservation_type(self):
        """Gets the reservation_type of this StorageLayerReservation.  # noqa: E501


        :return: The reservation_type of this StorageLayerReservation.  # noqa: E501
        :rtype: str
        """
        return self._reservation_type

    @reservation_type.setter
    def reservation_type(self, reservation_type):
        """Sets the reservation_type of this StorageLayerReservation.


        :param reservation_type: The reservation_type of this StorageLayerReservation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reservation_type is None:
            raise ValueError("Invalid value for `reservation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["UserReservation", "RoleReservation"]  # noqa: E501
        if (self._configuration.client_side_validation and
                reservation_type not in allowed_values):
            raise ValueError(
                "Invalid value for `reservation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(reservation_type, allowed_values)
            )

        self._reservation_type = reservation_type

    @property
    def start(self):
        """Gets the start of this StorageLayerReservation.  # noqa: E501


        :return: The start of this StorageLayerReservation.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this StorageLayerReservation.


        :param start: The start of this StorageLayerReservation.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this StorageLayerReservation.  # noqa: E501


        :return: The end of this StorageLayerReservation.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this StorageLayerReservation.


        :param end: The end of this StorageLayerReservation.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def reserved_for_id(self):
        """Gets the reserved_for_id of this StorageLayerReservation.  # noqa: E501


        :return: The reserved_for_id of this StorageLayerReservation.  # noqa: E501
        :rtype: int
        """
        return self._reserved_for_id

    @reserved_for_id.setter
    def reserved_for_id(self, reserved_for_id):
        """Sets the reserved_for_id of this StorageLayerReservation.


        :param reserved_for_id: The reserved_for_id of this StorageLayerReservation.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and reserved_for_id is None:
            raise ValueError("Invalid value for `reserved_for_id`, must not be `None`")  # noqa: E501

        self._reserved_for_id = reserved_for_id

    @property
    def description(self):
        """Gets the description of this StorageLayerReservation.  # noqa: E501


        :return: The description of this StorageLayerReservation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StorageLayerReservation.


        :param description: The description of this StorageLayerReservation.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(StorageLayerReservation, dict):
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
        if not isinstance(other, StorageLayerReservation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageLayerReservation):
            return True

        return self.to_dict() != other.to_dict()
