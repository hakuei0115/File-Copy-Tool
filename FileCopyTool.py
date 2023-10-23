import os
import shutil
import tkinter as tk

def copy_files():
    source_file = source_entry.get().strip('"') # 去除引號
    main_folder = folder_entry.get().strip('"') # 去除引號

    if not os.path.exists(source_file):
        result_label.config(text="指定的原始檔案不存在。請確保路徑正確。")
    else:
        for folder in os.listdir(main_folder):
            folder_path = os.path.join(main_folder, folder)
            if os.path.isdir(folder_path):
                target_path = os.path.join(folder_path, os.path.basename(source_file))
                try:
                    shutil.copy(source_file, target_path)
                    result_label.config(text=f"成功複製到: {target_path}")
                except Exception as ex:
                    result_label.config(text=f"複製到 {target_path} 失敗: {ex}")

# 創建Tkinter應用程式主視窗
root = tk.Tk()
root.title("檔案複製工具")

# 設定視窗大小
root.geometry("400x200")  # 調整成適合的寬度和高度

# 創建和設置Entry元件用於輸入
source_label = tk.Label(root, text="原始檔案路徑:")
source_label.pack()
source_entry = tk.Entry(root)
source_entry.pack()

folder_label = tk.Label(root, text="主資料夾路徑:")
folder_label.pack()
folder_entry = tk.Entry(root)
folder_entry.pack()

# 創建按鈕，連結到copy_files函式
copy_button = tk.Button(root, text="開始複製", command=copy_files)
copy_button.pack()

# 用於顯示結果的標籤
result_label = tk.Label(root, text="")
result_label.pack()

# 開始Tkinter應用程式的主迴圈
root.mainloop()
