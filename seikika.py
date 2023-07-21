from PIL import Image
import numpy as np

# 画像を読み込む
image = Image.open('output6.jpg')

# 画像をNumPy配列に変換
image_array = np.array(image)

# ピクセル値の最小値と最大値を求める
min_value = np.min(image_array)
max_value = np.max(image_array)

# ピクセル値を正規化する
normalized_image_array = (image_array - min_value) / (max_value - min_value)

# 正規化された画像を保存する
normalized_image = Image.fromarray((normalized_image_array * 255).astype(np.uint8))
normalized_image.save('6normalized_image.jpg')
