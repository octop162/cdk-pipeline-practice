import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_pipeline.cdk_pipeline_practice_stack import CdkPipelinePracticeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_pipeline_practice/cdk_pipeline_practice_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPipelinePracticeStack(app, "cdk-pipeline-practice")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
