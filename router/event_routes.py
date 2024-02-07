from fastapi import APIRouter, Body, Request, Response, status, Security
from typing import List
from models.Event import Event
from models.EventUpdate import EventUpdate
from router.default import PATHS, exception_404, response_descriptions
from router.default_functions import get_one, get_all, delete_one, update_one, create_one
from api_keys import get_api_key

COLLECTION_NAME = "events"
EXCEPTION_404_NOT_FOUND = exception_404("Event(s)")
RESPONSE_DES = response_descriptions("event(s)")


router = APIRouter()


@router.post(path=PATHS["post"], response_description=RESPONSE_DES["post"], status_code=status.HTTP_201_CREATED,
             response_model=Event)
def create_event(request: Request, event: Event = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return create_one(COLLECTION_NAME, request, event, EXCEPTION_404_NOT_FOUND)


@router.put(path=PATHS["put"], response_description=RESPONSE_DES["put"], response_model=Event)
def update_event(id: str, request: Request, event: EventUpdate = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return update_one(id, COLLECTION_NAME, request, event, EXCEPTION_404_NOT_FOUND)


@router.delete(path=PATHS["delete"], response_description=RESPONSE_DES["delete"])
def delete_event(id: str, request:Request, response: Response, api_key: str = Security(get_api_key, scopes=[])):
    return delete_one(id, COLLECTION_NAME, request, response, EXCEPTION_404_NOT_FOUND)


@router.get(path=PATHS["get_all"], response_description=RESPONSE_DES["get_all"], response_model=List[Event])
def list_events(request: Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_all(COLLECTION_NAME, request)


@router.get(path=PATHS["get"], response_description=RESPONSE_DES["get"], response_model=Event)
def get_event(id: str, request: Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_one(id, COLLECTION_NAME, request, EXCEPTION_404_NOT_FOUND)
