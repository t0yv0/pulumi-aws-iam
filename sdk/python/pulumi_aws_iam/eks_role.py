# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['EKSRoleArgs', 'EKSRole']

@pulumi.input_type
class EKSRoleArgs:
    def __init__(__self__, *,
                 cluster_service_accounts: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 provider_url_sa_pairs: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 role: Optional[pulumi.Input['RoleArgs']] = None,
                 role_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a EKSRole resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] cluster_service_accounts: EKS cluster and k8s ServiceAccount pairs. Each EKS cluster can have multiple k8s ServiceAccount. See README for details
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] provider_url_sa_pairs: OIDC provider URL and k8s ServiceAccount pairs. If the assume role policy requires a mix of EKS clusters and other OIDC providers then this can be used
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_policy_arns: ARNs of any policies to attach to the IAM role.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to add.
        """
        if cluster_service_accounts is not None:
            pulumi.set(__self__, "cluster_service_accounts", cluster_service_accounts)
        if force_detach_policies is None:
            force_detach_policies = False
        if force_detach_policies is not None:
            pulumi.set(__self__, "force_detach_policies", force_detach_policies)
        if max_session_duration is None:
            max_session_duration = 3600
        if max_session_duration is not None:
            pulumi.set(__self__, "max_session_duration", max_session_duration)
        if provider_url_sa_pairs is not None:
            pulumi.set(__self__, "provider_url_sa_pairs", provider_url_sa_pairs)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if role_policy_arns is not None:
            pulumi.set(__self__, "role_policy_arns", role_policy_arns)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterServiceAccounts")
    def cluster_service_accounts(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        EKS cluster and k8s ServiceAccount pairs. Each EKS cluster can have multiple k8s ServiceAccount. See README for details
        """
        return pulumi.get(self, "cluster_service_accounts")

    @cluster_service_accounts.setter
    def cluster_service_accounts(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "cluster_service_accounts", value)

    @property
    @pulumi.getter(name="forceDetachPolicies")
    def force_detach_policies(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether policies should be detached from this role when destroying.
        """
        return pulumi.get(self, "force_detach_policies")

    @force_detach_policies.setter
    def force_detach_policies(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_detach_policies", value)

    @property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum CLI/API session duration in seconds between 3600 and 43200.
        """
        return pulumi.get(self, "max_session_duration")

    @max_session_duration.setter
    def max_session_duration(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_session_duration", value)

    @property
    @pulumi.getter(name="providerUrlSaPairs")
    def provider_url_sa_pairs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        OIDC provider URL and k8s ServiceAccount pairs. If the assume role policy requires a mix of EKS clusters and other OIDC providers then this can be used
        """
        return pulumi.get(self, "provider_url_sa_pairs")

    @provider_url_sa_pairs.setter
    def provider_url_sa_pairs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "provider_url_sa_pairs", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input['RoleArgs']]:
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input['RoleArgs']]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="rolePolicyArns")
    def role_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        ARNs of any policies to attach to the IAM role.
        """
        return pulumi.get(self, "role_policy_arns")

    @role_policy_arns.setter
    def role_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_policy_arns", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to add.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class EKSRole(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_service_accounts: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 provider_url_sa_pairs: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['RoleArgs']]] = None,
                 role_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a EKSRole resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] cluster_service_accounts: EKS cluster and k8s ServiceAccount pairs. Each EKS cluster can have multiple k8s ServiceAccount. See README for details
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] provider_url_sa_pairs: OIDC provider URL and k8s ServiceAccount pairs. If the assume role policy requires a mix of EKS clusters and other OIDC providers then this can be used
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_policy_arns: ARNs of any policies to attach to the IAM role.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to add.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EKSRoleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a EKSRole resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param EKSRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EKSRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_service_accounts: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 provider_url_sa_pairs: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['RoleArgs']]] = None,
                 role_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EKSRoleArgs.__new__(EKSRoleArgs)

            __props__.__dict__["cluster_service_accounts"] = cluster_service_accounts
            if force_detach_policies is None:
                force_detach_policies = False
            __props__.__dict__["force_detach_policies"] = force_detach_policies
            if max_session_duration is None:
                max_session_duration = 3600
            __props__.__dict__["max_session_duration"] = max_session_duration
            __props__.__dict__["provider_url_sa_pairs"] = provider_url_sa_pairs
            __props__.__dict__["role"] = role
            __props__.__dict__["role_policy_arns"] = role_policy_arns
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["path"] = None
            __props__.__dict__["unique_id"] = None
        super(EKSRole, __self__).__init__(
            'aws-iam:index:EKSRole',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of IAM role.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of IAM role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Path of IAM role.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        Unique ID of IAM role.
        """
        return pulumi.get(self, "unique_id")

