# coding=utf-8
import os
from typing import List

from . import nfs, gcs, changelog, revert_fs
from database.models import FileStorage

__author__ = 'anh.dv'

NFS_PREFIX = os.getenv('NFS_PREFIX') or '/nfs/uploads/'


def converter(fss):
    """
    Convert FileStorage with storage_type=`local_storage` to `gcs`
    :param List[FileStorage] fss:
    """
    savers = {}
    for fs in fss:
        x = __convert(fs)
        not x or savers.update(x)
    log = changelog.Logger()
    log.write_changelog(savers)


def revert(path):
    """
    Please dont use this shit!!
    :param str path:
    :return:
    """
    content = changelog.Logger.read_changelog(path)
    revert_fs.revert(content)
    print('Revert finished!')


def __convert(fs: FileStorage) -> dict:
    stream = nfs.get_file(__create_abs_path(fs))
    new_path = __create_new_path(fs.path)
    gcs_path = __create_gcs_path(new_path=new_path, filename=fs.replacement_name, ext=fs.extension)
    gcs.upload(gcs_path=gcs_path, stream=stream, content_type=fs.content_type)
    changelog_object = __update_fs_model(fs, new_path)
    if changelog_object:
        return {fs.id: changelog_object}
    return changelog_object


def __update_fs_model(fs: FileStorage, new_path):
    saver = changelog.Saver(fs)
    saver.save(fs)
    fs.storage_type = fs.StorageType.GOOGLE_CLOUD_STORAGE.value
    fs.path = new_path
    fs.extension = fs.extension[1:]  # Remove dot before extension.
    saver.save(fs)
    return saver.export()


def __create_new_path(old_path: str):
    """
    Create new path from `old_path`
    :param str old_path: old path should have format [/nfs/uploads/<any_thing>] e.g: /nfs/uploads/2019/10/11/test.jpg
    :return:
    """
    return old_path.replace(NFS_PREFIX, '')


def __create_gcs_path(new_path, filename, ext): return os.path.join(new_path, f'{filename}{ext}')


def __create_abs_path(fs: FileStorage): return os.path.join(fs.path, f'{fs.replacement_name}{fs.extension}')
