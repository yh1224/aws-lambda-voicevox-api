#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import {AwsVoicevoxProxyStack} from "../lib/aws-voicevox-proxy-stack";

const app = new cdk.App();
new AwsVoicevoxProxyStack(app, "AwsVoicevoxProxyStack", {});
