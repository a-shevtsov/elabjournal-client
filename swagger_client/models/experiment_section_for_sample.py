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


class ExperimentSectionForSample(object):
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
        'exp_journal_id': 'int',
        'section_header': 'str',
        'section_type': 'str',
        'created': 'datetime',
        'experiment': 'ExperimentReference'
    }

    attribute_map = {
        'exp_journal_id': 'expJournalID',
        'section_header': 'sectionHeader',
        'section_type': 'sectionType',
        'created': 'created',
        'experiment': 'experiment'
    }

    def __init__(self, exp_journal_id=None, section_header=None, section_type=None, created=None, experiment=None, _configuration=None):  # noqa: E501
        """ExperimentSectionForSample - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._exp_journal_id = None
        self._section_header = None
        self._section_type = None
        self._created = None
        self._experiment = None
        self.discriminator = None

        if exp_journal_id is not None:
            self.exp_journal_id = exp_journal_id
        if section_header is not None:
            self.section_header = section_header
        if section_type is not None:
            self.section_type = section_type
        if created is not None:
            self.created = created
        if experiment is not None:
            self.experiment = experiment

    @property
    def exp_journal_id(self):
        """Gets the exp_journal_id of this ExperimentSectionForSample.  # noqa: E501


        :return: The exp_journal_id of this ExperimentSectionForSample.  # noqa: E501
        :rtype: int
        """
        return self._exp_journal_id

    @exp_journal_id.setter
    def exp_journal_id(self, exp_journal_id):
        """Sets the exp_journal_id of this ExperimentSectionForSample.


        :param exp_journal_id: The exp_journal_id of this ExperimentSectionForSample.  # noqa: E501
        :type: int
        """

        self._exp_journal_id = exp_journal_id

    @property
    def section_header(self):
        """Gets the section_header of this ExperimentSectionForSample.  # noqa: E501


        :return: The section_header of this ExperimentSectionForSample.  # noqa: E501
        :rtype: str
        """
        return self._section_header

    @section_header.setter
    def section_header(self, section_header):
        """Sets the section_header of this ExperimentSectionForSample.


        :param section_header: The section_header of this ExperimentSectionForSample.  # noqa: E501
        :type: str
        """

        self._section_header = section_header

    @property
    def section_type(self):
        """Gets the section_type of this ExperimentSectionForSample.  # noqa: E501


        :return: The section_type of this ExperimentSectionForSample.  # noqa: E501
        :rtype: str
        """
        return self._section_type

    @section_type.setter
    def section_type(self, section_type):
        """Sets the section_type of this ExperimentSectionForSample.


        :param section_type: The section_type of this ExperimentSectionForSample.  # noqa: E501
        :type: str
        """
        allowed_values = ["CANVAS", "COMMENT", "IMAGE", "NOTES", "FILES", "OUTPUTSAMPLES", "BASESAMPLES", "PARAGRAPH", "PROCEDURE", "DATATABLE", "SAMPLESIN", "SAMPLESOUT", "FILE", "EXCEL", "MARVINJS", "CHEMICAL", "CUSTOM"]  # noqa: E501
        if (self._configuration.client_side_validation and
                section_type not in allowed_values):
            raise ValueError(
                "Invalid value for `section_type` ({0}), must be one of {1}"  # noqa: E501
                .format(section_type, allowed_values)
            )

        self._section_type = section_type

    @property
    def created(self):
        """Gets the created of this ExperimentSectionForSample.  # noqa: E501


        :return: The created of this ExperimentSectionForSample.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ExperimentSectionForSample.


        :param created: The created of this ExperimentSectionForSample.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def experiment(self):
        """Gets the experiment of this ExperimentSectionForSample.  # noqa: E501


        :return: The experiment of this ExperimentSectionForSample.  # noqa: E501
        :rtype: ExperimentReference
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this ExperimentSectionForSample.


        :param experiment: The experiment of this ExperimentSectionForSample.  # noqa: E501
        :type: ExperimentReference
        """

        self._experiment = experiment

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
        if issubclass(ExperimentSectionForSample, dict):
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
        if not isinstance(other, ExperimentSectionForSample):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExperimentSectionForSample):
            return True

        return self.to_dict() != other.to_dict()
