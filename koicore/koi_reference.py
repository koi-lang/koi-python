#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import abc

from koicore import KoiObject
from koicore.types import KoiBoolean


class KoiReference(KoiObject):
    __metaclass__ = abc.ABCMeta

    def as_boolean(self):
        return KoiBoolean(True)
