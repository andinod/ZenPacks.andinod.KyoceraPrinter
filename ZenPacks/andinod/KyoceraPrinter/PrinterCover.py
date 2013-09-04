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


class PrinterCover(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "PrinterCover"

    coverstatus = None

    _properties = ManagedEntity._properties + (
        {'id': 'coverstatus', 'type': 'string' },
    )

    _relations = ManagedEntity._relations + (
        ('cover_printer', ToOne(ToManyCont,
            'ZenPacks.andinod.KyoceraPrinter.KyoceraPrinterDevice',
            'printer_covers',
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
        return self.cover_printer()

    def getRRDTemplateName(self):
        return 'PrinterCover'

    def getCoverStatus(self):
	cs = int(self.cacheRRDValue('prtCoverStatus'))

        if cs == 1:
       		coverstatus = 'Other'
        elif cs == 3:
                coverstatus = 'Open'
        elif cs == 4:
                coverstatus = 'Closed'
        elif cs == 5:
                coverstatus = 'InterLockOpen'
        elif cs == 6:
                coverstatus = 'InterLockClosed'
	return coverstatus
	
