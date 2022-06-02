// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsIam
{
    /// <summary>
    /// This resource helps you create predefined IAM roles (`admin`, `poweruser`, and `readonly`) which can be assumed
    /// by trusted resources using SAML Federated Users.
    /// 
    /// ## Example Usage
    /// ### Assumable Roles With SAML
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Pulumi.AwsIam;
    /// using Pulumi.AwsIam.Inputs;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var assumableRolesWithSaml = new AssumableRolesWithSAML("assumable-roles-with-saml", new AssumableRolesWithSAMLArgs
    ///         {
    ///             ProviderIds = {"arn:aws:iam::235367859851:saml-provider/idp_saml"},
    ///             Admin = new AdminRoleArgs(),
    ///             Readonly = new ReadonlyRoleArgs(),
    ///             Poweruser = new PoweruserRoleArgs
    ///             {
    ///                 Name = "developer",
    ///             },
    ///         });
    /// 
    ///         this.AssumableRolesWithSaml = Output.Create&lt;AssumableRolesWithSAML&gt;(assumableRolesWithSaml);
    ///     }
    /// 
    ///     [Output]
    ///     public Output&lt;AssumableRolesWithSAML&gt; AssumableRolesWithSaml { get; set; }
    /// }
    /// ```
    /// {{ /example }}
    /// </summary>
    [AwsIamResourceType("aws-iam:index:AssumableRolesWithSAML")]
    public partial class AssumableRolesWithSAML : Pulumi.ComponentResource
    {
        [Output("admin")]
        public Output<ImmutableDictionary<string, string>> Admin { get; private set; } = null!;

        [Output("poweruser")]
        public Output<ImmutableDictionary<string, string>?> Poweruser { get; private set; } = null!;

        [Output("readonly")]
        public Output<ImmutableDictionary<string, string>?> Readonly { get; private set; } = null!;


        /// <summary>
        /// Create a AssumableRolesWithSAML resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AssumableRolesWithSAML(string name, AssumableRolesWithSAMLArgs? args = null, ComponentResourceOptions? options = null)
            : base("aws-iam:index:AssumableRolesWithSAML", name, args ?? new AssumableRolesWithSAMLArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class AssumableRolesWithSAMLArgs : Pulumi.ResourceArgs
    {
        [Input("admin")]
        public Input<Inputs.AdminRoleArgs>? Admin { get; set; }

        /// <summary>
        /// AWS SAML Endpoint.
        /// </summary>
        [Input("awsSamlEndpoint")]
        public Input<string>? AwsSamlEndpoint { get; set; }

        /// <summary>
        /// Whether policies should be detached from this role when destroying.
        /// </summary>
        [Input("forceDetachPolicies")]
        public Input<bool>? ForceDetachPolicies { get; set; }

        /// <summary>
        /// Maximum CLI/API session duration in seconds between 3600 and 43200.
        /// </summary>
        [Input("maxSessionDuration")]
        public Input<int>? MaxSessionDuration { get; set; }

        [Input("poweruser")]
        public Input<Inputs.PoweruserRoleArgs>? Poweruser { get; set; }

        [Input("providerIds")]
        private InputList<string>? _providerIds;

        /// <summary>
        /// List of SAML Provider IDs.
        /// </summary>
        public InputList<string> ProviderIds
        {
            get => _providerIds ?? (_providerIds = new InputList<string>());
            set => _providerIds = value;
        }

        [Input("readonly")]
        public Input<Inputs.ReadonlyRoleArgs>? Readonly { get; set; }

        public AssumableRolesWithSAMLArgs()
        {
            AwsSamlEndpoint = "https://signin.aws.amazon.com/saml";
            ForceDetachPolicies = false;
            MaxSessionDuration = 3600;
        }
    }
}
