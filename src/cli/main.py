import os
import json
import fire
from dotenv import load_dotenv
from src.github import read_file, update_file, check_actions_by_sha
from src.aliyun import list_repos, list_tags

load_dotenv()


class DockerImagePusher:
    def read_github_images(self, repo=None, token=None):
        """读取 GitHub 上的 images.txt"""
        repo = repo or os.getenv("GITHUB_REPO")
        token = token or os.getenv("GITHUB_TOKEN")
        return read_file(repo, "images.txt", token)

    def update_github_images(self, content, repo=None, token=None, message="Update images.txt"):
        """更新 GitHub 上的 images.txt，返回 commit SHA 用于后续查询 Actions"""
        repo = repo or os.getenv("GITHUB_REPO")
        token = token or os.getenv("GITHUB_TOKEN")
        try:
            sha = update_file(repo, "images.txt", content, token, message)
            return {"success": True, "commit_sha": sha}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def check_actions(self, commit_sha, repo=None, token=None):
        """通过 commit SHA 查询 Actions 状态"""
        repo = repo or os.getenv("GITHUB_REPO")
        token = token or os.getenv("GITHUB_TOKEN")
        return check_actions_by_sha(repo, token, commit_sha)

    def list_images(self, namespace, repo_name=None, key_id=None, key_secret=None, region=None):
        """列出阿里云镜像。只给 namespace 列出 repos，给了 repo_name 列出 tags"""
        key_id = key_id or os.getenv("ALIYUN_ACCESS_KEY_ID")
        key_secret = key_secret or os.getenv("ALIYUN_ACCESS_KEY_SECRET")
        region = region or os.getenv("ALIYUN_REGION", "cn-hangzhou")

        if repo_name:
            return list_tags(namespace, repo_name, key_id, key_secret, region)
        else:
            return list_repos(namespace, key_id, key_secret, region)


def main():
    fire.Fire(DockerImagePusher())

if __name__ == "__main__":
    main()
