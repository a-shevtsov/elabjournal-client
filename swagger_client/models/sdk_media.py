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


class SDKMedia(object):
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
        'sdk_plugin_media_id': 'int',
        'order': 'int',
        'file_name': 'str',
        'media_type': 'str',
        'image_url': 'str'
    }

    attribute_map = {
        'sdk_plugin_media_id': 'sdkPluginMediaID',
        'order': 'order',
        'file_name': 'fileName',
        'media_type': 'mediaType',
        'image_url': 'imageURL'
    }

    def __init__(self, sdk_plugin_media_id=None, order=None, file_name=None, media_type=None, image_url=None, _configuration=None):  # noqa: E501
        """SDKMedia - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sdk_plugin_media_id = None
        self._order = None
        self._file_name = None
        self._media_type = None
        self._image_url = None
        self.discriminator = None

        if sdk_plugin_media_id is not None:
            self.sdk_plugin_media_id = sdk_plugin_media_id
        if order is not None:
            self.order = order
        if file_name is not None:
            self.file_name = file_name
        if media_type is not None:
            self.media_type = media_type
        if image_url is not None:
            self.image_url = image_url

    @property
    def sdk_plugin_media_id(self):
        """Gets the sdk_plugin_media_id of this SDKMedia.  # noqa: E501


        :return: The sdk_plugin_media_id of this SDKMedia.  # noqa: E501
        :rtype: int
        """
        return self._sdk_plugin_media_id

    @sdk_plugin_media_id.setter
    def sdk_plugin_media_id(self, sdk_plugin_media_id):
        """Sets the sdk_plugin_media_id of this SDKMedia.


        :param sdk_plugin_media_id: The sdk_plugin_media_id of this SDKMedia.  # noqa: E501
        :type: int
        """

        self._sdk_plugin_media_id = sdk_plugin_media_id

    @property
    def order(self):
        """Gets the order of this SDKMedia.  # noqa: E501


        :return: The order of this SDKMedia.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this SDKMedia.


        :param order: The order of this SDKMedia.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def file_name(self):
        """Gets the file_name of this SDKMedia.  # noqa: E501


        :return: The file_name of this SDKMedia.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SDKMedia.


        :param file_name: The file_name of this SDKMedia.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def media_type(self):
        """Gets the media_type of this SDKMedia.  # noqa: E501


        :return: The media_type of this SDKMedia.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this SDKMedia.


        :param media_type: The media_type of this SDKMedia.  # noqa: E501
        :type: str
        """
        allowed_values = ["LARGEICON", "SMALLICON", "IMAGE", "GIF"]  # noqa: E501
        if (self._configuration.client_side_validation and
                media_type not in allowed_values):
            raise ValueError(
                "Invalid value for `media_type` ({0}), must be one of {1}"  # noqa: E501
                .format(media_type, allowed_values)
            )

        self._media_type = media_type

    @property
    def image_url(self):
        """Gets the image_url of this SDKMedia.  # noqa: E501


        :return: The image_url of this SDKMedia.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this SDKMedia.


        :param image_url: The image_url of this SDKMedia.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

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
        if issubclass(SDKMedia, dict):
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
        if not isinstance(other, SDKMedia):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SDKMedia):
            return True

        return self.to_dict() != other.to_dict()
