import requests
import time
import hmac
import hashlib
import base64
from datetime import datetime
from urllib.parse import quote

def _sign(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha1).digest()

def list_tags(namespace, repo_name, access_key_id, access_key_secret, region="cn-hangzhou"):
    """列出阿里云镜像仓库的所有 tag"""
    endpoint = f"cr.{region}.aliyuncs.com"
    path = f"/repos/{namespace}/{repo_name}/tags"

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    nonce = str(int(time.time() * 1000))

    params = {
        "AccessKeyId": access_key_id,
        "Action": "GetRepoTags",
        "Format": "JSON",
        "SignatureMethod": "HMAC-SHA1",
        "SignatureNonce": nonce,
        "SignatureVersion": "1.0",
        "Timestamp": timestamp,
        "Version": "2016-06-07"
    }

    # 简化实现：直接使用 HTTP API
    url = f"https://{endpoint}{path}"
    headers = {"Authorization": f"Basic {base64.b64encode(f'{access_key_id}:{access_key_secret}'.encode()).decode()}"}

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()
