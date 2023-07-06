"""
给图片添加文件水印
输入水印文字，以及文字大小、透明度
数字1-9，表示左上、中上、右上、中左依次
程序会以当前images目录为准，png文件均需存储到此目录
"""
import os.path

from PIL import Image, ImageDraw, ImageFont


def get_position(image_width, image_height, text_width, text_height, position_id=9, margin=10):
    margin = 10
    if position_id == 1:
        return (margin, margin)
    elif position_id == 2:
        return (image_width // 2 - text_width // 2, margin)
    elif position_id == 3:
        return (image_width - text_width - margin, margin)
    elif position_id == 4:
        return (margin, image_height // 2 - text_height // 2)
    elif position_id == 5:
        return (image_width // 2 - text_width // 2, image_height // 2 - text_height // 2)
    elif position_id == 6:
        return (image_width - text_width - margin, image_height // 2 - text_height // 2)
    elif position_id == 7:
        return (margin, image_height - text_height - margin)
    elif position_id == 8:
        return (image_width // 2 - text_width // 2, image_height - text_height - margin)
    elif position_id == 9:
        return (image_width - text_width - margin, image_height - text_height - margin)


def add_watermark(filename, text, font_name='Roboto-Itallic.ttf', font_size=20, font_opacity=50, position_id=9):
    with Image.open(filename).convert('RGBA') as base:
        # 创建一个新的透明画面，大小和原图一样
        txt = Image.new('RGBA', base.size, (225, 225, 225, 0))
        # 使用指定字体
        fnt = ImageFont.truetype(font_name, font_size)
        # 准备画文字
        d = ImageDraw.Draw(txt)
        # 得到文字的宽度和高度
        text_width, text_height = d.textsize(text, font=fnt)
        # 得到文字位置
        pos = get_position(base.size[0], base.size[1], text_width, text_height, position_id=position_id)
        # 将文字画到画布上
        d.text(pos, text, font=fnt, fill=(225, 225, 225, 256 * font_opacity // 100))
        # 将画布和原图合并
        out = Image.alpha_composite(base, txt)
        # 保存图片
        out_filename = 'watermark/{}'.format(os.path.basename(filename))
        if not os.path.exists('watermark'):
            os.makedirs('watermark')
        out.save(out_filename, 'PNG')


if __name__ == '__main__':
    text = input('请输入水印文字：').strip()
    font_size = int(input('请输入文字大小：[20]') or '20')
    font_opacity = int(input('请输入文字透明度：[50]') or '50')
    position_id = int(input('请输入水印位置：[9]') or '9')
    font_name = 'D:/py_project/learn/simhei.ttf'
    for f in os.listdir('images'):
        if f.endswith('.png'):
            filename = 'images/{}'.format(f)
            print(f'给{filename}添加水印')
            add_watermark(filename, text, font_name, font_size, font_opacity, position_id)
