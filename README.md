# Docker Image Pusher

基于 [tech-shrimp/docker_image_pusher](https://github.com/tech-shrimp/docker_image_pusher) 的扩展版本，新增 CLI 工具和配套 Skills。

通过 CLI 一键将 Docker Hub 镜像搬运到阿里云，也可以让 AI 模型通过 CLI 自动完成镜像搬运。

## 文档

- 原仓库的 Actions 使用方式：[docs/old_readme.md](docs/old_readme.md)
- CLI 安装和使用：[docs/cli.md](docs/cli.md)

## Skills 安装

将 `skills/zh/SKILL.md`（中文）或 `skills/en/SKILL.md`（英文）复制到你的 Skills 目录：

```bash
# 安装到用户级（所有项目可用）
cp -r skills/zh ~/.claude/skills/docker-image-pusher

# 或安装到项目级（仅当前项目可用）
mkdir -p .claude/skills/docker-image-pusher
cp skills/zh/SKILL.md .claude/skills/docker-image-pusher/
```

安装后，AI 模型会自动引导你完成 CLI 的安装和配置。
