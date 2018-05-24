#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import abc

from koicore.types import KoiBoolean


class KoiObject(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def as_boolean(self) -> KoiBoolean:
        pass
