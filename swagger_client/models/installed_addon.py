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


class InstalledAddon(object):
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
        'is_configured': 'bool',
        'approved': 'bool',
        'original': 'bool',
        'sdk_plugin_id': 'int',
        'name': 'str',
        'master_id': 'int',
        'categories': 'list[AddonCategory]',
        'description': 'str',
        'version': 'str',
        'default_configuration': 'str',
        'required_elab_version': 'str',
        'price': 'str',
        'currency': 'str',
        'root_var': 'str',
        'media': 'list[SDKMedia]',
        'is_public': 'bool',
        'scope': 'str',
        'active': 'bool',
        'has_config': 'bool',
        'has_file_monitoring_support': 'bool',
        'author': 'str',
        'website_link': 'str',
        'developer_mail': 'str',
        'documentation_link': 'str',
        'release_notes': 'str',
        'icon_class': 'str',
        'has_targets': 'bool',
        'background_color': 'str',
        'compatible_with': 'str',
        'consent_message': 'str',
        'capabilities': 'list[AddonCapability]',
        'license_types': 'list[AddonLicenseType]',
        'dependencies': 'list[Dependency]',
        'o_auth_configuration': 'OAuthConfiguration'
    }

    attribute_map = {
        'is_configured': 'isConfigured',
        'approved': 'approved',
        'original': 'original',
        'sdk_plugin_id': 'sdkPluginID',
        'name': 'name',
        'master_id': 'masterID',
        'categories': 'categories',
        'description': 'description',
        'version': 'version',
        'default_configuration': 'defaultConfiguration',
        'required_elab_version': 'requiredElabVersion',
        'price': 'price',
        'currency': 'currency',
        'root_var': 'rootVar',
        'media': 'media',
        'is_public': 'isPublic',
        'scope': 'scope',
        'active': 'active',
        'has_config': 'hasConfig',
        'has_file_monitoring_support': 'hasFileMonitoringSupport',
        'author': 'author',
        'website_link': 'websiteLink',
        'developer_mail': 'developerMail',
        'documentation_link': 'documentationLink',
        'release_notes': 'releaseNotes',
        'icon_class': 'iconClass',
        'has_targets': 'HasTargets',
        'background_color': 'backgroundColor',
        'compatible_with': 'compatibleWith',
        'consent_message': 'consentMessage',
        'capabilities': 'capabilities',
        'license_types': 'licenseTypes',
        'dependencies': 'dependencies',
        'o_auth_configuration': 'oAuthConfiguration'
    }

    def __init__(self, is_configured=None, approved=None, original=None, sdk_plugin_id=None, name=None, master_id=None, categories=None, description=None, version=None, default_configuration=None, required_elab_version=None, price=None, currency=None, root_var=None, media=None, is_public=None, scope=None, active=None, has_config=None, has_file_monitoring_support=None, author=None, website_link=None, developer_mail=None, documentation_link=None, release_notes=None, icon_class=None, has_targets=None, background_color=None, compatible_with=None, consent_message=None, capabilities=None, license_types=None, dependencies=None, o_auth_configuration=None, _configuration=None):  # noqa: E501
        """InstalledAddon - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_configured = None
        self._approved = None
        self._original = None
        self._sdk_plugin_id = None
        self._name = None
        self._master_id = None
        self._categories = None
        self._description = None
        self._version = None
        self._default_configuration = None
        self._required_elab_version = None
        self._price = None
        self._currency = None
        self._root_var = None
        self._media = None
        self._is_public = None
        self._scope = None
        self._active = None
        self._has_config = None
        self._has_file_monitoring_support = None
        self._author = None
        self._website_link = None
        self._developer_mail = None
        self._documentation_link = None
        self._release_notes = None
        self._icon_class = None
        self._has_targets = None
        self._background_color = None
        self._compatible_with = None
        self._consent_message = None
        self._capabilities = None
        self._license_types = None
        self._dependencies = None
        self._o_auth_configuration = None
        self.discriminator = None

        if is_configured is not None:
            self.is_configured = is_configured
        if approved is not None:
            self.approved = approved
        if original is not None:
            self.original = original
        if sdk_plugin_id is not None:
            self.sdk_plugin_id = sdk_plugin_id
        if name is not None:
            self.name = name
        if master_id is not None:
            self.master_id = master_id
        if categories is not None:
            self.categories = categories
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if default_configuration is not None:
            self.default_configuration = default_configuration
        if required_elab_version is not None:
            self.required_elab_version = required_elab_version
        if price is not None:
            self.price = price
        if currency is not None:
            self.currency = currency
        if root_var is not None:
            self.root_var = root_var
        if media is not None:
            self.media = media
        if is_public is not None:
            self.is_public = is_public
        if scope is not None:
            self.scope = scope
        if active is not None:
            self.active = active
        if has_config is not None:
            self.has_config = has_config
        if has_file_monitoring_support is not None:
            self.has_file_monitoring_support = has_file_monitoring_support
        if author is not None:
            self.author = author
        if website_link is not None:
            self.website_link = website_link
        if developer_mail is not None:
            self.developer_mail = developer_mail
        if documentation_link is not None:
            self.documentation_link = documentation_link
        if release_notes is not None:
            self.release_notes = release_notes
        if icon_class is not None:
            self.icon_class = icon_class
        if has_targets is not None:
            self.has_targets = has_targets
        if background_color is not None:
            self.background_color = background_color
        if compatible_with is not None:
            self.compatible_with = compatible_with
        if consent_message is not None:
            self.consent_message = consent_message
        if capabilities is not None:
            self.capabilities = capabilities
        if license_types is not None:
            self.license_types = license_types
        if dependencies is not None:
            self.dependencies = dependencies
        if o_auth_configuration is not None:
            self.o_auth_configuration = o_auth_configuration

    @property
    def is_configured(self):
        """Gets the is_configured of this InstalledAddon.  # noqa: E501


        :return: The is_configured of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._is_configured

    @is_configured.setter
    def is_configured(self, is_configured):
        """Sets the is_configured of this InstalledAddon.


        :param is_configured: The is_configured of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._is_configured = is_configured

    @property
    def approved(self):
        """Gets the approved of this InstalledAddon.  # noqa: E501


        :return: The approved of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this InstalledAddon.


        :param approved: The approved of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._approved = approved

    @property
    def original(self):
        """Gets the original of this InstalledAddon.  # noqa: E501


        :return: The original of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this InstalledAddon.


        :param original: The original of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._original = original

    @property
    def sdk_plugin_id(self):
        """Gets the sdk_plugin_id of this InstalledAddon.  # noqa: E501


        :return: The sdk_plugin_id of this InstalledAddon.  # noqa: E501
        :rtype: int
        """
        return self._sdk_plugin_id

    @sdk_plugin_id.setter
    def sdk_plugin_id(self, sdk_plugin_id):
        """Sets the sdk_plugin_id of this InstalledAddon.


        :param sdk_plugin_id: The sdk_plugin_id of this InstalledAddon.  # noqa: E501
        :type: int
        """

        self._sdk_plugin_id = sdk_plugin_id

    @property
    def name(self):
        """Gets the name of this InstalledAddon.  # noqa: E501


        :return: The name of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstalledAddon.


        :param name: The name of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def master_id(self):
        """Gets the master_id of this InstalledAddon.  # noqa: E501


        :return: The master_id of this InstalledAddon.  # noqa: E501
        :rtype: int
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        """Sets the master_id of this InstalledAddon.


        :param master_id: The master_id of this InstalledAddon.  # noqa: E501
        :type: int
        """

        self._master_id = master_id

    @property
    def categories(self):
        """Gets the categories of this InstalledAddon.  # noqa: E501


        :return: The categories of this InstalledAddon.  # noqa: E501
        :rtype: list[AddonCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this InstalledAddon.


        :param categories: The categories of this InstalledAddon.  # noqa: E501
        :type: list[AddonCategory]
        """

        self._categories = categories

    @property
    def description(self):
        """Gets the description of this InstalledAddon.  # noqa: E501


        :return: The description of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstalledAddon.


        :param description: The description of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this InstalledAddon.  # noqa: E501


        :return: The version of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstalledAddon.


        :param version: The version of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def default_configuration(self):
        """Gets the default_configuration of this InstalledAddon.  # noqa: E501


        :return: The default_configuration of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._default_configuration

    @default_configuration.setter
    def default_configuration(self, default_configuration):
        """Sets the default_configuration of this InstalledAddon.


        :param default_configuration: The default_configuration of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._default_configuration = default_configuration

    @property
    def required_elab_version(self):
        """Gets the required_elab_version of this InstalledAddon.  # noqa: E501


        :return: The required_elab_version of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._required_elab_version

    @required_elab_version.setter
    def required_elab_version(self, required_elab_version):
        """Sets the required_elab_version of this InstalledAddon.


        :param required_elab_version: The required_elab_version of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._required_elab_version = required_elab_version

    @property
    def price(self):
        """Gets the price of this InstalledAddon.  # noqa: E501


        :return: The price of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InstalledAddon.


        :param price: The price of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def currency(self):
        """Gets the currency of this InstalledAddon.  # noqa: E501


        :return: The currency of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InstalledAddon.


        :param currency: The currency of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def root_var(self):
        """Gets the root_var of this InstalledAddon.  # noqa: E501


        :return: The root_var of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._root_var

    @root_var.setter
    def root_var(self, root_var):
        """Sets the root_var of this InstalledAddon.


        :param root_var: The root_var of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._root_var = root_var

    @property
    def media(self):
        """Gets the media of this InstalledAddon.  # noqa: E501


        :return: The media of this InstalledAddon.  # noqa: E501
        :rtype: list[SDKMedia]
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this InstalledAddon.


        :param media: The media of this InstalledAddon.  # noqa: E501
        :type: list[SDKMedia]
        """

        self._media = media

    @property
    def is_public(self):
        """Gets the is_public of this InstalledAddon.  # noqa: E501


        :return: The is_public of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this InstalledAddon.


        :param is_public: The is_public of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def scope(self):
        """Gets the scope of this InstalledAddon.  # noqa: E501


        :return: The scope of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this InstalledAddon.


        :param scope: The scope of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def active(self):
        """Gets the active of this InstalledAddon.  # noqa: E501


        :return: The active of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InstalledAddon.


        :param active: The active of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def has_config(self):
        """Gets the has_config of this InstalledAddon.  # noqa: E501


        :return: The has_config of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._has_config

    @has_config.setter
    def has_config(self, has_config):
        """Sets the has_config of this InstalledAddon.


        :param has_config: The has_config of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._has_config = has_config

    @property
    def has_file_monitoring_support(self):
        """Gets the has_file_monitoring_support of this InstalledAddon.  # noqa: E501


        :return: The has_file_monitoring_support of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._has_file_monitoring_support

    @has_file_monitoring_support.setter
    def has_file_monitoring_support(self, has_file_monitoring_support):
        """Sets the has_file_monitoring_support of this InstalledAddon.


        :param has_file_monitoring_support: The has_file_monitoring_support of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._has_file_monitoring_support = has_file_monitoring_support

    @property
    def author(self):
        """Gets the author of this InstalledAddon.  # noqa: E501


        :return: The author of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this InstalledAddon.


        :param author: The author of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def website_link(self):
        """Gets the website_link of this InstalledAddon.  # noqa: E501


        :return: The website_link of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._website_link

    @website_link.setter
    def website_link(self, website_link):
        """Sets the website_link of this InstalledAddon.


        :param website_link: The website_link of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._website_link = website_link

    @property
    def developer_mail(self):
        """Gets the developer_mail of this InstalledAddon.  # noqa: E501


        :return: The developer_mail of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._developer_mail

    @developer_mail.setter
    def developer_mail(self, developer_mail):
        """Sets the developer_mail of this InstalledAddon.


        :param developer_mail: The developer_mail of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._developer_mail = developer_mail

    @property
    def documentation_link(self):
        """Gets the documentation_link of this InstalledAddon.  # noqa: E501


        :return: The documentation_link of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._documentation_link

    @documentation_link.setter
    def documentation_link(self, documentation_link):
        """Sets the documentation_link of this InstalledAddon.


        :param documentation_link: The documentation_link of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._documentation_link = documentation_link

    @property
    def release_notes(self):
        """Gets the release_notes of this InstalledAddon.  # noqa: E501


        :return: The release_notes of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this InstalledAddon.


        :param release_notes: The release_notes of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

    @property
    def icon_class(self):
        """Gets the icon_class of this InstalledAddon.  # noqa: E501


        :return: The icon_class of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._icon_class

    @icon_class.setter
    def icon_class(self, icon_class):
        """Sets the icon_class of this InstalledAddon.


        :param icon_class: The icon_class of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._icon_class = icon_class

    @property
    def has_targets(self):
        """Gets the has_targets of this InstalledAddon.  # noqa: E501


        :return: The has_targets of this InstalledAddon.  # noqa: E501
        :rtype: bool
        """
        return self._has_targets

    @has_targets.setter
    def has_targets(self, has_targets):
        """Sets the has_targets of this InstalledAddon.


        :param has_targets: The has_targets of this InstalledAddon.  # noqa: E501
        :type: bool
        """

        self._has_targets = has_targets

    @property
    def background_color(self):
        """Gets the background_color of this InstalledAddon.  # noqa: E501


        :return: The background_color of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this InstalledAddon.


        :param background_color: The background_color of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def compatible_with(self):
        """Gets the compatible_with of this InstalledAddon.  # noqa: E501


        :return: The compatible_with of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._compatible_with

    @compatible_with.setter
    def compatible_with(self, compatible_with):
        """Sets the compatible_with of this InstalledAddon.


        :param compatible_with: The compatible_with of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._compatible_with = compatible_with

    @property
    def consent_message(self):
        """Gets the consent_message of this InstalledAddon.  # noqa: E501


        :return: The consent_message of this InstalledAddon.  # noqa: E501
        :rtype: str
        """
        return self._consent_message

    @consent_message.setter
    def consent_message(self, consent_message):
        """Sets the consent_message of this InstalledAddon.


        :param consent_message: The consent_message of this InstalledAddon.  # noqa: E501
        :type: str
        """

        self._consent_message = consent_message

    @property
    def capabilities(self):
        """Gets the capabilities of this InstalledAddon.  # noqa: E501


        :return: The capabilities of this InstalledAddon.  # noqa: E501
        :rtype: list[AddonCapability]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this InstalledAddon.


        :param capabilities: The capabilities of this InstalledAddon.  # noqa: E501
        :type: list[AddonCapability]
        """

        self._capabilities = capabilities

    @property
    def license_types(self):
        """Gets the license_types of this InstalledAddon.  # noqa: E501


        :return: The license_types of this InstalledAddon.  # noqa: E501
        :rtype: list[AddonLicenseType]
        """
        return self._license_types

    @license_types.setter
    def license_types(self, license_types):
        """Sets the license_types of this InstalledAddon.


        :param license_types: The license_types of this InstalledAddon.  # noqa: E501
        :type: list[AddonLicenseType]
        """

        self._license_types = license_types

    @property
    def dependencies(self):
        """Gets the dependencies of this InstalledAddon.  # noqa: E501


        :return: The dependencies of this InstalledAddon.  # noqa: E501
        :rtype: list[Dependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this InstalledAddon.


        :param dependencies: The dependencies of this InstalledAddon.  # noqa: E501
        :type: list[Dependency]
        """

        self._dependencies = dependencies

    @property
    def o_auth_configuration(self):
        """Gets the o_auth_configuration of this InstalledAddon.  # noqa: E501


        :return: The o_auth_configuration of this InstalledAddon.  # noqa: E501
        :rtype: OAuthConfiguration
        """
        return self._o_auth_configuration

    @o_auth_configuration.setter
    def o_auth_configuration(self, o_auth_configuration):
        """Sets the o_auth_configuration of this InstalledAddon.


        :param o_auth_configuration: The o_auth_configuration of this InstalledAddon.  # noqa: E501
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
        if issubclass(InstalledAddon, dict):
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
        if not isinstance(other, InstalledAddon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstalledAddon):
            return True

        return self.to_dict() != other.to_dict()
