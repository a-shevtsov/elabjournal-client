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


class AddonPublish(object):
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
        'back_ground_color': 'str',
        'icon': 'HttpFile',
        'image': 'list[HttpFile]',
        'icon_class': 'str',
        'icon_type': 'str',
        'categories': 'list[str]',
        'scope': 'str',
        'script': 'str',
        'author_name': 'str',
        'default_configuration': 'str',
        'name': 'str',
        'root_var': 'str',
        'description': 'str',
        'price': 'str',
        'currency': 'str',
        'release_notes': 'str',
        'version': 'str',
        'required_elab_version': 'str',
        'consent_message': 'str',
        'website_link': 'str',
        'developer_mail': 'str',
        'documentation_link': 'str',
        'is_public': 'bool',
        'approved': 'bool',
        'sdk_plugin_id': 'int',
        'product': 'str',
        'dependencies': 'list[Dependency]',
        'capabilities': 'list[str]',
        'o_auth_configuration': 'OAuthConfiguration'
    }

    attribute_map = {
        'back_ground_color': 'BackGroundColor',
        'icon': 'Icon',
        'image': 'Image',
        'icon_class': 'IconClass',
        'icon_type': 'IconType',
        'categories': 'Categories',
        'scope': 'Scope',
        'script': 'Script',
        'author_name': 'AuthorName',
        'default_configuration': 'DefaultConfiguration',
        'name': 'Name',
        'root_var': 'RootVar',
        'description': 'Description',
        'price': 'Price',
        'currency': 'Currency',
        'release_notes': 'ReleaseNotes',
        'version': 'Version',
        'required_elab_version': 'RequiredElabVersion',
        'consent_message': 'ConsentMessage',
        'website_link': 'WebsiteLink',
        'developer_mail': 'DeveloperMail',
        'documentation_link': 'DocumentationLink',
        'is_public': 'IsPublic',
        'approved': 'approved',
        'sdk_plugin_id': 'SdkPluginID',
        'product': 'Product',
        'dependencies': 'Dependencies',
        'capabilities': 'Capabilities',
        'o_auth_configuration': 'OAuthConfiguration'
    }

    def __init__(self, back_ground_color=None, icon=None, image=None, icon_class=None, icon_type=None, categories=None, scope=None, script=None, author_name=None, default_configuration=None, name=None, root_var=None, description=None, price=None, currency=None, release_notes=None, version=None, required_elab_version=None, consent_message=None, website_link=None, developer_mail=None, documentation_link=None, is_public=None, approved=None, sdk_plugin_id=None, product=None, dependencies=None, capabilities=None, o_auth_configuration=None, _configuration=None):  # noqa: E501
        """AddonPublish - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._back_ground_color = None
        self._icon = None
        self._image = None
        self._icon_class = None
        self._icon_type = None
        self._categories = None
        self._scope = None
        self._script = None
        self._author_name = None
        self._default_configuration = None
        self._name = None
        self._root_var = None
        self._description = None
        self._price = None
        self._currency = None
        self._release_notes = None
        self._version = None
        self._required_elab_version = None
        self._consent_message = None
        self._website_link = None
        self._developer_mail = None
        self._documentation_link = None
        self._is_public = None
        self._approved = None
        self._sdk_plugin_id = None
        self._product = None
        self._dependencies = None
        self._capabilities = None
        self._o_auth_configuration = None
        self.discriminator = None

        if back_ground_color is not None:
            self.back_ground_color = back_ground_color
        if icon is not None:
            self.icon = icon
        if image is not None:
            self.image = image
        if icon_class is not None:
            self.icon_class = icon_class
        if icon_type is not None:
            self.icon_type = icon_type
        if categories is not None:
            self.categories = categories
        if scope is not None:
            self.scope = scope
        if script is not None:
            self.script = script
        if author_name is not None:
            self.author_name = author_name
        if default_configuration is not None:
            self.default_configuration = default_configuration
        if name is not None:
            self.name = name
        if root_var is not None:
            self.root_var = root_var
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if currency is not None:
            self.currency = currency
        if release_notes is not None:
            self.release_notes = release_notes
        if version is not None:
            self.version = version
        if required_elab_version is not None:
            self.required_elab_version = required_elab_version
        if consent_message is not None:
            self.consent_message = consent_message
        if website_link is not None:
            self.website_link = website_link
        if developer_mail is not None:
            self.developer_mail = developer_mail
        if documentation_link is not None:
            self.documentation_link = documentation_link
        if is_public is not None:
            self.is_public = is_public
        if approved is not None:
            self.approved = approved
        if sdk_plugin_id is not None:
            self.sdk_plugin_id = sdk_plugin_id
        if product is not None:
            self.product = product
        if dependencies is not None:
            self.dependencies = dependencies
        if capabilities is not None:
            self.capabilities = capabilities
        if o_auth_configuration is not None:
            self.o_auth_configuration = o_auth_configuration

    @property
    def back_ground_color(self):
        """Gets the back_ground_color of this AddonPublish.  # noqa: E501


        :return: The back_ground_color of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._back_ground_color

    @back_ground_color.setter
    def back_ground_color(self, back_ground_color):
        """Sets the back_ground_color of this AddonPublish.


        :param back_ground_color: The back_ground_color of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._back_ground_color = back_ground_color

    @property
    def icon(self):
        """Gets the icon of this AddonPublish.  # noqa: E501


        :return: The icon of this AddonPublish.  # noqa: E501
        :rtype: HttpFile
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this AddonPublish.


        :param icon: The icon of this AddonPublish.  # noqa: E501
        :type: HttpFile
        """

        self._icon = icon

    @property
    def image(self):
        """Gets the image of this AddonPublish.  # noqa: E501


        :return: The image of this AddonPublish.  # noqa: E501
        :rtype: list[HttpFile]
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AddonPublish.


        :param image: The image of this AddonPublish.  # noqa: E501
        :type: list[HttpFile]
        """

        self._image = image

    @property
    def icon_class(self):
        """Gets the icon_class of this AddonPublish.  # noqa: E501


        :return: The icon_class of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._icon_class

    @icon_class.setter
    def icon_class(self, icon_class):
        """Sets the icon_class of this AddonPublish.


        :param icon_class: The icon_class of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._icon_class = icon_class

    @property
    def icon_type(self):
        """Gets the icon_type of this AddonPublish.  # noqa: E501


        :return: The icon_type of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._icon_type

    @icon_type.setter
    def icon_type(self, icon_type):
        """Sets the icon_type of this AddonPublish.


        :param icon_type: The icon_type of this AddonPublish.  # noqa: E501
        :type: str
        """
        allowed_values = ["IMAGE", "FONT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                icon_type not in allowed_values):
            raise ValueError(
                "Invalid value for `icon_type` ({0}), must be one of {1}"  # noqa: E501
                .format(icon_type, allowed_values)
            )

        self._icon_type = icon_type

    @property
    def categories(self):
        """Gets the categories of this AddonPublish.  # noqa: E501


        :return: The categories of this AddonPublish.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this AddonPublish.


        :param categories: The categories of this AddonPublish.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def scope(self):
        """Gets the scope of this AddonPublish.  # noqa: E501


        :return: The scope of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this AddonPublish.


        :param scope: The scope of this AddonPublish.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEM", "INSTITUTE", "GROUP", "USER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                scope not in allowed_values):
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def script(self):
        """Gets the script of this AddonPublish.  # noqa: E501


        :return: The script of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this AddonPublish.


        :param script: The script of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def author_name(self):
        """Gets the author_name of this AddonPublish.  # noqa: E501


        :return: The author_name of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this AddonPublish.


        :param author_name: The author_name of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._author_name = author_name

    @property
    def default_configuration(self):
        """Gets the default_configuration of this AddonPublish.  # noqa: E501


        :return: The default_configuration of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._default_configuration

    @default_configuration.setter
    def default_configuration(self, default_configuration):
        """Sets the default_configuration of this AddonPublish.


        :param default_configuration: The default_configuration of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._default_configuration = default_configuration

    @property
    def name(self):
        """Gets the name of this AddonPublish.  # noqa: E501


        :return: The name of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddonPublish.


        :param name: The name of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def root_var(self):
        """Gets the root_var of this AddonPublish.  # noqa: E501


        :return: The root_var of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._root_var

    @root_var.setter
    def root_var(self, root_var):
        """Sets the root_var of this AddonPublish.


        :param root_var: The root_var of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._root_var = root_var

    @property
    def description(self):
        """Gets the description of this AddonPublish.  # noqa: E501


        :return: The description of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddonPublish.


        :param description: The description of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def price(self):
        """Gets the price of this AddonPublish.  # noqa: E501


        :return: The price of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this AddonPublish.


        :param price: The price of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def currency(self):
        """Gets the currency of this AddonPublish.  # noqa: E501


        :return: The currency of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AddonPublish.


        :param currency: The currency of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def release_notes(self):
        """Gets the release_notes of this AddonPublish.  # noqa: E501


        :return: The release_notes of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this AddonPublish.


        :param release_notes: The release_notes of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

    @property
    def version(self):
        """Gets the version of this AddonPublish.  # noqa: E501


        :return: The version of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AddonPublish.


        :param version: The version of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def required_elab_version(self):
        """Gets the required_elab_version of this AddonPublish.  # noqa: E501


        :return: The required_elab_version of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._required_elab_version

    @required_elab_version.setter
    def required_elab_version(self, required_elab_version):
        """Sets the required_elab_version of this AddonPublish.


        :param required_elab_version: The required_elab_version of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._required_elab_version = required_elab_version

    @property
    def consent_message(self):
        """Gets the consent_message of this AddonPublish.  # noqa: E501


        :return: The consent_message of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._consent_message

    @consent_message.setter
    def consent_message(self, consent_message):
        """Sets the consent_message of this AddonPublish.


        :param consent_message: The consent_message of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._consent_message = consent_message

    @property
    def website_link(self):
        """Gets the website_link of this AddonPublish.  # noqa: E501


        :return: The website_link of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._website_link

    @website_link.setter
    def website_link(self, website_link):
        """Sets the website_link of this AddonPublish.


        :param website_link: The website_link of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._website_link = website_link

    @property
    def developer_mail(self):
        """Gets the developer_mail of this AddonPublish.  # noqa: E501


        :return: The developer_mail of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._developer_mail

    @developer_mail.setter
    def developer_mail(self, developer_mail):
        """Sets the developer_mail of this AddonPublish.


        :param developer_mail: The developer_mail of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._developer_mail = developer_mail

    @property
    def documentation_link(self):
        """Gets the documentation_link of this AddonPublish.  # noqa: E501


        :return: The documentation_link of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._documentation_link

    @documentation_link.setter
    def documentation_link(self, documentation_link):
        """Sets the documentation_link of this AddonPublish.


        :param documentation_link: The documentation_link of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._documentation_link = documentation_link

    @property
    def is_public(self):
        """Gets the is_public of this AddonPublish.  # noqa: E501


        :return: The is_public of this AddonPublish.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this AddonPublish.


        :param is_public: The is_public of this AddonPublish.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def approved(self):
        """Gets the approved of this AddonPublish.  # noqa: E501


        :return: The approved of this AddonPublish.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this AddonPublish.


        :param approved: The approved of this AddonPublish.  # noqa: E501
        :type: bool
        """

        self._approved = approved

    @property
    def sdk_plugin_id(self):
        """Gets the sdk_plugin_id of this AddonPublish.  # noqa: E501


        :return: The sdk_plugin_id of this AddonPublish.  # noqa: E501
        :rtype: int
        """
        return self._sdk_plugin_id

    @sdk_plugin_id.setter
    def sdk_plugin_id(self, sdk_plugin_id):
        """Sets the sdk_plugin_id of this AddonPublish.


        :param sdk_plugin_id: The sdk_plugin_id of this AddonPublish.  # noqa: E501
        :type: int
        """

        self._sdk_plugin_id = sdk_plugin_id

    @property
    def product(self):
        """Gets the product of this AddonPublish.  # noqa: E501


        :return: The product of this AddonPublish.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this AddonPublish.


        :param product: The product of this AddonPublish.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def dependencies(self):
        """Gets the dependencies of this AddonPublish.  # noqa: E501


        :return: The dependencies of this AddonPublish.  # noqa: E501
        :rtype: list[Dependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this AddonPublish.


        :param dependencies: The dependencies of this AddonPublish.  # noqa: E501
        :type: list[Dependency]
        """

        self._dependencies = dependencies

    @property
    def capabilities(self):
        """Gets the capabilities of this AddonPublish.  # noqa: E501


        :return: The capabilities of this AddonPublish.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this AddonPublish.


        :param capabilities: The capabilities of this AddonPublish.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    @property
    def o_auth_configuration(self):
        """Gets the o_auth_configuration of this AddonPublish.  # noqa: E501


        :return: The o_auth_configuration of this AddonPublish.  # noqa: E501
        :rtype: OAuthConfiguration
        """
        return self._o_auth_configuration

    @o_auth_configuration.setter
    def o_auth_configuration(self, o_auth_configuration):
        """Sets the o_auth_configuration of this AddonPublish.


        :param o_auth_configuration: The o_auth_configuration of this AddonPublish.  # noqa: E501
        :type: OAuthConfiguration
        """

        self._o_auth_configuration = o_auth_configuration

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
        if issubclass(AddonPublish, dict):
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
        if not isinstance(other, AddonPublish):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddonPublish):
            return True

        return self.to_dict() != other.to_dict()
