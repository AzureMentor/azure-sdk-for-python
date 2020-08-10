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


class CachedImagesListResult(Model):
    """The response containing cached images.

    :param value: The list of cached images.
    :type value: list[~azure.mgmt.containerinstance.models.CachedImages]
    :param next_link: The URI to fetch the next page of cached images.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CachedImages]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CachedImagesListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)