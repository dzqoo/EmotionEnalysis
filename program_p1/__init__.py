#! /usr/bin/env python
# encoding=utf-8
"""
@version:??
@author:都真全
@time:2016/10/24 21:58
"""
import numpy as np
import scipy as sy

import pandas as pd

import sklearn as sk
import re
import jieba
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
from snownlp import SnowNLP
from datetime import datetime
