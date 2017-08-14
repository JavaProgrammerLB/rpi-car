# -*- coding: utf-8 -*
from flask import Flask, render_template, request, abort
from car import Car
import config as c
import celeryconfig
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

app = Flask(__name__)

# 1-forward 2-backward 3-left 4-right
car = Car(1, True)

handle_map = {
    'forward': car.forward,
    'left': car.left,
    'right': car.right,
    'pause': car.stop,
    'backward': car.backward,
    'dir': car.dir,
    'trueFlag' : car.trueFlag,
    'falseFlag' : car.falseFlag,
    'bizhang' : car.bizhang,
}

@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")


@app.route('/handle', methods=['GET'])
def handle():
    try:
        # 获取GET参数
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)  # 返回 404
    else:
        if operation in handle_map.iterkeys():
            handle_map[operation]()
        else:
            abort(404)
    return 'ok'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=c.WEB_PORT, debug=False)
