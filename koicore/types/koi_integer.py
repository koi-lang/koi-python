#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from koicore import KoiValue


class KoiInteger(KoiValue):
    def __init__(self, value: int):
        self._value = value

    def as_integer(self):
        return KoiInteger(self._value)
