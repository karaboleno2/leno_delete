#Karabo Khomongoe
#Khomongoeki@gmail.com
#July-27-2022
# python3 -c "import gspread; print(gspread.__version__)"

import re
import os
from django import http
from django.shortcuts import render
from more_itertools import first
from twilio.rest import Client 
from django.views.decorators.csrf import csrf_exempt
import gspread  #5.4.0
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
import time
#ml
import os

import requests
from PIL import Image
import smtplib, ssl
import random
#Dictionary
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from spellchecker import SpellChecker

#0lOba0?2[6#yMW8?
businessphone= '+14155238886'
JSONFILE= os.path.join('assets/')

account_sid = 'AC9cfdfeaa5bce698906cff658aaf42499' 
auth_token = '7e5c5878fb3ec4de2862094dda5d788e' 
client = Client(account_sid, auth_token)

colon= {'learnerPhoneNo	':'C1','learnerName	':'C2','learnerEmail':'C3','learnerAge':'C4','learnerGrade':'C5','parentsEmail':'C6','parentName':'C7','ParentNo':'C8','whatsappPaging':'C9','classes':'C10','story':'C11','pronouns':'C12','handwriting':'C13', 'step':'C14'}
number= []

dictionary = SpellChecker()

#Quetions
images={'parentmenu':'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MMd9e423cdc26f9ef5148dfd062f478d0e/Media/MEce60bff49e9725772a4c9c16988d5ecd',
        0:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM0d5fd57eb8379f2b3df638c60979ad0a/Media/MEf4ac968725c4e228a7d0ddc910ce6e68',
        1:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MMe70d2eb8e5fdb58f7edf28d6fda8e84f/Media/ME60f3ff7e05c8dc2e01f07915d7d8abeb',
        2:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM0b82919f6ee0af8d4fc69eece745f818/Media/ME9dd5b145307683a8626e9f3be6c22533',
        3:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM4935238a106c9d4f868def417145c560/Media/ME57aeb39e99759eef9a57125ed357bb4e',
        4:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM76cc26cdb73432c595d5a244f51f68ff/Media/ME459fa963f9fbb52c12ad9e418b6acfe6',
        5:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM88f7cf0a046bf15518852ef4a7906f29/Media/ME8948a5b320fb1fd9e93e0973f1b1fcd6',
        6:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM8ad2221296f9007c0d21d44400e0c877/Media/MEc10a248e142ff8d4cc74285fdd4ef49e',
        7:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MMe981e6f7e7e898e81bf984dcef668967/Media/ME462bf203aa5a673d4f27c9d0f58fbc64',
        8:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM37ee471a5838f39f229b068c5d896538/Media/ME38b9dd34c0f6c609902adf71090dab83',
        9:'https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM7bf2167876257428d5b800988c17b714/Media/MEed38349de7e2191afbd71875345dc086',
    }

#####################################################################
##################           Funtions        ########################
#####################################################################
# This fuction sends menu
def sendMenuParentPIC(userPhone):
    message = client.messages.create( 
        from_=f'whatsapp:{businessphone}',  
        to=userPhone,
        media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MMac75d08d2336b4767d2f7ae631febb0b/Media/MEeb399727dd60c211f0c55581c206ddc7",
        )

def sendMenuParent(userPhone):
    message = client.messages.create( 
        from_=f'whatsapp:{businessphone}',  
        body="*SELECT A SERVICE👇* \n"+
        "*M. Monitoring progrees 📊*\n"+
        "Child's progress will be sent monthly or on-request.\n"+
        "*📌Note*: your child must be registered\n\n"+
        "*B. Bridged convestion🫱🏽‍🫲🏾*\n"+
        "Let me send messages to your child on your behalf.\n "+
        "*📌Note*: your child must be registered\n\n "+
        "*I. LENOKIDS for kids infoℹ️*\n"+
        "Lenokids packages📦 and pricing🔖.\n\n"+
        "*R. Register you child📝*\n3️⃣ Easy steps \n\n"+
        "*C. Customer service📞*\n"+
        "Customer queries, complaints and support\n\n"+
        "*Feedback⭐*\n"+
        "📌Use this link to give feedback: www.googleform.com",   
        to=userPhone,
        media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM19081ef8e7f1834164245750b0c3a81c/Media/MEd88c575f39f5b44e14a62a30db192d18",
        )

def sendMenuPIC(userPhone):
    message = client.messages.create( 
        from_=f'whatsapp:{businessphone}',     
        media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM3a60e69fb7d247ea15cbc58aa366ac41/Media/ME4b74bcdb2610766c608b894d888e3196",
        to=userPhone)

def sendMenu(userPhone):
    message = client.messages.create( 
        from_=f'whatsapp:{businessphone}',  
        body= " \n\nHow can I help you today🤗? \nPlease choose from the options below: \n\n"+
        "*1. Classes 🎒 and Games🎮*. \nLet us learn new things and play games together\n\n"+
        "*2. Story Telling*📖\n Do you love stories❓ \n\n"+
        "*3. Handwritting*✍\n Let me teach you how to write numbers and letters\n\n"+
        "*4. Define and pronounce*🗣 \n I can define and pronounce words for you \n\n"+
        "*5. User Manual*📜",      
        media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM19081ef8e7f1834164245750b0c3a81c/Media/MEd88c575f39f5b44e14a62a30db192d18",
        to=userPhone)



def getWordSuggestions(word):
    candidates = dictionary.candidates(word)
    candidates = [w for w in candidates if wordnet.synsets(w)]
    return candidates


def getRecords(word):
    resp = ""
    syn = wordnet.synsets(word)
    if not syn:
        return None

    dform = {
        "n": "noun",
        "v": "verb",
        "a": "adjective",
        "r": "adverb",
        "s": "adjective satellite",
    }
    ctr1 = 1
    ctr2 = 97
    antonyms = list()
    for i in syn[:4]:
        ctr2 = 97
        definition, examples, form = i.definition(), i.examples(), i.pos()
        resp = resp +"➡️ *"+ word + "*-" + dform[form] + "\n"
        resp = resp + "*Definition* : " + definition.capitalize() + "." + "\n\n"
        ctr1 += 1
        if len(examples) > 0:
            resp = resp + "*Usage :* " + "\n"
            for j in examples:
                resp = resp + chr(ctr2) + ". " + j.capitalize() + "." + "\n"
                ctr2 += 1
            resp+="\n"
        for j in i.lemmas():
            try:
                antonyms.append(j.antonyms()[0].name())
            except IndexError:
                pass
    if len(antonyms) > 0:
        resp = resp + "Antonyms : " + "\n"
        for i in antonyms:
            resp = resp + i + "\n"
    return resp

def sendChildmenu(response):
    pass

##################################################################
####################          END         ########################
##################################################################


##################################################################
####################         API          ########################
##################################################################

# Create your views here.
@csrf_exempt
def bot(request):
    userPhone=request.POST['From']
    userName=request.POST['ProfileName']
    creds = gspread.service_account(JSONFILE+'lenokids-10bfba07874f.json')
    try:
        sheet = creds.open("LenoKids Register")
    except Exception as e:
        print(e)
        message = client.messages.create( 
            from_=f'whatsapp:{businessphone}',  
            body="{} , 🙏Please resend, I was unable to connect to server",      
            to=userPhone)
        return http.HttpResponse("200")
    # getting data
    wks = sheet.worksheet('Sheet1')
    register=str(wks.find(userPhone))
    #parent app
    if ('None' == register):
        insertRow = ['','','','','','',userName,userPhone,'', '','','','','','pmenu','',1]
        wks.append_row(insertRow)
        sendMenuParent(userPhone)
        return http.HttpResponse("200")
    
    elif ('c8' in register.lower()):
        row=register.split()[1][1:2]
        stepP=wks.cell(row,15).value

        ## parent return answer
        if (stepP=='udate' and 'ud' == request.POST['Body'].lower()):
            message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body=request.POST['Body'].replace("command",""),      
                        to=wks.cell(row,1).value)
            time.sleep(2)
            message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body="Your message has been sent\n\n 0. To show menu🏠",      
                        to=userPhone)
            return http.HttpResponse("200")
        
        ## parents menu
        if stepP ==  'pmenu':
                # monitor child
                if ('m' == request.POST['Body'].lower() or 'monitor' in request.POST['Body'].lower()):
                    message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body="Okay you will get progress reports via email📧 soon\n\n 0. To show menu🏠 ",
                        to=userPhone)
                    return http.HttpResponse("200")
                # Bridged Convestion
                elif ('b' == str(request.POST['Body']).lower()):
                    message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body="*Bridged Convestion🤝*\n\n📨 To send a message to your child. \n*Use this format:* _command: 'Your message'_. \n\n👉🎯 Click on the image above to see an example\n\n 0. To show menu🏠 ",
                        media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM14612e75d76a343d54da6bbfaf383032/Media/ME60f258fc4c090240c54b51cf9351b8ea" ,    
                        to=userPhone)
                    return http.HttpResponse("200")
                # lenokinds info
                elif ('i' == str(request.POST['Body']).lower()):
                    message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body=" LENOKIDS for kids infoℹ️*\n\n"+
                             "Please 🙏 visit our website for Lenokids packages📦 and pricing🔖. \n*Website link:* www.lenokids.co.za.\f\F\\n\n 0. To show menu🏠 ",
                        to=userPhone)
                    return http.HttpResponse("200")
                
                # Customer Service
                elif ('c' == str(request.POST['Body']).lower()):
                    message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body="*Customer Service👨‍💻*\n\n*Business Hours⏰*\nMon-Fri 8:30am - 4:30pm\nSat 9:00am - 3:00pm\n\n*Contact Us*\n *☎️Call:* +27 71 157 3218 \n*📧Email:* helpdesk@lenokids.co.za \n\n 0. To show menu🏠",
                        to=userPhone)
                    return http.HttpResponse("200")
                
                # sends bridged message
                elif ('command' in str(request.POST['Body']).lower()):
                    print(wks.cell(row,1).value)
                    message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body=request.POST['Body'].replace("command",""),      
                        to=wks.cell(row,1).value)
                    time.sleep(2)
                    # child should reply to this message??
                    
                    message = client.messages.create(
                        from_=f'whatsapp:{businessphone}',  
                        body="Your message has been sent\n\n 0. To show menu🏠",      
                        to=userPhone)
                    return http.HttpResponse("200")
                
                # registation 1st step
                if ('r' == request.POST['Body'].lower()):
                    message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*Registration*\n\n*I will need 📌*"+
                    "\n\n 1️⃣ Email: you'll recieve updates and child's progress \n 2️⃣ Childs phone number \n 3️⃣ Child Grade\n\nPlease proceed below",  
                    to=userPhone)
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body="Send your Email📧:".format(userName),      
                        to=userPhone)
                    wks.update('R'+row+'C15', 'register')
                
                # menu
                elif ('0' == str(request.POST['Body']).lower() or 'menu' in str(request.POST['Body']).lower()):
                    print(wks.cell(row,1).value)
                    sendMenuParent(userPhone)
                else:
                    sendMenuParent(userPhone)
                return http.HttpResponse("200")
            
            # registation 2nd and 3rd steps
        if stepP == 'register':
                if ('@' in request.POST['Body'].lower()):
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body="Note: Confirmation will be sent, CH {email@domain.com} to update email📧\n\n*Child phone number📞*. Use this Fomart: +2774674747",      
                        to=userPhone)
                    port = 465  # For SSL
                    password = "ondirlobvdyqvpba"

                    # Create a secure SSL context
                    context = ssl.create_default_context()

                    with smtplib.SMTP_SSL("smtp.gmail.com", port , context=context) as server:
                        server.login("0731642387k@gmail.com", password)   #"3724029@myuwc.ac.za",
                        # TODO: Send email here
                        message = 'Subject: {}\n\n{}'.format("Confirmation", "Lenokids no-reply")
                        server.sendmail(request.POST['Body'].lower(),request.POST['Body'].lower(), message)

                    wks.update('R'+row+'C6', request.POST['Body'])
                elif ('+' in request.POST['Body'].lower()):
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body="*Grade* \n\n0. Grade 0\n\n1. Grade 1\n\n2. Grade 2\n\n3. Grade 3\n\n4. Grade 4".format(userName),      
                        to=userPhone)
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body="Hey I am Leno🤖😊, how are you❓",      
                        to=f'whatsapp:'+request.POST['Body'])
                    wks.update('R'+row+'C1', 'whatsapp:'+request.POST['Body'])
                    wks.update('R'+row+'C14', 'menu1')
                elif ('1' or '2' or '3'or '4' or '0' in request.POST['Body'].lower()):
                    wks.update('R'+row+'C5', request.POST['Body'])
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body="Thank you I got all the information I need".format(userName),      
                        to=userPhone)
                    time.sleep(3)
                    
                    sendMenuParent(userPhone)
                    wks.update('R'+row+'C15', 'pmenu')
                else:
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body="*menu🏠",      
                        to=userPhone)
                return http.HttpResponse("200")
        else:
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="Hey I don't get that ", 
                    to=userPhone)
        return http.HttpResponse("200")

    ##########################################################################################
    #########                               Kids                                    ##########
    ##########################################################################################

    row=register.split()[1][1:2]  # 
    step=wks.cell(row,14).value   # getting childs step. toresume where we stopped. e.i handwritting

    if (step=='menu1'):   # menu1 is only ran once
        message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="Okay {} I'm happy🤗 to hear that, and nice to know you. \nWe are going to learn about the world🌍 and also to play games🎮  \n\n ".format(userName),  
                    #media_url="https://public.bl.files.1drv.com/y4me9WLjd6iyN6mRyk6OMabbcxmC4XbWzkQMo2nL8CeIaL3kk72WzIuNvwbTTCoddsPwfRn1YYNAtp5MPJr68DZEWEv0-by41KvgI72eZhyX4STJ1pPk7kOYg2azax3DrSDfc6qCYiexjoVZC-IsRuOLTgJw_VDSXOCWZ-BTMkCZMDDHvdKExtfNgH1hUoulI9F9ryOycfPLi6NfnqOnhhMplvP9r_91IXR6DIhJHilZUY",    
                    to=userPhone)
        time.sleep(2)
        message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*Menu🏠: Learning and playing games*  \n\nHow can I help you today🤗? \nPlease choose from the options below: \n\n1. *Classes 🎒 and Games🎮*. \nLet us learn new things and play games together\n\n2. *Story Telling*📖\n Do you love stories❓ \n\n3. *Handwritting*✍\n Let me teach you how to write numbers and letter\n\n4. *Define and pronounce*🗣 \n I can pronounce and define words for you".format(userName),      
                    to=userPhone)
        wks.update('R'+row+'C14', 'menu')
        return http.HttpResponse("200")


    wks2 = sheet.worksheet('Sheet2')                # getting classs links
    classtoatted=int(wks.cell(row,17).value)        # getting class to attend 
    classlinks=wks2.row_values(classtoatted)        # getting classs links  wks2
    
    if step == 'menu':
            if ('1' in request.POST['Body'].lower() or 'class' in request.POST['Body'].lower()):
                
                wks.update('R'+row+'C17', classtoatted+1)       # incremeting to the next class
                
                if (classtoatted==1): # check if learner 1st time attending.
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body="TO JOIN CLASSES🤸‍♀️ \n\nVisit this link: *https://classroom.google.com/c/NTM3NzA0Nzk0MzUy?cjc=zjoqaq4*".format(userName),      
                        to=userPhone)
                    time.sleep(2)
                    
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*Instrcutions📌* "+
                    "\n\n1️⃣ First, we attend a class and 2️⃣ then play games🎮. "+
                    f"\n\nLet's meet in class👩‍🏫. \n*Class link🔗 {classlinks[0]}*",  
                    media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM1e740520fd8353935def4751366756cc/Media/MEe2fe62132d4365e42ffbbc4ada2658db",     
                    to=userPhone)
                time.sleep(2) 
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*Instrcutions📌* \n\n3️⃣ When you are done with your class and playing games, I'll give you a homework🤸‍♀️\n\n✅When you are done send *Done* I'll give you a homework🤸‍♀️.",  
                    to=userPhone)
                wks.update('R'+row+'C14', 'classes')
            elif ('2' in request.POST['Body'].lower() or 'story' in request.POST['Body'].lower()):
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="*Instrcutions📌* \n\n1️⃣ First, I will tell you a story or give you a book \n2️⃣ Then when you done✅ listening/reading my story tell me by sending *Done* \n3️⃣ Now it will be your turn to tell a story🥺🤗 \n4️⃣ I will give you feedback once I'm done listening to you story🤗😍", 
                    media_url='https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM7380a84e9e4c56ae0bb361462629d283/Media/MEd53b3215a6d43e66df27cec67217e762',
                    to=userPhone)
                time.sleep(2)
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="1️⃣ I made this for you, I hope you enjoy my friend🤗❤️\n\n*Zuko's Story🎉* \nUse this link: \n*https://drive.google.com/file/d/19APc6HdZSmhDFXbcTCqI1PyCc5i8F4xm/view?usp=sharing*\n\n*Instrcutions📌*: \n\nSend *Done* when you done✅ listerning to my story",      
                    #media_url="https://public.bl.files.1drv.com/y4mxndLK0QG-jREsBaMIsmvfLBRZXPgsI4kTNLnVbVjhX3wxkjPXK9dTtr1Vj2CSOBkauo2d3U1vtEAVyiVjoeqSOuSLQFPjREsnXzzlwiZaZ0GQbxXKe_ZAYdnzWCZI9ex2cm-2DjY-wEXQGUTi-1xVcpBty6wLwzBVq8bYiMPdx_ywabPCUMlYCu5kXVr3fYfXxjBKhztiYxd1xCbKtkzj7Yw2pvds9kjwXrz5VwbUNc",
                    to=userPhone)
                wks.update('R'+row+'C14', 'story')
            elif ('3' in str(request.POST['Body']).lower() or 'hand' in request.POST['Body'].lower() or 'handwritting' in request.POST['Body'].lower()):
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="*Instrcutions📌* \n\n 1️⃣ You will play tracing games🎮\n 2️⃣ Let me know when you are done playing \n3️⃣ I will send you tasks", 
                    media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM6cae6ac6b18549cbc8b64e2e26872b6f/Media/ME61ebdc8924a303dc0d1eb223eea536de",     
                    to=userPhone)
                wks.update('R'+row+'C14', 'handwritting')
                time.sleep(2)
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="1️⃣ *Tracing games* 🎮 \n\nVisit this link: *https://quizizz.com/join/quiz/62e97818736b19001d90d63f/start?studentShare=true*\n\n✅Send: *Done* when you're done",      
                    to=userPhone)
                wks.update('R'+row+'C14', 'handwritting')
            elif ('4' in str(request.POST['Body']).lower() or 'define' in request.POST['Body'].lower() or 'pronounc' in request.POST['Body'].lower()):
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="*Define*🗣 \n\n*Instrcutions📌*: use this commands: DF <Your word>",      
                    media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM3ee0dc2c36368afa877b6877ad4ff76d/Media/ME0a551e002b3ef5eeb3119709cb9cc48e",     
                    to=userPhone)
                time.sleep(2)
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="*Pronounce*🗣 \n\n*Instrcutions📌*: use this commands: Pn <Your word>",      
                    media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM5b38e0cb8fb1df7e915f147fcd1f95c2/Media/ME583bc7cb955586e5bc6b71240c3cd3bf",     
                    to=userPhone)

            elif ('5' in str(request.POST['Body']).lower()):
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body='*User Manual*📜 \n\nSorry, I will let you know when the manual is ready',      
                    media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM254b5dca92440a68c4972e94f82e44ed/Media/ME073e5ca7441f865189b8503fa23c8e91",     
                    to=userPhone)
            elif ('df' in str(request.POST['Body']).lower()):
                
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body=getRecords(str(request.POST['Body']).upper().replace("DF","").strip()),      
                    media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MMba398583f409fc99f0da93408142ae30/Media/ME2a992984b809b40f6cd5d6e81a13cdbe",     
                    to=userPhone)
            elif ('pn' in str(request.POST['Body']).lower()):
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="❗️This service is currently on mantainance I am really sorry🙏🙇‍♀️",      
                    media_url="https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM5c1ca79f062ef9aff8f19d4cd4cd4086/Media/ME19f313913b3de8baeddbb43c62ff3b2a",     
                    to=userPhone)
            else:
                #print(request.POST['MediaUrl0'])
                message = client.messages.create(
                    from_=f'whatsapp:{businessphone}',  
                    body="Hey, that is a wrong selection❗️❗️❗️",      
                    to=userPhone)
                time.sleep(1)
                sendMenu(userPhone)
            return http.HttpResponse("200")
        #classes
    if step == 'classes':
            if ( '✅' in request.POST['Body'].lower() or 'done' in request.POST['Body'].lower() or 'yes' in request.POST['Body'].lower()):
                if len(classlinks)>1:
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body=f"3️⃣Now we are a going to play games🤸‍♀️😁* \n\nVisit this link: {classlinks[1]}",      
                        to=userPhone)
                    time.sleep(1)
                    message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body=f"😁 Let's call it the day, see you tomorrow. Have a lovely day, and please play the game {userName}",      
                    to=userPhone)
                else:
                    message = client.messages.create( 
                        from_=f'whatsapp:{businessphone}',  
                        body=f"Sorry {userName} I am still prepareing a game for this lesson, \n 😁 We are done for the day. Have a lovely day",      
                        to=userPhone)

                wks.update('R'+row+'C14', 'menu')
                sendMenu(userPhone)
                
            elif ('menu' in request.POST['Body'].lower() or '0' in request.POST['Body'].lower()):
                sendMenu(userPhone)
                wks.update('R'+row+'C14', 'menu')
            # elif ('1' == request.POST['Body'].lower()):
            #     message = client.messages.create( 
            #         from_=f'whatsapp:{businessphone}',  
            #         media_url='https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MM47ede3c2fcfa539c150357cfe080401e/Media/ME3ca8d4ec1429faae554b8d0edd985d56',       
            #         to=userPhone)
            #     time.sleep(3)
            #     message = client.messages.create( 
            #         from_=f'whatsapp:{businessphone}',  
            #         body="Sorry my friend we learnt Alphabets today. \n\nPlease go watch the vidoe again and Don't forget to do your homework✨",  
            #         to=userPhone)
            #     time.sleep(1)
            #     message = client.messages.create( 
            #         from_=f'whatsapp:{businessphone}',  
            #         body="*Menu🏠: Learning and playing games*  \n\n*You can choose from any of the options below, I am so exited😍🤗* \n\n1. *Classes 🎒 and Games🎮*. \nLet us learn new things and play games together\n\n2. *Story Telling*📖\n Do you love stories❓ \n\n3. *Handwritting*✍\n Let me teach you to write numbers and letter\n\n4. *Define and pronounce*🗣 \n I can pronounce letters and words. and also define words ".format(userName),      
            #         to=userPhone)
            #     wks.update('R'+row+'C14', 'menu')

            # elif ('2' == request.POST['Body'].lower()):
            #     message = client.messages.create( 
            #         from_=f'whatsapp:{businessphone}',  
            #         media_url='https://api.twilio.com/2010-04-01/Accounts/AC9cfdfeaa5bce698906cff658aaf42499/Messages/MMff9e52c5ebe21414545794753b3160d6/Media/ME9883e5cd2e58d2b14e41fc6ce5e29a7c',       
            #         to=userPhone)
            #     time.sleep(3)
            #     message = client.messages.create( 
            #         from_=f'whatsapp:{businessphone}',  
            #         body="Yes my friend you nailed it🤗.\nWe done for the day, Don't forget to do your homework✨",
            #         to=userPhone)
            #     time.sleep(1)
            #     sendMenu(userPhone)
            #     wks.update('R'+row+'C14', 'menu')
            else:
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body=f"Hey {userName} are you done? \n ",      
                    to=userPhone)
            return http.HttpResponse("200")   
    if step == 'handwritting':
            
            if (request.POST['NumMedia']!='0'):
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="🙏 I give you feedback soon\n\nDo you what to continue❓\n0. menu🏠".format(userName),      
                    to=userPhone)
                time.sleep(3)

                ## Amazon rekognition here.

            elif ('done' in request.POST['Body'].lower()):
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*How to hold a pen🖊*\n\n*📌Note:* If you do not know how to hold a pen🖊 visit this link: *https://youtu.be/RclxBdiuvOM*.\nif you know please start your task👇".format(userName),      
                    to=userPhone) 
                question=images[random.randint(0, 9)]
                time.sleep(4)
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*Task✍*, \n\n*Instrcutions📌*: write the above👆 number on your book, when done✅ send the picture to me🤗.".format(userName),
                    media_url=question,       
                    to=userPhone)
            elif ('1' in request.POST['Body'].lower() or 'yes' in request.POST['Body'].lower()): 
                question=images[random.randint(0, 9)]
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*Task✍*, \n\nWrite the above👆 number on your book, when done✅ send the picture to me🤗.".format(userName),
                    media_url=question,       
                    to=userPhone)
            elif ('menu' in request.POST['Body'].lower() or '0' in request.POST['Body'].lower()):
                sendMenu(userPhone)
                wks.update('R'+row+'C14', 'menu')
            else:
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="*Handwritting*✍ \n\n0. menu",      
                    to=userPhone)
            return http.HttpResponse("200")
    if step == 'story':
            if ('done' in request.POST['Body'].lower() or 'yes' in request.POST['Body'].lower()  or 'thank' in request.POST['Body'].lower()):
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="Awesome Thank you😊, \n\n 3️⃣now it's your turn to tell a story, send text or voice".format(userName),      
                    to=userPhone)
            elif (request.POST['NumMedia']!='0'):
                message = client.messages.create( 
                    from_=f'whatsapp:{businessphone}',  
                    body="Thank you {} 😊\n\n I'll listen to you story, I'll give you feedback soon \n0. menu  ".format(userName),      
                    to=userPhone)
            elif ('menu' in request.POST['Body'].lower() or '0' in request.POST['Body'].lower()):
                sendMenu(userPhone)
                wks.update('R'+row+'C14', 'menu')
            return http.HttpResponse("200")
    else:
            message = client.messages.create( 
                from_=f'whatsapp:{businessphone}',  
                body="Hey I don't get that ", 
                to=userPhone)
    return http.HttpResponse("200")

