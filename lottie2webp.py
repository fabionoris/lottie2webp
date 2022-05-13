#!/usr/bin/env python

import sys
import os

lib_path = os.path.dirname(__file__) + os.path.sep + "lib"
sys.path.append(lib_path)

import pylottie

pylottie.convertLottie2Webp(sys.argv[1], sys.argv[2])