from aws_cdk import (
    Stack,
    aws_lambda as lambda_
)
from constructs import Construct


class CdkLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_.Function(
            self,
            "MyLambda",
            code=lambda_.Code.from_asset("mylambda"),
            handler='index.main',
            runtime=lambda_.Runtime.PYTHON_3_9,
        )