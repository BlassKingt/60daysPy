import sys
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading

class RequestsInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Requests 库安装指南")
        self.root.geometry("700x550")
        self.root.resizable(True, True)
        
        # 设置样式
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))
        style.configure("Subtitle.TLabel", font=("Arial", 12, "bold"))
        style.configure("Fixed.TLabel", font=("Courier", 10))
        
        self.create_widgets()
        
    def create_widgets(self):
        # 标题
        title = ttk.Label(self.root, text="ModuleNotFoundError: No module named 'requests'", 
                         style="Title.TLabel", foreground="red")
        title.pack(pady=10)
        
        # 问题描述
        desc = ttk.Label(self.root, text="您的Python环境缺少requests库。这个库用于发送HTTP请求，是Python中最常用的库之一。", 
                        wraplength=650)
        desc.pack(pady=5, padx=20, fill=tk.X)
        
        # 安装说明
        frame = ttk.LabelFrame(self.root, text="安装方法")
        frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # 方法1: 使用pip：pip install requests
        method1 = ttk.Label(frame, text="1. 使用pip安装 (推荐)", style="Subtitle.TLabel")
        method1.grid(row=0, column=0, sticky=tk.W, pady=(10, 5), padx=10)
        
        cmd1 = ttk.Label(frame, text="pip install requests", style="Fixed.TLabel")
        cmd1.grid(row=1, column=0, sticky=tk.W, padx=20)
        
        # 方法2: 使用conda
        method2 = ttk.Label(frame, text="2. 使用conda安装", style="Subtitle.TLabel")
        method2.grid(row=2, column=0, sticky=tk.W, pady=(20, 5), padx=10)
        
        cmd2 = ttk.Label(frame, text="conda install requests", style="Fixed.TLabel")
        cmd2.grid(row=3, column=0, sticky=tk.W, padx=20)
        
        # 方法3: 手动安装
        method3 = ttk.Label(frame, text="3. 手动安装", style="Subtitle.TLabel")
        method3.grid(row=4, column=0, sticky=tk.W, pady=(20, 5), padx=10)
        
        manual_desc = ttk.Label(frame, text="从PyPI下载whl或tar.gz文件，然后使用pip安装:", wraplength=600)
        manual_desc.grid(row=5, column=0, sticky=tk.W, padx=20)
        
        cmd3 = ttk.Label(frame, text="pip install requests-2.28.1-py3-none-any.whl", style="Fixed.TLabel")
        cmd3.grid(row=6, column=0, sticky=tk.W, padx=20)
        
        # 安装按钮
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.install_btn = ttk.Button(button_frame, text="使用pip自动安装", command=self.install_requests)
        self.install_btn.pack(side=tk.LEFT, padx=5)
        
        self.check_btn = ttk.Button(button_frame, text="检查requests是否已安装", command=self.check_installation)
        self.check_btn.pack(side=tk.LEFT, padx=5)
        
        # 输出区域
        output_frame = ttk.LabelFrame(self.root, text="安装输出")
        output_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=10, wrap=tk.WORD)
        self.output_text.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        
        # 状态栏
        self.status = ttk.Label(self.root, text="就绪", relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
        
    def install_requests(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "开始安装requests库...\n")
        self.status.config(text="正在安装...")
        
        # 在后台线程中运行安装过程
        thread = threading.Thread(target=self.run_installation)
        thread.daemon = True
        thread.start()
        
    def run_installation(self):
        try:
            # 使用当前Python解释器的pip
            pip_cmd = [sys.executable, "-m", "pip", "install", "requests"]
            
            process = subprocess.Popen(
                pip_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            
            stdout, stderr = process.communicate()
            
            # 更新GUI必须在主线程中执行
            self.root.after(0, self.update_output, stdout, stderr, process.returncode)
            
        except Exception as e:
            self.root.after(0, self.show_error, str(e))
            
    def update_output(self, stdout, stderr, returncode):
        self.output_text.insert(tk.END, stdout)
        if stderr:
            self.output_text.insert(tk.END, f"\n错误:\n{stderr}")
        
        if returncode == 0:
            self.output_text.insert(tk.END, "\n安装成功！")
            self.status.config(text="安装成功")
        else:
            self.output_text.insert(tk.END, f"\n安装失败，返回码: {returncode}")
            self.status.config(text="安装失败")
            
    def check_installation(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "检查requests库...\n")
        
        try:
            # 尝试导入requests
            import requests
            version = requests.__version__
            self.output_text.insert(tk.END, f"✓ requests已安装，版本: {version}\n")
            self.status.config(text="requests已安装")
        except ImportError:
            self.output_text.insert(tk.END, "✗ requests未安装\n")
            self.status.config(text="requests未安装")
            
    def show_error(self, error_msg):
        messagebox.showerror("错误", f"安装过程中发生错误:\n{error_msg}")
        self.status.config(text="安装错误")

if __name__ == "__main__":
    root = tk.Tk()
    app = RequestsInstaller(root)
    root.mainloop()