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


class ShoppingItem(object):
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
        'shopping_item_id': 'int',
        'subgroup_id': 'int',
        'user_id': 'int',
        'date_entered': 'datetime',
        'date_ordered': 'datetime',
        'date_received': 'datetime',
        'date_completed': 'datetime',
        'sample_id': 'int',
        'sample_type_id': 'int',
        'shop_item_type': 'str',
        'foreign_id': 'int',
        'catalog_item_id': 'int',
        'notify_user': 'bool',
        'amount': 'int',
        'status': 'str'
    }

    attribute_map = {
        'shopping_item_id': 'shoppingItemID',
        'subgroup_id': 'subgroupID',
        'user_id': 'userID',
        'date_entered': 'dateEntered',
        'date_ordered': 'dateOrdered',
        'date_received': 'dateReceived',
        'date_completed': 'dateCompleted',
        'sample_id': 'sampleID',
        'sample_type_id': 'sampleTypeID',
        'shop_item_type': 'shopItemType',
        'foreign_id': 'foreignID',
        'catalog_item_id': 'catalogItemID',
        'notify_user': 'notifyUser',
        'amount': 'amount',
        'status': 'status'
    }

    def __init__(self, shopping_item_id=None, subgroup_id=None, user_id=None, date_entered=None, date_ordered=None, date_received=None, date_completed=None, sample_id=None, sample_type_id=None, shop_item_type=None, foreign_id=None, catalog_item_id=None, notify_user=None, amount=None, status=None, _configuration=None):  # noqa: E501
        """ShoppingItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._shopping_item_id = None
        self._subgroup_id = None
        self._user_id = None
        self._date_entered = None
        self._date_ordered = None
        self._date_received = None
        self._date_completed = None
        self._sample_id = None
        self._sample_type_id = None
        self._shop_item_type = None
        self._foreign_id = None
        self._catalog_item_id = None
        self._notify_user = None
        self._amount = None
        self._status = None
        self.discriminator = None

        if shopping_item_id is not None:
            self.shopping_item_id = shopping_item_id
        if subgroup_id is not None:
            self.subgroup_id = subgroup_id
        if user_id is not None:
            self.user_id = user_id
        if date_entered is not None:
            self.date_entered = date_entered
        if date_ordered is not None:
            self.date_ordered = date_ordered
        if date_received is not None:
            self.date_received = date_received
        if date_completed is not None:
            self.date_completed = date_completed
        if sample_id is not None:
            self.sample_id = sample_id
        if sample_type_id is not None:
            self.sample_type_id = sample_type_id
        if shop_item_type is not None:
            self.shop_item_type = shop_item_type
        if foreign_id is not None:
            self.foreign_id = foreign_id
        self.catalog_item_id = catalog_item_id
        if notify_user is not None:
            self.notify_user = notify_user
        self.amount = amount
        if status is not None:
            self.status = status

    @property
    def shopping_item_id(self):
        """Gets the shopping_item_id of this ShoppingItem.  # noqa: E501


        :return: The shopping_item_id of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._shopping_item_id

    @shopping_item_id.setter
    def shopping_item_id(self, shopping_item_id):
        """Sets the shopping_item_id of this ShoppingItem.


        :param shopping_item_id: The shopping_item_id of this ShoppingItem.  # noqa: E501
        :type: int
        """

        self._shopping_item_id = shopping_item_id

    @property
    def subgroup_id(self):
        """Gets the subgroup_id of this ShoppingItem.  # noqa: E501


        :return: The subgroup_id of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._subgroup_id

    @subgroup_id.setter
    def subgroup_id(self, subgroup_id):
        """Sets the subgroup_id of this ShoppingItem.


        :param subgroup_id: The subgroup_id of this ShoppingItem.  # noqa: E501
        :type: int
        """

        self._subgroup_id = subgroup_id

    @property
    def user_id(self):
        """Gets the user_id of this ShoppingItem.  # noqa: E501


        :return: The user_id of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShoppingItem.


        :param user_id: The user_id of this ShoppingItem.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def date_entered(self):
        """Gets the date_entered of this ShoppingItem.  # noqa: E501


        :return: The date_entered of this ShoppingItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_entered

    @date_entered.setter
    def date_entered(self, date_entered):
        """Sets the date_entered of this ShoppingItem.


        :param date_entered: The date_entered of this ShoppingItem.  # noqa: E501
        :type: datetime
        """

        self._date_entered = date_entered

    @property
    def date_ordered(self):
        """Gets the date_ordered of this ShoppingItem.  # noqa: E501


        :return: The date_ordered of this ShoppingItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_ordered

    @date_ordered.setter
    def date_ordered(self, date_ordered):
        """Sets the date_ordered of this ShoppingItem.


        :param date_ordered: The date_ordered of this ShoppingItem.  # noqa: E501
        :type: datetime
        """

        self._date_ordered = date_ordered

    @property
    def date_received(self):
        """Gets the date_received of this ShoppingItem.  # noqa: E501


        :return: The date_received of this ShoppingItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_received

    @date_received.setter
    def date_received(self, date_received):
        """Sets the date_received of this ShoppingItem.


        :param date_received: The date_received of this ShoppingItem.  # noqa: E501
        :type: datetime
        """

        self._date_received = date_received

    @property
    def date_completed(self):
        """Gets the date_completed of this ShoppingItem.  # noqa: E501


        :return: The date_completed of this ShoppingItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """Sets the date_completed of this ShoppingItem.


        :param date_completed: The date_completed of this ShoppingItem.  # noqa: E501
        :type: datetime
        """

        self._date_completed = date_completed

    @property
    def sample_id(self):
        """Gets the sample_id of this ShoppingItem.  # noqa: E501


        :return: The sample_id of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._sample_id

    @sample_id.setter
    def sample_id(self, sample_id):
        """Sets the sample_id of this ShoppingItem.


        :param sample_id: The sample_id of this ShoppingItem.  # noqa: E501
        :type: int
        """

        self._sample_id = sample_id

    @property
    def sample_type_id(self):
        """Gets the sample_type_id of this ShoppingItem.  # noqa: E501


        :return: The sample_type_id of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._sample_type_id

    @sample_type_id.setter
    def sample_type_id(self, sample_type_id):
        """Sets the sample_type_id of this ShoppingItem.


        :param sample_type_id: The sample_type_id of this ShoppingItem.  # noqa: E501
        :type: int
        """

        self._sample_type_id = sample_type_id

    @property
    def shop_item_type(self):
        """Gets the shop_item_type of this ShoppingItem.  # noqa: E501


        :return: The shop_item_type of this ShoppingItem.  # noqa: E501
        :rtype: str
        """
        return self._shop_item_type

    @shop_item_type.setter
    def shop_item_type(self, shop_item_type):
        """Sets the shop_item_type of this ShoppingItem.


        :param shop_item_type: The shop_item_type of this ShoppingItem.  # noqa: E501
        :type: str
        """

        self._shop_item_type = shop_item_type

    @property
    def foreign_id(self):
        """Gets the foreign_id of this ShoppingItem.  # noqa: E501


        :return: The foreign_id of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._foreign_id

    @foreign_id.setter
    def foreign_id(self, foreign_id):
        """Sets the foreign_id of this ShoppingItem.


        :param foreign_id: The foreign_id of this ShoppingItem.  # noqa: E501
        :type: int
        """

        self._foreign_id = foreign_id

    @property
    def catalog_item_id(self):
        """Gets the catalog_item_id of this ShoppingItem.  # noqa: E501


        :return: The catalog_item_id of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._catalog_item_id

    @catalog_item_id.setter
    def catalog_item_id(self, catalog_item_id):
        """Sets the catalog_item_id of this ShoppingItem.


        :param catalog_item_id: The catalog_item_id of this ShoppingItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and catalog_item_id is None:
            raise ValueError("Invalid value for `catalog_item_id`, must not be `None`")  # noqa: E501

        self._catalog_item_id = catalog_item_id

    @property
    def notify_user(self):
        """Gets the notify_user of this ShoppingItem.  # noqa: E501


        :return: The notify_user of this ShoppingItem.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this ShoppingItem.


        :param notify_user: The notify_user of this ShoppingItem.  # noqa: E501
        :type: bool
        """

        self._notify_user = notify_user

    @property
    def amount(self):
        """Gets the amount of this ShoppingItem.  # noqa: E501


        :return: The amount of this ShoppingItem.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ShoppingItem.


        :param amount: The amount of this ShoppingItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def status(self):
        """Gets the status of this ShoppingItem.  # noqa: E501


        :return: The status of this ShoppingItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShoppingItem.


        :param status: The status of this ShoppingItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "ORDERED", "RECEIVED", "COMPLETED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ShoppingItem, dict):
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
        if not isinstance(other, ShoppingItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShoppingItem):
            return True

        return self.to_dict() != other.to_dict()