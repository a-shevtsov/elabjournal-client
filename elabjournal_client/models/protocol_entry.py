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


class ProtocolEntry(object):
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
        'prot_id': 'int',
        'storage_id': 'int',
        'created': 'datetime',
        'prot_version_id': 'int',
        'version': 'int',
        'draft': 'bool',
        'is_public': 'bool',
        'deleted': 'bool',
        'name': 'str',
        'description': 'str',
        'user_id': 'int',
        'author_id': 'int',
        'author': 'str',
        'group_id': 'int',
        'subgroup_id': 'int',
        'category_id': 'int',
        'category': 'str',
        'view_count': 'int',
        'rating': 'int',
        'num_steps': 'int',
        'group_share_count': 'int',
        'steps': 'list[ProtocolStep]',
        'vars': 'list[ProtocolVariable]',
        'app_view_url': 'str',
        'signing_status': 'SigningStatusDTO'
    }

    attribute_map = {
        'prot_id': 'protID',
        'storage_id': 'storageID',
        'created': 'created',
        'prot_version_id': 'protVersionID',
        'version': 'version',
        'draft': 'draft',
        'is_public': 'isPublic',
        'deleted': 'deleted',
        'name': 'name',
        'description': 'description',
        'user_id': 'userID',
        'author_id': 'authorID',
        'author': 'author',
        'group_id': 'groupID',
        'subgroup_id': 'subgroupID',
        'category_id': 'categoryID',
        'category': 'category',
        'view_count': 'viewCount',
        'rating': 'rating',
        'num_steps': 'numSteps',
        'group_share_count': 'groupShareCount',
        'steps': 'steps',
        'vars': 'vars',
        'app_view_url': 'appViewURL',
        'signing_status': 'signingStatus'
    }

    def __init__(self, prot_id=None, storage_id=None, created=None, prot_version_id=None, version=None, draft=None, is_public=None, deleted=None, name=None, description=None, user_id=None, author_id=None, author=None, group_id=None, subgroup_id=None, category_id=None, category=None, view_count=None, rating=None, num_steps=None, group_share_count=None, steps=None, vars=None, app_view_url=None, signing_status=None, _configuration=None):  # noqa: E501
        """ProtocolEntry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._prot_id = None
        self._storage_id = None
        self._created = None
        self._prot_version_id = None
        self._version = None
        self._draft = None
        self._is_public = None
        self._deleted = None
        self._name = None
        self._description = None
        self._user_id = None
        self._author_id = None
        self._author = None
        self._group_id = None
        self._subgroup_id = None
        self._category_id = None
        self._category = None
        self._view_count = None
        self._rating = None
        self._num_steps = None
        self._group_share_count = None
        self._steps = None
        self._vars = None
        self._app_view_url = None
        self._signing_status = None
        self.discriminator = None

        if prot_id is not None:
            self.prot_id = prot_id
        if storage_id is not None:
            self.storage_id = storage_id
        if created is not None:
            self.created = created
        if prot_version_id is not None:
            self.prot_version_id = prot_version_id
        if version is not None:
            self.version = version
        if draft is not None:
            self.draft = draft
        if is_public is not None:
            self.is_public = is_public
        if deleted is not None:
            self.deleted = deleted
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if user_id is not None:
            self.user_id = user_id
        if author_id is not None:
            self.author_id = author_id
        if author is not None:
            self.author = author
        if group_id is not None:
            self.group_id = group_id
        if subgroup_id is not None:
            self.subgroup_id = subgroup_id
        if category_id is not None:
            self.category_id = category_id
        if category is not None:
            self.category = category
        if view_count is not None:
            self.view_count = view_count
        if rating is not None:
            self.rating = rating
        if num_steps is not None:
            self.num_steps = num_steps
        if group_share_count is not None:
            self.group_share_count = group_share_count
        if steps is not None:
            self.steps = steps
        if vars is not None:
            self.vars = vars
        if app_view_url is not None:
            self.app_view_url = app_view_url
        if signing_status is not None:
            self.signing_status = signing_status

    @property
    def prot_id(self):
        """Gets the prot_id of this ProtocolEntry.  # noqa: E501


        :return: The prot_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._prot_id

    @prot_id.setter
    def prot_id(self, prot_id):
        """Sets the prot_id of this ProtocolEntry.


        :param prot_id: The prot_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._prot_id = prot_id

    @property
    def storage_id(self):
        """Gets the storage_id of this ProtocolEntry.  # noqa: E501


        :return: The storage_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this ProtocolEntry.


        :param storage_id: The storage_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._storage_id = storage_id

    @property
    def created(self):
        """Gets the created of this ProtocolEntry.  # noqa: E501


        :return: The created of this ProtocolEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ProtocolEntry.


        :param created: The created of this ProtocolEntry.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def prot_version_id(self):
        """Gets the prot_version_id of this ProtocolEntry.  # noqa: E501


        :return: The prot_version_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._prot_version_id

    @prot_version_id.setter
    def prot_version_id(self, prot_version_id):
        """Sets the prot_version_id of this ProtocolEntry.


        :param prot_version_id: The prot_version_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._prot_version_id = prot_version_id

    @property
    def version(self):
        """Gets the version of this ProtocolEntry.  # noqa: E501


        :return: The version of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProtocolEntry.


        :param version: The version of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def draft(self):
        """Gets the draft of this ProtocolEntry.  # noqa: E501


        :return: The draft of this ProtocolEntry.  # noqa: E501
        :rtype: bool
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this ProtocolEntry.


        :param draft: The draft of this ProtocolEntry.  # noqa: E501
        :type: bool
        """

        self._draft = draft

    @property
    def is_public(self):
        """Gets the is_public of this ProtocolEntry.  # noqa: E501


        :return: The is_public of this ProtocolEntry.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ProtocolEntry.


        :param is_public: The is_public of this ProtocolEntry.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def deleted(self):
        """Gets the deleted of this ProtocolEntry.  # noqa: E501


        :return: The deleted of this ProtocolEntry.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ProtocolEntry.


        :param deleted: The deleted of this ProtocolEntry.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def name(self):
        """Gets the name of this ProtocolEntry.  # noqa: E501


        :return: The name of this ProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtocolEntry.


        :param name: The name of this ProtocolEntry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProtocolEntry.  # noqa: E501


        :return: The description of this ProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProtocolEntry.


        :param description: The description of this ProtocolEntry.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def user_id(self):
        """Gets the user_id of this ProtocolEntry.  # noqa: E501


        :return: The user_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ProtocolEntry.


        :param user_id: The user_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def author_id(self):
        """Gets the author_id of this ProtocolEntry.  # noqa: E501


        :return: The author_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this ProtocolEntry.


        :param author_id: The author_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._author_id = author_id

    @property
    def author(self):
        """Gets the author of this ProtocolEntry.  # noqa: E501


        :return: The author of this ProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ProtocolEntry.


        :param author: The author of this ProtocolEntry.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def group_id(self):
        """Gets the group_id of this ProtocolEntry.  # noqa: E501


        :return: The group_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ProtocolEntry.


        :param group_id: The group_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def subgroup_id(self):
        """Gets the subgroup_id of this ProtocolEntry.  # noqa: E501


        :return: The subgroup_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._subgroup_id

    @subgroup_id.setter
    def subgroup_id(self, subgroup_id):
        """Sets the subgroup_id of this ProtocolEntry.


        :param subgroup_id: The subgroup_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._subgroup_id = subgroup_id

    @property
    def category_id(self):
        """Gets the category_id of this ProtocolEntry.  # noqa: E501


        :return: The category_id of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ProtocolEntry.


        :param category_id: The category_id of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def category(self):
        """Gets the category of this ProtocolEntry.  # noqa: E501


        :return: The category of this ProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ProtocolEntry.


        :param category: The category of this ProtocolEntry.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def view_count(self):
        """Gets the view_count of this ProtocolEntry.  # noqa: E501


        :return: The view_count of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this ProtocolEntry.


        :param view_count: The view_count of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._view_count = view_count

    @property
    def rating(self):
        """Gets the rating of this ProtocolEntry.  # noqa: E501


        :return: The rating of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this ProtocolEntry.


        :param rating: The rating of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._rating = rating

    @property
    def num_steps(self):
        """Gets the num_steps of this ProtocolEntry.  # noqa: E501


        :return: The num_steps of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._num_steps

    @num_steps.setter
    def num_steps(self, num_steps):
        """Sets the num_steps of this ProtocolEntry.


        :param num_steps: The num_steps of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._num_steps = num_steps

    @property
    def group_share_count(self):
        """Gets the group_share_count of this ProtocolEntry.  # noqa: E501


        :return: The group_share_count of this ProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._group_share_count

    @group_share_count.setter
    def group_share_count(self, group_share_count):
        """Sets the group_share_count of this ProtocolEntry.


        :param group_share_count: The group_share_count of this ProtocolEntry.  # noqa: E501
        :type: int
        """

        self._group_share_count = group_share_count

    @property
    def steps(self):
        """Gets the steps of this ProtocolEntry.  # noqa: E501


        :return: The steps of this ProtocolEntry.  # noqa: E501
        :rtype: list[ProtocolStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this ProtocolEntry.


        :param steps: The steps of this ProtocolEntry.  # noqa: E501
        :type: list[ProtocolStep]
        """

        self._steps = steps

    @property
    def vars(self):
        """Gets the vars of this ProtocolEntry.  # noqa: E501


        :return: The vars of this ProtocolEntry.  # noqa: E501
        :rtype: list[ProtocolVariable]
        """
        return self._vars

    @vars.setter
    def vars(self, vars):
        """Sets the vars of this ProtocolEntry.


        :param vars: The vars of this ProtocolEntry.  # noqa: E501
        :type: list[ProtocolVariable]
        """

        self._vars = vars

    @property
    def app_view_url(self):
        """Gets the app_view_url of this ProtocolEntry.  # noqa: E501


        :return: The app_view_url of this ProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._app_view_url

    @app_view_url.setter
    def app_view_url(self, app_view_url):
        """Sets the app_view_url of this ProtocolEntry.


        :param app_view_url: The app_view_url of this ProtocolEntry.  # noqa: E501
        :type: str
        """

        self._app_view_url = app_view_url

    @property
    def signing_status(self):
        """Gets the signing_status of this ProtocolEntry.  # noqa: E501


        :return: The signing_status of this ProtocolEntry.  # noqa: E501
        :rtype: SigningStatusDTO
        """
        return self._signing_status

    @signing_status.setter
    def signing_status(self, signing_status):
        """Sets the signing_status of this ProtocolEntry.


        :param signing_status: The signing_status of this ProtocolEntry.  # noqa: E501
        :type: SigningStatusDTO
        """

        self._signing_status = signing_status

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
        if issubclass(ProtocolEntry, dict):
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
        if not isinstance(other, ProtocolEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtocolEntry):
            return True

        return self.to_dict() != other.to_dict()