from fastapi import APIRouter
from dtos.chat.chat_query import ChatQueryDTO

router = APIRouter(
    prefix='/chatbot',
    tags=['chatbot']
)

@router.post(
    '',
    summary='Chatbot response',
    description='Receive a query from the user and response with an answer'
)
async def send_query(chatQueryDTO: ChatQueryDTO):
    similar_sentences = search_similar(query)