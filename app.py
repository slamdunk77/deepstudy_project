"""
程序中文字检测识别调用了百度paddle相应接口实现
程序中企业实体识别调用了百度easyDL相应接口
企业实体识别模型的训练由参赛者自行完成
其余代码皆为原创
"""
#  coding=utf-8
from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify, make_response
from flask_cors import CORS
import os
import zipfile
import xlwt
import re
import filetype
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import paddlehub as hub
import numpy as np
import numpyencoder as NpEncoder
import requests
import base64
from PIL import Image
import cv2
import oss2
import json



# 加载移动端预训练模型
# ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")
# 服务端可以加载大模型，效果更好
# ocr = hub.Module(name="chinese_ocr_db_crnn_server")


# oss相关信息，用于生成excel后访问oss进行保存
access_key_id = 'LTAI4GGYRQVaGW9MQSyvteuR'
access_key_secret = 'y5n93LDFCflKuTXXE0F9ssjmZjE7Mh'
bucket_name = 'ner-buaaer-software'
endpoint = 'http://oss-cn-beijing.aliyuncs.com'
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

# 配置flask跨域
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}},
            allow_headers={r"/*": {"Access-Control-Request-Headers": "*"}},
            supports_credentials=True)


# 识别图片内容
class CVRes(object):
    """
    docstring for CVRes
    :param number:返回码
    :param name:图片名称
    """
    def __init__(self, number, name):
        super(CVRes, self).__init__()
        self.number = str(number)
        self.name = str(name)


def obj2json(obj):
    """
    将CVRes类转换为Json格式
    :param obj:返回码
    :return:图片名称
    """
    return {
        "number": obj.number,
        "name": obj.name
    }


# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.integer):
#             return int(obj)
#         elif isinstance(obj, np.floating):
#             return float(obj)
#         elif isinstance(obj, np.ndarray):
#             return obj.tolist()
#         else:
#             return super(NpEncoder, self).default(obj)

def cv2_to_base64(image):
    """
    将图片转为base64格式
    :param image: 图片路径
    :return: 图片对应的base64的编码信息
    """
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tostring()).decode('utf8')


def get_content(img_path):
    """
    获得图片中的文字内容
    :param img_path: 图片路径
    :return: 识别结果
    """
    # 使用mobile模型
    # test_img_path = [file_path]
    # np_images = [cv2.imread(image_path) for image_path in test_img_path]
    # results = ocr.recognize_text(
    #     images=np_images,  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
    #     use_gpu=False,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
    #     output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result；
    #     visualization=True,  # 是否将识别结果保存为图片文件；
    #     box_thresh=0.5,  # 检测文本框置信度的阈值；
    #     text_thresh=0.5)  # 识别中文文本置信度的阈值；
    # 使用server模型
    data = {'images': [cv2_to_base64(cv2.imread(img_path))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/chinese_ocr_db_crnn_server"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    results = r.json()["results"]
    ans = []
    for result in results:
        data = result['data']
        for information in data:
            ans.append(information['text'])
    return ans


def zip_excel(name_list):
    """
    zip文件中的图片识别结果形成一个表
    :param name_list: 识别结果
    :return: excel表格网址
    """
    new_book = xlwt.Workbook()
    now_time = time.gmtime()
    note = int(time.mktime(now_time))
    work_sheet = new_book.add_sheet(str(note))
    work_sheet.write(0, 0, '图片')
    work_sheet.write(0, 1, '商铺名称')
    count = 1
    for eachVar in name_list:
        work_sheet.write(count, 0, eachVar["name"])
        work_sheet.write(count, 1, eachVar["words"][0])
        count = int(count) + 1
    # 保存excel文件
    save_path = "excel/" + str(note) + ".xls"
    new_book.save(save_path)
    result = bucket.put_object_from_file(save_path, save_path)
    excel_url = bucket.sign_url('GET', save_path, 60 * 60 * 24 * 30)
    return excel_url


def jpg_excel(company):
    """
    单张图片识别结果形成的表格
    :param company: 图片中识别出来的企业实体
    :return: excel表格网址
    """
    new_book = xlwt.Workbook()
    now_time = time.gmtime()
    note = int(time.mktime(now_time))
    work_sheet = new_book.add_sheet(str(note))
    work_sheet.write(0, 0, '图片')
    work_sheet.write(0, 1, '商铺名称')
    work_sheet.write(1, 0, company['name'])
    work_sheet.write(1, 1, company["words"][0])
    # 保存excel文件
    save_path = "excel/" + str(note) + ".xls"
    new_book.save(save_path)
    result = bucket.put_object_from_file(save_path, save_path)
    excel_url = bucket.sign_url('GET', save_path, 60 * 60 * 24 * 30)
    return excel_url


def is_valid_image(img_path):
    """
        判断文件是否为有效（完整）的图片
        :param img_path:图片路径
        :return:True：有效 False：无效
    """
    b_valid = True
    try:
        Image.open(img_path).verify()
    except:
        b_valid = False
    return b_valid


def transfer_image(img_path):
    """
    转换图片格式
    :param img_path:图片路径
    :return: True：成功 False：失败
    """
    if is_valid_image(img_path):
        try:
            my_type = filetype.guess(img_path)
            return_path = img_path.replace(str(my_type.extension), "jpg")
            im = Image.open(img_path)
            rgb_im = im.convert('RGB')
            rgb_im.save(return_path)
            return return_path
        except IOError:
            print("另存为图片失败")
    else:
        return None


def is_photo(img_type):
    """
    判断是否为图片
    :param img_type:
    :return: 1 是图片； 0 不是图片
    """
    types = ['jpg', 'png', 'gif', 'webp', 'cr2', 'tif', 'bmp', 'jxr', 'psd', 'ico']
    for eachVar in types:
        m = re.match(eachVar, img_type)
        if m is None:
            continue
        else:
            return 1
    return 0


def un_zip(file_path, file_name):
    """
    unzip zip file
    :param file_path:zip文件路径
    :param file_name: zip文件名字
    :return: 保存的zip路径
    """
    zip_file = zipfile.ZipFile(file_path)
    now_time = time.gmtime()
    note = int(time.mktime(now_time))
    path_name = file_name.replace(".zip", "")
    return_path = 'file/' + path_name + str(note)
    if os.path.exists(return_path) and os.path.isdir(return_path):
        pass
    else:
        os.mkdir(return_path)
    for names in zip_file.namelist():
        zip_file.extract(names, return_path + "/")
    zip_file.close()
    return return_path


class picture_information(object):
    """
    保存图片信息
    :param name: 图片名称
    :param words: 企业实体
    """
    def __init__(self, name, words):
        self.name = name
        self.words = words


def object_to_json(obj):
    """
    将picture_information类转换为json格式
    :param obj: picture_information类
    :return: 类对应的json格式
    """
    return {
        "name": obj.name,
        "words": obj.words
    }


def process_my_picture(img_path):
    """
    传入图片路径，处理图片
    :param img_path: 图片路径
    :return: json格式的picture_information类
    """
    file_name = os.path.basename(img_path)
    # easydl文本分类
    # request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/comSoft"
    # access_token = '[24.08334736def5db6ead6a95810b2a0d44.2592000.1601203661.282335-22337043]'
    request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/sankin"
    access_token = '[24.835588235143e22b2d027ad6af9da889.2592000.1604488670.282335-22471352]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    words = get_content(img_path)
    # max_word = [words[0]]
    # max_score = 0.9
    max_word = [""]
    max_score = 0.0
    for item in words:
        params = "{\"text\":\"" + item + "\"}"
        response = requests.post(request_url, data=params.encode('utf-8'), headers=headers)
        if response:
            res = response.json()
            res.setdefault('result', None)
            # if res['result']:
            res_score = res['results']
            score1 = res_score[0]['score']  # the bigger one, 0 or 1
            score2 = res_score[1]['score']
            if res_score[0]['name'] == '0':
                score1 = score2
            if score1 > max_score:
                max_score = score1
                max_word = []
                max_word.append(item)
    ans = picture_information(file_name, max_word)
    return object_to_json(ans)


def process_file(file_path):
    """
    处理解压后的zip文件
    :param file_path: 解压后文件路径
    :return: picture_information类列表
    """
    ans = []
    for filename in os.listdir(file_path):
        picture = file_path + '/' + filename
        if os.path.isdir(picture):
            ans.extend(process_file(picture))
        else:
            kind = filetype.guess(picture)
            result = is_photo(kind.extension)
            if result == 1:
                picture = transfer_image(picture)
                information = process_my_picture(picture)
                ans.append(information)
    return ans


def get_pictures_name(file_path):
    """
    获取图片名字
    :param file_path:解压后文件路径
    :return: list
    """
    ans = []
    for filename in os.listdir(file_path):
        picture = file_path + '/' + filename
        if os.path.isdir(picture):
            ans.extend(process_file(picture))
        else:
            kind = filetype.guess(picture)
            result = is_photo(kind.extension)
            if result == 1:
                ans.append(filename)
    return ans


def take_index(item):
    """
    对识别出的企业实体按照图片名称进行排序
    :param item: 图片信息类
    :return: 去掉文件拓展名的图片名称
    """
    s = item['name'].split(".", 1)[0]
    return int(s)


@app.route('/api/picture', methods=["GET", "POST"])
def process_picture():
    """
    上传图片
    :return: 返回码，图片名称，图片识别结果，表格网址
    """
    # Flask中获取文件
    file_obj = request.files.get('picture')
    if file_obj is None:
        response = dict(code=666, msg='未上传图片')
        return jsonify(response)
    # 保存文件
    picture_name = file_obj.filename
    file_path = os.path.join('file', picture_name)
    file_obj.save(file_path)
    file_path = transfer_image(file_path)
    ans = process_my_picture(file_path)
    excel_url = jpg_excel(ans)
    response = dict(code=200, msg='上传成功', picture=picture_name, datas=ans, excelUrl=excel_url)
    return jsonify(response)


@app.route('/api/zip', methods=["GET", "POST"])
def process_package():
    """
    上传压缩包
    :return: 返回码，压缩包名称，识别结果list，图片名称list，表格网址
    """
    # Flask中获取文件
    file_obj = request.files.get('file')
    if file_obj is None:
        response = dict(code=666, msg='未上传文件')
        return jsonify(response)
    # 保存文件
    now_time = time.gmtime()
    note = int(time.mktime(now_time))
    zip_path = str(note) + ".zip"
    file_path = os.path.join("file", zip_path)
    zip_name = file_obj.filename
    file_obj.save(file_path)
    file_path = un_zip(file_path, zip_name)
    ans = process_file(file_path)
    ans.sort(key=take_index)
    excel_path = zip_excel(ans)
    picture_name = get_pictures_name(file_path)
    response = dict(code=200, msg='处理成功', zip=zip_name, datas=ans, pictures=picture_name, excelUrl=excel_path)
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
