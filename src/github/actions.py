import requests
import time

def get_latest_run(repo, token, workflow_id="docker.yaml"):
    """获取最新的 workflow run"""
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/runs"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers, params={"per_page": 1})
    resp.raise_for_status()
    runs = resp.json()["workflow_runs"]
    return runs[0] if runs else None

def wait_for_run(repo, token, run_id, timeout=600):
    """等待 workflow run 完成"""
    url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}"
    headers = {"Authorization": f"token {token}"}
    start = time.time()

    while time.time() - start < timeout:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        status = resp.json()["status"]
        conclusion = resp.json().get("conclusion")

        if status == "completed":
            return {"status": status, "conclusion": conclusion}
        time.sleep(10)

    return {"status": "timeout", "conclusion": None}
