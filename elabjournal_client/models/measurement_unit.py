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

from elabjournal_client.configuration import Configuration


class MeasurementUnit(object):
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
        'quantity_id': 'int',
        'quantity_name': 'str',
        'unit_name': 'str',
        'unit_short': 'str',
        'calculation_factor': 'float'
    }

    attribute_map = {
        'quantity_id': 'quantityID',
        'quantity_name': 'quantityName',
        'unit_name': 'unitName',
        'unit_short': 'unitShort',
        'calculation_factor': 'calculationFactor'
    }

    def __init__(self, quantity_id=None, quantity_name=None, unit_name=None, unit_short=None, calculation_factor=None, _configuration=None):  # noqa: E501
        """MeasurementUnit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._quantity_id = None
        self._quantity_name = None
        self._unit_name = None
        self._unit_short = None
        self._calculation_factor = None
        self.discriminator = None

        if quantity_id is not None:
            self.quantity_id = quantity_id
        if quantity_name is not None:
            self.quantity_name = quantity_name
        if unit_name is not None:
            self.unit_name = unit_name
        if unit_short is not None:
            self.unit_short = unit_short
        if calculation_factor is not None:
            self.calculation_factor = calculation_factor

    @property
    def quantity_id(self):
        """Gets the quantity_id of this MeasurementUnit.  # noqa: E501


        :return: The quantity_id of this MeasurementUnit.  # noqa: E501
        :rtype: int
        """
        return self._quantity_id

    @quantity_id.setter
    def quantity_id(self, quantity_id):
        """Sets the quantity_id of this MeasurementUnit.


        :param quantity_id: The quantity_id of this MeasurementUnit.  # noqa: E501
        :type: int
        """

        self._quantity_id = quantity_id

    @property
    def quantity_name(self):
        """Gets the quantity_name of this MeasurementUnit.  # noqa: E501


        :return: The quantity_name of this MeasurementUnit.  # noqa: E501
        :rtype: str
        """
        return self._quantity_name

    @quantity_name.setter
    def quantity_name(self, quantity_name):
        """Sets the quantity_name of this MeasurementUnit.


        :param quantity_name: The quantity_name of this MeasurementUnit.  # noqa: E501
        :type: str
        """

        self._quantity_name = quantity_name

    @property
    def unit_name(self):
        """Gets the unit_name of this MeasurementUnit.  # noqa: E501


        :return: The unit_name of this MeasurementUnit.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this MeasurementUnit.


        :param unit_name: The unit_name of this MeasurementUnit.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

    @property
    def unit_short(self):
        """Gets the unit_short of this MeasurementUnit.  # noqa: E501


        :return: The unit_short of this MeasurementUnit.  # noqa: E501
        :rtype: str
        """
        return self._unit_short

    @unit_short.setter
    def unit_short(self, unit_short):
        """Sets the unit_short of this MeasurementUnit.


        :param unit_short: The unit_short of this MeasurementUnit.  # noqa: E501
        :type: str
        """

        self._unit_short = unit_short

    @property
    def calculation_factor(self):
        """Gets the calculation_factor of this MeasurementUnit.  # noqa: E501


        :return: The calculation_factor of this MeasurementUnit.  # noqa: E501
        :rtype: float
        """
        return self._calculation_factor

    @calculation_factor.setter
    def calculation_factor(self, calculation_factor):
        """Sets the calculation_factor of this MeasurementUnit.


        :param calculation_factor: The calculation_factor of this MeasurementUnit.  # noqa: E501
        :type: float
        """

        self._calculation_factor = calculation_factor

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
        if issubclass(MeasurementUnit, dict):
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
        if not isinstance(other, MeasurementUnit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeasurementUnit):
            return True

        return self.to_dict() != other.to_dict()