from aws_cdk import (
    pipelines,
    aws_lambda as lambda_,
    Stack,
    Stage,
    CfnOutput,
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
class MyOutputStage(Stage):
    def __init__(self, scope, id, *, env=None, outdir=None):
        super().__init__(scope, id, env=env, outdir=outdir)
        CdkLambdaStack(self, "CdkLambda")

    
class CdkPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = pipelines.CodePipeline(self, "Pipeline",
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
            pipeline_name='CDKPipeline',
            self_mutation=True,
        )
        stage = MyOutputStage(self, 'MyOutputStage')
        pipeline.add_stage(
            stage,
            pre=[
                pipelines.ManualApprovalStep("PremoteToPred")
            ],
        )
