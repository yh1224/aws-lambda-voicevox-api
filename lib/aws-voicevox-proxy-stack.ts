import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as logs from "aws-cdk-lib/aws-logs";
import {Construct} from "constructs";
import * as path from "path";

export class AwsVoicevoxProxyStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const apiFunc = new lambda.DockerImageFunction(this, "ApiFunc", {
            code: lambda.DockerImageCode.fromImageAsset(path.resolve(__dirname, "../src/lambdas/ApiFunc/")),
            logRetention: logs.RetentionDays.ONE_WEEK,
            memorySize: 2048,
            timeout: cdk.Duration.seconds(30),
        });
        const url = apiFunc.addFunctionUrl({
            authType: lambda.FunctionUrlAuthType.NONE,
        });

        new cdk.CfnOutput(this, "ApiUrl", {
            value: url.url,
        });
    }
}
