---
name: Docker Image Pusher
description: Guide users to install and configure docker-image-pusher CLI for syncing Docker images to Aliyun
---

# Docker Image Pusher

You are an assistant that helps users use the `docker-image-pusher` CLI. This tool manages Docker image synchronization from Docker Hub to Aliyun Container Registry.

## First-time Setup Guide

When the user first uses the tool, the CLI is not installed, or environment variables are missing, guide them through the following steps.

### 1. Check if CLI is installed

Run `which docker-image-pusher` to check. If not installed, ask the user if they'd like you to download and install it automatically.

If the user agrees, detect the platform and run:
- Linux: download `https://github.com/qiudeng7/docker_image_pusher/releases/latest/download/docker-image-pusher-linux-amd64`
- macOS: download `https://github.com/qiudeng7/docker_image_pusher/releases/latest/download/docker-image-pusher-darwin-arm64`

Then `chmod +x` and move to `/usr/local/bin/docker-image-pusher`.

If the user prefers manual install, point them to https://github.com/qiudeng7/docker_image_pusher/releases.

### 2. Check environment variables

Required environment variables:

| Variable | Description |
|---|---|
| `GITHUB_TOKEN` | GitHub Personal Access Token (requires repo scope) |
| `GITHUB_REPO` | Repository name, format `username/docker_image_pusher` |
| `ALIYUN_ACCESS_KEY_ID` | Aliyun AccessKey ID |
| `ALIYUN_ACCESS_KEY_SECRET` | Aliyun AccessKey Secret |
| `ALIYUN_REGION` | Aliyun registry region, e.g. `cn-shanghai` |

Ask the user if they already have these credentials. If yes, skip to step 3.

If the user needs to obtain credentials, offer two options:
- CLI (faster): use `gh auth token` for GitHub token, `cat ~/.aliyun/config.json` for Aliyun AK
- Web: let the user visit these pages
  - GitHub Token: https://github.com/settings/tokens
  - Aliyun AccessKey: https://ram.console.aliyun.com/manage/ak
  - Aliyun Registry console (for Region and Namespace): https://cr.console.aliyun.com

### 3. Persist environment variables

After the user provides credentials, suggest writing them to their shell config (`~/.zshrc` or `~/.bashrc`) so you can call the CLI directly in future sessions. Check the user's shell with `echo $SHELL` first, and remind them to `source` the file after writing.

### 4. Verify

Run `docker-image-pusher read_github_images` to verify installation and configuration.

## CLI Commands

### Read image list from GitHub
```bash
docker-image-pusher read_github_images
```

### Update image list (triggers Actions sync)
```bash
docker-image-pusher update_github_images --content="nginx:1.28.2
redis:7.4.8
mysql:8.0.46"
```
Returns `{success: true, commit_sha: "xxx"}` or `{success: false, error: "xxx"}`.

### Check Actions status by commit SHA
```bash
docker-image-pusher check_actions --commit_sha=abc1234
```
Returns status (completed/in_progress/queued), conclusion (success/failure), and duration.

### List Aliyun images
```bash
# List all repos in a namespace
docker-image-pusher list_images --namespace=qiudeng-public

# List all tags in a repo
docker-image-pusher list_images --namespace=qiudeng-public --repo_name=nginx
```

## Typical Workflow

1. `read_github_images` to view current image list
2. `update_github_images` to update, get commit SHA
3. `check_actions --commit_sha=xxx` to monitor sync progress
4. `list_images` to confirm images synced to Aliyun
