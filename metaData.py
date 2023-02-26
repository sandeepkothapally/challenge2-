import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Set the subscription ID and resource group name of the instance
subscription_id = 'your-subscription-id'
resource_group_name = 'your-resource-group-name'

# Set up the credentials for the Azure SDK
credential = DefaultAzureCredential()

# Set up the ComputeManagementClient to access the instance metadata
compute_client = ComputeManagementClient(credential, subscription_id)

# Get the instance metadata
instance = compute_client.virtual_machines.get(resource_group_name, 'your-instance-name', expand='instanceView')

# Convert the instance metadata to a JSON-formatted string
instance_json = json.dumps(instance.as_dict(), indent=2)

# Output the instance metadata in JSON format
print(instance_json)
