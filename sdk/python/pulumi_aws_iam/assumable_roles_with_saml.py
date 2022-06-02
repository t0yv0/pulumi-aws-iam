# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['AssumableRolesWithSAMLArgs', 'AssumableRolesWithSAML']

@pulumi.input_type
class AssumableRolesWithSAMLArgs:
    def __init__(__self__, *,
                 admin: Optional[pulumi.Input['AdminRoleArgs']] = None,
                 aws_saml_endpoint: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 poweruser: Optional[pulumi.Input['PoweruserRoleArgs']] = None,
                 provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 readonly: Optional[pulumi.Input['ReadonlyRoleArgs']] = None):
        """
        The set of arguments for constructing a AssumableRolesWithSAML resource.
        :param pulumi.Input[str] aws_saml_endpoint: AWS SAML Endpoint.
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] provider_ids: List of SAML Provider IDs.
        """
        if admin is not None:
            pulumi.set(__self__, "admin", admin)
        if aws_saml_endpoint is None:
            aws_saml_endpoint = 'https://signin.aws.amazon.com/saml'
        if aws_saml_endpoint is not None:
            pulumi.set(__self__, "aws_saml_endpoint", aws_saml_endpoint)
        if force_detach_policies is None:
            force_detach_policies = False
        if force_detach_policies is not None:
            pulumi.set(__self__, "force_detach_policies", force_detach_policies)
        if max_session_duration is None:
            max_session_duration = 3600
        if max_session_duration is not None:
            pulumi.set(__self__, "max_session_duration", max_session_duration)
        if poweruser is not None:
            pulumi.set(__self__, "poweruser", poweruser)
        if provider_ids is not None:
            pulumi.set(__self__, "provider_ids", provider_ids)
        if readonly is not None:
            pulumi.set(__self__, "readonly", readonly)

    @property
    @pulumi.getter
    def admin(self) -> Optional[pulumi.Input['AdminRoleArgs']]:
        return pulumi.get(self, "admin")

    @admin.setter
    def admin(self, value: Optional[pulumi.Input['AdminRoleArgs']]):
        pulumi.set(self, "admin", value)

    @property
    @pulumi.getter(name="awsSamlEndpoint")
    def aws_saml_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        AWS SAML Endpoint.
        """
        return pulumi.get(self, "aws_saml_endpoint")

    @aws_saml_endpoint.setter
    def aws_saml_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_saml_endpoint", value)

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
    @pulumi.getter
    def poweruser(self) -> Optional[pulumi.Input['PoweruserRoleArgs']]:
        return pulumi.get(self, "poweruser")

    @poweruser.setter
    def poweruser(self, value: Optional[pulumi.Input['PoweruserRoleArgs']]):
        pulumi.set(self, "poweruser", value)

    @property
    @pulumi.getter(name="providerIds")
    def provider_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of SAML Provider IDs.
        """
        return pulumi.get(self, "provider_ids")

    @provider_ids.setter
    def provider_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "provider_ids", value)

    @property
    @pulumi.getter
    def readonly(self) -> Optional[pulumi.Input['ReadonlyRoleArgs']]:
        return pulumi.get(self, "readonly")

    @readonly.setter
    def readonly(self, value: Optional[pulumi.Input['ReadonlyRoleArgs']]):
        pulumi.set(self, "readonly", value)


class AssumableRolesWithSAML(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin: Optional[pulumi.Input[pulumi.InputType['AdminRoleArgs']]] = None,
                 aws_saml_endpoint: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 poweruser: Optional[pulumi.Input[pulumi.InputType['PoweruserRoleArgs']]] = None,
                 provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 readonly: Optional[pulumi.Input[pulumi.InputType['ReadonlyRoleArgs']]] = None,
                 __props__=None):
        """
        This resource helps you create predefined IAM roles (`admin`, `poweruser`, and `readonly`) which can be assumed
        by trusted resources using SAML Federated Users.

        ## Example Usage
        ### Assumable Roles With SAML

        ```python
        import pulumi
        import pulumi_aws_iam as iam

        assumable_roles_with_saml = iam.AssumableRolesWithSAML(
            'assumable_roles_with_saml',
            provider_ids=['arn:aws:iam::235367859851:saml-provider/idp_saml'],
            admin=iam.AdminRoleArgs(),
            readonly=iam.ReadonlyRoleArgs(),
            poweruser=iam.PoweruserRoleArgs(
                name='developer',
            ),
        )

        pulumi.export('assumable_roles_with_saml', assumable_roles_with_saml)
        ```
        {{ /example }}

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_saml_endpoint: AWS SAML Endpoint.
        :param pulumi.Input[bool] force_detach_policies: Whether policies should be detached from this role when destroying.
        :param pulumi.Input[int] max_session_duration: Maximum CLI/API session duration in seconds between 3600 and 43200.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] provider_ids: List of SAML Provider IDs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AssumableRolesWithSAMLArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource helps you create predefined IAM roles (`admin`, `poweruser`, and `readonly`) which can be assumed
        by trusted resources using SAML Federated Users.

        ## Example Usage
        ### Assumable Roles With SAML

        ```python
        import pulumi
        import pulumi_aws_iam as iam

        assumable_roles_with_saml = iam.AssumableRolesWithSAML(
            'assumable_roles_with_saml',
            provider_ids=['arn:aws:iam::235367859851:saml-provider/idp_saml'],
            admin=iam.AdminRoleArgs(),
            readonly=iam.ReadonlyRoleArgs(),
            poweruser=iam.PoweruserRoleArgs(
                name='developer',
            ),
        )

        pulumi.export('assumable_roles_with_saml', assumable_roles_with_saml)
        ```
        {{ /example }}

        :param str resource_name: The name of the resource.
        :param AssumableRolesWithSAMLArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssumableRolesWithSAMLArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin: Optional[pulumi.Input[pulumi.InputType['AdminRoleArgs']]] = None,
                 aws_saml_endpoint: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[int]] = None,
                 poweruser: Optional[pulumi.Input[pulumi.InputType['PoweruserRoleArgs']]] = None,
                 provider_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 readonly: Optional[pulumi.Input[pulumi.InputType['ReadonlyRoleArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssumableRolesWithSAMLArgs.__new__(AssumableRolesWithSAMLArgs)

            __props__.__dict__["admin"] = admin
            if aws_saml_endpoint is None:
                aws_saml_endpoint = 'https://signin.aws.amazon.com/saml'
            __props__.__dict__["aws_saml_endpoint"] = aws_saml_endpoint
            if force_detach_policies is None:
                force_detach_policies = False
            __props__.__dict__["force_detach_policies"] = force_detach_policies
            if max_session_duration is None:
                max_session_duration = 3600
            __props__.__dict__["max_session_duration"] = max_session_duration
            __props__.__dict__["poweruser"] = poweruser
            __props__.__dict__["provider_ids"] = provider_ids
            __props__.__dict__["readonly"] = readonly
        super(AssumableRolesWithSAML, __self__).__init__(
            'aws-iam:index:AssumableRolesWithSAML',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def admin(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "admin")

    @property
    @pulumi.getter
    def poweruser(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "poweruser")

    @property
    @pulumi.getter
    def readonly(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "readonly")

