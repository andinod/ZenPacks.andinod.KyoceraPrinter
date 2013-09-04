/*
 * ##############################################################################
 * #
 * # Copyright (C) David Andino, CIV 138.286, Punto Fijo, Venezuela,
 * # all rights reserved.
 * #
 * # This program is free software; you can redistribute it and/or modify it
 * # under the terms of the GNU General Public License version 2 as published by
 * # the Free Software Foundation.
 * #
 * ##############################################################################
 */

(function(){

var ZC = Ext.ns('Zenoss.component');
var ZC1 = Ext.ns('Zenoss.component');

/*
 *  * Friendly names for the components. First parameter is the meta_type in your
 *   * custom component class. Second parameter is the singular form of the
 *    * friendly name to be displayed in the UI. Third parameter is the plural form.
 *     */
ZC.registerName('TonerContainer', _t('Toner'), _t('Toners'));
ZC1.registerName('PrinterCover', _t('Printer Cover'), _t('Printer Covers'));

/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componenType".
 */
ZC.TonerContainerPanel = Ext.extend(ZC.ComponentGridPanel, { 
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'TonerContainer',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'maxcapacity'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
		dataIndex: 'name',
                header: _t('Toner Name'),
                sortable: true,
                width: 300
            },{
                id: 'maxcapacity',
                dataIndex: 'maxcapacity',
                header: _t('Max Capacity'),
                sortable: true,
                width: 150
	    },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
	ZC.TonerContainerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('TonerContainerPanel', ZC.TonerContainerPanel);

ZC1.PrinterCoverPanel = Ext.extend(ZC1.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PrinterCover',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'coverstatus'},
		{name: 'status'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Cover Name'),
                sortable: true,
                width: 300
            },{
                id: 'coverstatus',
                dataIndex: 'coverstatus',
                header: _t('Cover Status'),
                sortable: true,
                width: 150
	    },{
                id: 'status',
                dataIndex: 'coverstatus',
                header: _t('Status'),
		renderer: function(cs) {
			if (cs.indexOf('Closed') != -1){
				return Zenoss.render.pingStatus('up');
			}else{
				return Zenoss.render.pingStatus('down');
			}
		},
                sortable: true,
                width: 150
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC1.PrinterCoverPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PrinterCoverPanel', ZC1.PrinterCoverPanel);

})();
