import os
import fire
import shutil
from pathlib import Path
from dotenv import load_dotenv
from src.github import read_file, update_file, get_latest_run, wait_for_run
from src.aliyun import list_tags

# 加载 .env 文件
load_dotenv()


class DockerImagePusher:
    def read_images(self, repo=None, token=None):
        """读取 images.txt 内容"""
        repo = repo or os.getenv("GITHUB_REPO")
        token = token or os.getenv("GITHUB_TOKEN")
        return read_file(repo, "images.txt", token)

    def update_images(self, content, repo=None, token=None, message="Update images.txt"):
        """更新 images.txt 并触发 Actions"""
        repo = repo or os.getenv("GITHUB_REPO")
        token = token or os.getenv("GITHUB_TOKEN")
        sha = update_file(repo, "images.txt", content, token, message)
        print(f"Updated images.txt, commit: {sha}")
        return sha

    def check_actions(self, repo=None, token=None, run_id=None):
        """查询 Actions 状态"""
        repo = repo or os.getenv("GITHUB_REPO")
        token = token or os.getenv("GITHUB_TOKEN")

        if run_id:
            result = wait_for_run(repo, token, run_id, timeout=0)
        else:
            result = get_latest_run(repo, token)

        print(f"Status: {result}")
        return result

    def list_aliyun_tags(self, namespace, repo_name, key_id=None, key_secret=None, region=None):
        """列出阿里云镜像 tag"""
        key_id = key_id or os.getenv("ALIYUN_ACCESS_KEY_ID")
        key_secret = key_secret or os.getenv("ALIYUN_ACCESS_KEY_SECRET")
        region = region or os.getenv("ALIYUN_REGION", "cn-hangzhou")

        tags = list_tags(namespace, repo_name, key_id, key_secret, region)
        print(f"Tags: {tags}")
        return tags

    def install_skill(self, scope="project", lang="zh"):
        """安装 skill 到 .claude/skills/"""
        skill_src = Path(__file__).parent.parent.parent / "skills" / lang

        if scope == "project":
            skill_dst = Path.cwd() / ".claude" / "skills" / "docker-image-pusher"
        else:
            skill_dst = Path.home() / ".claude" / "skills" / "docker-image-pusher"

        skill_dst.mkdir(parents=True, exist_ok=True)
        shutil.copytree(skill_src, skill_dst, dirs_exist_ok=True)
        print(f"Skill installed to: {skill_dst}")


def main():
    fire.Fire(DockerImagePusher())

if __name__ == "__main__":
    main()
