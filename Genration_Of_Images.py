#pip install --upgrade BingImageCreator
from os import system , listdir
from PIL import Image

C=COKKEE ##WATCH THIS IF YOU DON"T HAVE COKKEE OR YOU CAN PUT "0" as your cokkee https://www.youtube.com/watch?v=_PL7UMzaSBk 
def Generate_Images(prompt:str):
    system(f'python -m BingImageCreator --prompt "{prompt}" -U {C}')
    return listdir("output")[-4:]

class Show_Image:
    def __init__(self,li:list) -> None:
        self.listd=li
    def open(self,no):
        try:
            img = Image.open(f"output\\{self.listd[no]}")
            img.show()
        except:
            print("image was not good")
            self.open(no+1)
    def close(self,no):
        #TODO
        pass
