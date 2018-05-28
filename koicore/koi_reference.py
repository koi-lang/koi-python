#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import abc

from .koi_object import KoiObject


class KoiReference(KoiObject):
    __metaclass__ = abc.ABCMeta

    def as_boolean(self):
        from .types import KoiBoolean
        return KoiBoolean(True)

    def as_character(self):
        from .types import KoiCharacter
        return KoiCharacter("")

    def as_integer(self):
        from .types import KoiInteger
        return KoiInteger(0)

    def as_string(self):
        from .types import KoiString
        return KoiString("")
