# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScaleSetVMInstanceView(Model):
    """The instance view of a virtual machine scale set VM.

    :param platform_update_domain: The Update Domain count.
    :type platform_update_domain: int
    :param platform_fault_domain: The Fault Domain count.
    :type platform_fault_domain: int
    :param rdp_thumb_print: The Remote desktop certificate thumbprint.
    :type rdp_thumb_print: str
    :param vm_agent: The VM Agent running on the virtual machine.
    :type vm_agent: :class:`VirtualMachineAgentInstanceView
     <azure.mgmt.compute.v2016_04_30_preview.models.VirtualMachineAgentInstanceView>`
    :param disks: The disks information.
    :type disks: list of :class:`DiskInstanceView
     <azure.mgmt.compute.v2016_04_30_preview.models.DiskInstanceView>`
    :param extensions: The extensions information.
    :type extensions: list of :class:`VirtualMachineExtensionInstanceView
     <azure.mgmt.compute.v2016_04_30_preview.models.VirtualMachineExtensionInstanceView>`
    :param boot_diagnostics: The boot diagnostics.
    :type boot_diagnostics: :class:`BootDiagnosticsInstanceView
     <azure.mgmt.compute.v2016_04_30_preview.models.BootDiagnosticsInstanceView>`
    :param statuses: The resource status information.
    :type statuses: list of :class:`InstanceViewStatus
     <azure.mgmt.compute.v2016_04_30_preview.models.InstanceViewStatus>`
    :param placement_group_id: The placement group in which the VM is running.
     If the VM is deallocated it will not have a placementGroupId.
    :type placement_group_id: str
    """

    _attribute_map = {
        'platform_update_domain': {'key': 'platformUpdateDomain', 'type': 'int'},
        'platform_fault_domain': {'key': 'platformFaultDomain', 'type': 'int'},
        'rdp_thumb_print': {'key': 'rdpThumbPrint', 'type': 'str'},
        'vm_agent': {'key': 'vmAgent', 'type': 'VirtualMachineAgentInstanceView'},
        'disks': {'key': 'disks', 'type': '[DiskInstanceView]'},
        'extensions': {'key': 'extensions', 'type': '[VirtualMachineExtensionInstanceView]'},
        'boot_diagnostics': {'key': 'bootDiagnostics', 'type': 'BootDiagnosticsInstanceView'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
        'placement_group_id': {'key': 'placementGroupId', 'type': 'str'},
    }

    def __init__(self, platform_update_domain=None, platform_fault_domain=None, rdp_thumb_print=None, vm_agent=None, disks=None, extensions=None, boot_diagnostics=None, statuses=None, placement_group_id=None):
        self.platform_update_domain = platform_update_domain
        self.platform_fault_domain = platform_fault_domain
        self.rdp_thumb_print = rdp_thumb_print
        self.vm_agent = vm_agent
        self.disks = disks
        self.extensions = extensions
        self.boot_diagnostics = boot_diagnostics
        self.statuses = statuses
        self.placement_group_id = placement_group_id
