# -*- coding: utf-8 -*-
#
#    Author: Joël Grand-Guillaume, Jacques-Etienne Baudoux, Guewen Baconnier
#    Leonardo Pistone
#    Copyright 2013-2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{"name": "Logistics Budget",
 "version": "2.3.1",
 "author": "Camptocamp,Odoo Community Association (OCA)",
 "license": "AGPL-3",
 "category": "Purchase Management",
 'complexity': "normal",
 "images": [],
 "website": "http://www.camptocamp.com",
 "depends": ["logistic_requisition",
             "sale_exceptions",
             "sale_stock",
             ],
 "demo": [],
 "data": ["view/logistic_requisition.xml",
          "view/sale_order_budget_update.xml",
          "view/sale_order.xml",
          "view/report_logistic_requisition.xml",
          "view/report_saleorder.xml",
          "data/exceptions.xml",
          ],
 "auto_install": False,
 'installable': True,
 }
