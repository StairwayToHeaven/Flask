#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from hello_world import app
app.run(host="0.0.0.0", port=5004, debug=True)
