#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import, division, print_function


import os
from datetime import datetime, timedelta
from random import randint
from tools.helpers import mkdir


suffixes = ["{}".format(i) for i in range(1, 7)]
suffixes += ["final", "final_pretty_sure", "final2", "final2_USETHISONE", "final2_final_FORREALTHISTIME",
             "final2_final_FORREALTHISTIME_v2"]
EPOCH = datetime.utcfromtimestamp(0)

now = datetime.now() - timedelta(days=180)
mkdir('thesis/')

for suff in suffixes:
    path = "thesis/paper_{date}_{suff}.tex".format(date=now.strftime("%Y_%m_%d"),
                                            suff=suff)
    with open(path, 'w'):
        pass
    os.utime(path, times=((now - EPOCH).total_seconds(), ) * 2)

    now += timedelta(days=randint(0, 10), minutes=randint(0, 9600))
