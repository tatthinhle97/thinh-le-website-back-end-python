from fastapi import APIRouter, Depends
from databases.mysql import get_db_session
from repositories.state import StateRepository

router = APIRouter(
    prefix='/states',
    tags=['states']
)

@router.get(
    # [Tip] Should not put '/' because front end will receive status 307
    '',
    summary='Get all states',
    description='Get all states'
)
async def get_states(db_session = Depends(get_db_session)):
    state_repository = StateRepository(db_session)
    return state_repository.get_all()