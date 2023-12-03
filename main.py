from func.Chat import Chat
from func.SpeakOffline import Speak
from func.ListenJs import Listen
from func.DataOnline import Online_Scraper
from llm.ChatGpt import ChatGpt
from func.Ocr import Ocr
from llm.Filter import Filter

if __name__=="__main__":
    while 1:
        Q=Listen()
        QL=Q.lower()
        LQ=len(Q.split(" "))
        SQ=Q.split(" ")[0]           
        EQ=Q.split(" ")[-1]
        
        if (SQ=="click" or (SQ=="double" and "click" in Q)) and LQ<7:
            QL.replace("click","")
            QL.replace("on","")
            QL.replace("jarvis","")
            QL.replace("double","")
            A=Ocr(QL.strip())
            Speak(A)

        elif "jarvis"==SQ.lower():
            code = ChatGpt(Q," ***use python programing language. just write complete code nothing else***")
            code = Filter(code)
            exec(code)

        else :
            web=Online_Scraper(Q)
            if web!=None:
                Speak(web)
            elif Chat(QL)[1]>0.99:
                Speak(Chat(QL)[0])
            else:
                reply=ChatGpt(Q," ***reply like tony stark jarvis in less words***")
                Speak(reply)