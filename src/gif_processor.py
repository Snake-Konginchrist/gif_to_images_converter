import os
from PIL import Image


# 创建目录，如果目录不存在则创建
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# 将GIF文件逐帧导出为指定格式的图片
def export_frames_from_gif(gif_path, output_format='png'):
    with Image.open(gif_path) as img:
        # 获取GIF文件的名称（不包含扩展名）
        gif_name = os.path.splitext(os.path.basename(gif_path))[0]
        # 创建导出图片的目录
        output_dir = os.path.join(os.path.dirname(gif_path), gif_name)
        create_directory(output_dir)

        frame_number = 0
        while True:
            # 生成每一帧图片的路径和文件名
            frame_path = os.path.join(output_dir, f"{gif_name}_frame_{frame_number}.{output_format}")
            img.seek(frame_number)  # 定位到当前帧

            # 如果输出格式是 JPG，则将图像转换为 RGB 模式
            frame = img.convert('RGB') if output_format.lower() == 'jpg' else img

            frame.save(frame_path, output_format.upper())  # 保存当前帧为指定格式的图片
            frame_number += 1

            try:
                img.seek(frame_number)  # 尝试定位到下一帧
            except EOFError:
                break  # 如果已经到达GIF文件末尾，退出循环
