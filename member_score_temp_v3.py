# coding: utf-8

# -*-coding:utf8-*-
# this version was added the function of read ads_words_library.txt
import pandas as pd
from string import punctuation
import re

def get_user_score(user_name, user_region, user_city, user_sig):

    # delete punctuations 
    def remove_punctuation(s):
        # delete all spaces in text 
        s = s.replace(" ","")
        one_without_pun=''.join([c for c in s if c not in punctuation])
        punc = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+"
        string_n_pun = re.sub(punc,"",one_without_pun)
        return string_n_pun
    
    # check if the feature includes words in our words_library
    
    def ads_search(obj_content):
        file_obj = open('words_library.txt','r')
        words_library = file_obj.read()
        ads_library = re.compile(words_library,re.I)
        result = ads_library.findall(obj_content)
        return result
    
    # check if the feature includes phone numbers
    def phone_search(feature_s):
        phone_re = re.compile('(\d{3}\D{0,1}\d{3}\D{0,1}\d{4})')
        phone_label = phone_re.findall(feature_s)
        return phone_label
    
    # remove punctuation for nickname and signature
    nickname_n_pun = remove_punctuation(user_name)
    signature_n_pun =remove_punctuation(user_sig)

    # check whether the feature of signature and nickname include phone number and extract the number
    user_sig_phone = phone_search(signature_n_pun)
    user_nickname_phone = phone_search(nickname_n_pun)
    
    # check if the feature of nickname and signature have words in our words_libary
    ads_label_name = ads_search(nickname_n_pun)
    ads_label_signature = ads_search(signature_n_pun)
   
    # make decision on which level should be assigned to a user: 0, 1, 2
    if (user_sig_phone or user_nickname_phone or ads_label_name or ads_label_signature):
        user_score = 0

    elif nickname_n_pun and user_region and user_city and user_sig:
        user_score = 2

    else:
        user_score =1 
        pass
    
    return user_score
    


