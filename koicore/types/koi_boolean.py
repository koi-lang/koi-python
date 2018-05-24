#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from koicore import KoiValue


class KoiBoolean(KoiValue):
    def __init__(self, value: bool):
        self.value = value

    def as_boolean(self):
        return KoiBoolean(self.value)
