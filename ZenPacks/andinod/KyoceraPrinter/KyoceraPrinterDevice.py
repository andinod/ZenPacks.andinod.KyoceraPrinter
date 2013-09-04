from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class KyoceraPrinterDevice(Device):

    meta_type = portal_type = 'KyoceraPrinterDevice'

    _relations = Device._relations + (
        ('printer_elements', ToManyCont(ToOne,
            'ZenPacks.andinod.KyoceraPrinter.TonerContainer',
            'toner_container',
            ),
        ),
    )

    _relations += ( ('printer_covers', ToManyCont(ToOne, 'ZenPacks.andinod.KyoceraPrinter.PrinterCover', 'cover_printer',  ), ),)

