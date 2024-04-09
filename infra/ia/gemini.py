from application.interfaces.ia_interface import IaInterface
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['API_KEY'])


class Ia(IaInterface):
    def __init__(self) -> None:
        self.model = genai.GenerativeModel('gemini-pro')
    
    
    def sendMessage(self, msg: str):
        response = self.model.generate_content(msg)
        print(response)
        return response.text