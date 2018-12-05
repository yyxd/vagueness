# _*_ coding: utf-8 _*_
# @Author: Diane
# @Time  : 2018/12/5 13:20
# @File  : my_sentences.py
# @Goal

class MySentences(object):
    def __init__(self, fname):
        self.fname = fname

    def __iter__(self):
        for line in open(self.fname, 'r'):
            yield line.split()
