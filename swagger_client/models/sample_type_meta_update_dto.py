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


class SampleTypeMetaUpdateDto(object):
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
        'key': 'str',
        'sample_data_type': 'str',
        'required': 'bool',
        'notes': 'str',
        'order_column': 'int',
        'default_value': 'str',
        'default_year': 'int',
        'default_month': 'int',
        'default_day': 'int',
        'default_hour': 'int',
        'default_minute': 'int',
        'default_second': 'int',
        'show_inline_images': 'bool',
        'mask_reg_exp': 'str',
        'file_mask': 'str'
    }

    attribute_map = {
        'key': 'key',
        'sample_data_type': 'sampleDataType',
        'required': 'required',
        'notes': 'notes',
        'order_column': 'orderColumn',
        'default_value': 'defaultValue',
        'default_year': 'defaultYear',
        'default_month': 'defaultMonth',
        'default_day': 'defaultDay',
        'default_hour': 'defaultHour',
        'default_minute': 'defaultMinute',
        'default_second': 'defaultSecond',
        'show_inline_images': 'showInlineImages',
        'mask_reg_exp': 'maskRegExp',
        'file_mask': 'fileMask'
    }

    def __init__(self, key=None, sample_data_type=None, required=None, notes=None, order_column=None, default_value=None, default_year=None, default_month=None, default_day=None, default_hour=None, default_minute=None, default_second=None, show_inline_images=None, mask_reg_exp=None, file_mask=None, _configuration=None):  # noqa: E501
        """SampleTypeMetaUpdateDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._sample_data_type = None
        self._required = None
        self._notes = None
        self._order_column = None
        self._default_value = None
        self._default_year = None
        self._default_month = None
        self._default_day = None
        self._default_hour = None
        self._default_minute = None
        self._default_second = None
        self._show_inline_images = None
        self._mask_reg_exp = None
        self._file_mask = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if sample_data_type is not None:
            self.sample_data_type = sample_data_type
        if required is not None:
            self.required = required
        if notes is not None:
            self.notes = notes
        if order_column is not None:
            self.order_column = order_column
        if default_value is not None:
            self.default_value = default_value
        if default_year is not None:
            self.default_year = default_year
        if default_month is not None:
            self.default_month = default_month
        if default_day is not None:
            self.default_day = default_day
        if default_hour is not None:
            self.default_hour = default_hour
        if default_minute is not None:
            self.default_minute = default_minute
        if default_second is not None:
            self.default_second = default_second
        if show_inline_images is not None:
            self.show_inline_images = show_inline_images
        if mask_reg_exp is not None:
            self.mask_reg_exp = mask_reg_exp
        if file_mask is not None:
            self.file_mask = file_mask

    @property
    def key(self):
        """Gets the key of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The key of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SampleTypeMetaUpdateDto.


        :param key: The key of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def sample_data_type(self):
        """Gets the sample_data_type of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The sample_data_type of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._sample_data_type

    @sample_data_type.setter
    def sample_data_type(self, sample_data_type):
        """Sets the sample_data_type of this SampleTypeMetaUpdateDto.


        :param sample_data_type: The sample_data_type of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["TEXT", "TEXTAREA", "RADIO", "CHECKBOX", "NUMERIC", "COMBO", "DATE", "DATETIME", "FILE", "SAMPLELINK", "PROJECT", "CHEMICAL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sample_data_type not in allowed_values):
            raise ValueError(
                "Invalid value for `sample_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sample_data_type, allowed_values)
            )

        self._sample_data_type = sample_data_type

    @property
    def required(self):
        """Gets the required of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The required of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this SampleTypeMetaUpdateDto.


        :param required: The required of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def notes(self):
        """Gets the notes of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The notes of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this SampleTypeMetaUpdateDto.


        :param notes: The notes of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def order_column(self):
        """Gets the order_column of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The order_column of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: int
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        """Sets the order_column of this SampleTypeMetaUpdateDto.


        :param order_column: The order_column of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: int
        """

        self._order_column = order_column

    @property
    def default_value(self):
        """Gets the default_value of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The default_value of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this SampleTypeMetaUpdateDto.


        :param default_value: The default_value of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def default_year(self):
        """Gets the default_year of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The default_year of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: int
        """
        return self._default_year

    @default_year.setter
    def default_year(self, default_year):
        """Sets the default_year of this SampleTypeMetaUpdateDto.


        :param default_year: The default_year of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: int
        """

        self._default_year = default_year

    @property
    def default_month(self):
        """Gets the default_month of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The default_month of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: int
        """
        return self._default_month

    @default_month.setter
    def default_month(self, default_month):
        """Sets the default_month of this SampleTypeMetaUpdateDto.


        :param default_month: The default_month of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: int
        """

        self._default_month = default_month

    @property
    def default_day(self):
        """Gets the default_day of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The default_day of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: int
        """
        return self._default_day

    @default_day.setter
    def default_day(self, default_day):
        """Sets the default_day of this SampleTypeMetaUpdateDto.


        :param default_day: The default_day of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: int
        """

        self._default_day = default_day

    @property
    def default_hour(self):
        """Gets the default_hour of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The default_hour of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: int
        """
        return self._default_hour

    @default_hour.setter
    def default_hour(self, default_hour):
        """Sets the default_hour of this SampleTypeMetaUpdateDto.


        :param default_hour: The default_hour of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: int
        """

        self._default_hour = default_hour

    @property
    def default_minute(self):
        """Gets the default_minute of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The default_minute of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: int
        """
        return self._default_minute

    @default_minute.setter
    def default_minute(self, default_minute):
        """Sets the default_minute of this SampleTypeMetaUpdateDto.


        :param default_minute: The default_minute of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: int
        """

        self._default_minute = default_minute

    @property
    def default_second(self):
        """Gets the default_second of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The default_second of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: int
        """
        return self._default_second

    @default_second.setter
    def default_second(self, default_second):
        """Sets the default_second of this SampleTypeMetaUpdateDto.


        :param default_second: The default_second of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: int
        """

        self._default_second = default_second

    @property
    def show_inline_images(self):
        """Gets the show_inline_images of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The show_inline_images of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: bool
        """
        return self._show_inline_images

    @show_inline_images.setter
    def show_inline_images(self, show_inline_images):
        """Sets the show_inline_images of this SampleTypeMetaUpdateDto.


        :param show_inline_images: The show_inline_images of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: bool
        """

        self._show_inline_images = show_inline_images

    @property
    def mask_reg_exp(self):
        """Gets the mask_reg_exp of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The mask_reg_exp of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._mask_reg_exp

    @mask_reg_exp.setter
    def mask_reg_exp(self, mask_reg_exp):
        """Sets the mask_reg_exp of this SampleTypeMetaUpdateDto.


        :param mask_reg_exp: The mask_reg_exp of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: str
        """

        self._mask_reg_exp = mask_reg_exp

    @property
    def file_mask(self):
        """Gets the file_mask of this SampleTypeMetaUpdateDto.  # noqa: E501


        :return: The file_mask of this SampleTypeMetaUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._file_mask

    @file_mask.setter
    def file_mask(self, file_mask):
        """Sets the file_mask of this SampleTypeMetaUpdateDto.


        :param file_mask: The file_mask of this SampleTypeMetaUpdateDto.  # noqa: E501
        :type: str
        """

        self._file_mask = file_mask

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
        if issubclass(SampleTypeMetaUpdateDto, dict):
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
        if not isinstance(other, SampleTypeMetaUpdateDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleTypeMetaUpdateDto):
            return True

        return self.to_dict() != other.to_dict()
