import base64
import json
import random
import urllib
import uuid

try:
    import unzip_requirements
except ImportError:
    pass

import numpy
from PIL import Image, ImageDraw, ImageFont

import logging

logging.basicConfig(
    format='%(asctime)s - %(threadName)s - %(module)s:%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info('Loading function')


def handle(event, context):
    logger.info("event:{event}".format(event=event))
    logger.info("context:{context}".format(context=context))

    body = event['queryStringParameters']
    s = body['s']

    if len(s) > 20:
        logger.error('Parameter error. Parameter s length is too long.')
        return response(400, {'message': "Parameter error. Parameter s length is too long."})

    display_str = urllib.parse.unquote(body['s'])
    logger.info(f"display_str:{display_str}")

    color_hash = get_color_hash()

    # サイズが150の正方形を生成する
    im = Image.new('RGB', (150, 150), color_hash['bg'])

    # テキストを中心に出力します
    draw_text_at_center(im, display_str, color_hash['font'])

    save_file_path = f"/tmp/{uuid.uuid4()}.png"
    im.save(save_file_path)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/png",
        },
        "body": base64.b64encode(open(save_file_path, 'rb').read()).decode('utf-8'),
        "isBase64Encoded": True}


def response(status_code, message):
    return {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "body": json.dumps(message)
    }


# テキストを画像の中心に描画します
def draw_text_at_center(img, text, font_color):
    draw = ImageDraw.Draw(img)
    draw.font = ImageFont.truetype('GenJyuuGothicX-P-Bold.ttf', 48)
    img_size = numpy.array(img.size)
    txt_size = numpy.array(draw.font.getsize(text))
    pos = (img_size - txt_size) / 2

    draw.text(pos, text, font_color)


def get_color_hash():
    color_list = [
        {'font': (255, 255, 255), 'bg': (248, 4, 6)},
        {'font': (255, 255, 255), 'bg': (204, 0, 10)},
        {'font': (255, 255, 255), 'bg': (229, 72, 0)},  # 緋色
        {'font': (255, 255, 255), 'bg': (39, 38, 114)},  # 藍色
        {'font': (255, 255, 255), 'bg': (57, 3, 124)},  # 紺藍
        {'font': (255, 255, 255), 'bg': (11, 43, 21)},  # セルリアンブルー
        {'font': (255, 255, 255), 'bg': (251, 231, 9)},  # 卵色
        {'font': (255, 255, 255), 'bg': (228, 176, 55)},  # ブロンド
        {'font': (255, 255, 255), 'bg': (228, 162, 11)},  # 山吹色
        {'font': (255, 255, 255), 'bg': (51, 96, 69)},  # 深緑
    ]

    r = random.randrange(10)
    return color_list[r]


if __name__ == '__main__':
    subscriber_id = uuid.uuid4()
    user_id = uuid.uuid4()

    # ObjectKeyは /{subscriber_id}/user_images/{user_id}.png に保存する
    event = {'resource': '/create', 'path': '/create', 'httpMethod': 'GET', 'headers': None,
             'queryStringParameters': {'s': 'BS'}, 'pathParameters': None, 'stageVariables': None,
             'requestContext': {'path': '/create', 'resourceId': 'mmgrks',
                                'stage': 'test-invoke-stage', 'requestId': 'ae0367fe-5904-11e8-a178-259f37ad7e5e',
                                'resourcePath': '/create', 'httpMethod': 'GET'},
             'body': None, 'isBase64Encoded': False}

    handle(event, None)
