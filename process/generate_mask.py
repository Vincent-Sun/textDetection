import os
import shutil

mask_path = 'train_data/cv2_mask'
labelme_json_path = 'train_data/labelme_json'
# numberOfPics = 18000


for index in range(1, numberOfPics+1):
    json_path = 'img_%d_json' % index
    path = os.path.join(labelme_json_path, json_path)
    img_name = os.path.join(path, 'label.png')
    # print(img_name)
    filename = 'img_%d.png' % index
    filename = os.path.join(mask_path, filename)
    # print(filename)
    shutil.copyfile(img_name, filename)
