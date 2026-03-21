# 推理示例数据说明

## 文件

| 文件 | 说明 |
|------|------|
| `inference_sample.jsonl` | 推理输入列表：**每行一个 JSON 对象**（JSONL），字段 `captions`（文本）、`img_path`（图片路径） |
| `inference_sample_images/` | 与上面 `img_path` 对应的示例图片（256×256 PNG） |

## 使用方式

在项目根目录下运行推理时，将 `--test_file` 指向本文件，例如：

```bash
python inference.py --test_file="data/inference_sample.jsonl" ...
```

若在其它工作目录运行，请把 `img_path` 改成**绝对路径**，或保持从仓库根目录启动命令。

## 自行扩展

1. 把新图片放入 `inference_sample_images/`（或任意子目录）。
2. 在 `inference_sample.jsonl` **末尾追加一行** JSON，包含新的 `captions` 与 `img_path`。
3. 路径建议使用相对于仓库根目录的形式，例如：`data/inference_sample_images/my_photo.jpg`。
