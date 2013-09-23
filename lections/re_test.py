#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import sys
import re


_hre = '(:?^\w+(-\w+)*:[^\n]*\n)'
_HEADER_RE = re.compile(_hre, re.M)
_MAILER_RE = re.compile('mailer.?daemon', re.I)
_MS_RE = re.compile('^\s*Microsoft Mail Internet.*\n')
_DUP_SUBJECT_RE = re.compile('^[\s>]*Subject:', re.I | re.M)
_RFC822_RE = re.compile('message/rfc822', re.I)

print _hre
print _HEADER_RE

