// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * This resources helps you create an IAM User, Login Profile, and Access Key. Additionally you
 * can optionally upload an IAM SSH User Public Key.
 *
 * ## Example Usage
 * ### User
 *
 * ```typescript
 * import * as iam from "@pulumi/aws-iam";
 *
 * export const user = new iam.User("aws-iam-example-user", {
 *     name: "pulumipus",
 *     forceDestroy: true,
 *     pgpKey: "keybase:test",
 *     passwordResetRequired: false,
 * });
 * ```
 * {{ /example }}
 */
export class User extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'aws-iam:index:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * The IAM access key.
     */
    public /*out*/ readonly accessKey!: pulumi.Output<outputs.AccessKeyOutput>;
    public /*out*/ readonly keybase!: pulumi.Output<outputs.KeybaseOutput>;
    /**
     * PGP key used to encrypt sensitive data for this user (if empty - secrets are not encrypted).
     */
    public readonly pgpKey!: pulumi.Output<string>;
    /**
     * The IAM user.
     */
    public /*out*/ readonly userInfo!: pulumi.Output<outputs.UserOutput>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            resourceInputs["forceDestroy"] = args ? args.forceDestroy : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["passwordLength"] = args ? args.passwordLength : undefined;
            resourceInputs["passwordResetRequired"] = args ? args.passwordResetRequired : undefined;
            resourceInputs["path"] = (args ? args.path : undefined) ?? "/";
            resourceInputs["permissionsBoundary"] = args ? args.permissionsBoundary : undefined;
            resourceInputs["pgpKey"] = args ? args.pgpKey : undefined;
            resourceInputs["sshKeyEncoding"] = (args ? args.sshKeyEncoding : undefined) ?? "SSH";
            resourceInputs["sshPublicKey"] = args ? args.sshPublicKey : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["uploadIamUserSshKey"] = args ? args.uploadIamUserSshKey : undefined;
            resourceInputs["accessKey"] = undefined /*out*/;
            resourceInputs["keybase"] = undefined /*out*/;
            resourceInputs["userInfo"] = undefined /*out*/;
        } else {
            resourceInputs["accessKey"] = undefined /*out*/;
            resourceInputs["keybase"] = undefined /*out*/;
            resourceInputs["pgpKey"] = undefined /*out*/;
            resourceInputs["userInfo"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(User.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * When destroying this user, destroy even if it has non-Pulumi-managed IAM access keys, login profile or MFA devices. Without forceDestroy a user with non-Pulumi-managed access keys and login profile will fail to be destroyed.
     */
    forceDestroy?: pulumi.Input<boolean>;
    /**
     * Desired name for the IAM user.
     */
    name: pulumi.Input<string>;
    /**
     * The length of the generated password
     */
    passwordLength?: pulumi.Input<number>;
    /**
     * Whether the user should be forced to reset the generated password on first login.
     */
    passwordResetRequired?: pulumi.Input<boolean>;
    /**
     * Desired path for the IAM user.
     */
    path?: pulumi.Input<string>;
    /**
     * The ARN of the policy that is used to set the permissions boundary for the user.
     */
    permissionsBoundary?: pulumi.Input<string>;
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Used to encrypt password and access key.
     */
    pgpKey?: pulumi.Input<string>;
    /**
     * Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use SSH. To retrieve the public key in PEM format, use PEM.
     */
    sshKeyEncoding?: pulumi.Input<string>;
    /**
     * The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
     */
    sshPublicKey?: pulumi.Input<string>;
    /**
     * A map of tags to add.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Whether to upload a public ssh key to the IAM user.
     */
    uploadIamUserSshKey?: pulumi.Input<boolean>;
}
