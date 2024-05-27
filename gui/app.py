import tkinter as tk
from tkinter import filedialog, messagebox
from src.gif_processor import export_frames_from_gif


class GIFtoImagesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF to Images Converter")

        # 设置窗口大小
        self.root.geometry('300x250')  # 你可以根据需要调整宽度和高度

        # 标签，用于显示提示信息
        self.label = tk.Label(root, text="选择一个GIF文件：")
        self.label.pack(pady=10)

        # 按钮，用于浏览文件
        self.file_button = tk.Button(root, text="浏览", command=self.browse_file)
        self.file_button.pack(pady=5)

        # 单选按钮，用于选择输出格式
        self.format_var = tk.StringVar(value='png')
        self.radio_png = tk.Radiobutton(root, text="PNG", variable=self.format_var, value='png')
        self.radio_jpg = tk.Radiobutton(root, text="JPG", variable=self.format_var, value='jpg')

        self.radio_png.pack(pady=5)
        self.radio_jpg.pack(pady=5)

        # 按钮，用于开始转换
        self.convert_button = tk.Button(root, text="转换", command=self.convert_gif)
        self.convert_button.pack(pady=20)

        self.gif_path = ""

    # 浏览文件
    def browse_file(self):
        self.gif_path = filedialog.askopenfilename(filetypes=[("GIF文件", "*.gif")])
        if self.gif_path:
            self.label.config(text=f"已选择文件: {self.gif_path}")

    # 转换GIF文件
    def convert_gif(self):
        if not self.gif_path:
            messagebox.showerror("错误", "请先选择一个GIF文件。")
            return

        output_format = self.format_var.get()
        try:
            export_frames_from_gif(self.gif_path, output_format)
            messagebox.showinfo("成功", f"帧图像已成功导出为{output_format.upper()}格式。")
        except Exception as e:
            messagebox.showerror("错误", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = GIFtoImagesApp(root)
    root.mainloop()
