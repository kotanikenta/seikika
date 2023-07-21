from PIL import Image
import numpy as np
import os

# 入力画像フォルダと出力画像フォルダのパスを指定
input_folder = 'ikkatsu_input/'
output_folder = 'ikkatsu_output/'

# 入力画像フォルダ内のすべてのファイルに対して処理を行う
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 画像を読み込む
        image = Image.open(os.path.join(input_folder, filename))

        # 画像をNumPy配列に変換
        image_array = np.array(image)

        # ピクセル値の最小値と最大値を求める
        min_value = np.min(image_array)
        max_value = np.max(image_array)

        # ピクセル値を正規化する
        normalized_image_array = (image_array - min_value) / (max_value - min_value)

        # 正規化された画像を保存する
        normalized_image = Image.fromarray((normalized_image_array * 255).astype(np.uint8))
        output_path = os.path.join(output_folder, filename)
        normalized_image.save(output_path)
