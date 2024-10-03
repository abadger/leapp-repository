"""
Configuration keys for RHUI.

In case of RHUI in private regions it usual that publicly known RHUI data
is not valid. In such cases it's possible to provide the correct expected
RHUI data to correct the in-place upgrade process.
"""

from leapp.actors.configs import Config
from leapp.models import fields


class RhuiTargetPkg(Config):
    section = "rhui"
    name = "target_client_name"
    type_ = fields.String(default="rhui")
    default = "rhui"
    description = """
        The name of the target RHUI client RPM (to be installed on the system).
        Default: rhui
    """

class RhuiCloudProvider(Config):
    section = "rhui"
    name = "cloud_provider"
    type_ = fields.String(default="rhui")
    default = "provider"
    description = """
        Cloud provider name that should be used internally by leapp.

        Leapp recognizes the following cloud providers:
            - azure
            - azure-sap-apps
            - azure-sap-ha
            - aws
            - aws-sap
            - google
            - google-sap

        Cloud provider information is used for triggering some provider-specific modifications. The value also
        influences how leapp determines target repositories to enable.
    """

class RhuiUpgradeFiles(Config):
    section = "rhui"
    name = "upgrade_files"
    type_ = fields.StringMap(fields.String())
    description = """
        A mapping from source file paths to the destination where should they be
        placed in the upgrade container.

        Typically, these files should be provided by leapp-rhui-<PROVIDER> packages.

        These files are needed to facilitate access to target repositories. Typical examples are: repofile(s),
        certificates and keys.
    """

class RhuiEnabledTargetRepositories(Config):
    section = "rhui"
    name = "enabled_target_repositories"
    type_ = fields.List(fields.String())
    description = """
        List of target repositories enabled during the upgrade. Similar to executing leapp with --enablerepo.

        The repositories to be enabled need to be either in the repofiles givin within `upgrade_files` option,
        or in repofiles present on the source system.
    """

all_rhui_cfg = (RhuiTargetPkg, RhuiUpgradeFiles, RhuiEnabledTargetRepositories, RhuiCloudProvider)
