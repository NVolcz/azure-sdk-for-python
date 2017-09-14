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


class KeyVaultAndSecretReference(Model):
    """Key Vault Secret Url and vault id of the encryption key .

    :param source_vault: Resource id of the KeyVault containing the key or
     secret
    :type source_vault: :class:`SourceVault
     <azure.mgmt.compute.v2017_03_30.models.SourceVault>`
    :param secret_url: Url pointing to a key or secret in KeyVault
    :type secret_url: str
    """

    _validation = {
        'source_vault': {'required': True},
        'secret_url': {'required': True},
    }

    _attribute_map = {
        'source_vault': {'key': 'sourceVault', 'type': 'SourceVault'},
        'secret_url': {'key': 'secretUrl', 'type': 'str'},
    }

    def __init__(self, source_vault, secret_url):
        self.source_vault = source_vault
        self.secret_url = secret_url
