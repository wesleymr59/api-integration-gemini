from application.interfaces.ia_interface import IaInterface


class IAUseCase:
    def __init__(self, ia_interface: IaInterface) -> None:
        self.__ia_interface = ia_interface
    
    def send_message(self, msg: str):
        return self.__ia_interface.sendMessage(msg)