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


from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

# Classes we'll need for returning proper results from our modeler plugin's
# process method.
from Products.DataCollector.plugins.DataMaps import ObjectMap


class toner(SnmpPlugin):


    relname='printer_elements'
    modname='ZenPacks.andinod.KyoceraPrinter.TonerContainer'

    # snmpGetTableMaps and GetTableMap should be used to request SNMP tables.
    # The first parameter to GetTableMap is whatever you want the results of
    # this table to be stored in the results as. The second parameter is the
    # base OID for the table. More specifically this should be the "entry" OID
    # or more specifically the largest possible OID prefix that doesn't change
    # when walking the table. The third paramter is a dictionary that maps
    # columns in the table to names that will be used to access them in the
    # results.
    snmpGetTableMaps = (
        GetTableMap('prtMarkerSuppliesTable', '.1.3.6.1.2.1.43.11.1.1', {
            '.6.1': 'prtMarkerSuppliesDescription',
            '.8.1': 'prtMarkerSuppliesMaxCapacity',
	    '.9.1': 'prtMarkerSuppliesLevel',
            }),

        # More GetTableMap definitions can be added to this tuple to query
        # more SNMP tables.
        )

    # Modeler plugins can optionally implement the "condition" method. This
    # allows your plugin to determine if it should be run by looking at the
    # configuration of the device that's about to be modeled. Return True if
    # you want the modeler plugin to execute and False if you do not.
    #
    # The default is to return True. So ordinarily you wouldn't even implement
    # the method if you were just going to blindly return True like this
    # example.
    def condition(self, device, log):
        return True

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)

        printer_elements = results[1].get('prtMarkerSuppliesTable', {})

        # Getting the relation Map
	rm = self.relMap()

        for snmpindex, row in printer_elements.items():
		name = row.get('prtMarkerSuppliesDescription')
		capacity = row.get('prtMarkerSuppliesMaxCapacity')
 		level = row.get('prtMarkerSuppliesLevel')
		
		if not name or capacity <= 0 or level <= 0:
			log.warn('Skipping toner container with no name')
			continue

		rm.append( self.objectMap({
			'id':self.prepId(snmpindex.strip('.')),
			'title': name,
			'snmpindex': snmpindex.strip('.'),
			'maxcapacity': capacity,
			'tonername': name,
			}))
	#import pdb; pdb.set_trace()	
        return rm 
