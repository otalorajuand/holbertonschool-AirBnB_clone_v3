#!/usr/bin/python3
"""Module for Blueprint app_views"""
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')