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

from zope.component import adapts
from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos.template import RRDDataSourceInfo

from ZenPacks.andinod.KyoceraPrinter.TonerContainer import TonerContainer
from ZenPacks.andinod.KyoceraPrinter.PrinterCover import PrinterCover

from ZenPacks.andinod.KyoceraPrinter.interfaces \
    import ITonerContainerInfo

from ZenPacks.andinod.KyoceraPrinter.interfaces \
    import IPrinterCoverInfo

class TonerContainerInfo(ComponentInfo):
    implements(ITonerContainerInfo)
    adapts(TonerContainer)

    tonername = ProxyProperty("tonername")
    maxcapacity = ProxyProperty("maxcapacity")

class PrinterCoverInfo(ComponentInfo):
    implements(IPrinterCoverInfo)
    adapts(PrinterCover)


    @property
    def coverstatus(self):
	return self._object.getCoverStatus()
