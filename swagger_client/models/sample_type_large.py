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


class SampleTypeLarge(object):
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
        'sample_type_numbering': 'SampleTypeNumbering',
        'sample_type_id': 'int',
        'user_id': 'int',
        'group_id': 'int',
        'deleted': 'bool',
        'show_sections_in_tabs': 'bool',
        'has_expiration_date': 'bool',
        'default_unit_short': 'str',
        'name': 'str',
        'description': 'str',
        'background_color': 'str',
        'foreground_color': 'str',
        'quantity_required': 'bool',
        'default_quantity_type': 'str',
        'threshold_enabled': 'bool',
        'default_quantity_threshold': 'float',
        'default_quantity_amount': 'int',
        'default_threshold_action': 'str',
        'default_unit': 'str'
    }

    attribute_map = {
        'sample_type_numbering': 'sampleTypeNumbering',
        'sample_type_id': 'sampleTypeID',
        'user_id': 'userID',
        'group_id': 'groupID',
        'deleted': 'deleted',
        'show_sections_in_tabs': 'showSectionsInTabs',
        'has_expiration_date': 'hasExpirationDate',
        'default_unit_short': 'defaultUnitShort',
        'name': 'name',
        'description': 'description',
        'background_color': 'backgroundColor',
        'foreground_color': 'foregroundColor',
        'quantity_required': 'quantityRequired',
        'default_quantity_type': 'defaultQuantityType',
        'threshold_enabled': 'thresholdEnabled',
        'default_quantity_threshold': 'defaultQuantityThreshold',
        'default_quantity_amount': 'defaultQuantityAmount',
        'default_threshold_action': 'defaultThresholdAction',
        'default_unit': 'defaultUnit'
    }

    def __init__(self, sample_type_numbering=None, sample_type_id=None, user_id=None, group_id=None, deleted=None, show_sections_in_tabs=None, has_expiration_date=None, default_unit_short=None, name=None, description=None, background_color=None, foreground_color=None, quantity_required=None, default_quantity_type=None, threshold_enabled=None, default_quantity_threshold=None, default_quantity_amount=None, default_threshold_action=None, default_unit=None, _configuration=None):  # noqa: E501
        """SampleTypeLarge - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sample_type_numbering = None
        self._sample_type_id = None
        self._user_id = None
        self._group_id = None
        self._deleted = None
        self._show_sections_in_tabs = None
        self._has_expiration_date = None
        self._default_unit_short = None
        self._name = None
        self._description = None
        self._background_color = None
        self._foreground_color = None
        self._quantity_required = None
        self._default_quantity_type = None
        self._threshold_enabled = None
        self._default_quantity_threshold = None
        self._default_quantity_amount = None
        self._default_threshold_action = None
        self._default_unit = None
        self.discriminator = None

        if sample_type_numbering is not None:
            self.sample_type_numbering = sample_type_numbering
        if sample_type_id is not None:
            self.sample_type_id = sample_type_id
        if user_id is not None:
            self.user_id = user_id
        if group_id is not None:
            self.group_id = group_id
        if deleted is not None:
            self.deleted = deleted
        if show_sections_in_tabs is not None:
            self.show_sections_in_tabs = show_sections_in_tabs
        if has_expiration_date is not None:
            self.has_expiration_date = has_expiration_date
        if default_unit_short is not None:
            self.default_unit_short = default_unit_short
        self.name = name
        if description is not None:
            self.description = description
        if background_color is not None:
            self.background_color = background_color
        if foreground_color is not None:
            self.foreground_color = foreground_color
        if quantity_required is not None:
            self.quantity_required = quantity_required
        if default_quantity_type is not None:
            self.default_quantity_type = default_quantity_type
        if threshold_enabled is not None:
            self.threshold_enabled = threshold_enabled
        if default_quantity_threshold is not None:
            self.default_quantity_threshold = default_quantity_threshold
        if default_quantity_amount is not None:
            self.default_quantity_amount = default_quantity_amount
        if default_threshold_action is not None:
            self.default_threshold_action = default_threshold_action
        if default_unit is not None:
            self.default_unit = default_unit

    @property
    def sample_type_numbering(self):
        """Gets the sample_type_numbering of this SampleTypeLarge.  # noqa: E501


        :return: The sample_type_numbering of this SampleTypeLarge.  # noqa: E501
        :rtype: SampleTypeNumbering
        """
        return self._sample_type_numbering

    @sample_type_numbering.setter
    def sample_type_numbering(self, sample_type_numbering):
        """Sets the sample_type_numbering of this SampleTypeLarge.


        :param sample_type_numbering: The sample_type_numbering of this SampleTypeLarge.  # noqa: E501
        :type: SampleTypeNumbering
        """

        self._sample_type_numbering = sample_type_numbering

    @property
    def sample_type_id(self):
        """Gets the sample_type_id of this SampleTypeLarge.  # noqa: E501


        :return: The sample_type_id of this SampleTypeLarge.  # noqa: E501
        :rtype: int
        """
        return self._sample_type_id

    @sample_type_id.setter
    def sample_type_id(self, sample_type_id):
        """Sets the sample_type_id of this SampleTypeLarge.


        :param sample_type_id: The sample_type_id of this SampleTypeLarge.  # noqa: E501
        :type: int
        """

        self._sample_type_id = sample_type_id

    @property
    def user_id(self):
        """Gets the user_id of this SampleTypeLarge.  # noqa: E501


        :return: The user_id of this SampleTypeLarge.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SampleTypeLarge.


        :param user_id: The user_id of this SampleTypeLarge.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """Gets the group_id of this SampleTypeLarge.  # noqa: E501


        :return: The group_id of this SampleTypeLarge.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this SampleTypeLarge.


        :param group_id: The group_id of this SampleTypeLarge.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def deleted(self):
        """Gets the deleted of this SampleTypeLarge.  # noqa: E501


        :return: The deleted of this SampleTypeLarge.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this SampleTypeLarge.


        :param deleted: The deleted of this SampleTypeLarge.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def show_sections_in_tabs(self):
        """Gets the show_sections_in_tabs of this SampleTypeLarge.  # noqa: E501


        :return: The show_sections_in_tabs of this SampleTypeLarge.  # noqa: E501
        :rtype: bool
        """
        return self._show_sections_in_tabs

    @show_sections_in_tabs.setter
    def show_sections_in_tabs(self, show_sections_in_tabs):
        """Sets the show_sections_in_tabs of this SampleTypeLarge.


        :param show_sections_in_tabs: The show_sections_in_tabs of this SampleTypeLarge.  # noqa: E501
        :type: bool
        """

        self._show_sections_in_tabs = show_sections_in_tabs

    @property
    def has_expiration_date(self):
        """Gets the has_expiration_date of this SampleTypeLarge.  # noqa: E501


        :return: The has_expiration_date of this SampleTypeLarge.  # noqa: E501
        :rtype: bool
        """
        return self._has_expiration_date

    @has_expiration_date.setter
    def has_expiration_date(self, has_expiration_date):
        """Sets the has_expiration_date of this SampleTypeLarge.


        :param has_expiration_date: The has_expiration_date of this SampleTypeLarge.  # noqa: E501
        :type: bool
        """

        self._has_expiration_date = has_expiration_date

    @property
    def default_unit_short(self):
        """Gets the default_unit_short of this SampleTypeLarge.  # noqa: E501


        :return: The default_unit_short of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._default_unit_short

    @default_unit_short.setter
    def default_unit_short(self, default_unit_short):
        """Sets the default_unit_short of this SampleTypeLarge.


        :param default_unit_short: The default_unit_short of this SampleTypeLarge.  # noqa: E501
        :type: str
        """

        self._default_unit_short = default_unit_short

    @property
    def name(self):
        """Gets the name of this SampleTypeLarge.  # noqa: E501


        :return: The name of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SampleTypeLarge.


        :param name: The name of this SampleTypeLarge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this SampleTypeLarge.  # noqa: E501


        :return: The description of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SampleTypeLarge.


        :param description: The description of this SampleTypeLarge.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def background_color(self):
        """Gets the background_color of this SampleTypeLarge.  # noqa: E501


        :return: The background_color of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this SampleTypeLarge.


        :param background_color: The background_color of this SampleTypeLarge.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def foreground_color(self):
        """Gets the foreground_color of this SampleTypeLarge.  # noqa: E501


        :return: The foreground_color of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """Sets the foreground_color of this SampleTypeLarge.


        :param foreground_color: The foreground_color of this SampleTypeLarge.  # noqa: E501
        :type: str
        """

        self._foreground_color = foreground_color

    @property
    def quantity_required(self):
        """Gets the quantity_required of this SampleTypeLarge.  # noqa: E501


        :return: The quantity_required of this SampleTypeLarge.  # noqa: E501
        :rtype: bool
        """
        return self._quantity_required

    @quantity_required.setter
    def quantity_required(self, quantity_required):
        """Sets the quantity_required of this SampleTypeLarge.


        :param quantity_required: The quantity_required of this SampleTypeLarge.  # noqa: E501
        :type: bool
        """

        self._quantity_required = quantity_required

    @property
    def default_quantity_type(self):
        """Gets the default_quantity_type of this SampleTypeLarge.  # noqa: E501


        :return: The default_quantity_type of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._default_quantity_type

    @default_quantity_type.setter
    def default_quantity_type(self, default_quantity_type):
        """Sets the default_quantity_type of this SampleTypeLarge.


        :param default_quantity_type: The default_quantity_type of this SampleTypeLarge.  # noqa: E501
        :type: str
        """
        allowed_values = ["Empty", "Volume", "Mass", "Number"]  # noqa: E501
        if (self._configuration.client_side_validation and
                default_quantity_type not in allowed_values):
            raise ValueError(
                "Invalid value for `default_quantity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(default_quantity_type, allowed_values)
            )

        self._default_quantity_type = default_quantity_type

    @property
    def threshold_enabled(self):
        """Gets the threshold_enabled of this SampleTypeLarge.  # noqa: E501


        :return: The threshold_enabled of this SampleTypeLarge.  # noqa: E501
        :rtype: bool
        """
        return self._threshold_enabled

    @threshold_enabled.setter
    def threshold_enabled(self, threshold_enabled):
        """Sets the threshold_enabled of this SampleTypeLarge.


        :param threshold_enabled: The threshold_enabled of this SampleTypeLarge.  # noqa: E501
        :type: bool
        """

        self._threshold_enabled = threshold_enabled

    @property
    def default_quantity_threshold(self):
        """Gets the default_quantity_threshold of this SampleTypeLarge.  # noqa: E501


        :return: The default_quantity_threshold of this SampleTypeLarge.  # noqa: E501
        :rtype: float
        """
        return self._default_quantity_threshold

    @default_quantity_threshold.setter
    def default_quantity_threshold(self, default_quantity_threshold):
        """Sets the default_quantity_threshold of this SampleTypeLarge.


        :param default_quantity_threshold: The default_quantity_threshold of this SampleTypeLarge.  # noqa: E501
        :type: float
        """
        if (self._configuration.client_side_validation and
                default_quantity_threshold is not None and default_quantity_threshold > 100):  # noqa: E501
            raise ValueError("Invalid value for `default_quantity_threshold`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                default_quantity_threshold is not None and default_quantity_threshold < 0):  # noqa: E501
            raise ValueError("Invalid value for `default_quantity_threshold`, must be a value greater than or equal to `0`")  # noqa: E501

        self._default_quantity_threshold = default_quantity_threshold

    @property
    def default_quantity_amount(self):
        """Gets the default_quantity_amount of this SampleTypeLarge.  # noqa: E501


        :return: The default_quantity_amount of this SampleTypeLarge.  # noqa: E501
        :rtype: int
        """
        return self._default_quantity_amount

    @default_quantity_amount.setter
    def default_quantity_amount(self, default_quantity_amount):
        """Sets the default_quantity_amount of this SampleTypeLarge.


        :param default_quantity_amount: The default_quantity_amount of this SampleTypeLarge.  # noqa: E501
        :type: int
        """

        self._default_quantity_amount = default_quantity_amount

    @property
    def default_threshold_action(self):
        """Gets the default_threshold_action of this SampleTypeLarge.  # noqa: E501


        :return: The default_threshold_action of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._default_threshold_action

    @default_threshold_action.setter
    def default_threshold_action(self, default_threshold_action):
        """Sets the default_threshold_action of this SampleTypeLarge.


        :param default_threshold_action: The default_threshold_action of this SampleTypeLarge.  # noqa: E501
        :type: str
        """
        allowed_values = ["Nothing", "Notify", "Order", "NotifyAndOrder"]  # noqa: E501
        if (self._configuration.client_side_validation and
                default_threshold_action not in allowed_values):
            raise ValueError(
                "Invalid value for `default_threshold_action` ({0}), must be one of {1}"  # noqa: E501
                .format(default_threshold_action, allowed_values)
            )

        self._default_threshold_action = default_threshold_action

    @property
    def default_unit(self):
        """Gets the default_unit of this SampleTypeLarge.  # noqa: E501


        :return: The default_unit of this SampleTypeLarge.  # noqa: E501
        :rtype: str
        """
        return self._default_unit

    @default_unit.setter
    def default_unit(self, default_unit):
        """Sets the default_unit of this SampleTypeLarge.


        :param default_unit: The default_unit of this SampleTypeLarge.  # noqa: E501
        :type: str
        """
        allowed_values = ["Nothing", "Liter", "MilliLiter", "MicroLiter", "KiloGram", "Gram", "MilliGram", "MicroGram", "Unit"]  # noqa: E501
        if (self._configuration.client_side_validation and
                default_unit not in allowed_values):
            raise ValueError(
                "Invalid value for `default_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(default_unit, allowed_values)
            )

        self._default_unit = default_unit

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
        if issubclass(SampleTypeLarge, dict):
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
        if not isinstance(other, SampleTypeLarge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleTypeLarge):
            return True

        return self.to_dict() != other.to_dict()
