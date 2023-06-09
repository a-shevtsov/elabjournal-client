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


class StorageNew(object):
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
        'storage_type_id': 'int',
        'name': 'str',
        'department': 'str',
        'address': 'str',
        'building': 'str',
        'floor': 'str',
        'room': 'str',
        'notes': 'str',
        'has_planner': 'bool',
        'has_validation': 'bool',
        'hide_from_browser': 'bool'
    }

    attribute_map = {
        'storage_type_id': 'storageTypeID',
        'name': 'name',
        'department': 'department',
        'address': 'address',
        'building': 'building',
        'floor': 'floor',
        'room': 'room',
        'notes': 'notes',
        'has_planner': 'hasPlanner',
        'has_validation': 'hasValidation',
        'hide_from_browser': 'hideFromBrowser'
    }

    def __init__(self, storage_type_id=None, name=None, department=None, address=None, building=None, floor=None, room=None, notes=None, has_planner=None, has_validation=None, hide_from_browser=None, _configuration=None):  # noqa: E501
        """StorageNew - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._storage_type_id = None
        self._name = None
        self._department = None
        self._address = None
        self._building = None
        self._floor = None
        self._room = None
        self._notes = None
        self._has_planner = None
        self._has_validation = None
        self._hide_from_browser = None
        self.discriminator = None

        self.storage_type_id = storage_type_id
        self.name = name
        if department is not None:
            self.department = department
        if address is not None:
            self.address = address
        if building is not None:
            self.building = building
        if floor is not None:
            self.floor = floor
        if room is not None:
            self.room = room
        if notes is not None:
            self.notes = notes
        if has_planner is not None:
            self.has_planner = has_planner
        if has_validation is not None:
            self.has_validation = has_validation
        if hide_from_browser is not None:
            self.hide_from_browser = hide_from_browser

    @property
    def storage_type_id(self):
        """Gets the storage_type_id of this StorageNew.  # noqa: E501


        :return: The storage_type_id of this StorageNew.  # noqa: E501
        :rtype: int
        """
        return self._storage_type_id

    @storage_type_id.setter
    def storage_type_id(self, storage_type_id):
        """Sets the storage_type_id of this StorageNew.


        :param storage_type_id: The storage_type_id of this StorageNew.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and storage_type_id is None:
            raise ValueError("Invalid value for `storage_type_id`, must not be `None`")  # noqa: E501

        self._storage_type_id = storage_type_id

    @property
    def name(self):
        """Gets the name of this StorageNew.  # noqa: E501


        :return: The name of this StorageNew.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageNew.


        :param name: The name of this StorageNew.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def department(self):
        """Gets the department of this StorageNew.  # noqa: E501


        :return: The department of this StorageNew.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this StorageNew.


        :param department: The department of this StorageNew.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def address(self):
        """Gets the address of this StorageNew.  # noqa: E501


        :return: The address of this StorageNew.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this StorageNew.


        :param address: The address of this StorageNew.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def building(self):
        """Gets the building of this StorageNew.  # noqa: E501


        :return: The building of this StorageNew.  # noqa: E501
        :rtype: str
        """
        return self._building

    @building.setter
    def building(self, building):
        """Sets the building of this StorageNew.


        :param building: The building of this StorageNew.  # noqa: E501
        :type: str
        """

        self._building = building

    @property
    def floor(self):
        """Gets the floor of this StorageNew.  # noqa: E501


        :return: The floor of this StorageNew.  # noqa: E501
        :rtype: str
        """
        return self._floor

    @floor.setter
    def floor(self, floor):
        """Sets the floor of this StorageNew.


        :param floor: The floor of this StorageNew.  # noqa: E501
        :type: str
        """

        self._floor = floor

    @property
    def room(self):
        """Gets the room of this StorageNew.  # noqa: E501


        :return: The room of this StorageNew.  # noqa: E501
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room):
        """Sets the room of this StorageNew.


        :param room: The room of this StorageNew.  # noqa: E501
        :type: str
        """

        self._room = room

    @property
    def notes(self):
        """Gets the notes of this StorageNew.  # noqa: E501


        :return: The notes of this StorageNew.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this StorageNew.


        :param notes: The notes of this StorageNew.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def has_planner(self):
        """Gets the has_planner of this StorageNew.  # noqa: E501


        :return: The has_planner of this StorageNew.  # noqa: E501
        :rtype: bool
        """
        return self._has_planner

    @has_planner.setter
    def has_planner(self, has_planner):
        """Sets the has_planner of this StorageNew.


        :param has_planner: The has_planner of this StorageNew.  # noqa: E501
        :type: bool
        """

        self._has_planner = has_planner

    @property
    def has_validation(self):
        """Gets the has_validation of this StorageNew.  # noqa: E501


        :return: The has_validation of this StorageNew.  # noqa: E501
        :rtype: bool
        """
        return self._has_validation

    @has_validation.setter
    def has_validation(self, has_validation):
        """Sets the has_validation of this StorageNew.


        :param has_validation: The has_validation of this StorageNew.  # noqa: E501
        :type: bool
        """

        self._has_validation = has_validation

    @property
    def hide_from_browser(self):
        """Gets the hide_from_browser of this StorageNew.  # noqa: E501


        :return: The hide_from_browser of this StorageNew.  # noqa: E501
        :rtype: bool
        """
        return self._hide_from_browser

    @hide_from_browser.setter
    def hide_from_browser(self, hide_from_browser):
        """Sets the hide_from_browser of this StorageNew.


        :param hide_from_browser: The hide_from_browser of this StorageNew.  # noqa: E501
        :type: bool
        """

        self._hide_from_browser = hide_from_browser

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
        if issubclass(StorageNew, dict):
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
        if not isinstance(other, StorageNew):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageNew):
            return True

        return self.to_dict() != other.to_dict()
