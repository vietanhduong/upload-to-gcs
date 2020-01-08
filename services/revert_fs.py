# coding=utf-8
from database import session, models
__author__ = 'anh.dv'


def revert(content):
    """
    :param dict content:
    """
    idx = list(content.keys())
    fss = get_fss(idx)
    _ = [__revert(fs, content.get(str(fs_id))) for fs_id, fs in fss.items()]
    session.commit()


def get_fss(idx):
    FS = models.FileStorage
    all_ = session.query(FS).filter(FS.id.in_(idx)).all()
    return {fs.id: fs for fs in all_}


def __revert(fs: models.FileStorage, changelog: dict): [setattr(fs, k, v.get('before')) for k, v in changelog.items()]
