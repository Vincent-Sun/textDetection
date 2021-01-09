import os
import random

from PIL import Image

ROOT_DIR = os.getcwd()
pic_src_dir = os.path.join(ROOT_DIR, 'pictures')
pic_src_dir = os.path.join(ROOT_DIR, 'train_data/pic')

for root, dirs, files in os.walk(pic_src_dir):
    for file in files:
        currentPath = os.path.join(root, file)
        print(currentPath)
        # 读取图片
        img = Image.open(currentPath)

        # 以0.5概率水平翻转
        flip = bool(random.randint(0, 1))
        print(flip)
        flipped_img = img
        if flip:
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # 随机将图片的长和宽resize到640-2560之间，且不保证长宽比不变
        if flipped_img.mode == 'P':
            if 'transparency' in flipped_img.info:
                flipped_img = flipped_img.convert('RGBA')
            else:
                flipped_img = flipped_img.convert('RGB')

        if flipped_img.mode == "RGBA":
            # The image has transparency
            out = Image.new("RGB", flipped_img.size, (192, 192, 192))
            # Use the image's own alpha channel as the mask
            out.paste(flipped_img, mask=flipped_img)
        else:
            out = flipped_img

        length = random.randint(640, 2560)
        width = random.randint(640, 2560)
        resize_img = out.resize((length, width), Image.ANTIALIAS)
        print(length, width)

        # 随机在图片选择640*640大小的区域进行截取
        pos1 = [random.randint(0, length - 640), random.randint(0, width - 640)]
        pos2 = [pos1[0] + 640, pos1[1] + 640]
        cropped_img = resize_img.crop((pos1[0], pos1[1], pos2[0], pos2[1]))
        print(pos1, pos2)

        # 保存图片
        new_file = os.path.join(pic_dst_dir, file)
        print(new_file)
        print('======================================')
        cropped_img.save(new_file, quality=90, optimize=True)

