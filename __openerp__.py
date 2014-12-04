# -*- coding: utf-8 -*-
##############################################################################
#
#    Acespritech Solutions Pvt Ltd
#    Copyright (C) 2013-today
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
##############################################################################
{
    'name': 'Change Currency',
    'version': '1.0',
    'category': 'Tools',
    'description': """
This module is used for updating currency.
==================================

It change currency field value in records of installed module
    """,
    'author': 'Acespritech Solutions Pvt Ltd',
    'website': 'http://www.acespritech.com',
    'depends': ['base'],
    'data': [
        'wizard/currency_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
