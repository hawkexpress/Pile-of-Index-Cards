#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2017/08/20  7:26:00
# T. H. Sugano
#
# Note :
#  - Place this file to the directory "/var/www/sphinx/"
#  - Then run "% sudo python2 update_sphinx.py"
#

import os

filelist = ["index"]

githuburl = "https://github.com/hawkexpress/PoIC/raw/master/"

# Download File in the List @ Github Repository
for item in filelist:
   filename = item + ".rst"
   cmd1 = "wget -q " + githuburl + filename + " -O ./source/" + filename
   os.system(cmd1)

# Make Sphinx
cmd2 = "make html"
os.system(cmd2)
