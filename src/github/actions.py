import requests
from datetime import datetime

def check_actions_by_sha(repo, token, commit_sha):
    """通过 commit SHA 查询 Actions 状态"""
    url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}/check-runs"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    check_runs = resp.json().get("check_runs", [])
    if not check_runs:
        return {"status": "not_found", "message": "No check runs found for this commit"}

    # 取第一个 check run（通常是 workflow）
    cr = check_runs[0]

    # 计算运行时长和提交时长
    now = datetime.utcnow()
    started_at = datetime.fromisoformat(cr["started_at"].replace("Z", "+00:00")) if cr.get("started_at") else None
    completed_at = datetime.fromisoformat(cr["completed_at"].replace("Z", "+00:00")) if cr.get("completed_at") else None

    run_duration = None
    if started_at:
        if completed_at:
            run_duration = int((completed_at - started_at).total_seconds())
        else:
            run_duration = int((now - started_at.replace(tzinfo=None)).total_seconds())

    # 提交时长（从 started_at 到现在）
    submitted_duration = int((now - started_at.replace(tzinfo=None)).total_seconds()) if started_at else None

    return {
        "status": cr["status"],  # completed / in_progress / queued
        "conclusion": cr.get("conclusion"),  # success / failure / cancelled / null
        "run_duration_seconds": run_duration,
        "submitted_duration_seconds": submitted_duration,
        "name": cr["name"]
    }
