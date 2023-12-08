#pip install --upgrade BingImageCreator
from os import system , listdir
from PIL import Image

C="1BJs_7Ua-TZ_vNBLWNBw1_TN37SwGkir2D85PCrXrgiiO_zDrehH96bNNE_qQVgknst0GMUHgS7aQvcBnb7VW-T8Y0qcKdNrW4VGUgDVxEVbKSxbshqgljblTC_K20fzSpn7WPLc5dlqLd-vTMEX5SqPBH6kqJubt6myEkoLRq7q6DEiCfXv2Af_Qo17EhQ4S54mJhzPiXFuBL7ZhM--byCKA7A1L8j1jC57FdlRoEZM"
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