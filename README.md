# GIF to Images Converter

## 简介
GIF to Images Converter是一个用Python编写的应用程序，允许用户将GIF文件逐帧导出为JPG或PNG格式的图片。该应用程序提供了一个用户友好的图形界面（GUI），使得用户可以轻松选择GIF文件和输出格式，并将帧图像保存到一个与GIF文件同名的文件夹中。

## 项目结构
```
gif_to_images/
├── src/
│   ├── __init__.py
│   ├── gif_processor.py
│   └── main.py
└── gui/
    ├── __init__.py
    └── app.py
```

- `src/`: 包含核心功能代码。
  - `gif_processor.py`: 处理 GIF 文件并逐帧导出图片。
  - `main.py`: 命令行接口，用于执行逐帧导出操作。
  
- `gui/`: 包含图形用户界面（GUI）代码。
  - `app.py`: 提供用户界面，允许用户选择 GIF 文件和输出格式，并执行转换操作。

## 安装
在运行此项目之前，请确保已安装所需的依赖库。你可以使用以下命令来安装这些库：

```bash
pip install pillow tkinter
```

## 使用方法

### 运行 GUI 应用
1. 进入项目目录：
```bash
cd gif_to_images_converter
```

2. 运行 GUI 应用：
```bash
python gui/app.py
```

### 运行命令行接口
1. 进入项目目录：
```bash
cd gif_to_images_converter
```

2. 运行命令行接口，将 GIF 文件逐帧导出为 PNG 格式的图片：
```bash
python src/main.py path/to/your.gif --format png
```

或导出为 JPG 格式的图片：
```bash
python src/main.py path/to/your.gif --format jpg
```

## 贡献
如果你有任何改进建议或发现了任何问题，欢迎提交 issue 或 pull request。

## 许可证
本项目采用 MIT 许可证。详情请参阅 LICENSE 文件。