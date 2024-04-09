from fastapi import APIRouter, Depends, HTTPException
from domain.dto.schemas import HealtyResponse, MessageBody
from infra.ia.gemini import Ia
from domain.usecases.ia_usecase import IAUseCase
router = APIRouter()

ia = Ia()

ia_usecase = IAUseCase(
    ia_interface=ia
)

get_ia_usecase = lambda: ia_usecase


@router.get("/healthy_check/", response_model=HealtyResponse)
def healthy_check():
        return {"Message": "Ta on Carai"}
    
@router.post("/send/message/")
def send_message(msg: MessageBody, ia_usecase: IAUseCase = Depends(get_ia_usecase)):
        return ia_usecase.send_message(msg.Message)
