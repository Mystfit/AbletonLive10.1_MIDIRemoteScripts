# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyFadr/__init__.py
# Compiled at: 2019-04-09 19:23:44
from __future__ import absolute_import, print_function, unicode_literals
from .KeyFadr import KeyFadr
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=9901, product_ids=[
                         28150], model_name='Reloop KeyFadr'), 
       PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return KeyFadr(c_instance)