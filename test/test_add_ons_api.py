# coding: utf-8

"""
    eLabNext REST API

    ## Authentication    To authenticate use the `POST /api/v1/auth/user` call below in the Authentication tab with a username and password. This will return an API token as property `token`.    All API calls, with the exception of authentication, need this API token in the header as `Authorization: [API token]`. Omitting this header or supplying an invalid API token results in an error 401 Not Authorized.    Example: `Authorization: eec0727eaf6f7b127aaec1ec33c21caf`    To use this with the **Try it out** buttons, fill in the **api_key** field above with the API token.    ## Request Bodies    The API uses JSON with character set UTF-8 for request and response bodies.    In any call that utilizes request bodies you must supply the header `Content-Type: application/json; charset=utf-8`.    ## Response Codes    Status Code | Name | Meaning  ----------- | ---- | -------  200 | OK | Success. (JSON) content is included in the body.  204 | No Content | Success and no body content. This status is always returned when a call does not produce content.  400 | Bad Request | Bad/missing parameters or JSON input.  401 | Not Authorized | Authentication header is missing or the supplied API token is invalid.  403 | Forbidden | The user associated with the API token has no permission for the requested operation.  404 | Not Found | The resource specified in the request does not exist.  405 | Method Not Allowed | The API call was made with an unsupported HTTP method. (e.g. GET instead of POST.)  409 | Conflict | A POST or PUT operation failed because it conflicts with existing data.  500 | Internal Server Error | A generic error occurred on the server. The response's `message` property contains a description of the error.        # noqa: E501

    OpenAPI spec version: v1
    Contact: enquiries@elabnext.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.add_ons_api import AddOnsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAddOnsApi(unittest.TestCase):
    """AddOnsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.add_ons_api.AddOnsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_addon_approve_addon(self):
        """Test case for addon_approve_addon

        Approve an addon for installation by end users.  # noqa: E501
        """
        pass

    def test_addon_delete_addon(self):
        """Test case for addon_delete_addon

        Delete the specified installed add-on.  # noqa: E501
        """
        pass

    def test_addon_delete_media_from_addon(self):
        """Test case for addon_delete_media_from_addon

        Delete given media for the specified add-on.  # noqa: E501
        """
        pass

    def test_addon_disable_addon(self):
        """Test case for addon_disable_addon

        Disable the specified add-on for the given scope.  # noqa: E501
        """
        pass

    def test_addon_enable_addon(self):
        """Test case for addon_enable_addon

        Enable the specified add-on for the given scope.  # noqa: E501
        """
        pass

    def test_addon_get_addon(self):
        """Test case for addon_get_addon

        Get an available addon by ID for internal use  # noqa: E501
        """
        pass

    def test_addon_get_addon_config(self):
        """Test case for addon_get_addon_config

        Get the configuration details for the specified add-on.  # noqa: E501
        """
        pass

    def test_addon_get_available_addons(self):
        """Test case for addon_get_available_addons

        Retrieve list of addons for use in marketplace.  # noqa: E501
        """
        pass

    def test_addon_get_available_addons_grouped_by_version(self):
        """Test case for addon_get_available_addons_grouped_by_version

        Get all available addons grouped by rootVar and included lower versioned add-ons.  # noqa: E501
        """
        pass

    def test_addon_get_available_upgrades_count(self):
        """Test case for addon_get_available_upgrades_count

        Get the amount of available addon upgrades  # noqa: E501
        """
        pass

    def test_addon_get_groups_for_installed_addon(self):
        """Test case for addon_get_groups_for_installed_addon

        Get a list of groups which have the specified add-on installed  # noqa: E501
        """
        pass

    def test_addon_get_installed_addon(self):
        """Test case for addon_get_installed_addon

        Get the specified installed add-on.  # noqa: E501
        """
        pass

    def test_addon_get_installed_addons(self):
        """Test case for addon_get_installed_addons

        List installed add-ons  # noqa: E501
        """
        pass

    def test_addon_get_institures_for_installed_addon(self):
        """Test case for addon_get_institures_for_installed_addon

        Get a list of institutes which have the specified add-on installed  # noqa: E501
        """
        pass

    def test_addon_get_users_for_installed_addon(self):
        """Test case for addon_get_users_for_installed_addon

        Get a list of users which have the specified add-on installed  # noqa: E501
        """
        pass

    def test_addon_install_addon(self):
        """Test case for addon_install_addon

        Install the specified add-on for a given scope.  # noqa: E501
        """
        pass

    def test_addon_publish_addon(self):
        """Test case for addon_publish_addon

        Publish a new add-on.  # noqa: E501
        """
        pass

    def test_addon_save_addon_config(self):
        """Test case for addon_save_addon_config

        Set the configuration for the specified add-on.  # noqa: E501
        """
        pass

    def test_addon_sync_addons(self):
        """Test case for addon_sync_addons

        Synchronise the local addons with ones located in the remote sources  # noqa: E501
        """
        pass

    def test_addon_target_create_target_group(self):
        """Test case for addon_target_create_target_group

        Add new target group  # noqa: E501
        """
        pass

    def test_addon_target_create_target_organisation(self):
        """Test case for addon_target_create_target_organisation

        Add new target organisation  # noqa: E501
        """
        pass

    def test_addon_target_create_target_user(self):
        """Test case for addon_target_create_target_user

        Add new target user  # noqa: E501
        """
        pass

    def test_addon_target_create_targets(self):
        """Test case for addon_target_create_targets

        Create targets for addons (users, organisations and/or groups  # noqa: E501
        """
        pass

    def test_addon_target_get_groups_outside_target(self):
        """Test case for addon_target_get_groups_outside_target

        Get groups for addons that have the add-on installed but do not fall within the specified target  # noqa: E501
        """
        pass

    def test_addon_target_get_target_groups(self):
        """Test case for addon_target_get_target_groups

        List all target groups for specified addon  # noqa: E501
        """
        pass

    def test_addon_target_get_target_organisations(self):
        """Test case for addon_target_get_target_organisations

        List all target organisations for specified addon  # noqa: E501
        """
        pass

    def test_addon_target_get_target_users(self):
        """Test case for addon_target_get_target_users

        List all target users for specified addon  # noqa: E501
        """
        pass

    def test_addon_target_get_targets(self):
        """Test case for addon_target_get_targets

        Get targets for addons (users, organisations and/or groups  # noqa: E501
        """
        pass

    def test_addon_target_get_users_outside_target(self):
        """Test case for addon_target_get_users_outside_target

        """
        pass

    def test_addon_target_remove_target_group(self):
        """Test case for addon_target_remove_target_group

        Remove group target from addon  # noqa: E501
        """
        pass

    def test_addon_target_remove_target_organisation(self):
        """Test case for addon_target_remove_target_organisation

        Remove organisation target from addon  # noqa: E501
        """
        pass

    def test_addon_target_remove_target_user(self):
        """Test case for addon_target_remove_target_user

        Remove user target from addon  # noqa: E501
        """
        pass

    def test_addon_target_update_targets(self):
        """Test case for addon_target_update_targets

        Update targets for addons (users, organisations and/or groups  # noqa: E501
        """
        pass

    def test_addon_uninstall_addon(self):
        """Test case for addon_uninstall_addon

        Uninstall the specified add-on for a given scope.  # noqa: E501
        """
        pass

    def test_addon_update_addon(self):
        """Test case for addon_update_addon

        Update existing add-on contents.  # noqa: E501
        """
        pass

    def test_addon_update_all(self):
        """Test case for addon_update_all

        Update all other installed versions of this addon to this version  # noqa: E501
        """
        pass

    def test_addon_upload_media(self):
        """Test case for addon_upload_media

        Add media to the specified add-on.  # noqa: E501
        """
        pass

    def test_bundle_create_bundle(self):
        """Test case for bundle_create_bundle

        """
        pass

    def test_bundle_delete_bundle(self):
        """Test case for bundle_delete_bundle

        """
        pass

    def test_bundle_get_bundles(self):
        """Test case for bundle_get_bundles

        """
        pass

    def test_bundle_install_bundle(self):
        """Test case for bundle_install_bundle

        """
        pass

    def test_bundle_update_bundle(self):
        """Test case for bundle_update_bundle

        """
        pass

    def test_category_create_category(self):
        """Test case for category_create_category

        """
        pass

    def test_category_delete_category(self):
        """Test case for category_delete_category

        """
        pass

    def test_category_get_categories(self):
        """Test case for category_get_categories

        """
        pass

    def test_category_update_category(self):
        """Test case for category_update_category

        """
        pass

    def test_foreign_source_create_foreign_source(self):
        """Test case for foreign_source_create_foreign_source

        Create a new registered source  # noqa: E501
        """
        pass

    def test_foreign_source_delete_foreign_source(self):
        """Test case for foreign_source_delete_foreign_source

        Remove a registered source  # noqa: E501
        """
        pass

    def test_foreign_source_get_foreign_source(self):
        """Test case for foreign_source_get_foreign_source

        Get a specific source  # noqa: E501
        """
        pass

    def test_foreign_source_get_foreign_sources(self):
        """Test case for foreign_source_get_foreign_sources

        Get a list of registered sources  # noqa: E501
        """
        pass

    def test_foreign_source_update_foreign_source(self):
        """Test case for foreign_source_update_foreign_source

        Update a source  # noqa: E501
        """
        pass

    def test_permission_get_permissions(self):
        """Test case for permission_get_permissions

        """
        pass

    def test_sample_type_meta_get_addon_sample_meta(self):
        """Test case for sample_type_meta_get_addon_sample_meta

        """
        pass


if __name__ == '__main__':
    unittest.main()
