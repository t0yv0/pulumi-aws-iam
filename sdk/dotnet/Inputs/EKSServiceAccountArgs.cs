// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsIam.Inputs
{

    /// <summary>
    /// EKS cluster and k8s ServiceAccount pairs. Each EKS cluster can have multiple k8s ServiceAccount.
    /// </summary>
    public sealed class EKSServiceAccountArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the EKS cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("serviceAccounts")]
        private InputList<string>? _serviceAccounts;

        /// <summary>
        /// Service accounts to pair with the cluster.
        /// </summary>
        public InputList<string> ServiceAccounts
        {
            get => _serviceAccounts ?? (_serviceAccounts = new InputList<string>());
            set => _serviceAccounts = value;
        }

        public EKSServiceAccountArgs()
        {
        }
    }
}