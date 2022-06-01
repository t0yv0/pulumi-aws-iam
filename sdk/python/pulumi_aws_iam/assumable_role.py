# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['AssumableRoleArgs', 'AssumableRole']

@pulumi.input_type
class AssumableRoleArgs:
    def __init__(__self__, *,
                 attach_admin_policy: Optional[pulumi.Input[bool]] = None,
                 attach_poweruser_policy: Optional[pulumi.Input[bool]] = None,
                 attach_readonly_policy: Optional[pulumi.Input[bool]] = None,
                 custom_role_trust_policy: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 mfa_age: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input['RoleWithMFAArgs']] = None,
                 role_sts_external_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_role_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 trusted_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 trusted_role_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AssumableRole resource.
        :param pulumi.Input[bool] attach_admin_policy: Whether to attach an admin policy to a role.
        :param pulumi.Input[bool] attach_poweruser_policy: Whether to attach a poweruser policy to a role.
        :param pulumi.Input[bool] attach_readonly_policy: Whether to attach a readonly policy to a role.
        :param pulumi.Input[str] custom_role_trust_policy: A custom role trust policy.
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[int] mfa_age: Max age of valid MFA (in seconds) for roles which require MFA.
        :param pulumi.Input['RoleWithMFAArgs'] role: An IAM role that requires MFA.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_sts_external_ids: STS ExternalId condition values to use with a role (when MFA is not required).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to add.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trusted_role_actions: Actions of STS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trusted_role_arns: ARNs of AWS entities who can assume these roles.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trusted_role_services: AWS Services that can assume these roles.
        """
        if attach_admin_policy is None:
            attach_admin_policy = False
        if attach_admin_policy is not None:
            pulumi.set(__self__, "attach_admin_policy", attach_admin_policy)
        if attach_poweruser_policy is None:
            attach_poweruser_policy = False
        if attach_poweruser_policy is not None:
            pulumi.set(__self__, "attach_poweruser_policy", attach_poweruser_policy)
        if attach_readonly_policy is None:
            attach_readonly_policy = False
        if attach_readonly_policy is not None:
            pulumi.set(__self__, "attach_readonly_policy", attach_readonly_policy)
        if custom_role_trust_policy is None:
            custom_role_trust_policy = ''
        if custom_role_trust_policy is not None:
            pulumi.set(__self__, "custom_role_trust_policy", custom_role_trust_policy)
        if force_detach_policies is None:
            force_detach_policies = False
        if force_detach_policies is not None:
            pulumi.set(__self__, "force_detach_policies", force_detach_policies)
        if max_session_duration is None:
            max_session_duration = 3600
        if max_session_duration is not None:
            pulumi.set(__self__, "max_session_duration", max_session_duration)
        if mfa_age is None:
            mfa_age = 86400
        if mfa_age is not None:
            pulumi.set(__self__, "mfa_age", mfa_age)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if role_sts_external_ids is not None:
            pulumi.set(__self__, "role_sts_external_ids", role_sts_external_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if trusted_role_actions is not None:
            pulumi.set(__self__, "trusted_role_actions", trusted_role_actions)
        if trusted_role_arns is not None:
            pulumi.set(__self__, "trusted_role_arns", trusted_role_arns)
        if trusted_role_services is not None:
            pulumi.set(__self__, "trusted_role_services", trusted_role_services)

    @property
    @pulumi.getter(name="attachAdminPolicy")
    def attach_admin_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to attach an admin policy to a role.
        """
        return pulumi.get(self, "attach_admin_policy")

    @attach_admin_policy.setter
    def attach_admin_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attach_admin_policy", value)

    @property
    @pulumi.getter(name="attachPoweruserPolicy")
    def attach_poweruser_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to attach a poweruser policy to a role.
        """
        return pulumi.get(self, "attach_poweruser_policy")

    @attach_poweruser_policy.setter
    def attach_poweruser_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attach_poweruser_policy", value)

    @property
    @pulumi.getter(name="attachReadonlyPolicy")
    def attach_readonly_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to attach a readonly policy to a role.
        """
        return pulumi.get(self, "attach_readonly_policy")

    @attach_readonly_policy.setter
    def attach_readonly_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attach_readonly_policy", value)

    @property
    @pulumi.getter(name="customRoleTrustPolicy")
    def custom_role_trust_policy(self) -> Optional[pulumi.Input[str]]:
        """
        A custom role trust policy.
        """
        return pulumi.get(self, "custom_role_trust_policy")

    @custom_role_trust_policy.setter
    def custom_role_trust_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_role_trust_policy", value)

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
    @pulumi.getter(name="mfaAge")
    def mfa_age(self) -> Optional[pulumi.Input[int]]:
        """
        Max age of valid MFA (in seconds) for roles which require MFA.
        """
        return pulumi.get(self, "mfa_age")

    @mfa_age.setter
    def mfa_age(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mfa_age", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input['RoleWithMFAArgs']]:
        """
        An IAM role that requires MFA.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input['RoleWithMFAArgs']]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="roleStsExternalIds")
    def role_sts_external_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        STS ExternalId condition values to use with a role (when MFA is not required).
        """
        return pulumi.get(self, "role_sts_external_ids")

    @role_sts_external_ids.setter
    def role_sts_external_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_sts_external_ids", value)

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

    @property
    @pulumi.getter(name="trustedRoleActions")
    def trusted_role_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Actions of STS.
        """
        return pulumi.get(self, "trusted_role_actions")

    @trusted_role_actions.setter
    def trusted_role_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "trusted_role_actions", value)

    @property
    @pulumi.getter(name="trustedRoleArns")
    def trusted_role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        ARNs of AWS entities who can assume these roles.
        """
        return pulumi.get(self, "trusted_role_arns")

    @trusted_role_arns.setter
    def trusted_role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "trusted_role_arns", value)

    @property
    @pulumi.getter(name="trustedRoleServices")
    def trusted_role_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        AWS Services that can assume these roles.
        """
        return pulumi.get(self, "trusted_role_services")

    @trusted_role_services.setter
    def trusted_role_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "trusted_role_services", value)


class AssumableRole(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attach_admin_policy: Optional[pulumi.Input[bool]] = None,
                 attach_poweruser_policy: Optional[pulumi.Input[bool]] = None,
                 attach_readonly_policy: Optional[pulumi.Input[bool]] = None,
                 custom_role_trust_policy: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 mfa_age: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['RoleWithMFAArgs']]] = None,
                 role_sts_external_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_role_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 trusted_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 trusted_role_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a AssumableRole resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] attach_admin_policy: Whether to attach an admin policy to a role.
        :param pulumi.Input[bool] attach_poweruser_policy: Whether to attach a poweruser policy to a role.
        :param pulumi.Input[bool] attach_readonly_policy: Whether to attach a readonly policy to a role.
        :param pulumi.Input[str] custom_role_trust_policy: A custom role trust policy.
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[int] mfa_age: Max age of valid MFA (in seconds) for roles which require MFA.
        :param pulumi.Input[pulumi.InputType['RoleWithMFAArgs']] role: An IAM role that requires MFA.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_sts_external_ids: STS ExternalId condition values to use with a role (when MFA is not required).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to add.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trusted_role_actions: Actions of STS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trusted_role_arns: ARNs of AWS entities who can assume these roles.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] trusted_role_services: AWS Services that can assume these roles.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AssumableRoleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AssumableRole resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AssumableRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssumableRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attach_admin_policy: Optional[pulumi.Input[bool]] = None,
                 attach_poweruser_policy: Optional[pulumi.Input[bool]] = None,
                 attach_readonly_policy: Optional[pulumi.Input[bool]] = None,
                 custom_role_trust_policy: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 mfa_age: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['RoleWithMFAArgs']]] = None,
                 role_sts_external_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_role_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 trusted_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 trusted_role_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = AssumableRoleArgs.__new__(AssumableRoleArgs)

            if attach_admin_policy is None:
                attach_admin_policy = False
            __props__.__dict__["attach_admin_policy"] = attach_admin_policy
            if attach_poweruser_policy is None:
                attach_poweruser_policy = False
            __props__.__dict__["attach_poweruser_policy"] = attach_poweruser_policy
            if attach_readonly_policy is None:
                attach_readonly_policy = False
            __props__.__dict__["attach_readonly_policy"] = attach_readonly_policy
            if custom_role_trust_policy is None:
                custom_role_trust_policy = ''
            __props__.__dict__["custom_role_trust_policy"] = custom_role_trust_policy
            if force_detach_policies is None:
                force_detach_policies = False
            __props__.__dict__["force_detach_policies"] = force_detach_policies
            if max_session_duration is None:
                max_session_duration = 3600
            __props__.__dict__["max_session_duration"] = max_session_duration
            if mfa_age is None:
                mfa_age = 86400
            __props__.__dict__["mfa_age"] = mfa_age
            __props__.__dict__["role"] = role
            __props__.__dict__["role_sts_external_ids"] = role_sts_external_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["trusted_role_actions"] = trusted_role_actions
            __props__.__dict__["trusted_role_arns"] = trusted_role_arns
            __props__.__dict__["trusted_role_services"] = trusted_role_services
            __props__.__dict__["instance_profile"] = None
        super(AssumableRole, __self__).__init__(
            'aws-iam:index:AssumableRole',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="instanceProfile")
    def instance_profile(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "instance_profile")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "role")

