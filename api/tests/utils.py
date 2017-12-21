import io

from PIL import Image


def gen_image(name='test.png'):
    """Возвращает файл изображения."""
    file = io.BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = name
    file.seek(0)

    return file
