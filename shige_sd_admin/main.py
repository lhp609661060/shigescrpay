# coding=utf-8

import json

from flask import Flask
from flask import render_template, jsonify
app = Flask(__name__)

@app.route('/')
def admin():
    return render_template('admin.html')


@app.route('/search')
def search():
    return jsonify({'status':0})


@app.route('/start-spider')
def start_spider():
    return jsonify({'status':0})


@app.route('/stop-spider')
def stop_spider():
    return jsonify({'status':0})


@app.route('/restart-spider')
def restart_spider():
    return jsonify({'status':0})


@app.route('/start-spider')
def start_spider():
    return jsonify({'status':0})


@app.route('/delete-project')
def delete_project():
    return jsonify({'status':0})


@app.route('/create-project')
def craete_project():
    return jsonify({'status':0})


if __name__ == '__main__':
    app.run(port=8009)