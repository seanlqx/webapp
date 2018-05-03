--conding: utf-8 --

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request)
    return web.Response(body=b'<h1>Awesome</h1>')
	