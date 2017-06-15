# -*- coding: utf-8 -*-
"""
/***************************************************************************
 calcTc3
                                 A QGIS plugin
 calculate
                             -------------------
        begin                : 2017-06-01
        copyright            : (C) 2017 by Rikard
        email                : rikardg@web.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load calcTc3 class from file calcTc3.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .calc_Tc3 import calcTc3
    return calcTc3(iface)
