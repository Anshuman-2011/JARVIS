from func.Chat import Chat
from func.SpeakOnline import Speak
from func.ListenJs import Listen
from func.DataOnline import Online_Scraper
from llm.ChatGptColab import ChatGpt
from func.OcrOnline import Ocr
from llm.Filter import Filter
from buildin import ChromeCode
from buildin import KnowApps
import pygetwindow as gw
import keyboard

link=input("inter colab + ngrok like check the video. No link enter 69 -> ")
if link=="69":
    from llm.ChatGpt import ChatGpt
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
        except gw.PyGetWindowException:
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
            code = ChatGpt(f"{Q} ***use python programing language. just write complete code nothing else***",link=link)
            code = Filter(code)
            exec(code)

        if CURRENT_APP_NAME in KnowApps:
            
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
                    reply=ChatGpt(f"{Q} ***reply like tony stark jarvis in less words***",link=link)
                    Speak(reply)
        else :
                web=Online_Scraper(Q)
                if web!=None:
                    Speak(web)
                elif Chat(QL)[1]>0.99:
                    Speak(Chat(QL)[0])
                else:
                    reply=ChatGpt(f"{Q} ***reply like tony stark jarvis in less words***",link=link)
                    Speak(reply)

















