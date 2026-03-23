---
name: Docker 镜像推送助手
description: 管理 docker_image_pusher 仓库，更新镜像列表并同步到阿里云
---

# Docker 镜像推送助手

使用 `docker-image-pusher` CLI 工具管理镜像同步。

## 环境变量

需要配置以下环境变量：

- `GITHUB_TOKEN` - GitHub Personal Access Token
- `GITHUB_REPO` - 仓库名称（格式：用户名/仓库名）
- `ALIYUN_ACCESS_KEY_ID` - 阿里云 AccessKey ID
- `ALIYUN_ACCESS_KEY_SECRET` - 阿里云 AccessKey Secret
- `ALIYUN_NAME_SPACE` - 阿里云镜像命名空间

## 命令

### 读取镜像列表
```bash
docker-image-pusher read-images
```

### 更新镜像列表
```bash
docker-image-pusher update-images --content="nginx:1.28.2
mysql:8.0.46" --message="Update images"
```

### 查询 Actions 状态
```bash
docker-image-pusher check-actions
```

### 列出阿里云镜像 tag
```bash
docker-image-pusher list-aliyun-tags --repo-name=nginx
```

## 工作流程

1. 更新 images.txt 会自动触发 GitHub Actions
2. Actions 将镜像从 Docker Hub 同步到阿里云
3. 使用 check-actions 查询同步状态
