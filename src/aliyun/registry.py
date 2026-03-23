import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcr.request.v20160607 import GetRepoListByNamespaceRequest, GetRepoTagsRequest


def _make_client(access_key_id, access_key_secret, region):
    return AcsClient(access_key_id, access_key_secret, region)


def list_repos(namespace, access_key_id, access_key_secret, region="cn-hangzhou"):
    """列出 namespace 下的所有 repo"""
    client = _make_client(access_key_id, access_key_secret, region)
    req = GetRepoListByNamespaceRequest.GetRepoListByNamespaceRequest()
    req.set_RepoNamespace(namespace)
    req.set_PageSize(100)
    resp = client.do_action_with_exception(req)
    data = json.loads(resp)
    repos = data.get("data", {}).get("repos", [])
    return [{"name": r["repoName"], "summary": r.get("summary", ""), "repo_type": r.get("repoType", "")} for r in repos]


def list_tags(namespace, repo_name, access_key_id, access_key_secret, region="cn-hangzhou"):
    """列出 repo 下的所有 tag"""
    client = _make_client(access_key_id, access_key_secret, region)
    req = GetRepoTagsRequest.GetRepoTagsRequest()
    req.set_RepoNamespace(namespace)
    req.set_RepoName(repo_name)
    req.set_PageSize(100)
    resp = client.do_action_with_exception(req)
    data = json.loads(resp)
    tags = data.get("data", {}).get("tags", [])
    return [{"tag": t["tag"], "size": t.get("imageSize"), "updated": t.get("imageUpdate")} for t in tags]
