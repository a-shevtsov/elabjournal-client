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


class SampleAggregate(object):
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
        'samples': 'list[SampleLarge]',
        'sample_ids': 'list[int]',
        'type': 'str',
        'sample_id': 'int',
        'series_id': 'int',
        'total_series_size': 'int',
        'size': 'int',
        'name': 'str',
        'sample_type': 'SampleTypeShort',
        'storage_layer_id': 'int',
        'storage_layer_name': 'str',
        'location': 'Location',
        'position': 'int',
        'created': 'datetime',
        'user_id': 'int',
        'user': 'str',
        'expiration': 'datetime',
        'checked_out': 'bool',
        'meta': 'list[SampleMetaWithType]',
        'description': 'str',
        'note': 'str',
        'quantity': 'str',
        'alt_id': 'str'
    }

    attribute_map = {
        'samples': 'samples',
        'sample_ids': 'sampleIDs',
        'type': 'type',
        'sample_id': 'sampleID',
        'series_id': 'seriesID',
        'total_series_size': 'totalSeriesSize',
        'size': 'size',
        'name': 'name',
        'sample_type': 'sampleType',
        'storage_layer_id': 'storageLayerID',
        'storage_layer_name': 'storageLayerName',
        'location': 'location',
        'position': 'position',
        'created': 'created',
        'user_id': 'userID',
        'user': 'user',
        'expiration': 'expiration',
        'checked_out': 'checkedOut',
        'meta': 'meta',
        'description': 'description',
        'note': 'note',
        'quantity': 'quantity',
        'alt_id': 'altID'
    }

    def __init__(self, samples=None, sample_ids=None, type=None, sample_id=None, series_id=None, total_series_size=None, size=None, name=None, sample_type=None, storage_layer_id=None, storage_layer_name=None, location=None, position=None, created=None, user_id=None, user=None, expiration=None, checked_out=None, meta=None, description=None, note=None, quantity=None, alt_id=None, _configuration=None):  # noqa: E501
        """SampleAggregate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._samples = None
        self._sample_ids = None
        self._type = None
        self._sample_id = None
        self._series_id = None
        self._total_series_size = None
        self._size = None
        self._name = None
        self._sample_type = None
        self._storage_layer_id = None
        self._storage_layer_name = None
        self._location = None
        self._position = None
        self._created = None
        self._user_id = None
        self._user = None
        self._expiration = None
        self._checked_out = None
        self._meta = None
        self._description = None
        self._note = None
        self._quantity = None
        self._alt_id = None
        self.discriminator = None

        if samples is not None:
            self.samples = samples
        if sample_ids is not None:
            self.sample_ids = sample_ids
        if type is not None:
            self.type = type
        if sample_id is not None:
            self.sample_id = sample_id
        if series_id is not None:
            self.series_id = series_id
        if total_series_size is not None:
            self.total_series_size = total_series_size
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if sample_type is not None:
            self.sample_type = sample_type
        if storage_layer_id is not None:
            self.storage_layer_id = storage_layer_id
        if storage_layer_name is not None:
            self.storage_layer_name = storage_layer_name
        if location is not None:
            self.location = location
        if position is not None:
            self.position = position
        if created is not None:
            self.created = created
        if user_id is not None:
            self.user_id = user_id
        if user is not None:
            self.user = user
        if expiration is not None:
            self.expiration = expiration
        if checked_out is not None:
            self.checked_out = checked_out
        if meta is not None:
            self.meta = meta
        if description is not None:
            self.description = description
        if note is not None:
            self.note = note
        if quantity is not None:
            self.quantity = quantity
        if alt_id is not None:
            self.alt_id = alt_id

    @property
    def samples(self):
        """Gets the samples of this SampleAggregate.  # noqa: E501


        :return: The samples of this SampleAggregate.  # noqa: E501
        :rtype: list[SampleLarge]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this SampleAggregate.


        :param samples: The samples of this SampleAggregate.  # noqa: E501
        :type: list[SampleLarge]
        """

        self._samples = samples

    @property
    def sample_ids(self):
        """Gets the sample_ids of this SampleAggregate.  # noqa: E501


        :return: The sample_ids of this SampleAggregate.  # noqa: E501
        :rtype: list[int]
        """
        return self._sample_ids

    @sample_ids.setter
    def sample_ids(self, sample_ids):
        """Sets the sample_ids of this SampleAggregate.


        :param sample_ids: The sample_ids of this SampleAggregate.  # noqa: E501
        :type: list[int]
        """

        self._sample_ids = sample_ids

    @property
    def type(self):
        """Gets the type of this SampleAggregate.  # noqa: E501


        :return: The type of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SampleAggregate.


        :param type: The type of this SampleAggregate.  # noqa: E501
        :type: str
        """
        allowed_values = ["SAMPLE", "SERIES"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def sample_id(self):
        """Gets the sample_id of this SampleAggregate.  # noqa: E501


        :return: The sample_id of this SampleAggregate.  # noqa: E501
        :rtype: int
        """
        return self._sample_id

    @sample_id.setter
    def sample_id(self, sample_id):
        """Sets the sample_id of this SampleAggregate.


        :param sample_id: The sample_id of this SampleAggregate.  # noqa: E501
        :type: int
        """

        self._sample_id = sample_id

    @property
    def series_id(self):
        """Gets the series_id of this SampleAggregate.  # noqa: E501


        :return: The series_id of this SampleAggregate.  # noqa: E501
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this SampleAggregate.


        :param series_id: The series_id of this SampleAggregate.  # noqa: E501
        :type: int
        """

        self._series_id = series_id

    @property
    def total_series_size(self):
        """Gets the total_series_size of this SampleAggregate.  # noqa: E501


        :return: The total_series_size of this SampleAggregate.  # noqa: E501
        :rtype: int
        """
        return self._total_series_size

    @total_series_size.setter
    def total_series_size(self, total_series_size):
        """Sets the total_series_size of this SampleAggregate.


        :param total_series_size: The total_series_size of this SampleAggregate.  # noqa: E501
        :type: int
        """

        self._total_series_size = total_series_size

    @property
    def size(self):
        """Gets the size of this SampleAggregate.  # noqa: E501


        :return: The size of this SampleAggregate.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SampleAggregate.


        :param size: The size of this SampleAggregate.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def name(self):
        """Gets the name of this SampleAggregate.  # noqa: E501


        :return: The name of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SampleAggregate.


        :param name: The name of this SampleAggregate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sample_type(self):
        """Gets the sample_type of this SampleAggregate.  # noqa: E501


        :return: The sample_type of this SampleAggregate.  # noqa: E501
        :rtype: SampleTypeShort
        """
        return self._sample_type

    @sample_type.setter
    def sample_type(self, sample_type):
        """Sets the sample_type of this SampleAggregate.


        :param sample_type: The sample_type of this SampleAggregate.  # noqa: E501
        :type: SampleTypeShort
        """

        self._sample_type = sample_type

    @property
    def storage_layer_id(self):
        """Gets the storage_layer_id of this SampleAggregate.  # noqa: E501


        :return: The storage_layer_id of this SampleAggregate.  # noqa: E501
        :rtype: int
        """
        return self._storage_layer_id

    @storage_layer_id.setter
    def storage_layer_id(self, storage_layer_id):
        """Sets the storage_layer_id of this SampleAggregate.


        :param storage_layer_id: The storage_layer_id of this SampleAggregate.  # noqa: E501
        :type: int
        """

        self._storage_layer_id = storage_layer_id

    @property
    def storage_layer_name(self):
        """Gets the storage_layer_name of this SampleAggregate.  # noqa: E501


        :return: The storage_layer_name of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._storage_layer_name

    @storage_layer_name.setter
    def storage_layer_name(self, storage_layer_name):
        """Sets the storage_layer_name of this SampleAggregate.


        :param storage_layer_name: The storage_layer_name of this SampleAggregate.  # noqa: E501
        :type: str
        """

        self._storage_layer_name = storage_layer_name

    @property
    def location(self):
        """Gets the location of this SampleAggregate.  # noqa: E501


        :return: The location of this SampleAggregate.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SampleAggregate.


        :param location: The location of this SampleAggregate.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def position(self):
        """Gets the position of this SampleAggregate.  # noqa: E501


        :return: The position of this SampleAggregate.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SampleAggregate.


        :param position: The position of this SampleAggregate.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def created(self):
        """Gets the created of this SampleAggregate.  # noqa: E501


        :return: The created of this SampleAggregate.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SampleAggregate.


        :param created: The created of this SampleAggregate.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def user_id(self):
        """Gets the user_id of this SampleAggregate.  # noqa: E501


        :return: The user_id of this SampleAggregate.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SampleAggregate.


        :param user_id: The user_id of this SampleAggregate.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user(self):
        """Gets the user of this SampleAggregate.  # noqa: E501


        :return: The user of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SampleAggregate.


        :param user: The user of this SampleAggregate.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def expiration(self):
        """Gets the expiration of this SampleAggregate.  # noqa: E501


        :return: The expiration of this SampleAggregate.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this SampleAggregate.


        :param expiration: The expiration of this SampleAggregate.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def checked_out(self):
        """Gets the checked_out of this SampleAggregate.  # noqa: E501


        :return: The checked_out of this SampleAggregate.  # noqa: E501
        :rtype: bool
        """
        return self._checked_out

    @checked_out.setter
    def checked_out(self, checked_out):
        """Sets the checked_out of this SampleAggregate.


        :param checked_out: The checked_out of this SampleAggregate.  # noqa: E501
        :type: bool
        """

        self._checked_out = checked_out

    @property
    def meta(self):
        """Gets the meta of this SampleAggregate.  # noqa: E501


        :return: The meta of this SampleAggregate.  # noqa: E501
        :rtype: list[SampleMetaWithType]
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this SampleAggregate.


        :param meta: The meta of this SampleAggregate.  # noqa: E501
        :type: list[SampleMetaWithType]
        """

        self._meta = meta

    @property
    def description(self):
        """Gets the description of this SampleAggregate.  # noqa: E501


        :return: The description of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SampleAggregate.


        :param description: The description of this SampleAggregate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def note(self):
        """Gets the note of this SampleAggregate.  # noqa: E501


        :return: The note of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this SampleAggregate.


        :param note: The note of this SampleAggregate.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def quantity(self):
        """Gets the quantity of this SampleAggregate.  # noqa: E501


        :return: The quantity of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SampleAggregate.


        :param quantity: The quantity of this SampleAggregate.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def alt_id(self):
        """Gets the alt_id of this SampleAggregate.  # noqa: E501


        :return: The alt_id of this SampleAggregate.  # noqa: E501
        :rtype: str
        """
        return self._alt_id

    @alt_id.setter
    def alt_id(self, alt_id):
        """Sets the alt_id of this SampleAggregate.


        :param alt_id: The alt_id of this SampleAggregate.  # noqa: E501
        :type: str
        """

        self._alt_id = alt_id

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
        if issubclass(SampleAggregate, dict):
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
        if not isinstance(other, SampleAggregate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleAggregate):
            return True

        return self.to_dict() != other.to_dict()
