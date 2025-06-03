from factory_sdk import FactoryClient, DeploymentArgs
import os

tenant=os.environ.get("FACTORY_TENANT",None)
token=os.environ.get("FACTORY_TOKEN",None)
project=os.environ.get("FACTORY_PROJECT",None)

adapter_name=os.environ.get("FACTORY_ADAPTER_NAME",None)
revision_id=os.environ.get("FACTORY_ADAPTER_REVISION_ID",None)

deployment_name=os.environ.get("FACTORY_DEPLOYMENT_NAME",None)

port=os.environ.get("PORT",9000)
swap_space=os.environ.get("FACTORY_SWAP_SPACE",0)

assert tenant is not None, "FACTORY_TENANT is not set"
assert token is not None, "FACTORY_TOKEN is not set"
assert project is not None, "FACTORY_PROJECT is not set"
assert adapter_name is not None, "FACTORY_ADAPTER_NAME is not set"
assert revision_id is not None, "FACTORY_ADAPTER_REVISION_ID is not set"
assert deployment_name is not None, "FACTORY_DEPLOYMENT_NAME is not set"

if isinstance(port,str):
    port=int(port)
if isinstance(swap_space,str):
    swap_space=int(swap_space)

factory = FactoryClient(tenant=tenant,project=project, token=token)


adapter=factory.adapter.fetch(adapter_name,revision_id)

config=DeploymentArgs(
        dtype="fp16",
          port=port,
          swap_space=swap_space
      )

deployment=factory.deployment.with_name(deployment_name).for_adapter(adapter).with_config(config).run()


deployment.wait()
