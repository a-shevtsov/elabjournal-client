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


class ExperimentSignaturePreDeclinedLarge(object):
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
        'experiment_id': 'int',
        'experiment_name': 'str',
        'declined_by': 'str',
        'group_name': 'str',
        'experiment_pre_signature_id': 'int',
        'user_id': 'int',
        'reason': 'str',
        'decline_date': 'datetime'
    }

    attribute_map = {
        'experiment_id': 'experimentID',
        'experiment_name': 'experimentName',
        'declined_by': 'declinedBy',
        'group_name': 'groupName',
        'experiment_pre_signature_id': 'experimentPreSignatureID',
        'user_id': 'userID',
        'reason': 'reason',
        'decline_date': 'declineDate'
    }

    def __init__(self, experiment_id=None, experiment_name=None, declined_by=None, group_name=None, experiment_pre_signature_id=None, user_id=None, reason=None, decline_date=None, _configuration=None):  # noqa: E501
        """ExperimentSignaturePreDeclinedLarge - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._experiment_id = None
        self._experiment_name = None
        self._declined_by = None
        self._group_name = None
        self._experiment_pre_signature_id = None
        self._user_id = None
        self._reason = None
        self._decline_date = None
        self.discriminator = None

        if experiment_id is not None:
            self.experiment_id = experiment_id
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if declined_by is not None:
            self.declined_by = declined_by
        if group_name is not None:
            self.group_name = group_name
        if experiment_pre_signature_id is not None:
            self.experiment_pre_signature_id = experiment_pre_signature_id
        if user_id is not None:
            self.user_id = user_id
        if reason is not None:
            self.reason = reason
        if decline_date is not None:
            self.decline_date = decline_date

    @property
    def experiment_id(self):
        """Gets the experiment_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The experiment_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: int
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this ExperimentSignaturePreDeclinedLarge.


        :param experiment_id: The experiment_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: int
        """

        self._experiment_id = experiment_id

    @property
    def experiment_name(self):
        """Gets the experiment_name of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The experiment_name of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this ExperimentSignaturePreDeclinedLarge.


        :param experiment_name: The experiment_name of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: str
        """

        self._experiment_name = experiment_name

    @property
    def declined_by(self):
        """Gets the declined_by of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The declined_by of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: str
        """
        return self._declined_by

    @declined_by.setter
    def declined_by(self, declined_by):
        """Sets the declined_by of this ExperimentSignaturePreDeclinedLarge.


        :param declined_by: The declined_by of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: str
        """

        self._declined_by = declined_by

    @property
    def group_name(self):
        """Gets the group_name of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The group_name of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ExperimentSignaturePreDeclinedLarge.


        :param group_name: The group_name of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def experiment_pre_signature_id(self):
        """Gets the experiment_pre_signature_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The experiment_pre_signature_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: int
        """
        return self._experiment_pre_signature_id

    @experiment_pre_signature_id.setter
    def experiment_pre_signature_id(self, experiment_pre_signature_id):
        """Sets the experiment_pre_signature_id of this ExperimentSignaturePreDeclinedLarge.


        :param experiment_pre_signature_id: The experiment_pre_signature_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: int
        """

        self._experiment_pre_signature_id = experiment_pre_signature_id

    @property
    def user_id(self):
        """Gets the user_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The user_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ExperimentSignaturePreDeclinedLarge.


        :param user_id: The user_id of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def reason(self):
        """Gets the reason of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The reason of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ExperimentSignaturePreDeclinedLarge.


        :param reason: The reason of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def decline_date(self):
        """Gets the decline_date of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501


        :return: The decline_date of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :rtype: datetime
        """
        return self._decline_date

    @decline_date.setter
    def decline_date(self, decline_date):
        """Sets the decline_date of this ExperimentSignaturePreDeclinedLarge.


        :param decline_date: The decline_date of this ExperimentSignaturePreDeclinedLarge.  # noqa: E501
        :type: datetime
        """

        self._decline_date = decline_date

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
        if issubclass(ExperimentSignaturePreDeclinedLarge, dict):
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
        if not isinstance(other, ExperimentSignaturePreDeclinedLarge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExperimentSignaturePreDeclinedLarge):
            return True

        return self.to_dict() != other.to_dict()
