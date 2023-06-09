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


class CreateWorkstationFileDto(object):
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
        'file_name': 'str',
        'total_chunks': 'int',
        'chunk': 'int',
        'chunk_hash': 'str',
        'file_identifier': 'str'
    }

    attribute_map = {
        'file_name': 'fileName',
        'total_chunks': 'totalChunks',
        'chunk': 'chunk',
        'chunk_hash': 'chunkHash',
        'file_identifier': 'fileIdentifier'
    }

    def __init__(self, file_name=None, total_chunks=None, chunk=None, chunk_hash=None, file_identifier=None, _configuration=None):  # noqa: E501
        """CreateWorkstationFileDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_name = None
        self._total_chunks = None
        self._chunk = None
        self._chunk_hash = None
        self._file_identifier = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if total_chunks is not None:
            self.total_chunks = total_chunks
        if chunk is not None:
            self.chunk = chunk
        if chunk_hash is not None:
            self.chunk_hash = chunk_hash
        if file_identifier is not None:
            self.file_identifier = file_identifier

    @property
    def file_name(self):
        """Gets the file_name of this CreateWorkstationFileDto.  # noqa: E501


        :return: The file_name of this CreateWorkstationFileDto.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CreateWorkstationFileDto.


        :param file_name: The file_name of this CreateWorkstationFileDto.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def total_chunks(self):
        """Gets the total_chunks of this CreateWorkstationFileDto.  # noqa: E501


        :return: The total_chunks of this CreateWorkstationFileDto.  # noqa: E501
        :rtype: int
        """
        return self._total_chunks

    @total_chunks.setter
    def total_chunks(self, total_chunks):
        """Sets the total_chunks of this CreateWorkstationFileDto.


        :param total_chunks: The total_chunks of this CreateWorkstationFileDto.  # noqa: E501
        :type: int
        """

        self._total_chunks = total_chunks

    @property
    def chunk(self):
        """Gets the chunk of this CreateWorkstationFileDto.  # noqa: E501


        :return: The chunk of this CreateWorkstationFileDto.  # noqa: E501
        :rtype: int
        """
        return self._chunk

    @chunk.setter
    def chunk(self, chunk):
        """Sets the chunk of this CreateWorkstationFileDto.


        :param chunk: The chunk of this CreateWorkstationFileDto.  # noqa: E501
        :type: int
        """

        self._chunk = chunk

    @property
    def chunk_hash(self):
        """Gets the chunk_hash of this CreateWorkstationFileDto.  # noqa: E501


        :return: The chunk_hash of this CreateWorkstationFileDto.  # noqa: E501
        :rtype: str
        """
        return self._chunk_hash

    @chunk_hash.setter
    def chunk_hash(self, chunk_hash):
        """Sets the chunk_hash of this CreateWorkstationFileDto.


        :param chunk_hash: The chunk_hash of this CreateWorkstationFileDto.  # noqa: E501
        :type: str
        """

        self._chunk_hash = chunk_hash

    @property
    def file_identifier(self):
        """Gets the file_identifier of this CreateWorkstationFileDto.  # noqa: E501


        :return: The file_identifier of this CreateWorkstationFileDto.  # noqa: E501
        :rtype: str
        """
        return self._file_identifier

    @file_identifier.setter
    def file_identifier(self, file_identifier):
        """Sets the file_identifier of this CreateWorkstationFileDto.


        :param file_identifier: The file_identifier of this CreateWorkstationFileDto.  # noqa: E501
        :type: str
        """

        self._file_identifier = file_identifier

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
        if issubclass(CreateWorkstationFileDto, dict):
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
        if not isinstance(other, CreateWorkstationFileDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateWorkstationFileDto):
            return True

        return self.to_dict() != other.to_dict()
