#!/usr/local/bin/python
import argparse
from database import session, models
from services import converter, revert

__author__ = 'anh.dv'

parser = argparse.ArgumentParser(description='Upload from NFS to GCS and update FileStorage in database')
parser.add_argument('-a', '--action', help='Support 2 actions: `convert` and `revert`. Default is `convert`', required=False, default='convert')
parser.add_argument('-f', '--file', help='If action is `revert` option `file` is required. '
                                         'This is `json` file exported when you use action `convert`.', required=False, default=None)

argv = parser.parse_args()


def process_args(args_):
    action = str(args_.action).rstrip().lower()
    file = args_.file or ''

    if action not in ('convert', 'revert'):
        print(f'Action `{action}` is invalid. Use [-h | --help] for more details')
        raise

    if action == 'revert' and not file:
        print('Action `revert` required `file` option. Use [-h | --help] for more details')
        raise

    return action, file


def __convert():
    FS = models.FileStorage
    query = session.query(FS).filter(FS.storage_type == FS.StorageType.LOCAL_STORAGE.value)
    fss = query.all()
    converter(fss)


def __revert(path): revert(path)


if __name__ == '__main__':
    try:
        a, f = process_args(argv)
        __convert() if a == 'convert' else __revert(path=f)
        session.commit()
    except Exception as err:
        print(str(err))
        session.rollback()
