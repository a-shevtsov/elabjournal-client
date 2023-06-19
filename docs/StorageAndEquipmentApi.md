# elabjournal_client.StorageAndEquipmentApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_create_assignment**](StorageAndEquipmentApi.md#assignment_create_assignment) | **POST** /api/v1/storageLayers/{storageLayerID}/assignment | Create compartment assignment.
[**assignment_delete_assignment**](StorageAndEquipmentApi.md#assignment_delete_assignment) | **DELETE** /api/v1/storageLayers/assignment/{assignmentID} | Delete a compartment assignment.
[**assignment_get_assignment_by_storage_layer_id**](StorageAndEquipmentApi.md#assignment_get_assignment_by_storage_layer_id) | **GET** /api/v1/storageLayers/{storageLayerID}/assignment | Get active assignment of a compartment.
[**assignment_update_assignment**](StorageAndEquipmentApi.md#assignment_update_assignment) | **PUT** /api/v1/storageLayers/assignment/{assignmentID} | Update a compartment assignment.
[**booking_create_booking**](StorageAndEquipmentApi.md#booking_create_booking) | **POST** /api/v1/equipment/{equipmentID}/bookings | Create an equipment booking.
[**booking_delete_booking**](StorageAndEquipmentApi.md#booking_delete_booking) | **DELETE** /api/v1/equipment/bookings/{bookingID} | Delete an equipment booking.
[**booking_get_bookings**](StorageAndEquipmentApi.md#booking_get_bookings) | **GET** /api/v1/equipment/{equipmentID}/bookings | Get equipment bookings.
[**booking_update_booking**](StorageAndEquipmentApi.md#booking_update_booking) | **PUT** /api/v1/equipment/bookings/{bookingID} | Update an equipment booking.
[**storage_bulk_delete_storage_meta**](StorageAndEquipmentApi.md#storage_bulk_delete_storage_meta) | **DELETE** /api/v1/storage/meta/bulk | Delete multiple equipment or storage units meta fields
[**storage_bulk_patch_storage_meta**](StorageAndEquipmentApi.md#storage_bulk_patch_storage_meta) | **PATCH** /api/v1/storage/meta/bulk | Update multiple equipment or storage units meta fields
[**storage_create_bulk_storage_meta**](StorageAndEquipmentApi.md#storage_create_bulk_storage_meta) | **POST** /api/v1/storage/meta/bulk | Create multiple new equipment or storage unit meta fields
[**storage_create_child_storage_layer**](StorageAndEquipmentApi.md#storage_create_child_storage_layer) | **POST** /api/v1/storageLayers/{storageLayerID}/childLayers | Create a new compartment within an existing compartment
[**storage_create_child_storage_layers**](StorageAndEquipmentApi.md#storage_create_child_storage_layers) | **POST** /api/v1/storageLayers/{storageLayerID}/childLayers/bulk | Create multiple new compartments within an existing compartment
[**storage_create_storage**](StorageAndEquipmentApi.md#storage_create_storage) | **POST** /api/v1/storage | Create a new storage unit/equipment based on the specified type
[**storage_create_storage_layer_definition**](StorageAndEquipmentApi.md#storage_create_storage_layer_definition) | **POST** /api/v1/storage/{storageID}/storageLayerDefinitions | Create a new compartment definition for a storage unit. This is a template for creating one or more compartments.
[**storage_create_storage_layer_reservation**](StorageAndEquipmentApi.md#storage_create_storage_layer_reservation) | **POST** /api/v1/storageLayers/{storageLayerID}/reservations | Create a new storage/equipment compartment reservation
[**storage_create_storage_manager**](StorageAndEquipmentApi.md#storage_create_storage_manager) | **PUT** /api/v1/storage/{storageID}/managers | Add a userID as manager to a storage unit/equipment
[**storage_create_storage_managers**](StorageAndEquipmentApi.md#storage_create_storage_managers) | **PUT** /api/v1/storage/{storageID}/managers/bulk | Add multiple managers by userID to a storage unit/equipment
[**storage_create_storage_meta**](StorageAndEquipmentApi.md#storage_create_storage_meta) | **POST** /api/v1/storage/{storageID}/meta | Create a new equipment or storage unit meta field
[**storage_create_storage_type**](StorageAndEquipmentApi.md#storage_create_storage_type) | **POST** /api/v1/storageTypes | Create a new equipment type
[**storage_create_storage_validation**](StorageAndEquipmentApi.md#storage_create_storage_validation) | **POST** /api/v1/storage/{storageID}/validations | Create a new storage unit or equipment validation
[**storage_delete_storage_layer**](StorageAndEquipmentApi.md#storage_delete_storage_layer) | **DELETE** /api/v1/storageLayers/{storageLayerID} | Delete a storageLayer by storageLayerID
[**storage_delete_storage_layer_reservation**](StorageAndEquipmentApi.md#storage_delete_storage_layer_reservation) | **DELETE** /api/v1/storageLayers/{storageLayerID}/reservations/{storageLayerReservationID} | Delete a storage/equipment compartment reservation
[**storage_delete_storage_manager**](StorageAndEquipmentApi.md#storage_delete_storage_manager) | **DELETE** /api/v1/storage/{storageID}/managers/{userID} | Remove a manager from a storage unit/equipment by userID
[**storage_delete_storage_managers**](StorageAndEquipmentApi.md#storage_delete_storage_managers) | **DELETE** /api/v1/storage/{storageID}/managers/bulk | Remove multiple managers from a storage unit/equipment by userID
[**storage_delete_storage_meta**](StorageAndEquipmentApi.md#storage_delete_storage_meta) | **DELETE** /api/v1/storage/{storageID}/meta/{storageMetaID} | Delete an equipment meta field
[**storage_delete_storage_validation**](StorageAndEquipmentApi.md#storage_delete_storage_validation) | **DELETE** /api/v1/storage/{storageID}/validations/{storageValidationID} | Delete an equipment validation
[**storage_find_storage_free_location**](StorageAndEquipmentApi.md#storage_find_storage_free_location) | **GET** /api/v1/storage/{storageID}/freeLocation | Find a free sample location within a storage unit
[**storage_find_storage_layer_free_location**](StorageAndEquipmentApi.md#storage_find_storage_layer_free_location) | **GET** /api/v1/storageLayers/{storageLayerID}/freeLocation | Find a free sample location in or below a storage layer
[**storage_get_child_layers_by_id**](StorageAndEquipmentApi.md#storage_get_child_layers_by_id) | **GET** /api/v1/storageLayers/{storageLayerID}/childLayers | Get the storage compartments of a compartment
[**storage_get_child_layers_for_ids**](StorageAndEquipmentApi.md#storage_get_child_layers_for_ids) | **GET** /api/v1/storageLayers/childLayers | Get the storage compartments of several parent compartments
[**storage_get_empty_compartment_in_layer**](StorageAndEquipmentApi.md#storage_get_empty_compartment_in_layer) | **GET** /api/v1/storageLayers/{storageLayerID}/emptyStorageLayer | Find an empty compartment in a storage layer
[**storage_get_equipment_logs**](StorageAndEquipmentApi.md#storage_get_equipment_logs) | **GET** /api/v1/equipment/{storageID}/logs | Get full log of an equipment
[**storage_get_sample_logs**](StorageAndEquipmentApi.md#storage_get_sample_logs) | **GET** /api/v1/storage/{storageID}/samples/logs | Get a storage unit&#39;s sample logs
[**storage_get_storage**](StorageAndEquipmentApi.md#storage_get_storage) | **GET** /api/v1/storage | Get storage units/equipment
[**storage_get_storage_by_id**](StorageAndEquipmentApi.md#storage_get_storage_by_id) | **GET** /api/v1/storage/{storageID} | Get a storage unit/equipment by id
[**storage_get_storage_layer_ancestry**](StorageAndEquipmentApi.md#storage_get_storage_layer_ancestry) | **GET** /api/v1/storageLayers/{storageLayerID}/ancestry | Get the storage compartment ancestry of a compartment
[**storage_get_storage_layer_by_id**](StorageAndEquipmentApi.md#storage_get_storage_layer_by_id) | **GET** /api/v1/storageLayers/{storageLayerID} | Get a storage unit/equipment compartment by id
[**storage_get_storage_layer_definition_by_id**](StorageAndEquipmentApi.md#storage_get_storage_layer_definition_by_id) | **GET** /api/v1/storageLayerDefinitions/{storageLayerDefinitionID} | Get a compartment definition by id.
[**storage_get_storage_layer_definitions**](StorageAndEquipmentApi.md#storage_get_storage_layer_definitions) | **GET** /api/v1/storage/{storageID}/storageLayerDefinitions | Get all compartment definitions for a storage unit.
[**storage_get_storage_layer_logs**](StorageAndEquipmentApi.md#storage_get_storage_layer_logs) | **GET** /api/v1/storageLayers/{storageLayerID}/logs | Get a storage compartment&#39;s logs
[**storage_get_storage_layer_reservation**](StorageAndEquipmentApi.md#storage_get_storage_layer_reservation) | **GET** /api/v1/storageLayers/{storageLayerID}/reservations/{storageLayerReservationID} | Get a storage/equipment compartment reservation by id
[**storage_get_storage_layer_reservations**](StorageAndEquipmentApi.md#storage_get_storage_layer_reservations) | **GET** /api/v1/storageLayers/{storageLayerID}/reservations | Get all reservations of a storage/equipment compartment
[**storage_get_storage_layer_samples**](StorageAndEquipmentApi.md#storage_get_storage_layer_samples) | **GET** /api/v1/storageLayers/{storageLayerID}/samples | Get a storage layer&#39;s samples
[**storage_get_storage_layer_usage**](StorageAndEquipmentApi.md#storage_get_storage_layer_usage) | **GET** /api/v1/storagelayer/{storagelayerID}/usage | Get usage information on a specific storagelayer...
[**storage_get_storage_layers**](StorageAndEquipmentApi.md#storage_get_storage_layers) | **GET** /api/v1/storageLayers | Get storage unit/equipment compartments
[**storage_get_storage_layers_for_barcodes**](StorageAndEquipmentApi.md#storage_get_storage_layers_for_barcodes) | **GET** /api/v1/storageLayers/forBarcodes | Get a storage unit/equipment compartment by its barcode
[**storage_get_storage_logs**](StorageAndEquipmentApi.md#storage_get_storage_logs) | **GET** /api/v1/storage/{storageID}/logs | Get a storage unit&#39;s full logs
[**storage_get_storage_managers**](StorageAndEquipmentApi.md#storage_get_storage_managers) | **GET** /api/v1/storage/{storageID}/managers | Get all of a storage unit or equipment managers
[**storage_get_storage_meta**](StorageAndEquipmentApi.md#storage_get_storage_meta) | **GET** /api/v1/storage/{storageID}/meta/{storageMetaID} | Get an equipment or storage unit meta field by id
[**storage_get_storage_metas**](StorageAndEquipmentApi.md#storage_get_storage_metas) | **GET** /api/v1/storage/{storageID}/meta | Get all of a equipment or storage unit meta fields
[**storage_get_storage_report**](StorageAndEquipmentApi.md#storage_get_storage_report) | **GET** /api/v1/storage/{storageID}/report | Get an equipment reservations report
[**storage_get_storage_samples**](StorageAndEquipmentApi.md#storage_get_storage_samples) | **GET** /api/v1/storage/{storageID}/samples | Get a storage unit&#39;s samples
[**storage_get_storage_statistics**](StorageAndEquipmentApi.md#storage_get_storage_statistics) | **GET** /api/v1/storage/{storageID}/statistics | Get statistics for a storage unit
[**storage_get_storage_type_by_id**](StorageAndEquipmentApi.md#storage_get_storage_type_by_id) | **GET** /api/v1/storageTypes/{storageTypeID} | Get a storage unit/equipment type by id
[**storage_get_storage_types**](StorageAndEquipmentApi.md#storage_get_storage_types) | **GET** /api/v1/storageTypes | Get all storage unit/equipment types
[**storage_get_storage_validation**](StorageAndEquipmentApi.md#storage_get_storage_validation) | **GET** /api/v1/storage/{storageID}/validations/{storageValidationID} | Get an equipment validation by id
[**storage_get_storage_validations**](StorageAndEquipmentApi.md#storage_get_storage_validations) | **GET** /api/v1/storage/{storageID}/validations | Get all of an equipment&#39;s validations
[**storage_move_storage_layer_to_layer**](StorageAndEquipmentApi.md#storage_move_storage_layer_to_layer) | **POST** /api/v1/storageLayers/{storageLayerID}/moveToLayer/{newParentLayerID} | Move a storage compartment into another compartment
[**storage_patch_storage**](StorageAndEquipmentApi.md#storage_patch_storage) | **PATCH** /api/v1/storage/{storageID} | Update properties of a storage unit or equipment 
[**storage_patch_storage_layer**](StorageAndEquipmentApi.md#storage_patch_storage_layer) | **PATCH** /api/v1/storageLayers/{storageLayerID} | Update a storage compartment&#39;s properties
[**storage_patch_storage_layer_reservation**](StorageAndEquipmentApi.md#storage_patch_storage_layer_reservation) | **PATCH** /api/v1/storageLayers/{storageLayerID}/reservations/{storageLayerReservationID} | Update a storage/equipment compartment reservation
[**storage_patch_storage_meta**](StorageAndEquipmentApi.md#storage_patch_storage_meta) | **PATCH** /api/v1/storage/{storageID}/meta/{storageMetaID} | Update an equipment or storage unit meta field properties
[**storage_patch_storage_validation**](StorageAndEquipmentApi.md#storage_patch_storage_validation) | **PATCH** /api/v1/storage/{storageID}/validations/{storageValidationID} | Update an equipment validation properties


# **assignment_create_assignment**
> int assignment_create_assignment(storage_layer_id, assignment, x_requested_with=x_requested_with)

Create compartment assignment.

This call assigns a compartment. The assigned compartments descendants will also be assigned to the user or role.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
assignment = elabjournal_client.AssignmentNew() # AssignmentNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create compartment assignment.
    api_response = api_instance.assignment_create_assignment(storage_layer_id, assignment, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->assignment_create_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **assignment** | [**AssignmentNew**](AssignmentNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_delete_assignment**
> assignment_delete_assignment(assignment_id, x_requested_with=x_requested_with)

Delete a compartment assignment.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
assignment_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a compartment assignment.
    api_instance.assignment_delete_assignment(assignment_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->assignment_delete_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_get_assignment_by_storage_layer_id**
> Assignment assignment_get_assignment_by_storage_layer_id(storage_layer_id, x_requested_with=x_requested_with)

Get active assignment of a compartment.

This call gets the active assignment for a compartment.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get active assignment of a compartment.
    api_response = api_instance.assignment_get_assignment_by_storage_layer_id(storage_layer_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->assignment_get_assignment_by_storage_layer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**Assignment**](Assignment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_update_assignment**
> assignment_update_assignment(assignment_id, assignment, x_requested_with=x_requested_with)

Update a compartment assignment.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
assignment_id = 56 # int | 
assignment = elabjournal_client.AssignmentNew() # AssignmentNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a compartment assignment.
    api_instance.assignment_update_assignment(assignment_id, assignment, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->assignment_update_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**|  | 
 **assignment** | [**AssignmentNew**](AssignmentNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_create_booking**
> int booking_create_booking(equipment_id, booking, x_requested_with=x_requested_with)

Create an equipment booking.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
equipment_id = 56 # int | 
booking = elabjournal_client.BookingNew() # BookingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create an equipment booking.
    api_response = api_instance.booking_create_booking(equipment_id, booking, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->booking_create_booking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equipment_id** | **int**|  | 
 **booking** | [**BookingNew**](BookingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_delete_booking**
> booking_delete_booking(booking_id, x_requested_with=x_requested_with)

Delete an equipment booking.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
booking_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete an equipment booking.
    api_instance.booking_delete_booking(booking_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->booking_delete_booking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_get_bookings**
> booking_get_bookings(equipment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, _from=_from, to=to, x_requested_with=x_requested_with)

Get equipment bookings.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
equipment_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
_from = '_from_example' # str | Bookings where the start date/time is equal or greater than the given filter. (optional)
to = 'to_example' # str | Bookings where the end date/time is equal or less than the given filter. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get equipment bookings.
    api_instance.booking_get_bookings(equipment_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, _from=_from, to=to, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->booking_get_bookings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equipment_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **_from** | **str**| Bookings where the start date/time is equal or greater than the given filter. | [optional] 
 **to** | **str**| Bookings where the end date/time is equal or less than the given filter. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_update_booking**
> booking_update_booking(booking_id, booking, x_requested_with=x_requested_with)

Update an equipment booking.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
booking_id = 56 # int | 
booking = elabjournal_client.BookingNew() # BookingNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update an equipment booking.
    api_instance.booking_update_booking(booking_id, booking, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->booking_update_booking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_id** | **int**|  | 
 **booking** | [**BookingNew**](BookingNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_bulk_delete_storage_meta**
> storage_bulk_delete_storage_meta(storage_meta_ids, x_requested_with=x_requested_with)

Delete multiple equipment or storage units meta fields

This call will delete multiple equipment meta fields. To pass multiple storageMetaIDs the input has to be provided as an array e.g. '[1, 2, 3]'

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_meta_ids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete multiple equipment or storage units meta fields
    api_instance.storage_bulk_delete_storage_meta(storage_meta_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_bulk_delete_storage_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_meta_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_bulk_patch_storage_meta**
> storage_bulk_patch_storage_meta(delta, x_requested_with=x_requested_with)

Update multiple equipment or storage units meta fields

If you update a meta with type FILE you must supply a valid metaFileID of the file. See the Meta File calls. For other types the metaFileID is ignored.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
delta = [elabjournal_client.StorageMeta()] # list[StorageMeta] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update multiple equipment or storage units meta fields
    api_instance.storage_bulk_patch_storage_meta(delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_bulk_patch_storage_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delta** | [**list[StorageMeta]**](StorageMeta.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_bulk_storage_meta**
> list[StorageMeta] storage_create_bulk_storage_meta(dto, x_requested_with=x_requested_with)

Create multiple new equipment or storage unit meta fields

If you create a meta with type FILE you must supply a valid metaFileID of the file. See the Meta File calls. For other types the metaFileID is ignored.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
dto = [elabjournal_client.StorageMetaNewBulk()] # list[StorageMetaNewBulk] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create multiple new equipment or storage unit meta fields
    api_response = api_instance.storage_create_bulk_storage_meta(dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_bulk_storage_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**list[StorageMetaNewBulk]**](StorageMetaNewBulk.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[StorageMeta]**](StorageMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_child_storage_layer**
> int storage_create_child_storage_layer(storage_layer_id, storage_layer_new, x_requested_with=x_requested_with)

Create a new compartment within an existing compartment

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
storage_layer_new = elabjournal_client.StorageLayerNew() # StorageLayerNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new compartment within an existing compartment
    api_response = api_instance.storage_create_child_storage_layer(storage_layer_id, storage_layer_new, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_child_storage_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **storage_layer_new** | [**StorageLayerNew**](StorageLayerNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_child_storage_layers**
> list[int] storage_create_child_storage_layers(storage_layer_id, layers, x_requested_with=x_requested_with)

Create multiple new compartments within an existing compartment

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
layers = elabjournal_client.MultipleStorageLayerNew() # MultipleStorageLayerNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create multiple new compartments within an existing compartment
    api_response = api_instance.storage_create_child_storage_layers(storage_layer_id, layers, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_child_storage_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **layers** | [**MultipleStorageLayerNew**](MultipleStorageLayerNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**list[int]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage**
> StorageNewResult storage_create_storage(storage_new, x_requested_with=x_requested_with)

Create a new storage unit/equipment based on the specified type

  Note: this call can create either a storage unit or an equipment. This depends on the storageTypeID that you supply with this call. See the storageType calls.   

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_new = elabjournal_client.StorageNew() # StorageNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new storage unit/equipment based on the specified type
    api_response = api_instance.storage_create_storage(storage_new, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_new** | [**StorageNew**](StorageNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageNewResult**](StorageNewResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage_layer_definition**
> int storage_create_storage_layer_definition(storage_id, storage_layer_definition_new, x_requested_with=x_requested_with)

Create a new compartment definition for a storage unit. This is a template for creating one or more compartments.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
storage_layer_definition_new = elabjournal_client.StorageLayerDefinitionNew() # StorageLayerDefinitionNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new compartment definition for a storage unit. This is a template for creating one or more compartments.
    api_response = api_instance.storage_create_storage_layer_definition(storage_id, storage_layer_definition_new, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage_layer_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **storage_layer_definition_new** | [**StorageLayerDefinitionNew**](StorageLayerDefinitionNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage_layer_reservation**
> int storage_create_storage_layer_reservation(storage_layer_id, dto, x_requested_with=x_requested_with)

Create a new storage/equipment compartment reservation

Reservations must be created per compartment. For equipment simply use its main storageLayerID to reserve it. For storage units you can reserve a specific compartment by supplying its storageLayerID.    To create a permanent reservation omit the end date/time or set it to \"9999-12-31T00:00:00Z\".  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
dto = elabjournal_client.StorageLayerReservationNew() # StorageLayerReservationNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new storage/equipment compartment reservation
    api_response = api_instance.storage_create_storage_layer_reservation(storage_layer_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage_layer_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **dto** | [**StorageLayerReservationNew**](StorageLayerReservationNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage_manager**
> storage_create_storage_manager(storage_id, dto, x_requested_with=x_requested_with)

Add a userID as manager to a storage unit/equipment

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
dto = elabjournal_client.StorageManagerNew() # StorageManagerNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add a userID as manager to a storage unit/equipment
    api_instance.storage_create_storage_manager(storage_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **dto** | [**StorageManagerNew**](StorageManagerNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage_managers**
> storage_create_storage_managers(storage_id, user_ids, x_requested_with=x_requested_with)

Add multiple managers by userID to a storage unit/equipment

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
user_ids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Add multiple managers by userID to a storage unit/equipment
    api_instance.storage_create_storage_managers(storage_id, user_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **user_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage_meta**
> int storage_create_storage_meta(storage_id, dto, x_requested_with=x_requested_with)

Create a new equipment or storage unit meta field

  Note: only equipment currently supports meta fields. Creating these for storage units will have no effect.     If you create a meta with type FILE you must supply a valid metaFileID of the file. See the Meta File calls. For other types the metaFileID is ignored.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
dto = elabjournal_client.StorageMetaNew() # StorageMetaNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new equipment or storage unit meta field
    api_response = api_instance.storage_create_storage_meta(storage_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **dto** | [**StorageMetaNew**](StorageMetaNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage_type**
> int storage_create_storage_type(dto, x_requested_with=x_requested_with)

Create a new equipment type

  Note: the system only allows the creation of deviceType EQUIPMENT.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
dto = elabjournal_client.StorageTypeNew() # StorageTypeNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new equipment type
    api_response = api_instance.storage_create_storage_type(dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**StorageTypeNew**](StorageTypeNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_create_storage_validation**
> int storage_create_storage_validation(storage_id, dto, x_requested_with=x_requested_with)

Create a new storage unit or equipment validation

  Note: the hasValidation property of the equipment must be set to true before validation checking is enabled.   Both metaFileID and metaFileIDs are optional. If multiple validation files need to be added metaFileIDs has to be used.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
dto = elabjournal_client.StorageValidationNew() # StorageValidationNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create a new storage unit or equipment validation
    api_response = api_instance.storage_create_storage_validation(storage_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_create_storage_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **dto** | [**StorageValidationNew**](StorageValidationNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_delete_storage_layer**
> storage_delete_storage_layer(storage_layer_id, archive_samples=archive_samples, delete_storage_layer_samples_behaviour=delete_storage_layer_samples_behaviour, x_requested_with=x_requested_with)

Delete a storageLayer by storageLayerID

If the storage layer contains samples, use the deleteStorageLayerSamplesBehaviour parameter to specify whether the samples should be archived or moved to the parent storage layer.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
archive_samples = true # bool | deprecated (optional)
delete_storage_layer_samples_behaviour = 'delete_storage_layer_samples_behaviour_example' # str |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a storageLayer by storageLayerID
    api_instance.storage_delete_storage_layer(storage_layer_id, archive_samples=archive_samples, delete_storage_layer_samples_behaviour=delete_storage_layer_samples_behaviour, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_delete_storage_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **archive_samples** | **bool**| deprecated | [optional] 
 **delete_storage_layer_samples_behaviour** | **str**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_delete_storage_layer_reservation**
> storage_delete_storage_layer_reservation(storage_layer_id, storage_layer_reservation_id, x_requested_with=x_requested_with)

Delete a storage/equipment compartment reservation

Only a storage manager or the user who originally created the reservation may delete a reservation.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
storage_layer_reservation_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete a storage/equipment compartment reservation
    api_instance.storage_delete_storage_layer_reservation(storage_layer_id, storage_layer_reservation_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_delete_storage_layer_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **storage_layer_reservation_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_delete_storage_manager**
> storage_delete_storage_manager(storage_id, user_id, x_requested_with=x_requested_with)

Remove a manager from a storage unit/equipment by userID

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
user_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove a manager from a storage unit/equipment by userID
    api_instance.storage_delete_storage_manager(storage_id, user_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_delete_storage_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
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

# **storage_delete_storage_managers**
> storage_delete_storage_managers(storage_id, user_ids, x_requested_with=x_requested_with)

Remove multiple managers from a storage unit/equipment by userID

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
user_ids = [elabjournal_client.list[int]()] # list[int] | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Remove multiple managers from a storage unit/equipment by userID
    api_instance.storage_delete_storage_managers(storage_id, user_ids, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_delete_storage_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **user_ids** | **list[int]**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_delete_storage_meta**
> storage_delete_storage_meta(storage_id, storage_meta_id, x_requested_with=x_requested_with)

Delete an equipment meta field

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
storage_meta_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete an equipment meta field
    api_instance.storage_delete_storage_meta(storage_id, storage_meta_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_delete_storage_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **storage_meta_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_delete_storage_validation**
> storage_delete_storage_validation(storage_id, storage_validation_id, x_requested_with=x_requested_with)

Delete an equipment validation

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
storage_validation_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Delete an equipment validation
    api_instance.storage_delete_storage_validation(storage_id, storage_validation_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_delete_storage_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **storage_validation_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_find_storage_free_location**
> Location storage_find_storage_free_location(storage_id, consecutive_space=consecutive_space, x_requested_with=x_requested_with)

Find a free sample location within a storage unit

This call finds the first free location within the storage unit's sample boxes.    You can specify the amount of consecutive places that you require with the consecutiveSpace parameter. By default this is set to 1.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
consecutive_space = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Find a free sample location within a storage unit
    api_response = api_instance.storage_find_storage_free_location(storage_id, consecutive_space=consecutive_space, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_find_storage_free_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **consecutive_space** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**Location**](Location.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_find_storage_layer_free_location**
> Location storage_find_storage_layer_free_location(storage_layer_id, consecutive_space=consecutive_space, x_requested_with=x_requested_with)

Find a free sample location in or below a storage layer

This call finds the first free location in the specified storage layer (if it's a sample box) or below it (if it's contains sample boxes).    You can specify the amount of consecutive places that you require with the consecutiveSpace parameter. By default this is set to 1.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
consecutive_space = 56 # int |  (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Find a free sample location in or below a storage layer
    api_response = api_instance.storage_find_storage_layer_free_location(storage_layer_id, consecutive_space=consecutive_space, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_find_storage_layer_free_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **consecutive_space** | **int**|  | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**Location**](Location.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_child_layers_by_id**
> PagedOfStorageLayerLarge storage_get_child_layers_by_id(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, barcodes=barcodes, storage_id=storage_id, name=name, x_requested_with=x_requested_with)

Get the storage compartments of a compartment

  $expand values (separate with a comma for multiple expands):  * storage  * location  * storageLayers  * samples  * managers  * reservations / allReservations  * statistics  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
barcodes = 'barcodes_example' # str | Filter by barcodes (comma-separated) (optional)
storage_id = 'storage_id_example' # str | Filter by storageID (optional)
name = 'name_example' # str | Filter by name (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the storage compartments of a compartment
    api_response = api_instance.storage_get_child_layers_by_id(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, barcodes=barcodes, storage_id=storage_id, name=name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_child_layers_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **barcodes** | **str**| Filter by barcodes (comma-separated) | [optional] 
 **storage_id** | **str**| Filter by storageID | [optional] 
 **name** | **str**| Filter by name | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageLayerLarge**](PagedOfStorageLayerLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_child_layers_for_ids**
> PagedOfStorageLayerLarge storage_get_child_layers_for_ids(parent_storage_layer_ids, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the storage compartments of several parent compartments

  $expand values (separate with a comma for multiple expands):  * storage  * location  * storageLayers  * samples  * managers  * reservations / allReservations  * statistics  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
parent_storage_layer_ids = [56] # list[int] | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the storage compartments of several parent compartments
    api_response = api_instance.storage_get_child_layers_for_ids(parent_storage_layer_ids, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_child_layers_for_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_storage_layer_ids** | [**list[int]**](int.md)|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageLayerLarge**](PagedOfStorageLayerLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_empty_compartment_in_layer**
> StorageLayer storage_get_empty_compartment_in_layer(storage_layer_id, storage_layer_definition_id, x_requested_with=x_requested_with)

Find an empty compartment in a storage layer

This endpoint can be used to find a empty storage compartment in a storage tree that has a maximum of       six layers. Both the storageLayerID and the storageLayerDefinitionID is necessary to perform the search.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
storage_layer_definition_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Find an empty compartment in a storage layer
    api_response = api_instance.storage_get_empty_compartment_in_layer(storage_layer_id, storage_layer_definition_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_empty_compartment_in_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **storage_layer_definition_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageLayer**](StorageLayer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_equipment_logs**
> PagedOfEquipmentLogLarge storage_get_equipment_logs(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get full log of an equipment

Note: this call only shows logs for equipment, not storage units.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get full log of an equipment
    api_response = api_instance.storage_get_equipment_logs(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_equipment_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfEquipmentLogLarge**](PagedOfEquipmentLogLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_sample_logs**
> PagedOfSampleLogLarge storage_get_sample_logs(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, action=action, sample_meta_key=sample_meta_key, storage_layer_id=storage_layer_id, user_id=user_id, storage_id2=storage_id2, x_requested_with=x_requested_with)

Get a storage unit's sample logs

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
action = 'action_example' # str | Filter by action (CREATE/UPDATE/DELETE) (optional)
sample_meta_key = 'sample_meta_key_example' # str | Filter by a sample field (including \"Location\") (optional)
storage_layer_id = 'storage_layer_id_example' # str | Filter for samples in a storage layer (optional)
user_id = 'user_id_example' # str | Filter by the user who made the change (optional)
storage_id2 = 'storage_id_example' # str | Filter for samples in a storage unit (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage unit's sample logs
    api_response = api_instance.storage_get_sample_logs(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, action=action, sample_meta_key=sample_meta_key, storage_layer_id=storage_layer_id, user_id=user_id, storage_id2=storage_id2, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_sample_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **action** | **str**| Filter by action (CREATE/UPDATE/DELETE) | [optional] 
 **sample_meta_key** | **str**| Filter by a sample field (including \&quot;Location\&quot;) | [optional] 
 **storage_layer_id** | **str**| Filter for samples in a storage layer | [optional] 
 **user_id** | **str**| Filter by the user who made the change | [optional] 
 **storage_id2** | **str**| Filter for samples in a storage unit | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLogLarge**](PagedOfSampleLogLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage**
> PagedOfStorageLarge storage_get_storage(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, storage_type_id=storage_type_id, name=name, storage_type_name=storage_type_name, device_type=device_type, storage_meta_name=storage_meta_name, x_requested_with=x_requested_with)

Get storage units/equipment

  Note: the storage calls can return both storage units and equipment. You can differentiate between the two with the storage type's deviceType field which is either STORAGE or EQUIPMENT.     The hasPlanner and hasValidation properties are required for an EQUIPMENT storageType.    Setting hasPlanner to true will show the equipment calendar in eLab.    Setting hasValidation to true will show the equipment validation options in eLab and enable checking the validation. See the storageValidation calls. This is only supported for equipment, not storage units.    $expand values (separate with a comma for multiple expands):  * storageLayer  * managers  * institute  * meta    Note: the expand `statistics` is not available for this call because it's a resource intensive operation. You can only get a storage unit's statistics with the `GET /storage/{storageID}` call.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
storage_type_id = 'storage_type_id_example' # str | Filter by storageTypeID (optional)
name = 'name_example' # str | Filter by name (optional)
storage_type_name = 'storage_type_name_example' # str | Filter by the storageType name (optional)
device_type = 'device_type_example' # str | Filter by the storage type's device type (STORAGE or EQUIPMENT) (optional)
storage_meta_name = 'storage_meta_name_example' # str | Filter by storageMeta name (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get storage units/equipment
    api_response = api_instance.storage_get_storage(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, storage_type_id=storage_type_id, name=name, storage_type_name=storage_type_name, device_type=device_type, storage_meta_name=storage_meta_name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage: %s\n" % e)
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
 **storage_type_id** | **str**| Filter by storageTypeID | [optional] 
 **name** | **str**| Filter by name | [optional] 
 **storage_type_name** | **str**| Filter by the storageType name | [optional] 
 **device_type** | **str**| Filter by the storage type&#39;s device type (STORAGE or EQUIPMENT) | [optional] 
 **storage_meta_name** | **str**| Filter by storageMeta name | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageLarge**](PagedOfStorageLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_by_id**
> StorageLarge storage_get_storage_by_id(storage_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a storage unit/equipment by id

  $expand values (separate with a comma for multiple expands):  * storageLayer  * managers  * statistics  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage unit/equipment by id
    api_response = api_instance.storage_get_storage_by_id(storage_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageLarge**](StorageLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_ancestry**
> StorageLayerHierarchy storage_get_storage_layer_ancestry(storage_layer_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get the storage compartment ancestry of a compartment

  $expand values (separate with a comma for multiple expands):  * activeReservation  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get the storage compartment ancestry of a compartment
    api_response = api_instance.storage_get_storage_layer_ancestry(storage_layer_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_ancestry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageLayerHierarchy**](StorageLayerHierarchy.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_by_id**
> StorageLayerLarge storage_get_storage_layer_by_id(storage_layer_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a storage unit/equipment compartment by id

  $expand values (separate with a comma for multiple expands):  * storage  * location  * storageLayers  * samples  * managers  * reservations / allReservations  * statistics    Note: if you use the expand `storageLayers` and `statistics` simultaneously then statistics will also be added for the child storage layers.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage unit/equipment compartment by id
    api_response = api_instance.storage_get_storage_layer_by_id(storage_layer_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageLayerLarge**](StorageLayerLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_definition_by_id**
> StorageLayerDefinition storage_get_storage_layer_definition_by_id(storage_layer_definition_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a compartment definition by id.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_definition_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a compartment definition by id.
    api_response = api_instance.storage_get_storage_layer_definition_by_id(storage_layer_definition_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_definition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_definition_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageLayerDefinition**](StorageLayerDefinition.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_definitions**
> PagedOfStorageLayerDefinition storage_get_storage_layer_definitions(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, deleted=deleted, x_requested_with=x_requested_with)

Get all compartment definitions for a storage unit.

  $expand values (separate with a comma for multiple expands):  * storageLayer  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
deleted = 'deleted_example' # str | Filter by deleted (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all compartment definitions for a storage unit.
    api_response = api_instance.storage_get_storage_layer_definitions(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, deleted=deleted, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **deleted** | **str**| Filter by deleted | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageLayerDefinition**](PagedOfStorageLayerDefinition.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_logs**
> PagedOfStorageLog storage_get_storage_layer_logs(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a storage compartment's logs

Note: these are a subset of a storage unit's logs dealing with this specific compartment.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage compartment's logs
    api_response = api_instance.storage_get_storage_layer_logs(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageLog**](PagedOfStorageLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_reservation**
> StorageLayerReservation storage_get_storage_layer_reservation(storage_layer_id, storage_layer_reservation_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a storage/equipment compartment reservation by id

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
storage_layer_reservation_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage/equipment compartment reservation by id
    api_response = api_instance.storage_get_storage_layer_reservation(storage_layer_id, storage_layer_reservation_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **storage_layer_reservation_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageLayerReservation**](StorageLayerReservation.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_reservations**
> storage_get_storage_layer_reservations(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, not_expired=not_expired, is_permanent=is_permanent, end=end, _from=_from, reservation_type=reservation_type, reserved_for_id=reserved_for_id, created_by_user_id=created_by_user_id, start=start, to=to, x_requested_with=x_requested_with)

Get all reservations of a storage/equipment compartment

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
not_expired = 'not_expired_example' # str | Filter by non-expired reservations (true/false) (optional)
is_permanent = 'is_permanent_example' # str | Filter by (non-)permanent reservations (true/false) (optional)
end = 'end_example' # str | Filter by the exact end date/time (optional)
_from = '_from_example' # str | Search for reservations starting from this date/time (optional)
reservation_type = 'reservation_type_example' # str | Filter by UserReservation or RoleReservation (optional)
reserved_for_id = 'reserved_for_id_example' # str | Filter by the ID (a userID or a roleID) for which reservations were made (optional)
created_by_user_id = 'created_by_user_id_example' # str | Filter by the userID who created the reservation (optional)
start = 'start_example' # str | Filter by the exact start date/time (optional)
to = 'to_example' # str | Search for reservations ending at this date/time (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all reservations of a storage/equipment compartment
    api_instance.storage_get_storage_layer_reservations(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, not_expired=not_expired, is_permanent=is_permanent, end=end, _from=_from, reservation_type=reservation_type, reserved_for_id=reserved_for_id, created_by_user_id=created_by_user_id, start=start, to=to, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **not_expired** | **str**| Filter by non-expired reservations (true/false) | [optional] 
 **is_permanent** | **str**| Filter by (non-)permanent reservations (true/false) | [optional] 
 **end** | **str**| Filter by the exact end date/time | [optional] 
 **_from** | **str**| Search for reservations starting from this date/time | [optional] 
 **reservation_type** | **str**| Filter by UserReservation or RoleReservation | [optional] 
 **reserved_for_id** | **str**| Filter by the ID (a userID or a roleID) for which reservations were made | [optional] 
 **created_by_user_id** | **str**| Filter by the userID who created the reservation | [optional] 
 **start** | **str**| Filter by the exact start date/time | [optional] 
 **to** | **str**| Search for reservations ending at this date/time | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_samples**
> PagedOfSampleLarge storage_get_storage_layer_samples(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, sample_type_id=sample_type_id, barcodes=barcodes, name=name, search=search, quantity_id=quantity_id, minimum_quantity_amount=minimum_quantity_amount, checked_out=checked_out, x_requested_with=x_requested_with)

Get a storage layer's samples

$expand values (separate with a comma for multiple expands):  * location  * quantity  * meta  * experiments  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
sample_type_id = 'sample_type_id_example' # str | Filter by sampleTypeID (optional)
barcodes = 'barcodes_example' # str | Filter by barcodes (comma-separated) (optional)
name = 'name_example' # str | Filter by sample name (optional)
search = 'search_example' # str | Search term to use for filtering samples. (optional)
quantity_id = 'quantity_id_example' # str | Filter by quantityID (optional)
minimum_quantity_amount = 'minimum_quantity_amount_example' # str | Filter for samples that have a minimum quantity amount set (optional)
checked_out = 'checked_out_example' # str | Filter for checked out samples (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage layer's samples
    api_response = api_instance.storage_get_storage_layer_samples(storage_layer_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, sample_type_id=sample_type_id, barcodes=barcodes, name=name, search=search, quantity_id=quantity_id, minimum_quantity_amount=minimum_quantity_amount, checked_out=checked_out, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **sample_type_id** | **str**| Filter by sampleTypeID | [optional] 
 **barcodes** | **str**| Filter by barcodes (comma-separated) | [optional] 
 **name** | **str**| Filter by sample name | [optional] 
 **search** | **str**| Search term to use for filtering samples. | [optional] 
 **quantity_id** | **str**| Filter by quantityID | [optional] 
 **minimum_quantity_amount** | **str**| Filter for samples that have a minimum quantity amount set | [optional] 
 **checked_out** | **str**| Filter for checked out samples | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLarge**](PagedOfSampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layer_usage**
> list[StorageUnitUsage] storage_get_storage_layer_usage(storagelayer_id, x_requested_with=x_requested_with)

Get usage information on a specific storagelayer...

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storagelayer_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get usage information on a specific storagelayer...
    api_response = api_instance.storage_get_storage_layer_usage(storagelayer_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layer_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagelayer_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**list[StorageUnitUsage]**](StorageUnitUsage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layers**
> PagedOfStorageLayerLarge storage_get_storage_layers(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, parent_storage_layer_id=parent_storage_layer_id, parent_storage_layer_ids=parent_storage_layer_ids, storage_id=storage_id, barcodes=barcodes, name=name, x_requested_with=x_requested_with)

Get storage unit/equipment compartments

  $expand values (separate with a comma for multiple expands):  * storage  * location  * storageLayers  * samples  * managers  * reservations / allReservations    Note: the expand `statistics` is not available for this call because it's a resource intensive operation. You can only get a layer's statistics with the `GET /storageLayer/{storageLayerID}` call.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
parent_storage_layer_id = 'parent_storage_layer_id_example' # str | Filter by parentStorageLayerID (optional)
parent_storage_layer_ids = 'parent_storage_layer_ids_example' # str | Filter by parentStorageLayerIDs (comma-separated) (optional)
storage_id = 'storage_id_example' # str | Filter by storageID (optional)
barcodes = 'barcodes_example' # str | Filter by barcodes (comma-separated) (optional)
name = 'name_example' # str | Filter by name (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get storage unit/equipment compartments
    api_response = api_instance.storage_get_storage_layers(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, parent_storage_layer_id=parent_storage_layer_id, parent_storage_layer_ids=parent_storage_layer_ids, storage_id=storage_id, barcodes=barcodes, name=name, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layers: %s\n" % e)
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
 **parent_storage_layer_id** | **str**| Filter by parentStorageLayerID | [optional] 
 **parent_storage_layer_ids** | **str**| Filter by parentStorageLayerIDs (comma-separated) | [optional] 
 **storage_id** | **str**| Filter by storageID | [optional] 
 **barcodes** | **str**| Filter by barcodes (comma-separated) | [optional] 
 **name** | **str**| Filter by name | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageLayerLarge**](PagedOfStorageLayerLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_layers_for_barcodes**
> PagedOfStorageLayerLarge storage_get_storage_layers_for_barcodes(barcodes, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a storage unit/equipment compartment by its barcode

  $expand values (separate with a comma for multiple expands):  * storage  * location  * storageLayers  * samples  * managers  * reservations / allReservations  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
barcodes = ['barcodes_example'] # list[str] | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage unit/equipment compartment by its barcode
    api_response = api_instance.storage_get_storage_layers_for_barcodes(barcodes, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_layers_for_barcodes: %s\n" % e)
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

[**PagedOfStorageLayerLarge**](PagedOfStorageLayerLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_logs**
> PagedOfStorageLogLarge storage_get_storage_logs(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a storage unit's full logs

Note: this call only shows logs for storage units, not equipment.    The logs include all changes to a storage unit's compartments as well.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage unit's full logs
    api_response = api_instance.storage_get_storage_logs(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageLogLarge**](PagedOfStorageLogLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_managers**
> PagedOfStorageManager storage_get_storage_managers(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all of a storage unit or equipment managers

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all of a storage unit or equipment managers
    api_response = api_instance.storage_get_storage_managers(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageManager**](PagedOfStorageManager.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_meta**
> StorageMeta storage_get_storage_meta(storage_id, storage_meta_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get an equipment or storage unit meta field by id

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
storage_meta_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an equipment or storage unit meta field by id
    api_response = api_instance.storage_get_storage_meta(storage_id, storage_meta_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **storage_meta_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageMeta**](StorageMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_metas**
> PagedOfStorageMeta storage_get_storage_metas(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all of a equipment or storage unit meta fields

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all of a equipment or storage unit meta fields
    api_response = api_instance.storage_get_storage_metas(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_metas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageMeta**](PagedOfStorageMeta.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_report**
> storage_get_storage_report(storage_id, start, end, x_requested_with=x_requested_with)

Get an equipment reservations report

This call downloads an equipment report .csv file. Reports will only work with equipment type devices. N.B. It is currently not possible to run this from Swagger. 'Start' and 'end' are the start date and end date of the report. The correct date format is: 'yyyy-MM-dd HH:mm:ss'

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an equipment reservations report
    api_instance.storage_get_storage_report(storage_id, start, end, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_samples**
> PagedOfSampleLarge storage_get_storage_samples(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, quantity_id=quantity_id, barcodes=barcodes, sample_type_id=sample_type_id, name=name, minimum_quantity_amount=minimum_quantity_amount, checked_out=checked_out, search=search, x_requested_with=x_requested_with)

Get a storage unit's samples

$expand values (separate with a comma for multiple expands):  * location  * quantity  * meta  * experiments  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
quantity_id = 'quantity_id_example' # str | Filter by quantityID (optional)
barcodes = 'barcodes_example' # str | Filter by barcodes (comma-separated) (optional)
sample_type_id = 'sample_type_id_example' # str | Filter by sampleTypeID (optional)
name = 'name_example' # str | Filter by sample name (optional)
minimum_quantity_amount = 'minimum_quantity_amount_example' # str | Filter for samples that have a minimum quantity amount set (optional)
checked_out = 'checked_out_example' # str | Filter for checked out samples (optional)
search = 'search_example' # str | Search term to use for filtering samples. (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage unit's samples
    api_response = api_instance.storage_get_storage_samples(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, quantity_id=quantity_id, barcodes=barcodes, sample_type_id=sample_type_id, name=name, minimum_quantity_amount=minimum_quantity_amount, checked_out=checked_out, search=search, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **quantity_id** | **str**| Filter by quantityID | [optional] 
 **barcodes** | **str**| Filter by barcodes (comma-separated) | [optional] 
 **sample_type_id** | **str**| Filter by sampleTypeID | [optional] 
 **name** | **str**| Filter by sample name | [optional] 
 **minimum_quantity_amount** | **str**| Filter for samples that have a minimum quantity amount set | [optional] 
 **checked_out** | **str**| Filter for checked out samples | [optional] 
 **search** | **str**| Search term to use for filtering samples. | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfSampleLarge**](PagedOfSampleLarge.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_statistics**
> StorageStatistics storage_get_storage_statistics(storage_id, x_requested_with=x_requested_with)

Get statistics for a storage unit

  The following statistics are returned:  * totalSamples - the amount of samples in all storage layers  * totalGridLayers - the amount of grid (i.e. multi-dimensional) storage layers  * totalFilledBoxes - the amount of grid layers that are fully filled with samples  * totalBoxPositions - the total amount of positions in all grid layers  * totalFilledPositions - the total amount of grid positions that have samples in them  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get statistics for a storage unit
    api_response = api_instance.storage_get_storage_statistics(storage_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageStatistics**](StorageStatistics.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_type_by_id**
> StorageType storage_get_storage_type_by_id(storage_type_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get a storage unit/equipment type by id

  Note: the storage calls can return both storage units and equipment. You can differentiate between the two with the storage type's deviceType field which is either STORAGE or EQUIPMENT.   

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_type_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a storage unit/equipment type by id
    api_response = api_instance.storage_get_storage_type_by_id(storage_type_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_type_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageType**](StorageType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_types**
> PagedOfStorageType storage_get_storage_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all storage unit/equipment types

  Note: the storage calls can return both storage units and equipment. You can differentiate between the two with the storage type's deviceType field which is either STORAGE or EQUIPMENT.   

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all storage unit/equipment types
    api_response = api_instance.storage_get_storage_types(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_types: %s\n" % e)
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

[**PagedOfStorageType**](PagedOfStorageType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_validation**
> StorageValidation storage_get_storage_validation(storage_id, storage_validation_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get an equipment validation by id

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
storage_validation_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get an equipment validation by id
    api_response = api_instance.storage_get_storage_validation(storage_id, storage_validation_id, expand=expand, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **storage_validation_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**StorageValidation**](StorageValidation.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_get_storage_validations**
> PagedOfStorageValidation storage_get_storage_validations(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)

Get all of an equipment's validations

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get all of an equipment's validations
    api_response = api_instance.storage_get_storage_validations(storage_id, expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_get_storage_validations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **expand** | **str**| Expand an ID field to an object | [optional] 
 **sort** | **str**| Sort by a specific field | [optional] 
 **page** | **str**| Set the current page (0 based) | [optional] 
 **records** | **str**| Set the number of records to return (1000 maximum) | [optional] 
 **view_id** | **str**| Specify a viewID to customize the result | [optional] 
 **view_columns** | **str**| Specify viewColumns to extend the result | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfStorageValidation**](PagedOfStorageValidation.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_move_storage_layer_to_layer**
> storage_move_storage_layer_to_layer(storage_layer_id, new_parent_layer_id, x_requested_with=x_requested_with)

Move a storage compartment into another compartment

Note: you can not move a compartment into a box, only into other compartment types.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
new_parent_layer_id = 56 # int | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Move a storage compartment into another compartment
    api_instance.storage_move_storage_layer_to_layer(storage_layer_id, new_parent_layer_id, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_move_storage_layer_to_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **new_parent_layer_id** | **int**|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_patch_storage**
> storage_patch_storage(storage_id, delta, x_requested_with=x_requested_with)

Update properties of a storage unit or equipment 

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
delta = elabjournal_client.StorageNew() # StorageNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update properties of a storage unit or equipment 
    api_instance.storage_patch_storage(storage_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_patch_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **delta** | [**StorageNew**](StorageNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_patch_storage_layer**
> storage_patch_storage_layer(storage_layer_id, delta, x_requested_with=x_requested_with)

Update a storage compartment's properties

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
delta = elabjournal_client.StorageLayerUpdate() # StorageLayerUpdate | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a storage compartment's properties
    api_instance.storage_patch_storage_layer(storage_layer_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_patch_storage_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **delta** | [**StorageLayerUpdate**](StorageLayerUpdate.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_patch_storage_layer_reservation**
> storage_patch_storage_layer_reservation(storage_layer_id, storage_layer_reservation_id, delta, x_requested_with=x_requested_with)

Update a storage/equipment compartment reservation

To change to a permanent reservation set the end date/time to \"9999-12-31T00:00:00Z\".    Only a storage manager or the user who originally created the reservation may update a reservation.  

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_layer_id = 56 # int | 
storage_layer_reservation_id = 56 # int | 
delta = elabjournal_client.StorageLayerReservationNew() # StorageLayerReservationNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update a storage/equipment compartment reservation
    api_instance.storage_patch_storage_layer_reservation(storage_layer_id, storage_layer_reservation_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_patch_storage_layer_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_layer_id** | **int**|  | 
 **storage_layer_reservation_id** | **int**|  | 
 **delta** | [**StorageLayerReservationNew**](StorageLayerReservationNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_patch_storage_meta**
> storage_patch_storage_meta(storage_id, storage_meta_id, delta, x_requested_with=x_requested_with)

Update an equipment or storage unit meta field properties

If you update a meta with type FILE you must supply a valid metaFileID of the file. See the Meta File calls. For other types the metaFileID is ignored.

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
storage_meta_id = 56 # int | 
delta = elabjournal_client.StorageMeta() # StorageMeta | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update an equipment or storage unit meta field properties
    api_instance.storage_patch_storage_meta(storage_id, storage_meta_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_patch_storage_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **storage_meta_id** | **int**|  | 
 **delta** | [**StorageMeta**](StorageMeta.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_patch_storage_validation**
> storage_patch_storage_validation(storage_id, storage_validation_id, delta, x_requested_with=x_requested_with)

Update an equipment validation properties

### Example
```python
from __future__ import print_function
import time
import elabjournal_client
from elabjournal_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = elabjournal_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = elabjournal_client.StorageAndEquipmentApi(elabjournal_client.ApiClient(configuration))
storage_id = 56 # int | 
storage_validation_id = 56 # int | 
delta = elabjournal_client.StorageValidationNew() # StorageValidationNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update an equipment validation properties
    api_instance.storage_patch_storage_validation(storage_id, storage_validation_id, delta, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling StorageAndEquipmentApi->storage_patch_storage_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | 
 **storage_validation_id** | **int**|  | 
 **delta** | [**StorageValidationNew**](StorageValidationNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

