#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:19:13 2022

@author: sree
"""

import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':20,})
print(r.json())