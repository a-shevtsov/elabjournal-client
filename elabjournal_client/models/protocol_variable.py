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


class ProtocolVariable(object):
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
        'var_id': 'int',
        'prot_version_id': 'int',
        'name': 'str',
        'description': 'str',
        'var_type': 'str',
        'quantity_id': 'int',
        'unit': 'str',
        'contents': 'str',
        'data_set_id': 'int',
        'prot_var_attr': 'list[ProtocolVariableAttribute]',
        'default_checked': 'str',
        'data_set_items': 'list[ProtocolDataSetItem]'
    }

    attribute_map = {
        'var_id': 'varID',
        'prot_version_id': 'protVersionID',
        'name': 'name',
        'description': 'description',
        'var_type': 'varType',
        'quantity_id': 'quantityID',
        'unit': 'unit',
        'contents': 'contents',
        'data_set_id': 'dataSetID',
        'prot_var_attr': 'protVarAttr',
        'default_checked': 'defaultChecked',
        'data_set_items': 'dataSetItems'
    }

    def __init__(self, var_id=None, prot_version_id=None, name=None, description=None, var_type=None, quantity_id=None, unit=None, contents=None, data_set_id=None, prot_var_attr=None, default_checked=None, data_set_items=None, _configuration=None):  # noqa: E501
        """ProtocolVariable - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._var_id = None
        self._prot_version_id = None
        self._name = None
        self._description = None
        self._var_type = None
        self._quantity_id = None
        self._unit = None
        self._contents = None
        self._data_set_id = None
        self._prot_var_attr = None
        self._default_checked = None
        self._data_set_items = None
        self.discriminator = None

        if var_id is not None:
            self.var_id = var_id
        if prot_version_id is not None:
            self.prot_version_id = prot_version_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if var_type is not None:
            self.var_type = var_type
        if quantity_id is not None:
            self.quantity_id = quantity_id
        if unit is not None:
            self.unit = unit
        if contents is not None:
            self.contents = contents
        if data_set_id is not None:
            self.data_set_id = data_set_id
        if prot_var_attr is not None:
            self.prot_var_attr = prot_var_attr
        if default_checked is not None:
            self.default_checked = default_checked
        if data_set_items is not None:
            self.data_set_items = data_set_items

    @property
    def var_id(self):
        """Gets the var_id of this ProtocolVariable.  # noqa: E501


        :return: The var_id of this ProtocolVariable.  # noqa: E501
        :rtype: int
        """
        return self._var_id

    @var_id.setter
    def var_id(self, var_id):
        """Sets the var_id of this ProtocolVariable.


        :param var_id: The var_id of this ProtocolVariable.  # noqa: E501
        :type: int
        """

        self._var_id = var_id

    @property
    def prot_version_id(self):
        """Gets the prot_version_id of this ProtocolVariable.  # noqa: E501


        :return: The prot_version_id of this ProtocolVariable.  # noqa: E501
        :rtype: int
        """
        return self._prot_version_id

    @prot_version_id.setter
    def prot_version_id(self, prot_version_id):
        """Sets the prot_version_id of this ProtocolVariable.


        :param prot_version_id: The prot_version_id of this ProtocolVariable.  # noqa: E501
        :type: int
        """

        self._prot_version_id = prot_version_id

    @property
    def name(self):
        """Gets the name of this ProtocolVariable.  # noqa: E501


        :return: The name of this ProtocolVariable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtocolVariable.


        :param name: The name of this ProtocolVariable.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProtocolVariable.  # noqa: E501


        :return: The description of this ProtocolVariable.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProtocolVariable.


        :param description: The description of this ProtocolVariable.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def var_type(self):
        """Gets the var_type of this ProtocolVariable.  # noqa: E501


        :return: The var_type of this ProtocolVariable.  # noqa: E501
        :rtype: str
        """
        return self._var_type

    @var_type.setter
    def var_type(self, var_type):
        """Sets the var_type of this ProtocolVariable.


        :param var_type: The var_type of this ProtocolVariable.  # noqa: E501
        :type: str
        """
        allowed_values = ["checkbox", "combobox", "dataset", "date", "datetime", "formula", "sample", "samplefield", "textarea", "textfield", "time"]  # noqa: E501
        if (self._configuration.client_side_validation and
                var_type not in allowed_values):
            raise ValueError(
                "Invalid value for `var_type` ({0}), must be one of {1}"  # noqa: E501
                .format(var_type, allowed_values)
            )

        self._var_type = var_type

    @property
    def quantity_id(self):
        """Gets the quantity_id of this ProtocolVariable.  # noqa: E501


        :return: The quantity_id of this ProtocolVariable.  # noqa: E501
        :rtype: int
        """
        return self._quantity_id

    @quantity_id.setter
    def quantity_id(self, quantity_id):
        """Sets the quantity_id of this ProtocolVariable.


        :param quantity_id: The quantity_id of this ProtocolVariable.  # noqa: E501
        :type: int
        """

        self._quantity_id = quantity_id

    @property
    def unit(self):
        """Gets the unit of this ProtocolVariable.  # noqa: E501


        :return: The unit of this ProtocolVariable.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ProtocolVariable.


        :param unit: The unit of this ProtocolVariable.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def contents(self):
        """Gets the contents of this ProtocolVariable.  # noqa: E501


        :return: The contents of this ProtocolVariable.  # noqa: E501
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this ProtocolVariable.


        :param contents: The contents of this ProtocolVariable.  # noqa: E501
        :type: str
        """

        self._contents = contents

    @property
    def data_set_id(self):
        """Gets the data_set_id of this ProtocolVariable.  # noqa: E501


        :return: The data_set_id of this ProtocolVariable.  # noqa: E501
        :rtype: int
        """
        return self._data_set_id

    @data_set_id.setter
    def data_set_id(self, data_set_id):
        """Sets the data_set_id of this ProtocolVariable.


        :param data_set_id: The data_set_id of this ProtocolVariable.  # noqa: E501
        :type: int
        """

        self._data_set_id = data_set_id

    @property
    def prot_var_attr(self):
        """Gets the prot_var_attr of this ProtocolVariable.  # noqa: E501


        :return: The prot_var_attr of this ProtocolVariable.  # noqa: E501
        :rtype: list[ProtocolVariableAttribute]
        """
        return self._prot_var_attr

    @prot_var_attr.setter
    def prot_var_attr(self, prot_var_attr):
        """Sets the prot_var_attr of this ProtocolVariable.


        :param prot_var_attr: The prot_var_attr of this ProtocolVariable.  # noqa: E501
        :type: list[ProtocolVariableAttribute]
        """

        self._prot_var_attr = prot_var_attr

    @property
    def default_checked(self):
        """Gets the default_checked of this ProtocolVariable.  # noqa: E501


        :return: The default_checked of this ProtocolVariable.  # noqa: E501
        :rtype: str
        """
        return self._default_checked

    @default_checked.setter
    def default_checked(self, default_checked):
        """Sets the default_checked of this ProtocolVariable.


        :param default_checked: The default_checked of this ProtocolVariable.  # noqa: E501
        :type: str
        """

        self._default_checked = default_checked

    @property
    def data_set_items(self):
        """Gets the data_set_items of this ProtocolVariable.  # noqa: E501


        :return: The data_set_items of this ProtocolVariable.  # noqa: E501
        :rtype: list[ProtocolDataSetItem]
        """
        return self._data_set_items

    @data_set_items.setter
    def data_set_items(self, data_set_items):
        """Sets the data_set_items of this ProtocolVariable.


        :param data_set_items: The data_set_items of this ProtocolVariable.  # noqa: E501
        :type: list[ProtocolDataSetItem]
        """

        self._data_set_items = data_set_items

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
        if issubclass(ProtocolVariable, dict):
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
        if not isinstance(other, ProtocolVariable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtocolVariable):
            return True

        return self.to_dict() != other.to_dict()