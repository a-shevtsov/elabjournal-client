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


class SampleCloneOptions(object):
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
        'clone_times': 'int',
        'track_parent': 'bool',
        'quantity': 'QuantityCloneOptions',
        'storage_position_ranges': 'list[StoragePositionRange]'
    }

    attribute_map = {
        'clone_times': 'cloneTimes',
        'track_parent': 'trackParent',
        'quantity': 'quantity',
        'storage_position_ranges': 'storagePositionRanges'
    }

    def __init__(self, clone_times=None, track_parent=None, quantity=None, storage_position_ranges=None, _configuration=None):  # noqa: E501
        """SampleCloneOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clone_times = None
        self._track_parent = None
        self._quantity = None
        self._storage_position_ranges = None
        self.discriminator = None

        if clone_times is not None:
            self.clone_times = clone_times
        if track_parent is not None:
            self.track_parent = track_parent
        if quantity is not None:
            self.quantity = quantity
        if storage_position_ranges is not None:
            self.storage_position_ranges = storage_position_ranges

    @property
    def clone_times(self):
        """Gets the clone_times of this SampleCloneOptions.  # noqa: E501


        :return: The clone_times of this SampleCloneOptions.  # noqa: E501
        :rtype: int
        """
        return self._clone_times

    @clone_times.setter
    def clone_times(self, clone_times):
        """Sets the clone_times of this SampleCloneOptions.


        :param clone_times: The clone_times of this SampleCloneOptions.  # noqa: E501
        :type: int
        """

        self._clone_times = clone_times

    @property
    def track_parent(self):
        """Gets the track_parent of this SampleCloneOptions.  # noqa: E501


        :return: The track_parent of this SampleCloneOptions.  # noqa: E501
        :rtype: bool
        """
        return self._track_parent

    @track_parent.setter
    def track_parent(self, track_parent):
        """Sets the track_parent of this SampleCloneOptions.


        :param track_parent: The track_parent of this SampleCloneOptions.  # noqa: E501
        :type: bool
        """

        self._track_parent = track_parent

    @property
    def quantity(self):
        """Gets the quantity of this SampleCloneOptions.  # noqa: E501


        :return: The quantity of this SampleCloneOptions.  # noqa: E501
        :rtype: QuantityCloneOptions
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SampleCloneOptions.


        :param quantity: The quantity of this SampleCloneOptions.  # noqa: E501
        :type: QuantityCloneOptions
        """

        self._quantity = quantity

    @property
    def storage_position_ranges(self):
        """Gets the storage_position_ranges of this SampleCloneOptions.  # noqa: E501


        :return: The storage_position_ranges of this SampleCloneOptions.  # noqa: E501
        :rtype: list[StoragePositionRange]
        """
        return self._storage_position_ranges

    @storage_position_ranges.setter
    def storage_position_ranges(self, storage_position_ranges):
        """Sets the storage_position_ranges of this SampleCloneOptions.


        :param storage_position_ranges: The storage_position_ranges of this SampleCloneOptions.  # noqa: E501
        :type: list[StoragePositionRange]
        """

        self._storage_position_ranges = storage_position_ranges

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
        if issubclass(SampleCloneOptions, dict):
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
        if not isinstance(other, SampleCloneOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleCloneOptions):
            return True

        return self.to_dict() != other.to_dict()
