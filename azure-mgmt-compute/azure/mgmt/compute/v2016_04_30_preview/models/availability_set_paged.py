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

from msrest.paging import Paged


class AvailabilitySetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AvailabilitySet <azure.mgmt.compute.v2016_04_30_preview.models.AvailabilitySet>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AvailabilitySet]'}
    }

    def __init__(self, *args, **kwargs):

        super(AvailabilitySetPaged, self).__init__(*args, **kwargs)
