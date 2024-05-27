import argparse
from gif_processor import export_frames_from_gif


def main():
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="将GIF逐帧导出为JPG或PNG格式的图片")
    parser.add_argument("gif_path", type=str, help="GIF文件的路径")
    parser.add_argument("--format", type=str, choices=['jpg', 'png'], default='png', help="输出图片格式（默认：png）")

    args = parser.parse_args()

    # 调用函数导出GIF帧
    export_frames_from_gif(args.gif_path, args.format)


if __name__ == "__main__":
    main()
