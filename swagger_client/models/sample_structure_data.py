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


class SampleStructureData(object):
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
        'sample_id': 'int',
        'sample_type_name': 'str',
        'sample_meta_id': 'int',
        'name': 'str',
        'sample_meta_value': 'str',
        'location': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'quantity_type': 'str',
        'quantity_unit': 'str',
        'display_unit': 'str',
        'quantity_value': 'float',
        'created': 'datetime',
        'mdl_molfile': 'str',
        'mrv_document': 'str',
        'absolute_smiles': 'str',
        'unique_smiles': 'str'
    }

    attribute_map = {
        'sample_id': 'sampleID',
        'sample_type_name': 'sampleTypeName',
        'sample_meta_id': 'sampleMetaID',
        'name': 'name',
        'sample_meta_value': 'sampleMetaValue',
        'location': 'location',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'quantity_type': 'quantityType',
        'quantity_unit': 'quantityUnit',
        'display_unit': 'displayUnit',
        'quantity_value': 'quantityValue',
        'created': 'created',
        'mdl_molfile': 'mdlMolfile',
        'mrv_document': 'mrvDocument',
        'absolute_smiles': 'absoluteSmiles',
        'unique_smiles': 'uniqueSmiles'
    }

    def __init__(self, sample_id=None, sample_type_name=None, sample_meta_id=None, name=None, sample_meta_value=None, location=None, first_name=None, last_name=None, quantity_type=None, quantity_unit=None, display_unit=None, quantity_value=None, created=None, mdl_molfile=None, mrv_document=None, absolute_smiles=None, unique_smiles=None, _configuration=None):  # noqa: E501
        """SampleStructureData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sample_id = None
        self._sample_type_name = None
        self._sample_meta_id = None
        self._name = None
        self._sample_meta_value = None
        self._location = None
        self._first_name = None
        self._last_name = None
        self._quantity_type = None
        self._quantity_unit = None
        self._display_unit = None
        self._quantity_value = None
        self._created = None
        self._mdl_molfile = None
        self._mrv_document = None
        self._absolute_smiles = None
        self._unique_smiles = None
        self.discriminator = None

        if sample_id is not None:
            self.sample_id = sample_id
        if sample_type_name is not None:
            self.sample_type_name = sample_type_name
        if sample_meta_id is not None:
            self.sample_meta_id = sample_meta_id
        if name is not None:
            self.name = name
        if sample_meta_value is not None:
            self.sample_meta_value = sample_meta_value
        if location is not None:
            self.location = location
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if quantity_type is not None:
            self.quantity_type = quantity_type
        if quantity_unit is not None:
            self.quantity_unit = quantity_unit
        if display_unit is not None:
            self.display_unit = display_unit
        if quantity_value is not None:
            self.quantity_value = quantity_value
        if created is not None:
            self.created = created
        if mdl_molfile is not None:
            self.mdl_molfile = mdl_molfile
        if mrv_document is not None:
            self.mrv_document = mrv_document
        if absolute_smiles is not None:
            self.absolute_smiles = absolute_smiles
        if unique_smiles is not None:
            self.unique_smiles = unique_smiles

    @property
    def sample_id(self):
        """Gets the sample_id of this SampleStructureData.  # noqa: E501


        :return: The sample_id of this SampleStructureData.  # noqa: E501
        :rtype: int
        """
        return self._sample_id

    @sample_id.setter
    def sample_id(self, sample_id):
        """Sets the sample_id of this SampleStructureData.


        :param sample_id: The sample_id of this SampleStructureData.  # noqa: E501
        :type: int
        """

        self._sample_id = sample_id

    @property
    def sample_type_name(self):
        """Gets the sample_type_name of this SampleStructureData.  # noqa: E501


        :return: The sample_type_name of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._sample_type_name

    @sample_type_name.setter
    def sample_type_name(self, sample_type_name):
        """Sets the sample_type_name of this SampleStructureData.


        :param sample_type_name: The sample_type_name of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._sample_type_name = sample_type_name

    @property
    def sample_meta_id(self):
        """Gets the sample_meta_id of this SampleStructureData.  # noqa: E501


        :return: The sample_meta_id of this SampleStructureData.  # noqa: E501
        :rtype: int
        """
        return self._sample_meta_id

    @sample_meta_id.setter
    def sample_meta_id(self, sample_meta_id):
        """Sets the sample_meta_id of this SampleStructureData.


        :param sample_meta_id: The sample_meta_id of this SampleStructureData.  # noqa: E501
        :type: int
        """

        self._sample_meta_id = sample_meta_id

    @property
    def name(self):
        """Gets the name of this SampleStructureData.  # noqa: E501


        :return: The name of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SampleStructureData.


        :param name: The name of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sample_meta_value(self):
        """Gets the sample_meta_value of this SampleStructureData.  # noqa: E501


        :return: The sample_meta_value of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._sample_meta_value

    @sample_meta_value.setter
    def sample_meta_value(self, sample_meta_value):
        """Sets the sample_meta_value of this SampleStructureData.


        :param sample_meta_value: The sample_meta_value of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._sample_meta_value = sample_meta_value

    @property
    def location(self):
        """Gets the location of this SampleStructureData.  # noqa: E501


        :return: The location of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SampleStructureData.


        :param location: The location of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def first_name(self):
        """Gets the first_name of this SampleStructureData.  # noqa: E501


        :return: The first_name of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SampleStructureData.


        :param first_name: The first_name of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SampleStructureData.  # noqa: E501


        :return: The last_name of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SampleStructureData.


        :param last_name: The last_name of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def quantity_type(self):
        """Gets the quantity_type of this SampleStructureData.  # noqa: E501


        :return: The quantity_type of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._quantity_type

    @quantity_type.setter
    def quantity_type(self, quantity_type):
        """Sets the quantity_type of this SampleStructureData.


        :param quantity_type: The quantity_type of this SampleStructureData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Empty", "Volume", "Mass", "Number"]  # noqa: E501
        if (self._configuration.client_side_validation and
                quantity_type not in allowed_values):
            raise ValueError(
                "Invalid value for `quantity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quantity_type, allowed_values)
            )

        self._quantity_type = quantity_type

    @property
    def quantity_unit(self):
        """Gets the quantity_unit of this SampleStructureData.  # noqa: E501


        :return: The quantity_unit of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._quantity_unit

    @quantity_unit.setter
    def quantity_unit(self, quantity_unit):
        """Sets the quantity_unit of this SampleStructureData.


        :param quantity_unit: The quantity_unit of this SampleStructureData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Nothing", "Liter", "Gram", "Unit"]  # noqa: E501
        if (self._configuration.client_side_validation and
                quantity_unit not in allowed_values):
            raise ValueError(
                "Invalid value for `quantity_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(quantity_unit, allowed_values)
            )

        self._quantity_unit = quantity_unit

    @property
    def display_unit(self):
        """Gets the display_unit of this SampleStructureData.  # noqa: E501


        :return: The display_unit of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._display_unit

    @display_unit.setter
    def display_unit(self, display_unit):
        """Sets the display_unit of this SampleStructureData.


        :param display_unit: The display_unit of this SampleStructureData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Nothing", "Liter", "MilliLiter", "MicroLiter", "KiloGram", "Gram", "MilliGram", "MicroGram", "Unit"]  # noqa: E501
        if (self._configuration.client_side_validation and
                display_unit not in allowed_values):
            raise ValueError(
                "Invalid value for `display_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(display_unit, allowed_values)
            )

        self._display_unit = display_unit

    @property
    def quantity_value(self):
        """Gets the quantity_value of this SampleStructureData.  # noqa: E501


        :return: The quantity_value of this SampleStructureData.  # noqa: E501
        :rtype: float
        """
        return self._quantity_value

    @quantity_value.setter
    def quantity_value(self, quantity_value):
        """Sets the quantity_value of this SampleStructureData.


        :param quantity_value: The quantity_value of this SampleStructureData.  # noqa: E501
        :type: float
        """

        self._quantity_value = quantity_value

    @property
    def created(self):
        """Gets the created of this SampleStructureData.  # noqa: E501


        :return: The created of this SampleStructureData.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SampleStructureData.


        :param created: The created of this SampleStructureData.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def mdl_molfile(self):
        """Gets the mdl_molfile of this SampleStructureData.  # noqa: E501


        :return: The mdl_molfile of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._mdl_molfile

    @mdl_molfile.setter
    def mdl_molfile(self, mdl_molfile):
        """Sets the mdl_molfile of this SampleStructureData.


        :param mdl_molfile: The mdl_molfile of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._mdl_molfile = mdl_molfile

    @property
    def mrv_document(self):
        """Gets the mrv_document of this SampleStructureData.  # noqa: E501


        :return: The mrv_document of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._mrv_document

    @mrv_document.setter
    def mrv_document(self, mrv_document):
        """Sets the mrv_document of this SampleStructureData.


        :param mrv_document: The mrv_document of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._mrv_document = mrv_document

    @property
    def absolute_smiles(self):
        """Gets the absolute_smiles of this SampleStructureData.  # noqa: E501


        :return: The absolute_smiles of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._absolute_smiles

    @absolute_smiles.setter
    def absolute_smiles(self, absolute_smiles):
        """Sets the absolute_smiles of this SampleStructureData.


        :param absolute_smiles: The absolute_smiles of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._absolute_smiles = absolute_smiles

    @property
    def unique_smiles(self):
        """Gets the unique_smiles of this SampleStructureData.  # noqa: E501


        :return: The unique_smiles of this SampleStructureData.  # noqa: E501
        :rtype: str
        """
        return self._unique_smiles

    @unique_smiles.setter
    def unique_smiles(self, unique_smiles):
        """Sets the unique_smiles of this SampleStructureData.


        :param unique_smiles: The unique_smiles of this SampleStructureData.  # noqa: E501
        :type: str
        """

        self._unique_smiles = unique_smiles

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
        if issubclass(SampleStructureData, dict):
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
        if not isinstance(other, SampleStructureData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleStructureData):
            return True

        return self.to_dict() != other.to_dict()