from func.Chat import Chat
from func.SpeakOffline import Speak
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
from Genration_Of_Images import *
from colorama import Fore, Back, Style
from llm.OgChatGpt import ChatGpt
print()
link=input(Fore.RED+"inter colab + ngrok like check the video. No link enter 69 -> ")
if link=="69":
    from llm.OgChatGpt import ChatGpt
    from func.OcrOffline import Ocr

if __name__=="__main__":
    while 1:
        Q=Listen()
        QL=Q.lower()
        LQ=len(Q.split(" "))
        SQ=Q.split(" ")[0]
        EQ=Q.split(" ")[-1]
        CURRENT_APP=""
        try:
            CURRENT_APP = gw.getActiveWindowTitle()
        except :
            CURRENT_APP = ""
        #CURRENT_APP NAME
        CURRENT_APP_NAME=CURRENT_APP.split(" - ")[-1]

        if (SQ=="click" or (SQ=="double" and "click" in Q)) and LQ<7:
            QL.replace("click","")
            QL.replace("on","")
            QL.replace("jarvis","")
            QL.replace("double","")
            A=Ocr(QL.strip(),url=link)
            Speak(A)

        elif "jarvis"==SQ.lower():
            code = ChatGpt(f"{Q} ***use python programing language. just write complete code nothing else*** **you can use functions that i gave to you**",link=link)
            code = Filter(code)
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
                            code = CodeFilter(code)
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
















