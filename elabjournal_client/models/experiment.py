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


class Experiment(object):
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
        'group_id': 'int',
        'subgroup_id': 'int',
        'user_id': 'int',
        'workflow_step_id': 'int',
        'name': 'str',
        'description': 'str',
        'notes': 'str',
        'created': 'datetime',
        'status_changed': 'datetime',
        'dependency_experiment_id': 'int',
        'due': 'datetime',
        'deleted': 'bool',
        'template': 'bool'
    }

    attribute_map = {
        'experiment_id': 'experimentID',
        'group_id': 'groupID',
        'subgroup_id': 'subgroupID',
        'user_id': 'userID',
        'workflow_step_id': 'workflowStepID',
        'name': 'name',
        'description': 'description',
        'notes': 'notes',
        'created': 'created',
        'status_changed': 'statusChanged',
        'dependency_experiment_id': 'dependencyExperimentID',
        'due': 'due',
        'deleted': 'deleted',
        'template': 'template'
    }

    def __init__(self, experiment_id=None, group_id=None, subgroup_id=None, user_id=None, workflow_step_id=None, name=None, description=None, notes=None, created=None, status_changed=None, dependency_experiment_id=None, due=None, deleted=None, template=None, _configuration=None):  # noqa: E501
        """Experiment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._experiment_id = None
        self._group_id = None
        self._subgroup_id = None
        self._user_id = None
        self._workflow_step_id = None
        self._name = None
        self._description = None
        self._notes = None
        self._created = None
        self._status_changed = None
        self._dependency_experiment_id = None
        self._due = None
        self._deleted = None
        self._template = None
        self.discriminator = None

        if experiment_id is not None:
            self.experiment_id = experiment_id
        if group_id is not None:
            self.group_id = group_id
        if subgroup_id is not None:
            self.subgroup_id = subgroup_id
        if user_id is not None:
            self.user_id = user_id
        if workflow_step_id is not None:
            self.workflow_step_id = workflow_step_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if notes is not None:
            self.notes = notes
        if created is not None:
            self.created = created
        if status_changed is not None:
            self.status_changed = status_changed
        if dependency_experiment_id is not None:
            self.dependency_experiment_id = dependency_experiment_id
        if due is not None:
            self.due = due
        if deleted is not None:
            self.deleted = deleted
        if template is not None:
            self.template = template

    @property
    def experiment_id(self):
        """Gets the experiment_id of this Experiment.  # noqa: E501


        :return: The experiment_id of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this Experiment.


        :param experiment_id: The experiment_id of this Experiment.  # noqa: E501
        :type: int
        """

        self._experiment_id = experiment_id

    @property
    def group_id(self):
        """Gets the group_id of this Experiment.  # noqa: E501


        :return: The group_id of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Experiment.


        :param group_id: The group_id of this Experiment.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def subgroup_id(self):
        """Gets the subgroup_id of this Experiment.  # noqa: E501


        :return: The subgroup_id of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._subgroup_id

    @subgroup_id.setter
    def subgroup_id(self, subgroup_id):
        """Sets the subgroup_id of this Experiment.


        :param subgroup_id: The subgroup_id of this Experiment.  # noqa: E501
        :type: int
        """

        self._subgroup_id = subgroup_id

    @property
    def user_id(self):
        """Gets the user_id of this Experiment.  # noqa: E501


        :return: The user_id of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Experiment.


        :param user_id: The user_id of this Experiment.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def workflow_step_id(self):
        """Gets the workflow_step_id of this Experiment.  # noqa: E501


        :return: The workflow_step_id of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._workflow_step_id

    @workflow_step_id.setter
    def workflow_step_id(self, workflow_step_id):
        """Sets the workflow_step_id of this Experiment.


        :param workflow_step_id: The workflow_step_id of this Experiment.  # noqa: E501
        :type: int
        """

        self._workflow_step_id = workflow_step_id

    @property
    def name(self):
        """Gets the name of this Experiment.  # noqa: E501


        :return: The name of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Experiment.


        :param name: The name of this Experiment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Experiment.  # noqa: E501


        :return: The description of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Experiment.


        :param description: The description of this Experiment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def notes(self):
        """Gets the notes of this Experiment.  # noqa: E501


        :return: The notes of this Experiment.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Experiment.


        :param notes: The notes of this Experiment.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def created(self):
        """Gets the created of this Experiment.  # noqa: E501


        :return: The created of this Experiment.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Experiment.


        :param created: The created of this Experiment.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def status_changed(self):
        """Gets the status_changed of this Experiment.  # noqa: E501


        :return: The status_changed of this Experiment.  # noqa: E501
        :rtype: datetime
        """
        return self._status_changed

    @status_changed.setter
    def status_changed(self, status_changed):
        """Sets the status_changed of this Experiment.


        :param status_changed: The status_changed of this Experiment.  # noqa: E501
        :type: datetime
        """

        self._status_changed = status_changed

    @property
    def dependency_experiment_id(self):
        """Gets the dependency_experiment_id of this Experiment.  # noqa: E501


        :return: The dependency_experiment_id of this Experiment.  # noqa: E501
        :rtype: int
        """
        return self._dependency_experiment_id

    @dependency_experiment_id.setter
    def dependency_experiment_id(self, dependency_experiment_id):
        """Sets the dependency_experiment_id of this Experiment.


        :param dependency_experiment_id: The dependency_experiment_id of this Experiment.  # noqa: E501
        :type: int
        """

        self._dependency_experiment_id = dependency_experiment_id

    @property
    def due(self):
        """Gets the due of this Experiment.  # noqa: E501


        :return: The due of this Experiment.  # noqa: E501
        :rtype: datetime
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this Experiment.


        :param due: The due of this Experiment.  # noqa: E501
        :type: datetime
        """

        self._due = due

    @property
    def deleted(self):
        """Gets the deleted of this Experiment.  # noqa: E501


        :return: The deleted of this Experiment.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Experiment.


        :param deleted: The deleted of this Experiment.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def template(self):
        """Gets the template of this Experiment.  # noqa: E501


        :return: The template of this Experiment.  # noqa: E501
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Experiment.


        :param template: The template of this Experiment.  # noqa: E501
        :type: bool
        """

        self._template = template

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
        if issubclass(Experiment, dict):
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
        if not isinstance(other, Experiment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Experiment):
            return True

        return self.to_dict() != other.to_dict()