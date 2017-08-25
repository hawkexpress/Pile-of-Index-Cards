#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2017/08/20  7:26:00
# T. H. Sugano
#

import os

filelist = ["index",
            "getting_started"]

githuburl = "https://github.com/hawkexpress/PoIC/raw/master/"

# Download File in the List @ Github Repository
for item in filelist:
   filename = item + ".rst"
   cmd1 = "wget -q " + githuburl + filename + " -O ./" + filename
   os.system(cmd1)

# Make Sphinx
cmd2 = "make html"
os.system(cmd2)
