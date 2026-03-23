# Docker Image Pusher CLI

## 开发环境

### 配置环境
```bash
# 创建虚拟环境并安装依赖
uv venv
uv pip install fire requests python-dotenv

# 配置环境变量
cp example.env .env
# 编辑 .env 填入你的 GitHub token、阿里云 Access Key 等
```

### 使用
```bash
# 读取镜像列表
.venv/bin/python -m src.cli.main read_images

# 查询 Actions 状态
.venv/bin/python -m src.cli.main check_actions

# 列出阿里云镜像
.venv/bin/python -m src.cli.main list_aliyun_tags --namespace=your-ns --repo_name=nginx

# 更新镜像列表
.venv/bin/python -m src.cli.main update_images --content="nginx:1.28.2"
```

