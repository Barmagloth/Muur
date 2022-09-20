#!/usr/bin/env python
# coding: utf-8

# In[1]:


import telebot;
import random;
import requests
import json
import re
import glob
import os
import getjsons as gj
import time
import sys
#import urllib
from requests.exceptions import ConnectionError, ReadTimeout
from deep_translator import GoogleTranslator
from deep_translator import DeeplTranslator

# In[2]:


import sys
import clipboard
from time import sleep


# In[3]:


rate_up = ['+','+++','++++','++','+++++','++++++','+++++++','++++++++','+++++++++','++++++++++','+++++++++++','++++++++++++','+++++++++++++','Спасибо','Круть','спасибо','круть','круто','Круто']
rate_dn = ['-','---']
ratings = []
cookiehow = ['','','','','','','','застенчиво ','торжественно ','радостно ','тихонечко ','со всей душою ',', жмурясь от удовольствия, ']
cookiegive = ['дарит','подсовывает','вручает','выдаёт','даёт','преподносит','вручает в дар','отдаёт в собственность','оставляет на ответхранение','протягивает','приносит']
thecookie = ['печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','печеньку','печенюшку','печенюшечку','ОКРОВАВЛЕННУЮ ПЕЧЕНЬ','тортичек','вкусняшку','крекер-рыбку','вафельную трубочку','ТВОРОГ']

#### IsReply: 
#- 1 - отвечать только на реплай 
#- 2 - отвечать и просто на сообщение, и на реплай

#### CaseDep

#- 1 - регистрозависимо, во всех остальных случаях - нет

#### IsReg: 
#- 1 - если сообщение содержит искомый текст
#- <b>2 - если сообщение начинается с искомого текста</b>
#- <b>3 - если сообщение заканчивается на искомый текст</b>
#- <b>4 - регэксп  - СТОИТ ПЕРЕНЕСТИ В ОБЪЕКТ Questions</b>

#### Type: 
#- 1 - Or (рандомный выбор)
#- <b>2 - And</b>

#### Next:
#-   текст для следующего триггера, обрабатываемого отдельным файлом json

#### Answers:    
#- answ_poss: 0-100 - вероятность ответа на сообщение (никак не связано с вероятностью выбора варианта ответа, там тупой рандом) 
#- answ_text: текст ответа
#- isit_pic: 1 - картинка, 2 - gif или видео
#- answ_pic_aft_text: картинка после текста ответа
#- <b>answ_pic_bef_text: картинка до текста ответа</b>

#### Формат файла рейтингов:
# Ratings, в нём объекты, для каждого из которых:
#- id - идетнтификатор пользователя, 
#- rating - рейтинг
# In[4]:


# In[5]:

# Giphy
#chosen_tag = "kitten"

def fetch_gif_url(message):
    #translator= Translator(to_lang="English")
    msg_low = message.text.lower()
    chosen_tag='kitten'
    gif_triggers = ['!гифка', '!гиф', '!gif', '!gifka', 'gifka', 'gif', 'гифка', 'гиф']
    msg_list = msg_low.split()
    if msg_list[0] in gif_triggers:
        gif_tag = msg_low[len(msg_list[0])+1:]
        print (gif_tag)
        if len(gif_tag) >= 1:
            chosen_tag = GoogleTranslator(source='auto', target='en').translate(gif_tag)
        random_url = "https://api.giphy.com/v1/gifs/random"
        giphy_api_key_value = "DaOXY9EgVWBvuwOxLr1luX1iSUEhY06Z"
        print (chosen_tag)
        parametre = {'api_key': giphy_api_key_value,'tag': chosen_tag}

        response = requests.get(
                url=random_url,
                params=parametre,
        )

        data = response.json()
        picture = data["data"]["images"]["downsized_large"]["url"]
        #print(picture)
        bot.send_video(message.chat.id, picture)


def IfStartsWithPlus(message):
    if message.text[0] == '+':
        return True
    else:
        return False


# In[6]:


bot = telebot.TeleBot('ТОКЕН ДОЛЖЕН БЫТЬ ВОТ ТУТ') # <------- ЗДЕСЬ ВСТАВИТЬ ТОКЕН ДЛЯ БОТА


# In[7]:


def LoadJson(path):
    read_file = open(path,'r')
    return (json.load(read_file))


# In[8]:


def GotCookie(rt):
    rt = str(rt)
    if len(rt) > 1:
        if rt[-2:] not in ['11','12','13','14']:
            if rt[-1:] in ['2','3','4']:
                cooki = 'печеньки'
            elif rt[-1:] in ['1']:
                cooki = 'печенька'
            else:
                cooki = 'печенек'
        else:
            cooki = 'печенек'
    elif rt == '1':
        cooki = 'печенька'
    elif rt in ['2','3','4']:
        cooki = 'печеньки'
    else:
        cooki = 'печенек'
    return cooki


# In[9]:


def LostCookie(rt):
    rt = str(rt)
    if len(rt) > 1:
        if rt[-2:] not in ['11','12','13','14']:
            if rt[-1:] in ['2','3','4']:
                cooki = 'печеньки'
            elif rt[-1:] in ['1']:
                cooki = 'печеньку'
            else:
                cooki = 'печенек'
        else:
            cooki = 'печенек'
    elif rt == '1':
        cooki = 'печеньку'
    elif rt in ['2','3','4']:
        cooki = 'печеньки'
    else:
        cooki = 'печенек'
    return cooki


# In[10]:


def SayMe(message):
    IsReply = False
    text = message.text
    name = message.from_user.first_name
    text = text.replace('/me',name)
    if message.reply_to_message != None:
        repl_id = message.reply_to_message
        reply_to_name = message.reply_to_message.from_user.first_name
        text = text.replace('{reply_to_name}',reply_to_name)
        IsReply = True
    bot.delete_message(message.chat.id, message.message_id)
    if IsReply:
        bot.reply_to(repl_id, text)                                             ################## КАК ОТПРАВЛЯТЬ ОТВЕТ !!!!
    else:
        bot.send_message(message.chat.id, text)

def CatFuck(message):
    cat_fuck = ['кота ебал','ебал кота','кота твоего ебал','твоего кота ебал','твоего ебал кота','ебал твоего кота','кота ебал твоего','ебать кота','кота ебать','твоего кота ебать','твоего ебать кота','кота твоего ебать','ебать твоего кота','кот ебаный мной','ебал котов','котов ебал']
    text = message.text
    text = text.lower()
    eng2rus = {ord('a'):'а',
               ord('e'):'е',
               ord('o'):'о',
                       ord('k'):'к',
                       ord('t'):'т',
                       ord('0'):'о',
                       ord('6'):'б',
               ord('y'):'у'
              }
    text = text.translate(eng2rus)
    #bot.send_message(message.chat.id, text)
    pattern = re.compile("(([кkKК][oOОо0][тТtT][AaаА].*[eEЕе][б6Б][AaаА](([лЛ])|([TtТт][Ььb6])))|.*([eEЕе][б6Б][AaаА](([лЛ])|([TtТт][Ььb6])).*[кkKК][oOОо0][тТtT][AaаА]))")
    pattern.match(text)
    #for each in cat_fuck:
    if pattern.match(text):
        bot.delete_message(message.chat.id, message.message_id)
# In[11]:


def get_answer(data,message):
    name = message.from_user.first_name
    answers = data['Answers']
    if data['Type'] == 1 or data['Type'] == "1":  # OR
        #for each in answers:
        each = random.choice(answers) # допилить здесь вероятность выпадения каждого конкретного случая
        #random.seed()
        output = each['answ_text'].replace('{name}',name)
        #print (f'{output}')
        if random.randint(1,100) <= int(each['answ_poss']):
            if 'isit_pic' in each: # если присутствует ключ обозначающий картинку
                if (each['isit_pic'] == 1) or (int(each['isit_pic']) == 1):
                    bot.send_photo(message.chat.id, output)## отправить фото
                if (each['isit_pic'] == 2) or (int(each['isit_pic']) == 2):
                    bot.send_video(message.chat.id, output)## отправить гифку
            else: #elif each['isit_pic'] == 0:
                bot.send_message(message.chat.id, output)  ## отправить текст
            if 'answ_pic_aft_text' in each:
                bot.send_photo(message.chat.id, each['answ_pic_aft_text'])
    elif data['Type'] == 2: #AND
        #for each in answers:
        pass


# In[12]:


def get_some_reply(data,message,name,reply_to_name):
    answers = data['Answers']
    if data['Type'] == 1 or data['Type'] == "1":  # OR
        each = random.choice(answers) # допилить здесь вероятность выпадения каждого конкретного случая
        #random.seed()
        #bot.send_message(message.chat.id, 'это ветка реплаев')  ## debug info
        output = each['answ_text'].replace('{name}',name)
        output = output.replace('{reply_to_name}',reply_to_name)
        #print (f"{name}   {reply_to_name}")vj;
        if random.randint(1,100) <= int(each['answ_poss']):
            if 'isit_pic' in each: # если присутствует ключ обозначающий картинку
                if (each['isit_pic'] == 1) or (int(each['isit_pic']) == 1):
                    bot.send_photo(message.chat.id, output)## отправить фото
                if (each['isit_pic'] == 2) or (int(each['isit_pic']) == 2):
                    bot.send_video(message.chat.id, output)## отправить гифку
            else: #elif each['isit_pic'] == 0:
                bot.send_message(message.chat.id, output)  ## отправить текст
            if 'answ_pic_aft_text' in each:
                #print (' -=  GOT MATCH!!!! =-')
                bot.send_photo(message.chat.id, each['answ_pic_aft_text'])
                
    elif data['Type'] == 2: #AND
        #for each in answers:
        pass


# In[13]:


def RateUp(message, name, reply_to_name):
    Rating_data = LoadJson('TrigExport\Rating.json')
    Ratings = Rating_data['Ratings']
    id = message.reply_to_message.from_user.id
    done = False
    for each in Ratings:
        if each['id'] == id:
            incr = message.text.count('+')
            each['rating'] += incr
            result = each['rating']
            done = True
    if done == False:
            NewId = {'id':id, 'rating':1}
            Ratings.append(NewId)
            #print (Ratings)
            #RatePlus = int(Ratings['id'])
            #RatePlus += 1
            #Ratings['id'] = str(RatePlus)
            result = 1
    with open ('TrigExport\Rating.json','w') as file_write:
        json.dump(Rating_data, file_write)
    return result
#print(RateUp())


# In[14]:


def RateDn(message, name, reply_to_name):
    Rating_data = LoadJson('TrigExport\Rating.json')
    Ratings = Rating_data['Ratings']
    id = message.reply_to_message.from_user.id
    found = False
    for each in Ratings:
        if each['id'] == id:
            each['rating'] -= 1
            result = each['rating']
            found = True
    if found == False:
            NewId = {'id':id, 'rating':-1}
            Ratings.append(NewId)
            #print (Ratings)
            #RatePlus = int(Ratings['id'])
            #RatePlus += 1
            #Ratings['id'] = str(RatePlus)
            result = -1
    with open ('TrigExport\Rating.json','w') as file_write:
        json.dump(Rating_data, file_write)
    return result
#print(RateUp())


# In[15]:


def GetMyInfo(message):
    Rating_data = LoadJson('TrigExport\Rating.json')
    Ratings = Rating_data['Ratings']
    id = message.from_user.id
    for each in Ratings:
        if each['id'] == id:
            rt = each['rating']
            text = f'Ваш рейтинг - {rt} печенюшек!'
            bot.send_message(message.chat.id, text)


# In[16]:


def GetRateInfo(message):
    Rating_data = LoadJson('TrigExport\Rating.json')
    Ratings = Rating_data['Ratings']
    found = False
    if message.reply_to_message == None:
        id = message.from_user.id
        for each in Ratings:
            if each['id'] == id:
                rt = each['rating']
                if rt >= 0:
                    cooki = GotCookie(rt)
                    text = f'У вас - {rt} {cooki}!'
                else:
                    cooki = LostCookie(rt)
                    text = f'Вы задолжали {abs(rt)} {cooki}!'
                found = True
                bot.send_message(message.chat.id, text)
        if found == False:
            bot.send_message(message.chat.id, 'Вам ещё никто не дарил печенек Т__Т')
    else:
        id = message.reply_to_message.from_user.id
        name = message.reply_to_message.from_user.first_name
        for each in Ratings:
            if each['id'] == id:
                rt = each['rating']
                if rt >= 0:
                    cooki = GotCookie(rt)
                    text = f'У {name} - {rt} {cooki}!'
                else:
                    cooki = LostCookie(rt)
                    text = f'{name} задолжал {abs(rt)} {cooki}!'
                found = True
                bot.send_message(message.chat.id, text)

        if found == False:
            text = f'{name} ещё никто не дарил печенек Т__Т'
            bot.send_message(message.chat.id, text)


# In[17]:


def ExistChk(data,what): # проверка, существует ли значение, цифра или символ цифры. Если да, вернёт значение, если нет - False
    if what in data:
        try:
            data[what].isdigit()
            return int(data[what])
        except:
            return data[what]
    else:
        return False


# In[18]:


def Send_Answer (data, message):
    IsReply = ExistChk(data,'IsReply')
    CaseDep = ExistChk(data,'CaseDep')
    IsReg = ExistChk(data,'IsReg')
    Type = ExistChk(data,'Type')
    Next = ExistChk(data,'Next')
    Questions = data['Questions']
    Answers = data['Answers']
    if IsReply:
        if IsReply == 1:
            pass
            # Это только в реплай
        elif IsReply == 2:
            pass
            # Пофиг, реплай или нет
        else:
            pass
            # Не реплай


# In[ ]:





# In[19]:


@bot.message_handler(commands=['start'])
def start_bot(message):
    jsons_data = gj.GetJsons()
    #print(jsons_data)
    bot.send_message(message.chat.id, 'Ня! Я министра культуры! :3')
    
@bot.message_handler(commands=['rating'])
def get_text_messages(message):
    jsons_data = gj.GetJsons()
    #print(jsons_data)
    GetRateInfo(message)
   
@bot.message_handler(commands=['me'])
def get_text_messages(message):
    jsons_data = gj.GetJsons()
    #print(jsons_data)
    SayMe(message)    
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    fetch_gif_url(message)
    CatFuck(message)
    #path1 = 'TrigExport/question.txt'
    #ifcat = message.text[0:4].lower()
    #alptrue = message.text[3:5].lower().isalpha()
    #if ifcat == 'муур' and not alptrue:
        #print(message.text[4:])
    #    neurquest = '"Q:\"'+message.text[4:]+'\"\nA:\"'
    #    result = GetNN(neurquest)
    #    bot.reply_to(message, result)
    #with open(path1, 'w') as write_file:
    #    write_file.write(f'user1:"{message.text}"\nuser2:"')
    #    write_file.close()
    jsons_data = gj.GetJsons()
    #print(jsons_data)
    #bot.send_message(message.chat.id,message.from_user.id) # - мой ИД
    #mesg = message.text
    #IsRating(message)
    if message.reply_to_message == None: #если это не реплай'
        
        #data = LoadJson(path)
        #answers = data['Answers']
        for data in jsons_data:    
            IsReply = ExistChk(data,'IsReply')
            CaseDep = ExistChk(data,'CaseDep')
            IsReg = ExistChk(data,'IsReg')
            Type = ExistChk(data,'Type')
            Next = ExistChk(data,'Next')
            Questions = ExistChk(data,'Questions')
            Answers = ExistChk(data,'Answers')
            if Questions:
                if not CaseDep: # если не регистрозависимое
                    for each in Questions:
                        msg_lower = message.text.lower()
                        quest_lower = each['quest_text'].lower()
                        if msg_lower == quest_lower: # если вопрос строго совпадает с триггером, без учёта регистра
                            if not IsReply: # если это не должно быть ответом
                                get_answer(data,message)
                                #bot.send_message(message.chat.id, '1') #             111111111111111111111111111111
                                if Next: # если есть дальнейший триггер
                                    #message.text = data['Next']
                                    #bot.send_message(message.chat.id, data['Next'])
                                    #get_text_messages(message)
                                    message.text = Next
                                    #get_text_messages(message)
                            elif IsReply and IsReply == 2: # оставить, потом поменять на each после переноса тэга в Answers      если пофиг, ответ или нет
                                get_answer(data,message)
                                #bot.send_message(message.chat.id, '2') # 22222222222222222222222222222222222222
                                if Next: # если есть дальнейший триггер
                                    #message.text = data['Next']
                                    #bot.send_message(message.chat.id, data['Next'])
                                    #get_text_messages(message)
                                    message.text = Next
                                    #get_text_messages(message)
                            break # чтобы не перебирал все варианты в Questions (исправить потом, для строгой регистразависимости)
                        elif (each['quest_text'] in message.text) and IsReg: # если триггер содержится в вопросе, без учёта регистра
                            if IsReg == 1: #если сообщение содержит искомый текст
                                #print ('найдено СК в сообщении без учёта регистра')
                                get_answer(data,message)
                                #bot.send_message(message.chat.id, '3') # 333333333333333333333333333333333333333
                            if IsReg == 2: #если сообщение начинается с искомого текста
                                pass
                            if IsReg == 3: #если сообщение заканчивается на искомый текст
                                pass
                            break
                elif CaseDep and CaseDep == 1: # если регистрозависимо
                    for each in Questions:
                        if message.text == each['quest_text']:
                            if not IsReply:
                                get_answer(data,message)
                                #bot.send_message(message.chat.id, '4')  # 444444444444444444444444444
                                if Next:
                                    #message.text = data['Next']
                                    #bot.send_message(message.chat.id, data['Next'])
                                    #get_text_messages(message)
                                    message.text = Next
                                    #get_text_messages(message)
                            elif IsReply and IsReply == 2: # оставить, потом поменять на each после переноса тэга в Answers
                                get_answer(data,message)
                                #bot.send_message(message.chat.id, '5') # 5555555555555555555555555555
                                if Next:
                                    #message.text = data['Next']
                                    #bot.send_message(message.chat.id, data['Next'])
                                    #get_text_messages(message)
                                    message.text = Next
                                    #get_text_messages(message)
                        elif (each['quest_text'] in message.text) and IsReg: # если триггер содержится в вопросе, с учётом регистра
                            #print ('найдено СК в сообщении без учёта регистра')
                            if IsReg == 1: #если сообщение содержит искомый текст
                                get_answer(data,message)
                                #bot.send_message(message.chat.id, '6')  # 666666666666666666666666666666666666666
                            if IsReg == 2: #если сообщение начинается с искомого текста
                                pass
                            if IsReg == 3: #если сообщение заканчивается на искомый текст
                                pass
                            if IsReg == 4: #РегЭксп
                                pass
    else: #если это реплай
        name = message.from_user.first_name
        reply_to_name = message.reply_to_message.from_user.first_name
        for data in jsons_data:
            IsReply = ExistChk(data,'IsReply')
            CaseDep = ExistChk(data,'CaseDep')
            IsReg = ExistChk(data,'IsReg')
            Type = ExistChk(data,'Type')
            Next = ExistChk(data,'Next')
            Questions = ExistChk(data,'Questions')
            Answers = ExistChk(data,'Answers')
            if Questions:
                if not CaseDep:
                    for each in Questions:
                        msg_lower = message.text.lower()
                        quest_lower = each['quest_text'].lower()
                        if msg_lower == quest_lower:
                        #if message.text == each['quest_text']:
                            if IsReply and IsReply == 1 or 2:
                                get_some_reply(data,message,name,reply_to_name)
                                if Next:
                                    message.text = Next
                                    #get_text_messages(message)
                                    #bot.send_message(message.chat.id,data['Next'])
                            break
                        elif (each['quest_text'] in message.text) and IsReg:
                            #print ('найдено СК в ответе без учёта регистра')
                            if IsReg == 1 and IsReply: #если сообщение содержит искомый текст
                                get_answer(data,message)
                            if IsReg == 2 and IsReply: #если сообщение начинается с искомого текста
                                pass
                            if IsReg == 3 and IsReply: #если сообщение заканчивается на искомый текст
                                pass      
                            if IsReg == 4 and IsReply: #РегЭксп
                                pass
                            break
                elif CaseDep and CaseDep == 1:
                    for each in Questions:
                        if message.text == each['quest_text']:
                            if IsReply and IsReply == 1 or 2:
                                get_some_reply(data,message,name,reply_to_name)
                                if Next:
                                    message.text = data['Next']
                                    #get_text_messages(message)
                                    #bot.send_message(message.chat.id,data['Next'])
                            break
                        elif (each['quest_text'] in message.text) and IsReg:
                            #print ('найдено СК в ответе регистрозависимых')
                            if IsReg == 1 and IsReply: #если сообщение содержит искомый текст
                                get_answer(data,message)
                            if IsReg == 2 and IsReply: #если сообщение начинается с искомого текста
                                pass
                            if IsReg == 3 and IsReply: #если сообщение заканчивается на искомый текст
                                pass      
                            if IsReg == 4 and IsReply: #РегЭксп
                                pass
                            break
        if message.text in rate_up or IfStartsWithPlus(message): #если рейтинг
            #text = "рейтинг пока не работает, но знайте, что " + name + " всегда готов поделиться печенькой с " + reply_to_name
            Ratingg = RateUp(message, name, reply_to_name)
            cookie_how = random.choice(cookiehow)
            cookie_give = random.choice(cookiegive)
            the_cookie = random.choice(thecookie)
            text = f'{name} {cookie_how}{cookie_give} {reply_to_name} {the_cookie}!'
            bot.send_message(message.chat.id,text)
        if message.text in rate_dn: #если рейтинг
            #text = "рейтинг пока не работает, но знайте, что " + name + " всегда готов поделиться печенькой с " + reply_to_name
            Ratingg = RateDn(message, name, reply_to_name)
            the_cookie = random.choice(thecookie)
            text = f'{name} отбирает у {reply_to_name} {the_cookie}!'
            bot.send_message(message.chat.id,text)
        


# In[ ]:


try:
    bot.polling(none_stop=True, interval=0)
except:
    sys.stdout.flush()
    os.execv(sys.executable, [sys.executable] + sys.argv)
else:
    bot.polling(none_stop=True, interval=0)

