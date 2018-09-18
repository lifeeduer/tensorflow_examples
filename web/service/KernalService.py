# -*- coding: utf-8 -*-
# @Time  : 2018/9/18 下午4:59
# @Author: Zhangjingpeng
# @Site  : KernalService.py

from datetime import datetime
from __future__ import absolute_import
from web.kernal.models import Kernal
from web.dataset.models import Dataset

class KernalService():
    def create(self, kernal):
        # 1. dataset is exist?
        ret = Kernal.objects.create(kernal)
        return ret

    def update(self, kernal_id, params):
        kernal = Kernal.objects.get(kernal_id=kernal_id)
        for key, value in params:
            kernal_id.key = value
        ret = kernal.save()
        return ret

    def fork(self, kernal_id, user_id):
        ret = None
        kernal = Kernal.objects.get(kernal_id=kernal_id)
        if kernal != None:
            kernal.creator = user_id
            kernal.ctime   = datetime.now()
            kernal.mtime   = datetime.now()
            ret = Kernal.objects.create(kernal)
        return ret

    def run(self, kernal_id):
        #1. 是否在执行中
        #2. 是的话
        kernal = Kernal.objects.get(kernal_id=kernal_id)

    def check_run_status(self):


