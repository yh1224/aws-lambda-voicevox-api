#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import {AwsLambdaVoicevoxApiStack} from "../lib/aws-lambda-voicevox-api-stack";

const app = new cdk.App();
new AwsLambdaVoicevoxApiStack(app, "AwsLambdaVoicevoxApiStack", {});
