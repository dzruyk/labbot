#!/usr/bin/python3
import willie

@willie.module.commands('helloworld')
def helloworld(bot, trigger):
    bot.say('Hello, world!')
