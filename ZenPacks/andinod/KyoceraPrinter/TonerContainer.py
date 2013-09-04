##############################################################################
#
# Copyright (C) David Andino, CIV 138.286, Punto Fijo, Venezuela,
# all rights reserved.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
##############################################################################

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class TonerContainer(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "TonerContainer"

    tonername = None
    maxcapacity = None

    _properties = ManagedEntity._properties + (
        {'id': 'tonername', 'type': 'string' },
        {'id': 'maxcapacity', 'type': 'int'},
    )

    _relations = ManagedEntity._relations + (
        ('toner_container', ToOne(ToManyCont,
            'ZenPacks.andinod.KyoceraPrinter.KyoceraPrinterDevice',
            'printer_elements',
            ),
        ),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)

    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.toner_container()

    def getRRDTemplateName(self):
        return 'TonerContainer'
