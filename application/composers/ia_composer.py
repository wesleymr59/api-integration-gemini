
from infra.ia.gemini import Ia
from domain.usecases.ia_usecase import IAUseCase


class IaComposer():
    
    @staticmethod
    def ia_composer():
        ia = Ia()
        ia_usecase = IAUseCase(ia_interface=ia)
        return ia_usecase