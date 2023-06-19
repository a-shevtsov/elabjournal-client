# elabjournal_client.SuppliesApi

All URIs are relative to *https://www.elabjournal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_item_get_catalog_items**](SuppliesApi.md#catalog_item_get_catalog_items) | **GET** /api/v1/supplies/catalogitems | Get a list of catalog items
[**order_create_order**](SuppliesApi.md#order_create_order) | **POST** /api/v1/supplies/orders/{sampleID} | Create new order
[**order_get_orders**](SuppliesApi.md#order_get_orders) | **GET** /api/v1/supplies/orders | Get a list of orders
[**order_update_order**](SuppliesApi.md#order_update_order) | **PUT** /api/v1/supplies/orders/{orderID} | Update order


# **catalog_item_get_catalog_items**
> PagedOfCatalogItem catalog_item_get_catalog_items(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, quantity=quantity, name=name, catalog_item_id=catalog_item_id, supplier_id=supplier_id, x_requested_with=x_requested_with)

Get a list of catalog items

Gets catalog items associated with the current working group. The data can be filtered by   supplierID, quantity and the name of the catalog item. The endpoint name parameter supports partial matches for  the catalog name. The items within the catalog can also be sorted by `name`, `calalogNumber`, `supplierID`

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
api_instance = elabjournal_client.SuppliesApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
quantity = 'quantity_example' # str | Filter by quantity type (optional)
name = 'name_example' # str | Search catalog items by name (optional)
catalog_item_id = 'catalog_item_id_example' # str | Search catalog items by catalogItemID (optional)
supplier_id = 'supplier_id_example' # str | Filter by suplier ID (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of catalog items
    api_response = api_instance.catalog_item_get_catalog_items(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, quantity=quantity, name=name, catalog_item_id=catalog_item_id, supplier_id=supplier_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliesApi->catalog_item_get_catalog_items: %s\n" % e)
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
 **quantity** | **str**| Filter by quantity type | [optional] 
 **name** | **str**| Search catalog items by name | [optional] 
 **catalog_item_id** | **str**| Search catalog items by catalogItemID | [optional] 
 **supplier_id** | **str**| Filter by suplier ID | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfCatalogItem**](PagedOfCatalogItem.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_create_order**
> int order_create_order(sample_id, dto, x_requested_with=x_requested_with)

Create new order

Add a new order for the given sample, catalogItemID with a given amount

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
api_instance = elabjournal_client.SuppliesApi(elabjournal_client.ApiClient(configuration))
sample_id = 56 # int | 
dto = elabjournal_client.ShoppingItemNew() # ShoppingItemNew | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Create new order
    api_response = api_instance.order_create_order(sample_id, dto, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliesApi->order_create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**|  | 
 **dto** | [**ShoppingItemNew**](ShoppingItemNew.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_orders**
> PagedOfShoppingItem order_get_orders(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, status=status, sample_id=sample_id, catalog_item_id=catalog_item_id, x_requested_with=x_requested_with)

Get a list of orders

Retrieves a paged list of shopping items associated with the current working group, passed in catalogItemID.

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
api_instance = elabjournal_client.SuppliesApi(elabjournal_client.ApiClient(configuration))
expand = 'expand_example' # str | Expand an ID field to an object (optional)
sort = 'sort_example' # str | Sort by a specific field (optional)
page = 'page_example' # str | Set the current page (0 based) (optional)
records = 'records_example' # str | Set the number of records to return (1000 maximum) (optional)
view_id = 'view_id_example' # str | Specify a viewID to customize the result (optional)
view_columns = 'view_columns_example' # str | Specify viewColumns to extend the result (optional)
status = 'status_example' # str | Filter by status, fetch shopping items which have the given status (multiple options can be selected as a comma seperated string). Valid options here are [PENDING,ORDERED,RECEIVED,COMPLETED] (optional)
sample_id = 'sample_id_example' # str | Filter sampleID (optional)
catalog_item_id = 'catalog_item_id_example' # str | Filter by catalogitemID (optional)
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Get a list of orders
    api_response = api_instance.order_get_orders(expand=expand, sort=sort, page=page, records=records, view_id=view_id, view_columns=view_columns, status=status, sample_id=sample_id, catalog_item_id=catalog_item_id, x_requested_with=x_requested_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliesApi->order_get_orders: %s\n" % e)
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
 **status** | **str**| Filter by status, fetch shopping items which have the given status (multiple options can be selected as a comma seperated string). Valid options here are [PENDING,ORDERED,RECEIVED,COMPLETED] | [optional] 
 **sample_id** | **str**| Filter sampleID | [optional] 
 **catalog_item_id** | **str**| Filter by catalogitemID | [optional] 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

[**PagedOfShoppingItem**](PagedOfShoppingItem.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_update_order**
> order_update_order(order_id, dto, x_requested_with=x_requested_with)

Update order

Update the order of the given orderID

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
api_instance = elabjournal_client.SuppliesApi(elabjournal_client.ApiClient(configuration))
order_id = 56 # int | 
dto = elabjournal_client.ShoppingItemUpdate() # ShoppingItemUpdate | 
x_requested_with = 'Swagger' # str |  (optional) (default to Swagger)

try:
    # Update order
    api_instance.order_update_order(order_id, dto, x_requested_with=x_requested_with)
except ApiException as e:
    print("Exception when calling SuppliesApi->order_update_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **dto** | [**ShoppingItemUpdate**](ShoppingItemUpdate.md)|  | 
 **x_requested_with** | **str**|  | [optional] [default to Swagger]

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/html, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

