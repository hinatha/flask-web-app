import torchvision

# 画像データの前処理
# Pytorchに対応する型に変更するためテンソル型に変換（ndarray型に似ている）
def image_to_tensor(image):
    """画像データをテンソル型の数値データへ変換"""
    image_tensor = torchvision.transforms.functional.to_tensor(image)
    return image_tensor