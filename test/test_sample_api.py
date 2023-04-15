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
from swagger_client.api.sample_api import SampleApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSampleApi(unittest.TestCase):
    """SampleApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sample_api.SampleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sample_add_amount_to_series_quantity(self):
        """Test case for sample_add_amount_to_series_quantity

        Add to quantity amount for all samples in a series  # noqa: E501
        """
        pass

    def test_sample_add_quantity_amount(self):
        """Test case for sample_add_quantity_amount

        Add an amount to a sample's quantity  # noqa: E501
        """
        pass

    def test_sample_add_samples_to_series(self):
        """Test case for sample_add_samples_to_series

        Add samples to a series  # noqa: E501
        """
        pass

    def test_sample_archive_sample(self):
        """Test case for sample_archive_sample

        Archive a sample  # noqa: E501
        """
        pass

    def test_sample_archive_sample_series(self):
        """Test case for sample_archive_sample_series

        Archive all samples in a series and remove the series  # noqa: E501
        """
        pass

    def test_sample_archive_samples(self):
        """Test case for sample_archive_samples

        Archive multiple samples.  # noqa: E501
        """
        pass

    def test_sample_archive_samples_deprecated(self):
        """Test case for sample_archive_samples_deprecated

        Archive multiple samples  # noqa: E501
        """
        pass

    def test_sample_change_locations(self):
        """Test case for sample_change_locations

        Change the locations of multiple samples in a box compartment  # noqa: E501
        """
        pass

    def test_sample_change_sample_owner(self):
        """Test case for sample_change_sample_owner

        Change the owner of a sample  # noqa: E501
        """
        pass

    def test_sample_change_sample_owner_bulk(self):
        """Test case for sample_change_sample_owner_bulk

        Change the owner of a sample  # noqa: E501
        """
        pass

    def test_sample_change_sample_owner_bulk_deprecated(self):
        """Test case for sample_change_sample_owner_bulk_deprecated

        Change the owner of a sample  # noqa: E501
        """
        pass

    def test_sample_check_in_sample(self):
        """Test case for sample_check_in_sample

        Check in a previously checked out sample  # noqa: E501
        """
        pass

    def test_sample_check_in_samples(self):
        """Test case for sample_check_in_samples

        Check in multiple samples  # noqa: E501
        """
        pass

    def test_sample_check_out_sample(self):
        """Test case for sample_check_out_sample

        Check out a sample  # noqa: E501
        """
        pass

    def test_sample_check_out_samples(self):
        """Test case for sample_check_out_samples

        Check out multiple samples  # noqa: E501
        """
        pass

    def test_sample_clear_quantity(self):
        """Test case for sample_clear_quantity

        Clear a sample's amount  # noqa: E501
        """
        pass

    def test_sample_clear_quantity_of_all_samples_in_series(self):
        """Test case for sample_clear_quantity_of_all_samples_in_series

        Clear amount of all samples in a series  # noqa: E501
        """
        pass

    def test_sample_clone_sample(self):
        """Test case for sample_clone_sample

        Creates one or more clones of a sample  # noqa: E501
        """
        pass

    def test_sample_clone_sample_to_series(self):
        """Test case for sample_clone_sample_to_series

        Creates a series out of one or more clones of the specified sample  # noqa: E501
        """
        pass

    def test_sample_clone_series(self):
        """Test case for sample_clone_series

        Copy a sample series to the given location  # noqa: E501
        """
        pass

    def test_sample_create_sample(self):
        """Test case for sample_create_sample

        Create a new sample  # noqa: E501
        """
        pass

    def test_sample_create_sample_from_hl7(self):
        """Test case for sample_create_sample_from_hl7

        Create a new sample by using HL7 2.x.x standards  # noqa: E501
        """
        pass

    def test_sample_create_sample_meta(self):
        """Test case for sample_create_sample_meta

        Create a new sample's meta field  # noqa: E501
        """
        pass

    def test_sample_create_sample_series(self):
        """Test case for sample_create_sample_series

        Create a new sample series  # noqa: E501
        """
        pass

    def test_sample_create_sample_series_with_samples(self):
        """Test case for sample_create_sample_series_with_samples

        Create a new sample series, together with samples, sample meta fields and sample quantity settings.  # noqa: E501
        """
        pass

    def test_sample_create_samples_bulk(self):
        """Test case for sample_create_samples_bulk

        Create multiple new samples with metas  # noqa: E501
        """
        pass

    def test_sample_delete(self):
        """Test case for sample_delete

        Delete a sample's quantity settings  # noqa: E501
        """
        pass

    def test_sample_delete_sample_meta(self):
        """Test case for sample_delete_sample_meta

        Delete a sample's meta field  # noqa: E501
        """
        pass

    def test_sample_get_available_view_columns(self):
        """Test case for sample_get_available_view_columns

        Get the available columns for the sample list table  # noqa: E501
        """
        pass

    def test_sample_get_quantity(self):
        """Test case for sample_get_quantity

        Get a sample's quantity settings  # noqa: E501
        """
        pass

    def test_sample_get_sample_by_id(self):
        """Test case for sample_get_sample_by_id

        Get a sample by id  # noqa: E501
        """
        pass

    def test_sample_get_sample_children(self):
        """Test case for sample_get_sample_children

        Get a sample's direct children  # noqa: E501
        """
        pass

    def test_sample_get_sample_experiments(self):
        """Test case for sample_get_sample_experiments

        Get all experiment sections where the sample is used  # noqa: E501
        """
        pass

    def test_sample_get_sample_logs(self):
        """Test case for sample_get_sample_logs

        Get a sample's change logs  # noqa: E501
        """
        pass

    def test_sample_get_sample_meta(self):
        """Test case for sample_get_sample_meta

        Get a sample's meta field by id  # noqa: E501
        """
        pass

    def test_sample_get_sample_metas(self):
        """Test case for sample_get_sample_metas

        Get all of a sample's meta fields  # noqa: E501
        """
        pass

    def test_sample_get_sample_parents(self):
        """Test case for sample_get_sample_parents

        Get a sample's full parent ancestry  # noqa: E501
        """
        pass

    def test_sample_get_sample_series(self):
        """Test case for sample_get_sample_series

        Get sample series  # noqa: E501
        """
        pass

    def test_sample_get_sample_series_by_id(self):
        """Test case for sample_get_sample_series_by_id

        Get a sample series by id  # noqa: E501
        """
        pass

    def test_sample_get_samples(self):
        """Test case for sample_get_samples

        Get samples  # noqa: E501
        """
        pass

    def test_sample_get_samples_and_series(self):
        """Test case for sample_get_samples_and_series

        Get single samples and sample series in an aggregated list  # noqa: E501
        """
        pass

    def test_sample_get_samples_by_barcode(self):
        """Test case for sample_get_samples_by_barcode

        Get a list of samples for multiple barcodes  # noqa: E501
        """
        pass

    def test_sample_get_samples_by_id(self):
        """Test case for sample_get_samples_by_id

        Get a list of samples for multiple ids  # noqa: E501
        """
        pass

    def test_sample_get_samples_for_names(self):
        """Test case for sample_get_samples_for_names

        Get a list of samples for multiple names  # noqa: E501
        """
        pass

    def test_sample_get_structure_samples(self):
        """Test case for sample_get_structure_samples

        Perform a similarity, substructure or exact search on chemical sample data  # noqa: E501
        """
        pass

    def test_sample_move_sample_series_to_layer(self):
        """Test case for sample_move_sample_series_to_layer

        Move all samples in a series to another storage layer  # noqa: E501
        """
        pass

    def test_sample_move_sample_to_layer(self):
        """Test case for sample_move_sample_to_layer

        Move a sample to another storage layer  # noqa: E501
        """
        pass

    def test_sample_move_samples_to_layer(self):
        """Test case for sample_move_samples_to_layer

        Move samples to another storage layer  # noqa: E501
        """
        pass

    def test_sample_move_samples_to_layer_deprecated(self):
        """Test case for sample_move_samples_to_layer_deprecated

        Move samples to another storage layer  # noqa: E501
        """
        pass

    def test_sample_patch_quantity(self):
        """Test case for sample_patch_quantity

        Update a sample's quantity settings  # noqa: E501
        """
        pass

    def test_sample_patch_sample(self):
        """Test case for sample_patch_sample

        Update a sample's properties  # noqa: E501
        """
        pass

    def test_sample_patch_sample_meta(self):
        """Test case for sample_patch_sample_meta

        Update a sample's meta field properties  # noqa: E501
        """
        pass

    def test_sample_patch_sample_series(self):
        """Test case for sample_patch_sample_series

        Update a sampleseries properties  # noqa: E501
        """
        pass

    def test_sample_patch_sample_series_samples(self):
        """Test case for sample_patch_sample_series_samples

        Update all samples in a sample series  # noqa: E501
        """
        pass

    def test_sample_put_quantity(self):
        """Test case for sample_put_quantity

        Add or replace a sample's quantity settings  # noqa: E501
        """
        pass

    def test_sample_put_sample_meta(self):
        """Test case for sample_put_sample_meta

        Create or update a sample's meta field  # noqa: E501
        """
        pass

    def test_sample_put_sample_meta_bulk(self):
        """Test case for sample_put_sample_meta_bulk

        Create or update a sample's meta field properties in bulk, based on its sampleTypeMetaID  # noqa: E501
        """
        pass

    def test_sample_put_sample_metas(self):
        """Test case for sample_put_sample_metas

        Create or update multiple sample's meta fields  # noqa: E501
        """
        pass

    def test_sample_put_series_quantity(self):
        """Test case for sample_put_series_quantity

        Add or replace quantity settings for all samples in a series  # noqa: E501
        """
        pass

    def test_sample_remove_samples_from_series(self):
        """Test case for sample_remove_samples_from_series

        Remove samples from a series  # noqa: E501
        """
        pass

    def test_sample_remove_samples_from_their_locations(self):
        """Test case for sample_remove_samples_from_their_locations

        Remove the location from multiples samples  # noqa: E501
        """
        pass

    def test_sample_subtract_amount_from_series_quantity(self):
        """Test case for sample_subtract_amount_from_series_quantity

        Subtract from quantity amount for all samples in a series  # noqa: E501
        """
        pass

    def test_sample_subtract_quantity_amount(self):
        """Test case for sample_subtract_quantity_amount

        Subtract an amount from a sample's quantity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()