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


class JournalExportRequest(object):
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
        'items': 'list[JournalExportItem]',
        'format': 'str',
        'file_version': 'str'
    }

    attribute_map = {
        'items': 'items',
        'format': 'format',
        'file_version': 'fileVersion'
    }

    def __init__(self, items=None, format=None, file_version=None, _configuration=None):  # noqa: E501
        """JournalExportRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._items = None
        self._format = None
        self._file_version = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if format is not None:
            self.format = format
        if file_version is not None:
            self.file_version = file_version

    @property
    def items(self):
        """Gets the items of this JournalExportRequest.  # noqa: E501


        :return: The items of this JournalExportRequest.  # noqa: E501
        :rtype: list[JournalExportItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this JournalExportRequest.


        :param items: The items of this JournalExportRequest.  # noqa: E501
        :type: list[JournalExportItem]
        """

        self._items = items

    @property
    def format(self):
        """Gets the format of this JournalExportRequest.  # noqa: E501


        :return: The format of this JournalExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this JournalExportRequest.


        :param format: The format of this JournalExportRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["pdf", "html", "json", "xml"]  # noqa: E501
        if (self._configuration.client_side_validation and
                format not in allowed_values):
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def file_version(self):
        """Gets the file_version of this JournalExportRequest.  # noqa: E501


        :return: The file_version of this JournalExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_version

    @file_version.setter
    def file_version(self, file_version):
        """Sets the file_version of this JournalExportRequest.


        :param file_version: The file_version of this JournalExportRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["earliest", "latest"]  # noqa: E501
        if (self._configuration.client_side_validation and
                file_version not in allowed_values):
            raise ValueError(
                "Invalid value for `file_version` ({0}), must be one of {1}"  # noqa: E501
                .format(file_version, allowed_values)
            )

        self._file_version = file_version

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
        if issubclass(JournalExportRequest, dict):
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
        if not isinstance(other, JournalExportRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JournalExportRequest):
            return True

        return self.to_dict() != other.to_dict()
