from fastapi import APIRouter
from dtos.chat.chat_query import ChatQueryDto
#from services.qdrant import search_similar_points_by_query, find_highest_score

router = APIRouter(
    prefix='/chatbot',
    tags=['chatbot']
)

@router.post(
    '',
    summary='Send user message',
    description='Receive a query from the user and response with an answer'
)
async def send_message(chatQueryDto: ChatQueryDto):
    # search_response = search_similar_points_by_query(
    #     'website_metadata',
    #     chatQueryDto.message)
    #
    # point_with_highest_score = find_highest_score(search_response.points)
    #
    # if point_with_highest_score.score < 0.25:
    #     return None

    #return point_with_highest_score
    return None