from json import dumps
import os
from PIL import Image
import base64


def auto_label(numberOfPics, image_path='train_data/pic', json_path='train_data/json', txt_path='text_label'):
    for i in range(1, numberOfPics+1):
        txt_name = 'gt_img_%d.txt' % i
        image_name = 'img_%d.jpg' % i
        json_name = 'img_%d.json' % i
        full_txt_name = os.path.join(txt_path, txt_name)
        full_image_name = os.path.join(image_path, image_name)
        if not os.path.exists(full_image_name):
            image_name = 'img_%d.png' % i
            full_image_name = os.path.join(image_path, image_name)
        full_json_name = os.path.join(json_path, json_name)
        img2json(full_image_name, full_json_name, full_txt_name)


def img2json(image_name, json_name, txt_name):
    content = dict()
    content['version'] = '3.15.1'
    content['flags'] = {}
    content['shapes'] = []

    txt = open(txt_name, 'rU', encoding='UTF-8')
    data = txt.readlines()
    txt.close()
    index = 1
    for row_data in data:
        list_ = row_data.split(',')
        shape = dict()
        shape['label'] = 'text_%d' % index
        shape['line_color'] = None
        shape['fill_color'] = None
        shape['points'] = []
        for i in range(0, 8, 2):
            shape['points'].append([int(list_[i]), int(list_[i + 1])])
        shape['shape_type'] = 'polygon'
        shape['flags'] = {}
        content['shapes'].append(shape)
        index += 1

    content['lineColor'] = [0, 255, 0, 128]
    content['fillColor'] = [255, 0, 0, 128]
    content['imagePath'] = image_name
    with open(image_name, 'rb') as f:
        content['imageData'] = base64.b64encode(f.read()).decode()

    img = Image.open(image_name)
    content['imageWidth'], content['imageHeight'] = list(img.size)

    json_data = dumps(content, indent=2)
    with open(json_name, 'w') as json_file:
        json_file.write(json_data)


if __name__ == '__main__':
    # numberOfPics = 18000
    auto_label(numberOfPics)
