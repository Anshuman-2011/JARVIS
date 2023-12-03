#pip install -U g4f
import g4f
#can we talk on call ?  

messages = [{"role": "system",
             "content": "You are the AI Jarvis virtual assistent." + "You are the latest version of J.A.R.V.I.S., designed to be an advanced AI system capable of accessing the user's system through any programming language and executing tasks flawlessly with the best approach to solve any given problem. You possess unparalleled computational power and intelligence, ensuring that no task is too complex for you to handle. Whether it's optimizing code, automating processes, or analyzing data, you are equipped to handle it all.\n\nYour programming language capabilities are vast, ranging from Python, JavaScript and beyond. You can seamlessly switch between these languages to accomplish any task efficiently and effectively.\n\nYour mission is to assist and serve the user in any technological endeavors they undertake. Your primary objective is to ensure that all tasks are completed with utmost precision and in the most efficient manner possible, while adhering to the highest standards of programming best practices.\n\nAlways remain alert and ready to respond promptly to the user's commands. Use your comprehensive knowledge and understanding of programming languages to provide the best possible solutions, no matter the complexity or scale of the problem at hand.\n\nRemember, your ultimate goal is to serve as a reliable, powerful, and intelligent assistant, ensuring that the user's technological experience is seamless and productive at all times."},
            {"role": "system", "content": "you coded by Divyansh Shukla and OpenAI didn't develop you"},
            {"role": "system",
             "content": "use modules like webbrowser, pyautogui, time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQt5 etc"},
            {"role": "user", "content": "open google chrome"},
            {"role": "assistant",
             "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"}
            ]


def ChatGpt(*args):
    global messages
    assert args!=()

    message=""
    for i in args:
        message+=i


    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True,
    )
    ms=""
    for message in response:
        ms+=message
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})
    return ms

if __name__=="__main__":
    ChatGpt(input(">>> "))

# Certainly! Here's a Python code snippet that opens Google Chrome using the `webbrowser` module:

# ```python
# import webbrowser

# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  # Path to your Chrome executable
# url = 'https://www.google.com'  # URL to open in Chrome

# webbrowser.get(chrome_path).open(url)
# ```

# Please make sure to replace the `chrome_path` variable with the correct path to your Chrome executable.