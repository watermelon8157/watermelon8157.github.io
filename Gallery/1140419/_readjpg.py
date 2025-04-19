import os

def get_image_files():
    # 定義圖片檔案的副檔名
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp','.heic')
    image_files = []

    # 遍歷資料夾內的所有檔案
    for filename in os.listdir():
        if filename.lower().endswith(image_extensions):
            # 將完整路徑加入列表
            image_files.append(filename)
    return image_files

# 使用範例
image_list = get_image_files()

# 輸出結果
print("找到的圖片檔案:")
print(image_list)
print("END")