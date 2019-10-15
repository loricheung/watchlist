#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: loricheung
from flask import render_template
from watchlist import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', ), 404
