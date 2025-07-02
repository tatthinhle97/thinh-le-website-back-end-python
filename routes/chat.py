from fastapi import APIRouter
from dtos.chat.chat_query import ChatQueryDto
from services.qdrant import search_similar_points_by_query, find_highest_score

router = APIRouter(
    prefix='/chatbot',
    tags=['chatbot']
)

@router.post(
    '',
    summary='Chatbot response',
    description='Receive a query from the user and response with an answer'
)
async def send_message(chatQueryDto: ChatQueryDto):
    search_response = search_similar_points_by_query(
        chatQueryDto.collection_name,
        chatQueryDto.message)

    point_with_highest_score = find_highest_score(search_response.points)

    return point_with_highest_score