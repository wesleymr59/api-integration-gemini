from fastapi import APIRouter, Depends, HTTPException
from domain.dto.schemas import HealtyResponse, MessageBody
from application.composers.ia_composer import IaComposer
from domain.usecases.ia_usecase import IAUseCase

router = APIRouter()


@router.get("/healthy_check/", response_model=HealtyResponse)
def healthy_check():
        return {"Message": "Ta on Carai"}
    
@router.post("/send/message/")
def send_message(msg: MessageBody, ia_usecase: IAUseCase = Depends(IaComposer.ia_composer)):
        return ia_usecase.send_message(msg.Message)
