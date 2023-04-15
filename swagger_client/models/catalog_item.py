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


class CatalogItem(object):
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
        'catalog_item_id': 'int',
        'group_id': 'int',
        'supplier_id': 'int',
        'supplier': 'Supplier',
        'catalog_number': 'str',
        'price': 'float',
        'amount': 'float',
        'quantity_type': 'str',
        'name': 'str',
        'catalog_name': 'str',
        'currency': 'str',
        'details': 'str',
        'barcode': 'str',
        'unit_short': 'str',
        'display_unit': 'str',
        'currency_symbol': 'str',
        'content': 'str',
        'product_image': 'str'
    }

    attribute_map = {
        'catalog_item_id': 'catalogItemID',
        'group_id': 'groupID',
        'supplier_id': 'supplierID',
        'supplier': 'supplier',
        'catalog_number': 'catalogNumber',
        'price': 'price',
        'amount': 'amount',
        'quantity_type': 'quantityType',
        'name': 'name',
        'catalog_name': 'catalogName',
        'currency': 'currency',
        'details': 'details',
        'barcode': 'barcode',
        'unit_short': 'unitShort',
        'display_unit': 'displayUnit',
        'currency_symbol': 'currencySymbol',
        'content': 'content',
        'product_image': 'productImage'
    }

    def __init__(self, catalog_item_id=None, group_id=None, supplier_id=None, supplier=None, catalog_number=None, price=None, amount=None, quantity_type=None, name=None, catalog_name=None, currency=None, details=None, barcode=None, unit_short=None, display_unit=None, currency_symbol=None, content=None, product_image=None, _configuration=None):  # noqa: E501
        """CatalogItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._catalog_item_id = None
        self._group_id = None
        self._supplier_id = None
        self._supplier = None
        self._catalog_number = None
        self._price = None
        self._amount = None
        self._quantity_type = None
        self._name = None
        self._catalog_name = None
        self._currency = None
        self._details = None
        self._barcode = None
        self._unit_short = None
        self._display_unit = None
        self._currency_symbol = None
        self._content = None
        self._product_image = None
        self.discriminator = None

        if catalog_item_id is not None:
            self.catalog_item_id = catalog_item_id
        if group_id is not None:
            self.group_id = group_id
        if supplier_id is not None:
            self.supplier_id = supplier_id
        if supplier is not None:
            self.supplier = supplier
        if catalog_number is not None:
            self.catalog_number = catalog_number
        if price is not None:
            self.price = price
        if amount is not None:
            self.amount = amount
        if quantity_type is not None:
            self.quantity_type = quantity_type
        if name is not None:
            self.name = name
        if catalog_name is not None:
            self.catalog_name = catalog_name
        if currency is not None:
            self.currency = currency
        if details is not None:
            self.details = details
        if barcode is not None:
            self.barcode = barcode
        if unit_short is not None:
            self.unit_short = unit_short
        if display_unit is not None:
            self.display_unit = display_unit
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if content is not None:
            self.content = content
        if product_image is not None:
            self.product_image = product_image

    @property
    def catalog_item_id(self):
        """Gets the catalog_item_id of this CatalogItem.  # noqa: E501


        :return: The catalog_item_id of this CatalogItem.  # noqa: E501
        :rtype: int
        """
        return self._catalog_item_id

    @catalog_item_id.setter
    def catalog_item_id(self, catalog_item_id):
        """Sets the catalog_item_id of this CatalogItem.


        :param catalog_item_id: The catalog_item_id of this CatalogItem.  # noqa: E501
        :type: int
        """

        self._catalog_item_id = catalog_item_id

    @property
    def group_id(self):
        """Gets the group_id of this CatalogItem.  # noqa: E501


        :return: The group_id of this CatalogItem.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CatalogItem.


        :param group_id: The group_id of this CatalogItem.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def supplier_id(self):
        """Gets the supplier_id of this CatalogItem.  # noqa: E501


        :return: The supplier_id of this CatalogItem.  # noqa: E501
        :rtype: int
        """
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        """Sets the supplier_id of this CatalogItem.


        :param supplier_id: The supplier_id of this CatalogItem.  # noqa: E501
        :type: int
        """

        self._supplier_id = supplier_id

    @property
    def supplier(self):
        """Gets the supplier of this CatalogItem.  # noqa: E501


        :return: The supplier of this CatalogItem.  # noqa: E501
        :rtype: Supplier
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this CatalogItem.


        :param supplier: The supplier of this CatalogItem.  # noqa: E501
        :type: Supplier
        """

        self._supplier = supplier

    @property
    def catalog_number(self):
        """Gets the catalog_number of this CatalogItem.  # noqa: E501


        :return: The catalog_number of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._catalog_number

    @catalog_number.setter
    def catalog_number(self, catalog_number):
        """Sets the catalog_number of this CatalogItem.


        :param catalog_number: The catalog_number of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._catalog_number = catalog_number

    @property
    def price(self):
        """Gets the price of this CatalogItem.  # noqa: E501


        :return: The price of this CatalogItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CatalogItem.


        :param price: The price of this CatalogItem.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def amount(self):
        """Gets the amount of this CatalogItem.  # noqa: E501


        :return: The amount of this CatalogItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CatalogItem.


        :param amount: The amount of this CatalogItem.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def quantity_type(self):
        """Gets the quantity_type of this CatalogItem.  # noqa: E501


        :return: The quantity_type of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._quantity_type

    @quantity_type.setter
    def quantity_type(self, quantity_type):
        """Sets the quantity_type of this CatalogItem.


        :param quantity_type: The quantity_type of this CatalogItem.  # noqa: E501
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
    def name(self):
        """Gets the name of this CatalogItem.  # noqa: E501


        :return: The name of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CatalogItem.


        :param name: The name of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def catalog_name(self):
        """Gets the catalog_name of this CatalogItem.  # noqa: E501


        :return: The catalog_name of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this CatalogItem.


        :param catalog_name: The catalog_name of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._catalog_name = catalog_name

    @property
    def currency(self):
        """Gets the currency of this CatalogItem.  # noqa: E501


        :return: The currency of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CatalogItem.


        :param currency: The currency of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def details(self):
        """Gets the details of this CatalogItem.  # noqa: E501


        :return: The details of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this CatalogItem.


        :param details: The details of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def barcode(self):
        """Gets the barcode of this CatalogItem.  # noqa: E501


        :return: The barcode of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this CatalogItem.


        :param barcode: The barcode of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._barcode = barcode

    @property
    def unit_short(self):
        """Gets the unit_short of this CatalogItem.  # noqa: E501


        :return: The unit_short of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._unit_short

    @unit_short.setter
    def unit_short(self, unit_short):
        """Sets the unit_short of this CatalogItem.


        :param unit_short: The unit_short of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._unit_short = unit_short

    @property
    def display_unit(self):
        """Gets the display_unit of this CatalogItem.  # noqa: E501


        :return: The display_unit of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._display_unit

    @display_unit.setter
    def display_unit(self, display_unit):
        """Sets the display_unit of this CatalogItem.


        :param display_unit: The display_unit of this CatalogItem.  # noqa: E501
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
    def currency_symbol(self):
        """Gets the currency_symbol of this CatalogItem.  # noqa: E501


        :return: The currency_symbol of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this CatalogItem.


        :param currency_symbol: The currency_symbol of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def content(self):
        """Gets the content of this CatalogItem.  # noqa: E501


        :return: The content of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CatalogItem.


        :param content: The content of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def product_image(self):
        """Gets the product_image of this CatalogItem.  # noqa: E501


        :return: The product_image of this CatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._product_image

    @product_image.setter
    def product_image(self, product_image):
        """Sets the product_image of this CatalogItem.


        :param product_image: The product_image of this CatalogItem.  # noqa: E501
        :type: str
        """

        self._product_image = product_image

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
        if issubclass(CatalogItem, dict):
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
        if not isinstance(other, CatalogItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogItem):
            return True

        return self.to_dict() != other.to_dict()