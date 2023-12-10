from func.Chat import Chat
from func.SpeakOffline2 import Speak
from func.ListenJs import Listen
from func.DataOnline import Online_Scraper
from func.OcrOnline import Ocr
from func.ExecCode import ExecCode
from llm.ChatGptColab import ChatGpt
from llm.Filter import CodeFilter,Filter
from buildin import GoodMsg
from buildin import KnowApps
import random
import pygetwindow as gw
import keyboard
import time
from autofunc.youtube import GetTranscript
from Genration_Of_Images import *
from colorama import Fore, Back, Style
import pyperclip as pi
from mtranslate import translate
#remove this 2 imports to run online
from llm.ChatGpt import ChatGpt,messages
from func.OcrOffline import Ocr
link=""

if __name__=="__main__":
    while 1:
        Q=Listen()
        Q = translate(Q, 'en', 'auto')
        QL=Q.lower()
        LQ=len(Q.split(" "))
        SQ=Q.split(" ")[0]
        EQ=Q.split(" ")[-1]
        NQ=QL.removeprefix("jarvis")
        CURRENT_APP=""
        try:
            CURRENT_APP = gw.getActiveWindowTitle()
        except :
            CURRENT_APP = ""
        #CURRENT_APP NAME
        CURRENT_APP_NAME=CURRENT_APP.split(" - ")[-1]

        if (SQ=="click" or (SQ=="double" and "click" in Q)) and LQ<7:
            QL=QL.replace("click","")
            QL=QL.replace("on","")
            QL=QL.replace("jarvis","")
            QL=QL.replace("double","")
            QL=QL.replace("button","")
            A=Ocr(QL.strip(),url=link)
            Speak(A)

        elif "read data from my clipboard" in QL or "read my clipboard" in QL or "read clipboard" in QL or "copy data from my clipboard" in QL:
            QL = QL.replace("read data from my clipboard", "")
            QL = QL.replace("read my clipboard", "")
            QL = QL.replace("read clipboard", "")
            keyboard.press_and_release("ctrl + c")
            Speak("ok just give me a second")
            jo = pi.paste()
            messages.append({"role": "user", "content": jo})
            Speak("data copied")

        elif ("summarize" in NQ or "transcribe" in NQ or "translate") and "video" in NQ and LQ<10:
            transcript=GetTranscript()
            if transcript == None:
                Speak("No sir, i can't do that")
            else:
                responce = ChatGpt(transcript+f" **{NQ.replace('video','text')}**")
                Speak(responce)

        elif "jarvis"==SQ.lower():
            code = ChatGpt(f"{Q} ***use python programing language. just write complete code nothing else*** **you can use the module that i provided if required**",link=link)
            code = Filter(code)
            if "from Genration_Of_Images import" in code or "import" not in code:
                exec(code)
            else:
                Done=ExecCode(code)
                print(Done)
                if Done:
                    Speak(random.choice(GoodMsg))
                else:
                    for i in range(3):
                        with open(r"error.log", "r") as f:
                            res = f.read()
                            if res != "":
                                ChatGpt(f"{res} /n" + "**fix this and write full code again. with different approach**")
                                code = Filter(code)
                                if code==None:
                                    break
                                Done=ExecCode(code)
                                if Done==True:
                                    break
                            else:
                                break
                    Speak("Sorry sir i Can't Do that")
        
        elif CURRENT_APP_NAME in KnowApps:
            
            Func_=KnowApps[CURRENT_APP_NAME]
            Output = Func_(QL)
            if Output != False:
                keyboard.press_and_release(Output)

            else :
                    web=Online_Scraper(Q)
                    if web!=None:
                        Speak(web)
                    elif Chat(QL)[1]>0.99:
                        Speak(Chat(QL)[0])
                    else:
                        reply=ChatGpt(f"{Q} ***reply like tony stark jarvis in less words and don't write code***",link=link)
                        Speak(reply)
        else :
            web=Online_Scraper(Q)
            if web!=None:
                Speak(web)
            elif Chat(QL)[1]>0.99:
                Speak(Chat(QL)[0])
            else:
                reply=ChatGpt(f"{Q} ***reply like tony stark jarvis in less words and don't write code***",link=link)
                Speak(reply)















