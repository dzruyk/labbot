# coding=utf8
"""
get random joke from some site
"""

import urllib2
from xml.dom import minidom

import willie.module
import willie.tools
from willie.config import ConfigurationError


@willie.module.commands('joke')
def send_joke(bot, trigger):
    """
    """
    url='http://shortiki.com/export/api.php?format=xml&type=random&amount=1'

    try:
        r = urllib2.urlopen(url)
    except:
        pass
    buf = r.read()
    dom = minidom.parseString(buf)
    elems = dom.getElementsByTagName('description')
    joke = elems[1].firstChild.nodeValue
    bot.msg(trigger.nick, joke)

