import requests
import base64

def read_file(repo, path, token):
    """读取 GitHub 仓库文件内容"""
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return base64.b64decode(resp.json()["content"]).decode()

def update_file(repo, path, content, token, message="Update file"):
    """更新 GitHub 仓库文件"""
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {"Authorization": f"token {token}"}

    # 获取当前文件 SHA
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    sha = resp.json()["sha"]

    # 更新文件
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "sha": sha
    }
    resp = requests.put(url, json=data, headers=headers)
    resp.raise_for_status()
    return resp.json()["commit"]["sha"]
