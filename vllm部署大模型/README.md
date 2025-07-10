# Qwen2.5-VL-3B-Instruct 模型部署指南

本指南将帮助您在 AutoDL 平台上部署 Qwen2.5-VL-3B-Instruct 多模态大语言模型。

## 环境准备

1. **租用 GPU 服务器**
   - 在 AutoDL 平台租用 GPU 服务器
   - 选择包含 vLLM 的社区镜像
   - 登录 Jupyter Lab

2. **配置网络加速**
   ```bash
   source /etc/network_turbo
   ```

## 模型下载

1. **创建模型目录**
   ```bash
   mkdir -p ~/autodl-tmp/model
   ```

2. **创建下载脚本**
   创建 `download.py` 文件并添加以下内容：
   ```python
   from modelscope import snapshot_download
   
   model_dir = snapshot_download(
       'Qwen/Qwen2.5-VL-3B-Instruct',
       cache_dir='/autodl-tmp/model'
   )
   ```

3. **运行下载脚本**
   ```bash
   python download.py
   ```

## 启动模型服务

使用 vLLM 工具运行模型：

```bash
python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/model/Qwen/Qwen2.5-VL-3B-Instruct \
  --served-model-name Qwen2.5-VL-3B-Instruct \
  --max-model-len 24576 \
  --host 0.0.0.0 \
  --port 8000 \
  --trust-remote-code \
  --limit-mm-per-prompt image=5
```

## 端口映射

1. 在 AutoDL 控制台找到自定义服务
2. 复制 SSH 端口转发命令
3. 在本地终端中运行该命令，将远程端口映射到本地
   - 将右侧端口修改为本地端口（如 8000）
   - 左侧端口保持为 8000

## 使用说明

- 模型服务启动后，您可以在本地运行test.py调用模型

## 注意事项

- 确保服务器有足够的存储空间下载模型
- 模型运行需要较大的 GPU 显存
- 建议在稳定网络环境下操作

## 故障排除

- 如果遇到端口冲突，请修改 `--port` 参数
- 确保所有文件路径正确
- 检查网络连接是否正常