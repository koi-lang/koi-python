#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import abc

from koicore.types import KoiBoolean, KoiCharacter


class KoiObject(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def as_boolean(self) -> KoiBoolean:
        pass

    @abc.abstractmethod
    def as_character(self) -> KoiCharacter:
        pass
