#!/usr/bin/env python3
# -*-coding: utf-8 -*-

_author_='Seanlqx'

#编写Web App骨架

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

#制作响应函数
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')
	
@asyncio.coroutine
def init(loop):#Web app服务器初始化
    app = web.Application(loop=loop) #制作响应函数集合
	app.router.add_route('GET', '/', index)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv
	
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()