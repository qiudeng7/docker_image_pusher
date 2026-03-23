---
name: Docker Image Pusher
description: Manage docker_image_pusher repository and sync images to Aliyun
---

# Docker Image Pusher

Use `docker-image-pusher` CLI to manage image synchronization.

## Environment Variables

Required environment variables:

- `GITHUB_TOKEN` - GitHub Personal Access Token
- `GITHUB_REPO` - Repository name (format: username/repo)
- `ALIYUN_ACCESS_KEY_ID` - Aliyun AccessKey ID
- `ALIYUN_ACCESS_KEY_SECRET` - Aliyun AccessKey Secret
- `ALIYUN_NAME_SPACE` - Aliyun registry namespace

## Commands

### Read image list
```bash
docker-image-pusher read-images
```

### Update image list
```bash
docker-image-pusher update-images --content="nginx:1.28.2
mysql:8.0.46" --message="Update images"
```

### Check Actions status
```bash
docker-image-pusher check-actions
```

### List Aliyun image tags
```bash
docker-image-pusher list-aliyun-tags --repo-name=nginx
```

## Workflow

1. Updating images.txt triggers GitHub Actions automatically
2. Actions sync images from Docker Hub to Aliyun
3. Use check-actions to query sync status
