#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pipeline.cdk_pipeline_stack import CdkPipelineStack

app = cdk.App()
CdkPipelineStack(app, "CdkPipelineStack")

app.synth()
