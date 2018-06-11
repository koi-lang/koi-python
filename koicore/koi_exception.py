#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import sys

class KoiException(object):
    def __init__(self, text):
        sys.exit(text)
