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


class PagedOfStorageValidation(object):
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
        'record_count': 'int',
        'current_page': 'int',
        'max_records': 'int',
        'total_records': 'int',
        'data': 'list[StorageValidation]'
    }

    attribute_map = {
        'record_count': 'recordCount',
        'current_page': 'currentPage',
        'max_records': 'maxRecords',
        'total_records': 'totalRecords',
        'data': 'data'
    }

    def __init__(self, record_count=None, current_page=None, max_records=None, total_records=None, data=None, _configuration=None):  # noqa: E501
        """PagedOfStorageValidation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._record_count = None
        self._current_page = None
        self._max_records = None
        self._total_records = None
        self._data = None
        self.discriminator = None

        if record_count is not None:
            self.record_count = record_count
        if current_page is not None:
            self.current_page = current_page
        if max_records is not None:
            self.max_records = max_records
        if total_records is not None:
            self.total_records = total_records
        if data is not None:
            self.data = data

    @property
    def record_count(self):
        """Gets the record_count of this PagedOfStorageValidation.  # noqa: E501


        :return: The record_count of this PagedOfStorageValidation.  # noqa: E501
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this PagedOfStorageValidation.


        :param record_count: The record_count of this PagedOfStorageValidation.  # noqa: E501
        :type: int
        """

        self._record_count = record_count

    @property
    def current_page(self):
        """Gets the current_page of this PagedOfStorageValidation.  # noqa: E501


        :return: The current_page of this PagedOfStorageValidation.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this PagedOfStorageValidation.


        :param current_page: The current_page of this PagedOfStorageValidation.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def max_records(self):
        """Gets the max_records of this PagedOfStorageValidation.  # noqa: E501


        :return: The max_records of this PagedOfStorageValidation.  # noqa: E501
        :rtype: int
        """
        return self._max_records

    @max_records.setter
    def max_records(self, max_records):
        """Sets the max_records of this PagedOfStorageValidation.


        :param max_records: The max_records of this PagedOfStorageValidation.  # noqa: E501
        :type: int
        """

        self._max_records = max_records

    @property
    def total_records(self):
        """Gets the total_records of this PagedOfStorageValidation.  # noqa: E501


        :return: The total_records of this PagedOfStorageValidation.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this PagedOfStorageValidation.


        :param total_records: The total_records of this PagedOfStorageValidation.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def data(self):
        """Gets the data of this PagedOfStorageValidation.  # noqa: E501


        :return: The data of this PagedOfStorageValidation.  # noqa: E501
        :rtype: list[StorageValidation]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PagedOfStorageValidation.


        :param data: The data of this PagedOfStorageValidation.  # noqa: E501
        :type: list[StorageValidation]
        """

        self._data = data

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
        if issubclass(PagedOfStorageValidation, dict):
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
        if not isinstance(other, PagedOfStorageValidation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagedOfStorageValidation):
            return True

        return self.to_dict() != other.to_dict()
