# coding=utf-8
import os
import json
from datetime import datetime

__author__ = 'anh.dv'


class Saver(object):

    def __init__(self, model_cls):
        self.cols = tuple([c.name for c in model_cls.__table__.columns])
        self.before = {}
        self.after = {}

    def save(self, model):
        if self.before:
            self.after = self.__load(model)
        else:
            self.before = self.__load(model)

    def export(self):
        return {bk: {'before': bv, 'after': self.after[bk]} for bk, bv in self.before.items() if bv != self.after[bk]}

    def __load(self, model):
        return {c: getattr(model, c) for c in self.cols}


class Logger(object):

    def write_changelog(self, content):
        filename = self.__create_filename()
        dest = os.path.join('/app/changelog', filename)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'w') as f:
            json.dump(content, f, ensure_ascii=False, indent=4)
        print('Changelog path: ', dest)

    @staticmethod
    def read_changelog(path):
        if not os.path.exists(path):
            raise Exception(f'Changelog: {path} does not exists')

        with open(path, 'r') as f:
            return json.load(f)

    @staticmethod
    def __create_filename():
        formatted_date = datetime.now().strftime('%Y_%m_%d')
        return f'changelog_{formatted_date}.json'

