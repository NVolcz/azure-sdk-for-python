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

from .resource import Resource


class VirtualMachineScaleSet(Resource):
    """Describes a Virtual Machine Scale Set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param sku: The virtual machine scale set sku.
    :type sku: :class:`Sku <azure.mgmt.compute.v2017_03_30.models.Sku>`
    :param plan: Specifies information about the marketplace image used to
     create the virtual machine. This element is only used for marketplace
     images. Before you can use a marketplace image from an API, you must
     enable the image for programmatic use.  In the Azure portal, find the
     marketplace image that you want to use and then click **Want to deploy
     programmatically, Get Started ->**. Enter any required information and
     then click **Save**.
    :type plan: :class:`Plan <azure.mgmt.compute.v2017_03_30.models.Plan>`
    :param upgrade_policy: The upgrade policy.
    :type upgrade_policy: :class:`UpgradePolicy
     <azure.mgmt.compute.v2017_03_30.models.UpgradePolicy>`
    :param virtual_machine_profile: The virtual machine profile.
    :type virtual_machine_profile: :class:`VirtualMachineScaleSetVMProfile
     <azure.mgmt.compute.v2017_03_30.models.VirtualMachineScaleSetVMProfile>`
    :ivar provisioning_state: The provisioning state, which only appears in
     the response.
    :vartype provisioning_state: str
    :param overprovision: Specifies whether the Virtual Machine Scale Set
     should be overprovisioned.
    :type overprovision: bool
    :ivar unique_id: Specifies the ID which uniquely identifies a Virtual
     Machine Scale Set.
    :vartype unique_id: str
    :param single_placement_group: When true this limits the scale set to a
     single placement group, of max size 100 virtual machines.
    :type single_placement_group: bool
    :param identity: The identity of the virtual machine scale set, if
     configured.
    :type identity: :class:`VirtualMachineScaleSetIdentity
     <azure.mgmt.compute.v2017_03_30.models.VirtualMachineScaleSetIdentity>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'unique_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'upgrade_policy': {'key': 'properties.upgradePolicy', 'type': 'UpgradePolicy'},
        'virtual_machine_profile': {'key': 'properties.virtualMachineProfile', 'type': 'VirtualMachineScaleSetVMProfile'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'overprovision': {'key': 'properties.overprovision', 'type': 'bool'},
        'unique_id': {'key': 'properties.uniqueId', 'type': 'str'},
        'single_placement_group': {'key': 'properties.singlePlacementGroup', 'type': 'bool'},
        'identity': {'key': 'identity', 'type': 'VirtualMachineScaleSetIdentity'},
    }

    def __init__(self, location, tags=None, sku=None, plan=None, upgrade_policy=None, virtual_machine_profile=None, overprovision=None, single_placement_group=None, identity=None):
        super(VirtualMachineScaleSet, self).__init__(location=location, tags=tags)
        self.sku = sku
        self.plan = plan
        self.upgrade_policy = upgrade_policy
        self.virtual_machine_profile = virtual_machine_profile
        self.provisioning_state = None
        self.overprovision = overprovision
        self.unique_id = None
        self.single_placement_group = single_placement_group
        self.identity = identity
