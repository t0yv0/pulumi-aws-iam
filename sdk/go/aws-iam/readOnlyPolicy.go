// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package awsiam

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-iam/sdk/go/aws-iam/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource helps you create an IAM read-only policy for the services you specify. The default AWS
// read-only policies may not include services you need or may contain services you do not need access to.
// This resource helps ensure your read-only policy has permissions to exactly what you specify.
//
// ## Example Usage
// ## RDS and Dynamo Read Only Policy
//
// ```go
// package main
//
// import (
//
//	iam "github.com/pulumi/pulumi-aws-iam/sdk/go/aws-iam"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//	    pulumi.Run(func(ctx *pulumi.Context) error {
//	        readOnlyPolicy, err := iam.NewReadOnlyPolicy(ctx, "read-only-policy", &iam.ReadOnlyPolicyArgs{
//	            Name:            pulumi.String("example"),
//	            Path:            pulumi.String("/"),
//	            Description:     pulumi.String("My example policy"),
//	            AllowedServices: pulumi.ToStringArray([]string{"rds", "dynamodb"}),
//	        })
//	        if err != nil {
//	            return err
//	        }
//
//	        ctx.Export("readOnlyPolicy", readOnlyPolicy)
//
//	        return nil
//	    })
//	}
//
// ```
// {{ /example }}
type ReadOnlyPolicy struct {
	pulumi.ResourceState

	// The ARN assigned by AWS to this policy.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The description of the policy.
	Description pulumi.StringOutput `pulumi:"description"`
	// The name of the policy.
	Name pulumi.StringOutput `pulumi:"name"`
	// The path of the policy in IAM.
	Path pulumi.StringOutput `pulumi:"path"`
	// The policy document.
	Policy pulumi.StringOutput `pulumi:"policy"`
	// The policy's ID.
	PolicyId pulumi.StringOutput `pulumi:"policyId"`
	// Policy document as json. Useful if you need document but do not want to create IAM policy itself. For example for SSO Permission Set inline policies.
	PolicyJson pulumi.StringOutput `pulumi:"policyJson"`
}

// NewReadOnlyPolicy registers a new resource with the given unique name, arguments, and options.
func NewReadOnlyPolicy(ctx *pulumi.Context,
	name string, args *ReadOnlyPolicyArgs, opts ...pulumi.ResourceOption) (*ReadOnlyPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.AdditionalPolicyJson == nil {
		args.AdditionalPolicyJson = pulumi.StringPtr("{}")
	}
	if args.AllowCloudwatchLogsQuery == nil {
		args.AllowCloudwatchLogsQuery = pulumi.BoolPtr(true)
	}
	if args.AllowPredefinedStsActions == nil {
		args.AllowPredefinedStsActions = pulumi.BoolPtr(true)
	}
	if args.AllowWebConsoleServices == nil {
		args.AllowWebConsoleServices = pulumi.BoolPtr(true)
	}
	if args.Description == nil {
		args.Description = pulumi.StringPtr("IAM Policy")
	}
	if args.Path == nil {
		args.Path = pulumi.StringPtr("/")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ReadOnlyPolicy
	err := ctx.RegisterRemoteComponentResource("aws-iam:index:ReadOnlyPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type readOnlyPolicyArgs struct {
	// JSON policy document if you want to add custom actions.
	AdditionalPolicyJson *string `pulumi:"additionalPolicyJson"`
	// Allows StartQuery/StopQuery/FilterLogEvents CloudWatch actions.
	AllowCloudwatchLogsQuery *bool `pulumi:"allowCloudwatchLogsQuery"`
	// Allows GetCallerIdentity/GetSessionToken/GetAccessKeyInfo sts actions.
	AllowPredefinedStsActions *bool `pulumi:"allowPredefinedStsActions"`
	// Allows List/Get/Describe/View actions for services used when browsing AWS console (e.g. resource-groups, tag, health services).
	AllowWebConsoleServices *bool `pulumi:"allowWebConsoleServices"`
	// List of services to allow Get/List/Describe/View options. Service name should be the same as corresponding service IAM prefix. See what it is for each service here https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html.
	AllowedServices []string `pulumi:"allowedServices"`
	// The description of the policy.
	Description *string `pulumi:"description"`
	// The name of the policy.
	Name string `pulumi:"name"`
	// The path of the policy in IAM.
	Path *string `pulumi:"path"`
	// A map of tags to add.
	Tags map[string]string `pulumi:"tags"`
	// List of web console services to allow.
	WebConsoleServices []string `pulumi:"webConsoleServices"`
}

// The set of arguments for constructing a ReadOnlyPolicy resource.
type ReadOnlyPolicyArgs struct {
	// JSON policy document if you want to add custom actions.
	AdditionalPolicyJson pulumi.StringPtrInput
	// Allows StartQuery/StopQuery/FilterLogEvents CloudWatch actions.
	AllowCloudwatchLogsQuery pulumi.BoolPtrInput
	// Allows GetCallerIdentity/GetSessionToken/GetAccessKeyInfo sts actions.
	AllowPredefinedStsActions pulumi.BoolPtrInput
	// Allows List/Get/Describe/View actions for services used when browsing AWS console (e.g. resource-groups, tag, health services).
	AllowWebConsoleServices pulumi.BoolPtrInput
	// List of services to allow Get/List/Describe/View options. Service name should be the same as corresponding service IAM prefix. See what it is for each service here https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html.
	AllowedServices pulumi.StringArrayInput
	// The description of the policy.
	Description pulumi.StringPtrInput
	// The name of the policy.
	Name pulumi.StringInput
	// The path of the policy in IAM.
	Path pulumi.StringPtrInput
	// A map of tags to add.
	Tags pulumi.StringMapInput
	// List of web console services to allow.
	WebConsoleServices pulumi.StringArrayInput
}

func (ReadOnlyPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*readOnlyPolicyArgs)(nil)).Elem()
}

type ReadOnlyPolicyInput interface {
	pulumi.Input

	ToReadOnlyPolicyOutput() ReadOnlyPolicyOutput
	ToReadOnlyPolicyOutputWithContext(ctx context.Context) ReadOnlyPolicyOutput
}

func (*ReadOnlyPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**ReadOnlyPolicy)(nil)).Elem()
}

func (i *ReadOnlyPolicy) ToReadOnlyPolicyOutput() ReadOnlyPolicyOutput {
	return i.ToReadOnlyPolicyOutputWithContext(context.Background())
}

func (i *ReadOnlyPolicy) ToReadOnlyPolicyOutputWithContext(ctx context.Context) ReadOnlyPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReadOnlyPolicyOutput)
}

// ReadOnlyPolicyArrayInput is an input type that accepts ReadOnlyPolicyArray and ReadOnlyPolicyArrayOutput values.
// You can construct a concrete instance of `ReadOnlyPolicyArrayInput` via:
//
//	ReadOnlyPolicyArray{ ReadOnlyPolicyArgs{...} }
type ReadOnlyPolicyArrayInput interface {
	pulumi.Input

	ToReadOnlyPolicyArrayOutput() ReadOnlyPolicyArrayOutput
	ToReadOnlyPolicyArrayOutputWithContext(context.Context) ReadOnlyPolicyArrayOutput
}

type ReadOnlyPolicyArray []ReadOnlyPolicyInput

func (ReadOnlyPolicyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ReadOnlyPolicy)(nil)).Elem()
}

func (i ReadOnlyPolicyArray) ToReadOnlyPolicyArrayOutput() ReadOnlyPolicyArrayOutput {
	return i.ToReadOnlyPolicyArrayOutputWithContext(context.Background())
}

func (i ReadOnlyPolicyArray) ToReadOnlyPolicyArrayOutputWithContext(ctx context.Context) ReadOnlyPolicyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReadOnlyPolicyArrayOutput)
}

// ReadOnlyPolicyMapInput is an input type that accepts ReadOnlyPolicyMap and ReadOnlyPolicyMapOutput values.
// You can construct a concrete instance of `ReadOnlyPolicyMapInput` via:
//
//	ReadOnlyPolicyMap{ "key": ReadOnlyPolicyArgs{...} }
type ReadOnlyPolicyMapInput interface {
	pulumi.Input

	ToReadOnlyPolicyMapOutput() ReadOnlyPolicyMapOutput
	ToReadOnlyPolicyMapOutputWithContext(context.Context) ReadOnlyPolicyMapOutput
}

type ReadOnlyPolicyMap map[string]ReadOnlyPolicyInput

func (ReadOnlyPolicyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ReadOnlyPolicy)(nil)).Elem()
}

func (i ReadOnlyPolicyMap) ToReadOnlyPolicyMapOutput() ReadOnlyPolicyMapOutput {
	return i.ToReadOnlyPolicyMapOutputWithContext(context.Background())
}

func (i ReadOnlyPolicyMap) ToReadOnlyPolicyMapOutputWithContext(ctx context.Context) ReadOnlyPolicyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReadOnlyPolicyMapOutput)
}

type ReadOnlyPolicyOutput struct{ *pulumi.OutputState }

func (ReadOnlyPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ReadOnlyPolicy)(nil)).Elem()
}

func (o ReadOnlyPolicyOutput) ToReadOnlyPolicyOutput() ReadOnlyPolicyOutput {
	return o
}

func (o ReadOnlyPolicyOutput) ToReadOnlyPolicyOutputWithContext(ctx context.Context) ReadOnlyPolicyOutput {
	return o
}

// The ARN assigned by AWS to this policy.
func (o ReadOnlyPolicyOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *ReadOnlyPolicy) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The description of the policy.
func (o ReadOnlyPolicyOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *ReadOnlyPolicy) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The name of the policy.
func (o ReadOnlyPolicyOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ReadOnlyPolicy) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The path of the policy in IAM.
func (o ReadOnlyPolicyOutput) Path() pulumi.StringOutput {
	return o.ApplyT(func(v *ReadOnlyPolicy) pulumi.StringOutput { return v.Path }).(pulumi.StringOutput)
}

// The policy document.
func (o ReadOnlyPolicyOutput) Policy() pulumi.StringOutput {
	return o.ApplyT(func(v *ReadOnlyPolicy) pulumi.StringOutput { return v.Policy }).(pulumi.StringOutput)
}

// The policy's ID.
func (o ReadOnlyPolicyOutput) PolicyId() pulumi.StringOutput {
	return o.ApplyT(func(v *ReadOnlyPolicy) pulumi.StringOutput { return v.PolicyId }).(pulumi.StringOutput)
}

// Policy document as json. Useful if you need document but do not want to create IAM policy itself. For example for SSO Permission Set inline policies.
func (o ReadOnlyPolicyOutput) PolicyJson() pulumi.StringOutput {
	return o.ApplyT(func(v *ReadOnlyPolicy) pulumi.StringOutput { return v.PolicyJson }).(pulumi.StringOutput)
}

type ReadOnlyPolicyArrayOutput struct{ *pulumi.OutputState }

func (ReadOnlyPolicyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ReadOnlyPolicy)(nil)).Elem()
}

func (o ReadOnlyPolicyArrayOutput) ToReadOnlyPolicyArrayOutput() ReadOnlyPolicyArrayOutput {
	return o
}

func (o ReadOnlyPolicyArrayOutput) ToReadOnlyPolicyArrayOutputWithContext(ctx context.Context) ReadOnlyPolicyArrayOutput {
	return o
}

func (o ReadOnlyPolicyArrayOutput) Index(i pulumi.IntInput) ReadOnlyPolicyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ReadOnlyPolicy {
		return vs[0].([]*ReadOnlyPolicy)[vs[1].(int)]
	}).(ReadOnlyPolicyOutput)
}

type ReadOnlyPolicyMapOutput struct{ *pulumi.OutputState }

func (ReadOnlyPolicyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ReadOnlyPolicy)(nil)).Elem()
}

func (o ReadOnlyPolicyMapOutput) ToReadOnlyPolicyMapOutput() ReadOnlyPolicyMapOutput {
	return o
}

func (o ReadOnlyPolicyMapOutput) ToReadOnlyPolicyMapOutputWithContext(ctx context.Context) ReadOnlyPolicyMapOutput {
	return o
}

func (o ReadOnlyPolicyMapOutput) MapIndex(k pulumi.StringInput) ReadOnlyPolicyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ReadOnlyPolicy {
		return vs[0].(map[string]*ReadOnlyPolicy)[vs[1].(string)]
	}).(ReadOnlyPolicyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ReadOnlyPolicyInput)(nil)).Elem(), &ReadOnlyPolicy{})
	pulumi.RegisterInputType(reflect.TypeOf((*ReadOnlyPolicyArrayInput)(nil)).Elem(), ReadOnlyPolicyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ReadOnlyPolicyMapInput)(nil)).Elem(), ReadOnlyPolicyMap{})
	pulumi.RegisterOutputType(ReadOnlyPolicyOutput{})
	pulumi.RegisterOutputType(ReadOnlyPolicyArrayOutput{})
	pulumi.RegisterOutputType(ReadOnlyPolicyMapOutput{})
}
