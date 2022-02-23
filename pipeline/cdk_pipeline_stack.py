from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    pipelines,
)
from constructs import Construct


class CdkPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipelines.CodePipeline(self, "Pipeline",
            synth=pipelines.ShellStep("Synth",
                input=pipelines.CodePipelineSource.connection(
                    'octop162/cdk-pipeline-practice',
                    'main',
                    connection_arn='arn:aws:codestar-connections:ap-northeast-1:595135303684:connection/42c46967-2a5a-45d7-9b0c-1e50bc2a6101'
                ),
                commands=[
                    "pip install -r requirements.txt",
                    "npm install -g aws-cdk",
                    "cdk synth"
                ]
            ),
        )
