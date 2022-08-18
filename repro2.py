"""Create prefect deployments."""
from prefect import flow
from prefect.deployments import Deployment


@flow
def flow_method():
    """flow method."""
    print("hello")


deployment = Deployment.build_from_flow(
    flow=flow_method,
    name="flow-deployment",
)

deployment.apply()
