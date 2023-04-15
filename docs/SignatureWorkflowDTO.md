# SignatureWorkflowDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature_workflow_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**created_by** | [**UserReferenceDTO**](UserReferenceDTO.md) |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**projects** | [**list[WorkflowProjectDTO]**](WorkflowProjectDTO.md) |  | [optional] 
**steps** | [**list[SignatureWorkflowStepDTO]**](SignatureWorkflowStepDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


