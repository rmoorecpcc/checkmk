#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Alternative,
    Tuple,
    Age,
    FixedValue,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersNetworking,
)


def _vs_fortinet_signatures(title):
    return Alternative(title=title,
                       style="dropdown",
                       elements=[
                           Tuple(title=_("Set levels"),
                                 elements=[
                                     Age(title=_("Warning at"), default_value=86400),
                                     Age(title=_("Critical at"), default_value=2 * 86400),
                                 ]),
                           Tuple(title=_("No levels"),
                                 elements=[
                                     FixedValue(None, totext=""),
                                     FixedValue(None, totext=""),
                                 ]),
                       ])


@rulespec_registry.register
class RulespecCheckgroupParametersFortinetSignatures(CheckParameterRulespecWithoutItem):
    @property
    def group(self):
        return RulespecGroupCheckParametersNetworking

    @property
    def check_group_name(self):
        return "fortinet_signatures"

    @property
    def title(self):
        return _("Fortigate Signatures")

    @property
    def match_type(self):
        return "dict"

    @property
    def parameter_valuespec(self):
        return Dictionary(elements=[
            ('av_age', _vs_fortinet_signatures(_("Age of Anti-Virus signature"))),
            ('av_ext_age',
             _vs_fortinet_signatures(_("Age of Anti-Virus signature extended database"))),
            ('ips_age', _vs_fortinet_signatures(_("Age of Intrusion Prevention signature"))),
            ('ips_ext_age',
             _vs_fortinet_signatures(_("Age of Intrusion Prevention signature extended database"))),
        ],)
