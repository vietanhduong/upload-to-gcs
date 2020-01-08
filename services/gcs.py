# coding=utf-8
import json
import os

from base64 import b64decode as decode
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials


__author__ = 'anh.dv'

__BUCKET = os.getenv('GCS_BUCKET') or 'teko-cc-develop'

__gcs_credential = json.loads(decode(os.getenv('GCS')))
__credentials = ServiceAccountCredentials.from_json_keyfile_dict(__gcs_credential)
__client = storage.Client(credentials=__credentials, project=__gcs_credential.get('project_id'))
__bucket = __client.bucket(__BUCKET)


def upload(gcs_path, stream, content_type):
    """
    Upload file to Google cloud storage
    :param str gcs_path: it should be year/month/day/filename.ext e.g: 2020/1/10/IMG03.jpg
    :param bytes stream:
    :param str content_type:
    """
    blob = __bucket.blob(gcs_path)
    if not blob.exists():
        blob.upload_from_string(stream, content_type)
    else:
        print(f'{gcs_path} already existed')
