# swagger_client.SampleApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sample_add_amount_to_series_quantity**](SampleApi.md#sample_add_amount_to_series_quantity) | **POST** /api/v1/sampleSeries/{seriesID}/quantity/add | Add to quantity amount for all samples in a series
[**sample_add_quantity_amount**](SampleApi.md#sample_add_quantity_amount) | **POST** /api/v1/samples/{sampleID}/quantity/add | Add an amount to a sample&#39;s quantity
[**sample_add_samples_to_series**](SampleApi.md#sample_add_samples_to_series) | **POST** /api/v1/sampleSeries/{sampleSeriesID}/samples/add | Add samples to a series
[**sample_archive_sample**](SampleApi.md#sample_archive_sample) | **DELETE** /api/v1/samples/{sampleID} | Archive a sample
[**sample_archive_sample_series**](SampleApi.md#sample_archive_sample_series) | **DELETE** /api/v1/sampleSeries/{sampleSeriesID} | Archive all samples in a series and remove the series
[**sample_archive_samples**](SampleApi.md#sample_archive_samples) | **POST** /api/v1/samples/archive | Archive multiple samples.
[**sample_archive_samples_deprecated**](SampleApi.md#sample_archive_samples_deprecated) | **DELETE** /api/v1/samples/bulk | Archive multiple samples
[**sample_change_locations**](SampleApi.md#sample_change_locations) | **POST** /api/v1/samples/changeLocations | Change the locations of multiple samples in a box compartment
[**sample_change_sample_owner**](SampleApi.md#sample_change_sample_owner) | **POST** /api/v1/samples/{sampleID}/changeOwner/{userId} | Change the owner of a sample
[**sample_change_sample_owner_bulk**](SampleApi.md#sample_change_sample_owner_bulk) | **POST** /api/v1/samples/changeOwner | Change the owner of a sample
[**sample_change_sample_owner_bulk_deprecated**](SampleApi.md#sample_change_sample_owner_bulk_deprecated) | **POST** /api/v1/samples/changeOwner/bulk/{userId} | Change the owner of a sample
[**sample_check_in_sample**](SampleApi.md#sample_check_in_sample) | **POST** /api/v1/samples/{sampleID}/checkin | Check in a previously checked out sample
[**sample_check_in_samples**](SampleApi.md#sample_check_in_samples) | **POST** /api/v1/samples/checkin | Check in multiple samples
[**sample_check_out_sample**](SampleApi.md#sample_check_out_sample) | **POST** /api/v1/samples/{sampleID}/checkout | Check out a sample
[**sample_check_out_samples**](SampleApi.md#sample_check_out_samples) | **POST** /api/v1/samples/checkout | Check out multiple samples
[**sample_clear_quantity**](SampleApi.md#sample_clear_quantity) | **POST** /api/v1/samples/{sampleID}/quantity/clear | Clear a sample&#39;s amount
[**sample_clear_quantity_of_all_samples_in_series**](SampleApi.md#sample_clear_quantity_of_all_samples_in_series) | **POST** /api/v1/sampleSeries/{seriesID}/quantity/clear | Clear amount of all samples in a series
[**sample_clone_sample**](SampleApi.md#sample_clone_sample) | **POST** /api/v1/samples/{sampleID}/clone | Creates one or more clones of a sample
[**sample_clone_sample_to_series**](SampleApi.md#sample_clone_sample_to_series) | **POST** /api/v1/samples/{sampleID}/cloneIntoSeries | Creates a series out of one or more clones of the specified sample
[**sample_clone_series**](SampleApi.md#sample_clone_series) | **POST** /api/v1/sampleSeries/{sampleSeriesID}/clone | Copy a sample series to the given location
[**sample_create_sample**](SampleApi.md#sample_create_sample) | **POST** /api/v1/samples | Create a new sample
[**sample_create_sample_from_hl7**](SampleApi.md#sample_create_sample_from_hl7) | **POST** /api/v1/samples/hl7 | Create a new sample by using HL7 2.x.x standards
[**sample_create_sample_meta**](SampleApi.md#sample_create_sample_meta) | **POST** /api/v1/samples/{sampleID}/meta | Create a new sample&#39;s meta field
[**sample_create_sample_series**](SampleApi.md#sample_create_sample_series) | **POST** /api/v1/sampleSeries | Create a new sample series
[**sample_create_sample_series_with_samples**](SampleApi.md#sample_create_sample_series_with_samples) | **POST** /api/v1/sampleSeries/createWithSamples | Create a new sample series, together with samples, sample meta fields and sample quantity settings.
[**sample_create_samples_bulk**](SampleApi.md#sample_create_samples_bulk) | **POST** /api/v1/samples/bulk | Create multiple new samples with metas
[**sample_delete**](SampleApi.md#sample_delete) | **DELETE** /api/v1/samples/{sampleID}/quantity | Delete a sample&#39;s quantity settings
[**sample_delete_sample_meta**](SampleApi.md#sample_delete_sample_meta) | **DELETE** /api/v1/samples/{sampleID}/meta/{sampleMetaID} | Delete a sample&#39;s meta field
[**sample_get_available_view_columns**](SampleApi.md#sample_get_available_view_columns) | **GET** /api/v1/samples/viewcolumns | Get the available columns for the sample list table
[**sample_get_quantity**](SampleApi.md#sample_get_quantity) | **GET** /api/v1/samples/{sampleID}/quantity | Get a sample&#39;s quantity settings
[**sample_get_sample_by_id**](SampleApi.md#sample_get_sample_by_id) | **GET** /api/v1/samples/{sampleID} | Get a sample by id
[**sample_get_sample_children**](SampleApi.md#sample_get_sample_children) | **GET** /api/v1/samples/{sampleID}/children | Get a sample&#39;s direct children
[**sample_get_sample_experiments**](SampleApi.md#sample_get_sample_experiments) | **GET** /api/v1/samples/{sampleID}/experiments/sections | Get all experiment sections where the sample is used
[**sample_get_sample_logs**](SampleApi.md#sample_get_sample_logs) | **GET** /api/v1/samples/{sampleID}/logs | Get a sample&#39;s change logs
[**sample_get_sample_meta**](SampleApi.md#sample_get_sample_meta) | **GET** /api/v1/samples/{sampleID}/meta/{sampleMetaID} | Get a sample&#39;s meta field by id
[**sample_get_sample_metas**](SampleApi.md#sample_get_sample_metas) | **GET** /api/v1/samples/{sampleID}/meta | Get all of a sample&#39;s meta fields
[**sample_get_sample_parents**](SampleApi.md#sample_get_sample_parents) | **GET** /api/v1/samples/{sampleID}/parents | Get a sample&#39;s full parent ancestry
[**sample_get_sample_series**](SampleApi.md#sample_get_sample_series) | **GET** /api/v1/sampleSeries | Get sample series
[**sample_get_sample_series_by_id**](SampleApi.md#sample_get_sample_series_by_id) | **GET** /api/v1/sampleSeries/{sampleSeriesID} | Get a sample series by id
[**sample_get_samples**](SampleApi.md#sample_get_samples) | **GET** /api/v1/samples | Get samples
[**sample_get_samples_and_series**](SampleApi.md#sample_get_samples_and_series) | **GET** /api/v1/samplesAndSeries | Get single samples and sample series in an aggregated list
[**sample_get_samples_by_barcode**](SampleApi.md#sample_get_samples_by_barcode) | **GET** /api/v1/samples/forBarcodes | Get a list of samples for multiple barcodes
[**sample_get_samples_by_id**](SampleApi.md#sample_get_samples_by_id) | **GET** /api/v1/samples/get | Get a list of samples for multiple ids
[**sample_get_samples_for_names**](SampleApi.md#sample_get_samples_for_names) | **GET** /api/v1/samples/forNames | Get a list of samples for multiple names
[**sample_get_structure_samples**](SampleApi.md#sample_get_structure_samples) | **GET** /api/v1/samples/structuresearch/{searchMethod} | Perform a similarity, substructure or exact search on chemical sample data
[**sample_move_sample_series_to_layer**](SampleApi.md#sample_move_sample_series_to_layer) | **POST** /api/v1/sampleSeries/{sampleSeriesID}/moveToLayer/{storageLayerID} | Move all samples in a series to another storage layer
[**sample_move_sample_to_layer**](SampleApi.md#sample_move_sample_to_layer) | **POST** /api/v1/samples/{sampleID}/moveToLayer/{storageLayerID} | Move a sample to another storage layer
[**sample_move_samples_to_layer**](SampleApi.md#sample_move_samples_to_layer) | **POST** /api/v1/samples/moveToLayer | Move samples to another storage layer
[**sample_move_samples_to_layer_deprecated**](SampleApi.md#sample_move_samples_to_layer_deprecated) | **POST** /api/v1/samples/moveToLayer/{storageLayerID} | Move samples to another storage layer
[**sample_patch_quantity**](SampleApi.md#sample_patch_quantity) | **PATCH** /api/v1/samples/{sampleID}/quantity | Update a sample&#39;s quantity settings
[**sample_patch_sample**](SampleApi.md#sample_patch_sample) | **PATCH** /api/v1/samples/{sampleID} | Update a sample&#39;s properties
[**sample_patch_sample_meta**](SampleApi.md#sample_patch_sample_meta) | **PATCH** /api/v1/samples/{sampleID}/meta/{sampleMetaID} | Update a sample&#39;s meta field properties
[**sample_patch_sample_series**](SampleApi.md#sample_patch_sample_series) | **PATCH** /api/v1/sampleseries/{sampleSeriesID} | Update a sampleseries properties
[**sample_patch_sample_series_samples**](SampleApi.md#sample_patch_sample_series_samples) | **PATCH** /api/v1/sampleSeries/{sampleSeriesID}/samples | Update all samples in a sample series
[**sample_put_quantity**](SampleApi.md#sample_put_quantity) | **PUT** /api/v1/samples/{sampleID}/quantity | Add or replace a sample&#39;s quantity settings
[**sample_put_sample_meta**](SampleApi.md#sample_put_sample_meta) | **PUT** /api/v1/samples/{sampleID}/meta | Create or update a sample&#39;s meta field
[**sample_put_sample_meta_bulk**](SampleApi.md#sample_put_sample_meta_bulk) | **PUT** /api/v1/samples/meta/{sampleTypeMetaID} | Create or update a sample&#39;s meta field properties in bulk, based on its sampleTypeMetaID
[**sample_put_sample_metas**](SampleApi.md#sample_put_sample_metas) | **PUT** /api/v1/samples/{sampleID}/metas | Create or update multiple sample&#39;s meta fields
[**sample_put_series_quantity**](SampleApi.md#sample_put_series_quantity) | **PUT** /api/v1/sampleSeries/{seriesID}/quantity | Add or replace quantity settings for all samples in a series
[**sample_remove_samples_from_series**](SampleApi.md#sample_remove_samples_from_series) | **POST** /api/v1/sampleSeries/{sampleSeriesID}/samples/remove | Remove samples from a series
[**sample_remove_samples_from_their_locations**](SampleApi.md#sample_remove_samples_from_their_locations) | **POST** /api/v1/samples/removeFromLocation | Remove the location from multiples samples
[**sample_subtract_amount_from_series_quantity**](SampleApi.md#sample_subtract_amount_from_series_quantity) | **POST** /api/v1/sampleSeries/{seriesID}/quantity/subtract | Subtract from quantity amount for all samples in a series
[**sample_subtract_quantity_amount**](SampleApi.md#sample_subtract_quantity_amount) | **POST** /api/v1/samples/{sampleID}/quantity/subtract | Subtract an amount from a sample&#39;s quantity


# **sample_add_amount_to_series_quantity**
> sample_add_amount_to_series_quantity(series_id, delta, x_requested_with=x_requested_with)

Add to quantity amount for all samples in a series

This call adds the given amount to the current quantity amounts of all samples in the series. All samples must have a quantity set and need to have the same quantity type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
series_id = 56 # int | 
delta = 1.2 # float | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add to quantity amount for all samples in a series
    api_instance.sample_add_amount_to_series_quantity(series_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_add_amount_to_series_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **delta** | **float**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_add_quantity_amount**
> float sample_add_quantity_amount(sample_id, delta, x_requested_with=x_requested_with)

Add an amount to a sample's quantity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
delta = 1.2 # float | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add an amount to a sample's quantity
    api_response = api_instance.sample_add_quantity_amount(sample_id, delta, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_add_quantity_amount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **delta** | **float**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**float**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_add_samples_to_series**
> sample_add_samples_to_series(sample_series_id, sample_ids, x_requested_with=x_requested_with)

Add samples to a series

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add samples to a series
    api_instance.sample_add_samples_to_series(sample_series_id, sample_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_add_samples_to_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_archive_sample**
> sample_archive_sample(sample_id, x_requested_with=x_requested_with)

Archive a sample

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Archive a sample
    api_instance.sample_archive_sample(sample_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_archive_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_archive_sample_series**
> sample_archive_sample_series(sample_series_id, x_requested_with=x_requested_with)

Archive all samples in a series and remove the series

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Archive all samples in a series and remove the series
    api_instance.sample_archive_sample_series(sample_series_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_archive_sample_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_archive_samples**
> sample_archive_samples(input, x_requested_with=x_requested_with)

Archive multiple samples.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
input = swagger_client.ArchiveSamples() # ArchiveSamples | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Archive multiple samples.
    api_instance.sample_archive_samples(input, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_archive_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ArchiveSamples**](ArchiveSamples.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_archive_samples_deprecated**
> sample_archive_samples_deprecated(sample_ids, x_requested_with=x_requested_with)

Archive multiple samples

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Archive multiple samples
    api_instance.sample_archive_samples_deprecated(sample_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_archive_samples_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_change_locations**
> sample_change_locations(updates, x_requested_with=x_requested_with)

Change the locations of multiple samples in a box compartment

      If you set the optional body parameter 'storageLayerID' then the samples are also moved to that storage compartment.      If you omit this parameter then the samples are only moved within their own compartment.        With this call you can, for example, switch sample positions. Note that if two samples would end up in the same position      as a result of this call a status 409 Conflict is returned.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
updates = swagger_client.SampleLocationUpdates() # SampleLocationUpdates | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Change the locations of multiple samples in a box compartment
    api_instance.sample_change_locations(updates, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_change_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updates** | [**SampleLocationUpdates**](SampleLocationUpdates.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_change_sample_owner**
> sample_change_sample_owner(sample_id, user_id, x_requested_with=x_requested_with)

Change the owner of a sample

This call changes the owner of the specified sample.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
user_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Change the owner of a sample
    api_instance.sample_change_sample_owner(sample_id, user_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_change_sample_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **user_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_change_sample_owner_bulk**
> sample_change_sample_owner_bulk(input, x_requested_with=x_requested_with)

Change the owner of a sample

This call changes the owner of the specified samples.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
input = swagger_client.ChangeSampleOwner() # ChangeSampleOwner | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Change the owner of a sample
    api_instance.sample_change_sample_owner_bulk(input, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_change_sample_owner_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ChangeSampleOwner**](ChangeSampleOwner.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_change_sample_owner_bulk_deprecated**
> sample_change_sample_owner_bulk_deprecated(user_id, sample_ids, x_requested_with=x_requested_with)

Change the owner of a sample

This call changes the owner of the specified samples.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Change the owner of a sample
    api_instance.sample_change_sample_owner_bulk_deprecated(user_id, sample_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_change_sample_owner_bulk_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_check_in_sample**
> sample_check_in_sample(sample_id, x_requested_with=x_requested_with)

Check in a previously checked out sample

This call removes the _checked out_ status of a sample.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check in a previously checked out sample
    api_instance.sample_check_in_sample(sample_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_check_in_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_check_in_samples**
> list[int] sample_check_in_samples(sample_ids, x_requested_with=x_requested_with)

Check in multiple samples

This call removes the _checked out_ status of the specified samples.    Any samples that weren't checked out are ignored. The sample IDs that were actually checked in are returned as an array.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check in multiple samples
    api_response = api_instance.sample_check_in_samples(sample_ids, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_check_in_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[int]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_check_out_sample**
> sample_check_out_sample(sample_id, x_requested_with=x_requested_with)

Check out a sample

This call marks a sample as _checked out_ while keeping its location reserved.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check out a sample
    api_instance.sample_check_out_sample(sample_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_check_out_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_check_out_samples**
> list[int] sample_check_out_samples(sample_ids, x_requested_with=x_requested_with)

Check out multiple samples

This call marks samples as _checked out_ while keeping their locations reserved.    Any samples that were already checked out are ignored. The sample IDs that were actually checked out are returned as an array.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Check out multiple samples
    api_response = api_instance.sample_check_out_samples(sample_ids, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_check_out_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[int]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_clear_quantity**
> SampleAmount sample_clear_quantity(sample_id, x_requested_with=x_requested_with)

Clear a sample's amount

This call clears the amount and unit specifications of a sample quantity. This call differs from the delete quantity, where delete quantityremoves the quantity settings, this call keeps the threshold settings and only clears the amount and unit settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Clear a sample's amount
    api_response = api_instance.sample_clear_quantity(sample_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_clear_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleAmount**](SampleAmount.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_clear_quantity_of_all_samples_in_series**
> sample_clear_quantity_of_all_samples_in_series(series_id, x_requested_with=x_requested_with)

Clear amount of all samples in a series

This call clears the amount and unit specifications linked to the quantity of all samples in a series.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
series_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Clear amount of all samples in a series
    api_instance.sample_clear_quantity_of_all_samples_in_series(series_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_clear_quantity_of_all_samples_in_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_clone_sample**
> sample_clone_sample(sample_id, options, x_requested_with=x_requested_with)

Creates one or more clones of a sample

The storage position ranges for the cloned samples can be given in the storagePositionRanges array, where the offset is the starting position in the storage position range and the limit is how many samples will be placed after the starting position. The total number of storage positions (the sum of limit) must be equal to cloneTimes. If no storage position ranges are specified, the cloned samples will not be added to a storage unit.    The quantity of the cloned samples can be changed using quantity amount and unit.     The trackParent parameter is a boolean indicating whether the original sample should be linked as parent to the clone sample(s).    example:        {          storagePositionRanges: [{              storageLayerID: 109061,              limit: 1,              offset: 2          }],          quantity: {              amount: 1,              unit: \"KiloGram\"          },          cloneTimes: 1,          trackParent: true      }      

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
options = swagger_client.SampleCloneOptions() # SampleCloneOptions | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Creates one or more clones of a sample
    api_instance.sample_clone_sample(sample_id, options, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_clone_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **options** | [**SampleCloneOptions**](SampleCloneOptions.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_clone_sample_to_series**
> int sample_clone_sample_to_series(sample_id, options, x_requested_with=x_requested_with)

Creates a series out of one or more clones of the specified sample

The storage position ranges for the cloned samples can be given in the storagePositionRanges array, where the offset is the starting position in the storage position range and the limit is how many samples will be placed after the starting position. The total number of storage positions (the sum of limit) must be equal to cloneTimes. If no storage position ranges are specified, the cloned samples will not be added to a storage unit.    The quantity of the cloned samples can be changed using quantity amount and unit.     The trackParent parameter is a boolean indicating whether the original sample should be linked as parent to the clone sample(s).    The seriesName parameter is the name of the newly created series.    The incrementSampleName parameter contains all the data for when you want to add an increment to the sample name. The numberPlacement can be 'Prepend' or 'Append'.    The includeSourceSample parameter is a boolean indicating whether the original sample is going to be included into the new series.    example:        {          storagePositionRanges: [{              storageLayerID: 109061,              limit: 1,              offset: 2,          }],          quantity: {              amount: 1,              unit: \"KiloGram\"          },          cloneTimes: 1,          trackParent: true          includeSourceSample: true,          seriesName: \"exampleSeries\",          ignoreAutoNumbering: true,          incrementSampleName: {              startNumber: 0,              stepSize: 5,              numberPosition: \"prepend\"          }      }      

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
options = swagger_client.SampleCloneIntoSeriesOptions() # SampleCloneIntoSeriesOptions | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Creates a series out of one or more clones of the specified sample
    api_response = api_instance.sample_clone_sample_to_series(sample_id, options, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_clone_sample_to_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **options** | [**SampleCloneIntoSeriesOptions**](SampleCloneIntoSeriesOptions.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_clone_series**
> sample_clone_series(sample_series_id, options, x_requested_with=x_requested_with)

Copy a sample series to the given location

  The storage position ranges for the cloned samples can be given in the storagePositionRanges array, where the offset is the starting position in the storage position range and the limit is how many samples will be placed after the starting position. The total number of storage positions (the sum of limit) must be equal to cloneTimes. If no storage position ranges are specified, the cloned samples will not be added to a storage unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
options = swagger_client.CloneSeriesOptions() # CloneSeriesOptions | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Copy a sample series to the given location
    api_instance.sample_clone_series(sample_series_id, options, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_clone_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **options** | [**CloneSeriesOptions**](CloneSeriesOptions.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_create_sample**
> int sample_create_sample(sample, auto_create_meta_defaults=auto_create_meta_defaults, x_requested_with=x_requested_with)

Create a new sample

By default this call will **not** create any meta fields even if there are required fields.    If you add the query parameter autoCreateMetaDefaults=true to this call then it will create the meta fields with their default or auto-numbering values as defined in the sample type. **Note:** meta fields in the sample type that don't have a default value or have auto-numbering enabled are **not** created.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample = swagger_client.SampleComplete() # SampleComplete | 
auto_create_meta_defaults = true # bool |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new sample
    api_response = api_instance.sample_create_sample(sample, auto_create_meta_defaults=auto_create_meta_defaults, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_create_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample** | [**SampleComplete**](SampleComplete.md)|  | 
 **auto_create_meta_defaults** | **bool**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_create_sample_from_hl7**
> object sample_create_sample_from_hl7(hl7, mapping, auto_create_meta_defaults, x_requested_with=x_requested_with)

Create a new sample by using HL7 2.x.x standards

This call will create samples and meta fields using HL7 standards and based on the provided mapping document (e.g. representing vials or tubes),   Values only support ST (string) datatypes. In case of a Batch HL7 file, multiple samples are created. An FHS line with File Name/ID (FHS-9) must be included for the ACK response to return the proper ID.  If ommitted, an ACK will be given to only the last MSH message. As the sample creation is done in transaction, this single ACK represents all the messages.   **Note:** HL7 messages need to be accompanied by a mapping parameter that describes the mapping as a JSON object.     This call does not support automatic naming even if configured as such in the sampletype. Always specify the name explicitly in your calls.    Example:  ```  {      \"sampleTypeID\": 12485,      \"storageLayerID\": 0, /* Optional */      \"position\": 0, /* Optional */      \"name\": {          \"segment\": \"MSH\",          \"field\": 10      },      \"description\": { /* Optional */          \"segment\": \"MSH\",          \"field\": 9,          \"component\": 3      },      \"altBarcode\": { /* Optional: Alternative barcode information. */          \"segment\": \"OBR\",          \"field\": 31      },      \"sampleTypeMetaIDMapping\": [ /* Optional: Array of mappings for the sampleTypeMetaID to the respective segment in the HL7 message */          {              \"sampleTypeMetaID\": 85318,              \"segment\": \"OBX\",              \"field\": 5          },          {              \"sampleTypeMetaID\": 85317,              \"segment\": \"ORC\",              \"field\": 2          }      ]  }   ```  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
hl7 = 'hl7_example' # str | 
mapping = 'mapping_example' # str | 
auto_create_meta_defaults = true # bool | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new sample by using HL7 2.x.x standards
    api_response = api_instance.sample_create_sample_from_hl7(hl7, mapping, auto_create_meta_defaults, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_create_sample_from_hl7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hl7** | **str**|  | 
 **mapping** | **str**|  | 
 **auto_create_meta_defaults** | **bool**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/hl7-v2, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_create_sample_meta**
> int sample_create_sample_meta(sample_id, dto, x_requested_with=x_requested_with)

Create a new sample's meta field

If you create a sample meta field that is defined in the sample type, make sure that you specify the correct sampleTypeMetaID for it. In addition, the sampleDataType should be the same as defined in the sample type.    You can create a meta field that isn't defined by leaving the sampleTypeMetaID blank. This is not advisable though, and results in the meta field's value not to be searchable!    In case of a meta field with selectable value - data types CHECKBOX, COMBO and RADIO - make sure that you only specify the values that are listed in the sample type's optionValues property. In case of multiple selected values, separate each value with a comma.    Note: it's advisable to use the PUT variant of this call. The POST variant will always make a new field, even if one already exists.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
dto = swagger_client.SampleMetaNew() # SampleMetaNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new sample's meta field
    api_response = api_instance.sample_create_sample_meta(sample_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_create_sample_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **dto** | [**SampleMetaNew**](SampleMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_create_sample_series**
> int sample_create_sample_series(series, x_requested_with=x_requested_with)

Create a new sample series

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
series = swagger_client.SampleSeriesNewWithSampleIDs() # SampleSeriesNewWithSampleIDs | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new sample series
    api_response = api_instance.sample_create_sample_series(series, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_create_sample_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series** | [**SampleSeriesNewWithSampleIDs**](SampleSeriesNewWithSampleIDs.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_create_sample_series_with_samples**
> int sample_create_sample_series_with_samples(series, auto_create_meta_defaults=auto_create_meta_defaults, x_requested_with=x_requested_with)

Create a new sample series, together with samples, sample meta fields and sample quantity settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
series = swagger_client.SampleSeriesComplete() # SampleSeriesComplete | 
auto_create_meta_defaults = true # bool |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new sample series, together with samples, sample meta fields and sample quantity settings.
    api_response = api_instance.sample_create_sample_series_with_samples(series, auto_create_meta_defaults=auto_create_meta_defaults, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_create_sample_series_with_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series** | [**SampleSeriesComplete**](SampleSeriesComplete.md)|  | 
 **auto_create_meta_defaults** | **bool**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_create_samples_bulk**
> list[int] sample_create_samples_bulk(sample_and_metas, auto_create_meta_defaults=auto_create_meta_defaults, x_requested_with=x_requested_with)

Create multiple new samples with metas

By default this call will **not** create any meta fields even if there are required fields.    If you add the query parameter autoCreateMetaDefaults=true to this call then it will create the meta fields with their default values as defined in the sample type. **Note:** meta fields in the sample type that don't have a default value are **not** created.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_and_metas = [swagger_client.SampleAndMeta()] # list[SampleAndMeta] | 
auto_create_meta_defaults = true # bool |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create multiple new samples with metas
    api_response = api_instance.sample_create_samples_bulk(sample_and_metas, auto_create_meta_defaults=auto_create_meta_defaults, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_create_samples_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_and_metas** | [**list[SampleAndMeta]**](SampleAndMeta.md)|  | 
 **auto_create_meta_defaults** | **bool**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[int]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_delete**
> sample_delete(sample_id, x_requested_with=x_requested_with)

Delete a sample's quantity settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a sample's quantity settings
    api_instance.sample_delete(sample_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_delete_sample_meta**
> sample_delete_sample_meta(sample_id, sample_meta_id, x_requested_with=x_requested_with)

Delete a sample's meta field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
sample_meta_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a sample's meta field
    api_instance.sample_delete_sample_meta(sample_id, sample_meta_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_delete_sample_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **sample_meta_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_available_view_columns**
> list[ViewColumn] sample_get_available_view_columns(x_requested_with=x_requested_with)

Get the available columns for the sample list table

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the available columns for the sample list table
    api_response = api_instance.sample_get_available_view_columns(x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_available_view_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[ViewColumn]**](ViewColumn.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_quantity**
> SampleAmount sample_get_quantity(sample_id, x_requested_with=x_requested_with)

Get a sample's quantity settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample's quantity settings
    api_response = api_instance.sample_get_quantity(sample_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleAmount**](SampleAmount.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_by_id**
> SampleLarge sample_get_sample_by_id(sample_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample by id

This call will also fetch archived samples.    $expand values (separate with comma for multiple expands):  * location  * quantity  * meta  * experiments  * catalogItem  * parent  * children  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample by id
    api_response = api_instance.sample_get_sample_by_id(sample_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleLarge**](SampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_children**
> PagedOfSampleLarge sample_get_sample_children(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample's direct children

This call will **not** fetch archived samples.    $expand values (separate with comma for multiple expands):  * location  * quantity  * meta  * experiments  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample's direct children
    api_response = api_instance.sample_get_sample_children(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLarge**](PagedOfSampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_experiments**
> PagedOfExperimentSectionForSample sample_get_sample_experiments(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all experiment sections where the sample is used

With this endpoint you can retrieve all the experiment sections where the given sample is created or used.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all experiment sections where the sample is used
    api_response = api_instance.sample_get_sample_experiments(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfExperimentSectionForSample**](PagedOfExperimentSectionForSample.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_logs**
> PagedOfSampleLogLarge sample_get_sample_logs(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, user_id=user_id, storage_id=storage_id, storage_layer_id=storage_layer_id, action=action, sample_meta_key=sample_meta_key, x_requested_with=x_requested_with)

Get a sample's change logs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
user_id = 'user_id_example' # str | Filter by the user who made the change (optional)
storage_id = 'storage_id_example' # str | Filter for samples in a storage unit (optional)
storage_layer_id = 'storage_layer_id_example' # str | Filter for samples in a storage layer (optional)
action = 'action_example' # str | Filter by action (CREATE/UPDATE/DELETE) (optional)
sample_meta_key = 'sample_meta_key_example' # str | Filter by a sample field (including \"Location\") (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample's change logs
    api_response = api_instance.sample_get_sample_logs(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, user_id=user_id, storage_id=storage_id, storage_layer_id=storage_layer_id, action=action, sample_meta_key=sample_meta_key, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **user_id** | **str**| Filter by the user who made the change | [optional] 
 **storage_id** | **str**| Filter for samples in a storage unit | [optional] 
 **storage_layer_id** | **str**| Filter for samples in a storage layer | [optional] 
 **action** | **str**| Filter by action (CREATE/UPDATE/DELETE) | [optional] 
 **sample_meta_key** | **str**| Filter by a sample field (including \&quot;Location\&quot;) | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLogLarge**](PagedOfSampleLogLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_meta**
> SampleMetaBase sample_get_sample_meta(sample_id, sample_meta_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample's meta field by id

This call will also fetch a meta field from an archived sample.    A meta field of type SAMPLELINK may contain archived samples.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
sample_meta_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample's meta field by id
    api_response = api_instance.sample_get_sample_meta(sample_id, sample_meta_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **sample_meta_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleMetaBase**](SampleMetaBase.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_metas**
> PagedOfSampleMetaLarge sample_get_sample_metas(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all of a sample's meta fields

This call will also fetch meta fields from an archived sample.            Meta fields of type SAMPLELINK may contain archived samples.          $expand values (separate with comma for multiple expands):  * sampleTypeSection          

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all of a sample's meta fields
    api_response = api_instance.sample_get_sample_metas(sample_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_metas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleMetaLarge**](PagedOfSampleMetaLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_parents**
> SampleLarge sample_get_sample_parents(sample_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample's full parent ancestry

The result is the direct parent with its `parent` property containing the grandparent and so forth.    This call will **not** fetch archived samples.    $expand values (separate with comma for multiple expands):  * location  * quantity  * meta  * experiments  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample's full parent ancestry
    api_response = api_instance.sample_get_sample_parents(sample_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_parents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleLarge**](SampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_series**
> PagedOfSampleSeries sample_get_sample_series(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get sample series

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get sample series
    api_response = api_instance.sample_get_sample_series(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleSeries**](PagedOfSampleSeries.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_sample_series_by_id**
> SampleSeriesLarge sample_get_sample_series_by_id(sample_series_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a sample series by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a sample series by id
    api_response = api_instance.sample_get_sample_series_by_id(sample_series_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_sample_series_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleSeriesLarge**](SampleSeriesLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples**
> PagedOfSampleLarge sample_get_samples(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, search=search, storage_id=storage_id, name=name, barcodes=barcodes, archived=archived, quantity_id=quantity_id, minimum_quantity_amount=minimum_quantity_amount, checked_out=checked_out, storage_layer_id=storage_layer_id, series_id=series_id, user_id=user_id, sample_type_id=sample_type_id, filter_by_sample_type_meta_values=filter_by_sample_type_meta_values, filter_by_minimum_date=filter_by_minimum_date, filter_by_maximum_date=filter_by_maximum_date, x_requested_with=x_requested_with)

Get samples

If the archived parameter isn't set, archived=false is automatically implied. To get both archived and non-archived samples you have to make two calls.    Searching for archived samples is not possible. The search parameter is ignored when archived=true.    $expand values (separate with comma for multiple expands):  * location  * quantity  * meta  * experiments  * parent  * children  * activeReservation  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
search = 'search_example' # str | Search term to use for filtering samples. This parameter can't be combined with archived=true. (optional)
storage_id = 'storage_id_example' # str | Filter for samples in a storage unit (optional)
name = 'name_example' # str | Filter by sample name (optional)
barcodes = 'barcodes_example' # str | Filter by barcodes (comma-separated) (optional)
archived = 'archived_example' # str | Filter by archived or non-archived samples. If set to true the search parameter has no effect. (optional)
quantity_id = 'quantity_id_example' # str | Filter by quantityID (optional)
minimum_quantity_amount = 'minimum_quantity_amount_example' # str | Filter for samples that have a minimum quantity amount set (optional)
checked_out = 'checked_out_example' # str | Filter for checked out samples (optional)
storage_layer_id = 'storage_layer_id_example' # str | Filter for samples in a storage layer (optional)
series_id = 'series_id_example' # str | Filter for samples in a series (optional)
user_id = 'user_id_example' # str | Filter by userID (optional)
sample_type_id = 'sample_type_id_example' # str | Filter by sampleTypeID (optional)
filter_by_sample_type_meta_values = 'filter_by_sample_type_meta_values_example' # str | (Optional) JSON array used to filter results. Only exact matches will be returned. This parameter can't be combined with archived=true. Example: [{\"sampleTypeMetaID\": 1234, \"metaValue\":\"No\"}] (optional)
filter_by_minimum_date = 'filter_by_minimum_date_example' # str | (Optional) date in ISO 8601 (YYYY-MM-DDThh:mm:ss) in UTC (optional)
filter_by_maximum_date = 'filter_by_maximum_date_example' # str | (Optional) date in ISO 8601 (YYYY-MM-DDThh:mm:ss) in UTC (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get samples
    api_response = api_instance.sample_get_samples(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, search=search, storage_id=storage_id, name=name, barcodes=barcodes, archived=archived, quantity_id=quantity_id, minimum_quantity_amount=minimum_quantity_amount, checked_out=checked_out, storage_layer_id=storage_layer_id, series_id=series_id, user_id=user_id, sample_type_id=sample_type_id, filter_by_sample_type_meta_values=filter_by_sample_type_meta_values, filter_by_minimum_date=filter_by_minimum_date, filter_by_maximum_date=filter_by_maximum_date, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **search** | **str**| Search term to use for filtering samples. This parameter can&#39;t be combined with archived&#x3D;true. | [optional] 
 **storage_id** | **str**| Filter for samples in a storage unit | [optional] 
 **name** | **str**| Filter by sample name | [optional] 
 **barcodes** | **str**| Filter by barcodes (comma-separated) | [optional] 
 **archived** | **str**| Filter by archived or non-archived samples. If set to true the search parameter has no effect. | [optional] 
 **quantity_id** | **str**| Filter by quantityID | [optional] 
 **minimum_quantity_amount** | **str**| Filter for samples that have a minimum quantity amount set | [optional] 
 **checked_out** | **str**| Filter for checked out samples | [optional] 
 **storage_layer_id** | **str**| Filter for samples in a storage layer | [optional] 
 **series_id** | **str**| Filter for samples in a series | [optional] 
 **user_id** | **str**| Filter by userID | [optional] 
 **sample_type_id** | **str**| Filter by sampleTypeID | [optional] 
 **filter_by_sample_type_meta_values** | **str**| (Optional) JSON array used to filter results. Only exact matches will be returned. This parameter can&#39;t be combined with archived&#x3D;true. Example: [{\&quot;sampleTypeMetaID\&quot;: 1234, \&quot;metaValue\&quot;:\&quot;No\&quot;}] | [optional] 
 **filter_by_minimum_date** | **str**| (Optional) date in ISO 8601 (YYYY-MM-DDThh:mm:ss) in UTC | [optional] 
 **filter_by_maximum_date** | **str**| (Optional) date in ISO 8601 (YYYY-MM-DDThh:mm:ss) in UTC | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLarge**](PagedOfSampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_and_series**
> sample_get_samples_and_series(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, user_id=user_id, sample_type_id=sample_type_id, name=name, storage_layer_id=storage_layer_id, unassigned_sample_location=unassigned_sample_location, exp_journal_id=exp_journal_id, search=search, storage_id=storage_id, show_shared_samples=show_shared_samples, x_requested_with=x_requested_with)

Get single samples and sample series in an aggregated list

Note that in case of an item with type SERIES the sample type and location are taken from the **first** sample in the series.    $expand values (separate with a comma for multiple expands):  * location  * quantity  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
user_id = 'user_id_example' # str | Filter by userID (optional)
sample_type_id = 'sample_type_id_example' # str | Filter by sampleTypeID (optional)
name = 'name_example' # str | Filter by sample name (optional)
storage_layer_id = 'storage_layer_id_example' # str | Filter by StorageLayerID (optional)
unassigned_sample_location = 'unassigned_sample_location_example' # str | Filter by samples with unassigned locations: values: 1/0 | True/False (optional)
exp_journal_id = 'exp_journal_id_example' # str | Filter by expJournalID (optional)
search = 'search_example' # str | Search term to use for filtering samples. (optional)
storage_id = 'storage_id_example' # str | Filter by storageID (optional)
show_shared_samples = 'show_shared_samples_example' # str | Display shared samples (true | false) (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get single samples and sample series in an aggregated list
    api_instance.sample_get_samples_and_series(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, user_id=user_id, sample_type_id=sample_type_id, name=name, storage_layer_id=storage_layer_id, unassigned_sample_location=unassigned_sample_location, exp_journal_id=exp_journal_id, search=search, storage_id=storage_id, show_shared_samples=show_shared_samples, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_and_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **user_id** | **str**| Filter by userID | [optional] 
 **sample_type_id** | **str**| Filter by sampleTypeID | [optional] 
 **name** | **str**| Filter by sample name | [optional] 
 **storage_layer_id** | **str**| Filter by StorageLayerID | [optional] 
 **unassigned_sample_location** | **str**| Filter by samples with unassigned locations: values: 1/0 | True/False | [optional] 
 **exp_journal_id** | **str**| Filter by expJournalID | [optional] 
 **search** | **str**| Search term to use for filtering samples. | [optional] 
 **storage_id** | **str**| Filter by storageID | [optional] 
 **show_shared_samples** | **str**| Display shared samples (true | false) | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_by_barcode**
> PagedOfSampleLarge sample_get_samples_by_barcode(barcodes, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a list of samples for multiple barcodes

This call will also fetch archived samples.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
barcodes = ['barcodes_example'] # list[str] | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of samples for multiple barcodes
    api_response = api_instance.sample_get_samples_by_barcode(barcodes, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_by_barcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcodes** | [**list[str]**](str.md)|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLarge**](PagedOfSampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_by_id**
> list[SampleLarge] sample_get_samples_by_id(sample_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a list of samples for multiple ids

This call will also fetch archived samples.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = [56] # list[int] | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of samples for multiple ids
    api_response = api_instance.sample_get_samples_by_id(sample_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | [**list[int]**](int.md)|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[SampleLarge]**](SampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_samples_for_names**
> PagedOfSampleLarge sample_get_samples_for_names(names, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, archived=archived, x_requested_with=x_requested_with)

Get a list of samples for multiple names

If the archived parameter isn't set, archived=false is automatically implied. To get both archived and non-archived samples you have to make two calls.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
names = ['names_example'] # list[str] | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
archived = 'archived_example' # str | Filter by archived or non-archived samples. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of samples for multiple names
    api_response = api_instance.sample_get_samples_for_names(names, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, archived=archived, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_samples_for_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **archived** | **str**| Filter by archived or non-archived samples. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLarge**](PagedOfSampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get_structure_samples**
> SearchStructureData sample_get_structure_samples(search_method, search_params_query=search_params_query, search_params_search_type=search_params_search_type, search_params_search_archive=search_params_search_archive, search_params_reaction_table_search=search_params_reaction_table_search, search_params_result_set_number=search_params_result_set_number, search_params_threshold=search_params_threshold, x_requested_with=x_requested_with)

Perform a similarity, substructure or exact search on chemical sample data

searchMethod can be either:      * similarity: structure similarity based on the Tanimoto algorithm      * substructure: whether the substructure query is present in the target structure      * exact: exact structure match        Example values:      * searchMethod: similarity      * query: CC(C)CC(=O)      * searchType: smiles      * searchArchive: false      * reactionTableSearch: false      * resultSetNumber: 0      * threshold: 85

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
search_method = 'search_method_example' # str | 
search_params_query = 'search_params_query_example' # str |  (optional)
search_params_search_type = 'search_params_search_type_example' # str |  (optional)
search_params_search_archive = true # bool |  (optional)
search_params_reaction_table_search = true # bool |  (optional)
search_params_result_set_number = 56 # int |  (optional)
search_params_threshold = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Perform a similarity, substructure or exact search on chemical sample data
    api_response = api_instance.sample_get_structure_samples(search_method, search_params_query=search_params_query, search_params_search_type=search_params_search_type, search_params_search_archive=search_params_search_archive, search_params_reaction_table_search=search_params_reaction_table_search, search_params_result_set_number=search_params_result_set_number, search_params_threshold=search_params_threshold, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_get_structure_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_method** | **str**|  | 
 **search_params_query** | **str**|  | [optional] 
 **search_params_search_type** | **str**|  | [optional] 
 **search_params_search_archive** | **bool**|  | [optional] 
 **search_params_reaction_table_search** | **bool**|  | [optional] 
 **search_params_result_set_number** | **int**|  | [optional] 
 **search_params_threshold** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SearchStructureData**](SearchStructureData.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_move_sample_series_to_layer**
> sample_move_sample_series_to_layer(sample_series_id, storage_layer_id, body, x_requested_with=x_requested_with)

Move all samples in a series to another storage layer

You can provide an optional position within the storage layer with the following request body:  ```  {    \"position\": 12  }  ```    Note: the storage layer must have enough contiguous free space left to fit the series, starting from the specified position.      

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
storage_layer_id = 56 # int | 
body = NULL # object | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Move all samples in a series to another storage layer
    api_instance.sample_move_sample_series_to_layer(sample_series_id, storage_layer_id, body, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_move_sample_series_to_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **storage_layer_id** | **int**|  | 
 **body** | **object**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_move_sample_to_layer**
> sample_move_sample_to_layer(sample_id, storage_layer_id, body, x_requested_with=x_requested_with)

Move a sample to another storage layer

For boxes you must provide a position with the following request body:  ```  {    \"position\": 12  }  ```  For any other storage layer the request body should be an empty object.      

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
storage_layer_id = 56 # int | 
body = NULL # object | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Move a sample to another storage layer
    api_instance.sample_move_sample_to_layer(sample_id, storage_layer_id, body, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_move_sample_to_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **storage_layer_id** | **int**|  | 
 **body** | **object**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_move_samples_to_layer**
> sample_move_samples_to_layer(input, x_requested_with=x_requested_with)

Move samples to another storage layer

For boxes you must provide a position with the following request body:  ```  {    \"position\": 12  }  ```  In boxes this will move the samples contiguously from the indicated position. If there is no space for all samples, or there are other samples in those position, this call will result in an error 400.  For any other storage layer the request body should be an empty object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
input = swagger_client.MoveSamplesToLayer() # MoveSamplesToLayer | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Move samples to another storage layer
    api_instance.sample_move_samples_to_layer(input, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_move_samples_to_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**MoveSamplesToLayer**](MoveSamplesToLayer.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_move_samples_to_layer_deprecated**
> sample_move_samples_to_layer_deprecated(sample_ids, storage_layer_id, body, x_requested_with=x_requested_with)

Move samples to another storage layer

For boxes you must provide a position with the following request body:  ```  {    \"position\": 12  }  ```  In boxes this will move the samples contiguously from the indicated position. If there is no space for all samples, or there are other samples in those position, this call will result in an error 400.  For any other storage layer the request body should be an empty object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_ids = [56] # list[int] | 
storage_layer_id = 56 # int | 
body = NULL # object | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Move samples to another storage layer
    api_instance.sample_move_samples_to_layer_deprecated(sample_ids, storage_layer_id, body, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_move_samples_to_layer_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_ids** | [**list[int]**](int.md)|  | 
 **storage_layer_id** | **int**|  | 
 **body** | **object**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_patch_quantity**
> SampleAmount sample_patch_quantity(sample_id, delta, x_requested_with=x_requested_with)

Update a sample's quantity settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
delta = swagger_client.SampleAmountNew() # SampleAmountNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a sample's quantity settings
    api_response = api_instance.sample_patch_quantity(sample_id, delta, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_patch_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **delta** | [**SampleAmountNew**](SampleAmountNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleAmount**](SampleAmount.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_patch_sample**
> sample_patch_sample(sample_id, delta=delta, x_requested_with=x_requested_with)

Update a sample's properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
delta = swagger_client.SampleUpdateDocs() # SampleUpdateDocs |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a sample's properties
    api_instance.sample_patch_sample(sample_id, delta=delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_patch_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **delta** | [**SampleUpdateDocs**](SampleUpdateDocs.md)|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_patch_sample_meta**
> sample_patch_sample_meta(sample_id, sample_meta_id, delta, x_requested_with=x_requested_with)

Update a sample's meta field properties

Use this call to update a meta field's value, or linked files/samples.    In case of a meta field with selectable value - data types CHECKBOX, COMBO and RADIO - make sure that you only specify the values that are listed in the sample type's optionValues property. In case of multiple selected values, separate each value with a comma. If you want to unselect all options supply an empty string to the value property.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
sample_meta_id = 56 # int | 
delta = swagger_client.SampleMeta() # SampleMeta | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a sample's meta field properties
    api_instance.sample_patch_sample_meta(sample_id, sample_meta_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_patch_sample_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **sample_meta_id** | **int**|  | 
 **delta** | [**SampleMeta**](SampleMeta.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_patch_sample_series**
> sample_patch_sample_series(sample_series_id, delta, x_requested_with=x_requested_with)

Update a sampleseries properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
delta = swagger_client.SampleSeriesNewWithSampleIDs() # SampleSeriesNewWithSampleIDs | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a sampleseries properties
    api_instance.sample_patch_sample_series(sample_series_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_patch_sample_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **delta** | [**SampleSeriesNewWithSampleIDs**](SampleSeriesNewWithSampleIDs.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_patch_sample_series_samples**
> sample_patch_sample_series_samples(sample_series_id, sample=sample, x_requested_with=x_requested_with)

Update all samples in a sample series

This call updates all the samples within a sample series.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
sample = swagger_client.UpdateSampleSeriesCompleteDocs() # UpdateSampleSeriesCompleteDocs |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update all samples in a sample series
    api_instance.sample_patch_sample_series_samples(sample_series_id, sample=sample, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_patch_sample_series_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **sample** | [**UpdateSampleSeriesCompleteDocs**](UpdateSampleSeriesCompleteDocs.md)|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_put_quantity**
> SampleAmount sample_put_quantity(sample_id, quantity, x_requested_with=x_requested_with)

Add or replace a sample's quantity settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
quantity = swagger_client.SampleAmountNew() # SampleAmountNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add or replace a sample's quantity settings
    api_response = api_instance.sample_put_quantity(sample_id, quantity, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_put_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **quantity** | [**SampleAmountNew**](SampleAmountNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleAmount**](SampleAmount.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_put_sample_meta**
> int sample_put_sample_meta(sample_id, dto, x_requested_with=x_requested_with)

Create or update a sample's meta field

If you create a sample meta field that is defined in the sample type, make sure that you specify the correct sampleTypeMetaID for it. In addition, the sampleDataType should be the same as defined in the sample type.    You can create a meta field that isn't defined by leaving the sampleTypeMetaID blank. This is not advisable though, and results in the meta field's value not to be searchable!    In case of a meta field with selectable value - data types CHECKBOX, COMBO and RADIO - make sure that you only specify the values that are listed in the sample type's optionValues property. In case of multiple selected values, separate each value with a comma.    This call will check if a meta field with the specified key already exists. If so it overwrites that meta field unless the value is the same; otherwise it creates a new meta field. Note: the sampleMetaID will be newly created on an overwrite.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
dto = swagger_client.SampleMetaNew() # SampleMetaNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create or update a sample's meta field
    api_response = api_instance.sample_put_sample_meta(sample_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_put_sample_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **dto** | [**SampleMetaNew**](SampleMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_put_sample_meta_bulk**
> sample_put_sample_meta_bulk(new_value, sample_type_meta_id, sample_ids, x_requested_with=x_requested_with)

Create or update a sample's meta field properties in bulk, based on its sampleTypeMetaID

Use this call to update a meta field's value, or linked files/samples.    In case of a meta field with selectable value - data types CHECKBOX, COMBO and RADIO - make sure that you only specify the values that are listed in the sample type's optionValues property. In case of multiple selected values, separate each value with a comma. If you want to unselect all options supply an empty string to the value property.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
new_value = 'new_value_example' # str | 
sample_type_meta_id = 56 # int | 
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create or update a sample's meta field properties in bulk, based on its sampleTypeMetaID
    api_instance.sample_put_sample_meta_bulk(new_value, sample_type_meta_id, sample_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_put_sample_meta_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_value** | **str**|  | 
 **sample_type_meta_id** | **int**|  | 
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_put_sample_metas**
> list[int] sample_put_sample_metas(sample_id, dtos, x_requested_with=x_requested_with)

Create or update multiple sample's meta fields

If you create a sample meta field that is defined in the sample type, make sure that you specify the correct sampleTypeMetaID for it. In addition, the sampleDataType should be the same as defined in the sample type as defined in the sample type.    You can create a meta field that isn't defined by leaving the sampleTypeMetaID blank. This is not advisable though, and results in the meta field's value not to be searchable!    In case of a meta field with selectable value - data types CHECKBOX, COMBO and RADIO - make sure that you only specify the values that are listed in the sample type's optionValues property. In case of multiple selected values, separate each value with a comma.    This call will check if a meta field with the specified key already exists. If so it overwrites that meta field unless the value is the same; otherwise it creates a new meta field. Note: the sampleMetaID will be newly created on an overwrite.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
dtos = [swagger_client.SampleMetaNew()] # list[SampleMetaNew] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create or update multiple sample's meta fields
    api_response = api_instance.sample_put_sample_metas(sample_id, dtos, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_put_sample_metas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **dtos** | [**list[SampleMetaNew]**](SampleMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[int]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_put_series_quantity**
> SampleAmount sample_put_series_quantity(series_id, quantity, x_requested_with=x_requested_with)

Add or replace quantity settings for all samples in a series

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
series_id = 56 # int | 
quantity = swagger_client.SampleAmountNew() # SampleAmountNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add or replace quantity settings for all samples in a series
    api_response = api_instance.sample_put_series_quantity(series_id, quantity, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_put_series_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **quantity** | [**SampleAmountNew**](SampleAmountNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**SampleAmount**](SampleAmount.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_remove_samples_from_series**
> sample_remove_samples_from_series(sample_series_id, sample_ids, x_requested_with=x_requested_with)

Remove samples from a series

When all samples are removed from a series then the series is automatically disbanded.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_series_id = 56 # int | 
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove samples from a series
    api_instance.sample_remove_samples_from_series(sample_series_id, sample_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_remove_samples_from_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_series_id** | **int**|  | 
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_remove_samples_from_their_locations**
> sample_remove_samples_from_their_locations(sample_ids, x_requested_with=x_requested_with)

Remove the location from multiples samples

This call removes the location from specified samples.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_ids = [swagger_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove the location from multiples samples
    api_instance.sample_remove_samples_from_their_locations(sample_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_remove_samples_from_their_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_subtract_amount_from_series_quantity**
> sample_subtract_amount_from_series_quantity(series_id, delta, x_requested_with=x_requested_with)

Subtract from quantity amount for all samples in a series

This call subtracts the given amount from the current quantity amounts of all samples in the series. All samples must have a quantity set and need to have the same quantity type. The amount of a sample cannot be dropped below 0

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
series_id = 56 # int | 
delta = 1.2 # float | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Subtract from quantity amount for all samples in a series
    api_instance.sample_subtract_amount_from_series_quantity(series_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SampleApi->sample_subtract_amount_from_series_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **delta** | **float**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_subtract_quantity_amount**
> float sample_subtract_quantity_amount(sample_id, delta, x_requested_with=x_requested_with)

Subtract an amount from a sample's quantity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration))
sample_id = 56 # int | 
delta = 1.2 # float | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Subtract an amount from a sample's quantity
    api_response = api_instance.sample_subtract_quantity_amount(sample_id, delta, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->sample_subtract_quantity_amount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **delta** | **float**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**float**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

