#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pipeline.cdk_pipeline_stack import CdkPipelineStack
from application.cdk_lambda_stack import CdkLambdaStack


app = cdk.App()
CdkPipelineStack(app, "CdkPipelineStack")
CdkLambdaStack(app, "CdkLambda")

app.synth()
