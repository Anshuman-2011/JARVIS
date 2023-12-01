from func.Chat import Chat
from func.SpeakOffline import Speak
from func.ListenJs import Listen
from func.DataOnline import Online_Scraper
from llm.ChatGpt import ChatGpt

if __name__=="__main__":
    while 1:
        Q=Listen()
        QL=Q.lower()
        LQ=len(Q.split(" "))
        SQ=Q.split(" ")[0]           
        EQ=Q.split(" ")[-1]
        

        Speak(GhatGpt(Q))

    
        

