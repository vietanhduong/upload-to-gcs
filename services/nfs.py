# coding=utf-8
import os

__author__ = 'anh.dv'


def get_file(abs_path: str) -> bytes:
    if not os.path.exists(abs_path):
        raise Exception(f'{abs_path} does not exists')

    with open(abs_path, 'rb') as f:
        return f.read()
