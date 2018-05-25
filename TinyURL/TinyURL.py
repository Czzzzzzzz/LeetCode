#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:32:10 2018

@author: zhengcao
"""

import random
import string

class Codec:
    
    urlMap = {}
    
    def randomValue(self, num):
        valueList = "123456789abcdefghijklmnopqrstuvwxyz"
#        valueList = string.ascii_letters + '0123456789'
        
        randomList = ''
        for i in range(num):
            index = random.randint(0, len(valueList)-1)            
            randomList += valueList[index]
            
#            randomList = ''.join(random.choice(valueList) for _ in range(6))
        
        return randomList
    
    def encode(self, longUrl):
        shortUrl = "http://"
        
        splittedUrl = longUrl.split('-')
        midUrl = splittedUrl[len(splittedUrl)-1]
        shortUrl += midUrl + '/'
        
        while True:
            tempUrl = shortUrl + self.randomValue(6)
            if tempUrl not in self.urlMap:
                self.urlMap[tempUrl] = longUrl
                shortUrl = tempUrl
                break
            
        
        return shortUrl
        
    def decode(self, shortUrl):

        longUrl = ''
        if shortUrl in self.urlMap:
            longUrl = self.urlMap[shortUrl]
        
        return longUrl
    
        
if __name__ == "__main__":
    
    url = "https://leetcode.com/problems/design-tinyurl";
#    target url = "http://tinyurl.com/4e9iAk"
    
    codec = Codec()
    codec.decode(codec.encode(url))
    
    shortUrl = codec.encode(url)
    print(shortUrl)
    
    longUrl = codec.decode(shortUrl)
    print(longUrl)
    
#    alphabet = string.ascii_letters + '0123456789'
#    print(alphabet[1:2])