# Docker Image Pusher CLI

## 开发环境

### 配置环境
```bash
# 创建虚拟环境并安装依赖
uv venv
uv pip install fire requests python-dotenv aliyun-python-sdk-core aliyun-python-sdk-cr

# 配置环境变量
cp example.env .env
# 编辑 .env 填入你的 GitHub token、阿里云 Access Key 等
```

### 使用
```bash
# 读取 GitHub 上的 images.txt
.venv/bin/python -m src.cli.main read_github_images

# 更新 GitHub 上的 images.txt（返回 commit SHA）
.venv/bin/python -m src.cli.main update_github_images --content="nginx:1.28.2
redis:7.4.8"

# 通过 commit SHA 查询 Actions 构建状态
.venv/bin/python -m src.cli.main check_actions --commit_sha=abc1234

# 列出阿里云 namespace 下的所有 repo
.venv/bin/python -m src.cli.main list_images --namespace=qiudeng-public

# 列出阿里云 repo 下的所有 tag
.venv/bin/python -m src.cli.main list_images --namespace=qiudeng-public --repo_name=nginx
```

## 安装

### 二进制
从 [Releases](https://github.com/qiudeng7/docker_image_pusher/releases) 下载对应平台的二进制文件：
```bash
# Linux
wget https://github.com/qiudeng7/docker_image_pusher/releases/latest/download/docker-image-pusher-linux-amd64
chmod +x docker-image-pusher-linux-amd64
sudo mv docker-image-pusher-linux-amd64 /usr/local/bin/docker-image-pusher
```

### Docker
```bash
docker pull ghcr.io/qiudeng7/docker_image_pusher:latest
docker run --env-file .env ghcr.io/qiudeng7/docker_image_pusher read_github_images
```
