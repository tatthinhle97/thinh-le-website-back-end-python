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

    print(search_response.points)

    point_with_highest_score = find_highest_score(search_response.points)

    # results.append({
    #     "score": point.score,
    #     "title": search_result.payload["title"],
    #     "summary": search_result.payload["summary"],
    #     "url": search_result.payload["url"],
    #     "type": search_result.payload.get("type", ""),
    # })


    return point_with_highest_score