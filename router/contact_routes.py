from fastapi import APIRouter, Body, Request, Response, status, Security
from typing import List
from models.ImportantContact import ImportantContact
from models.ImportantContactUpdate import ImportantContactUpdate
from router.default import PATHS, exception_404, response_descriptions
from router.default_functions import get_one, get_all, delete_one, update_one, create_one
from api_keys import get_api_key


COLLECTION_NAME = "contacts"
EXCEPTION_404_NOT_FOUND = exception_404("Contact(s)")
RESPONSE_DES = response_descriptions("contact(s)")


router = APIRouter()


@router.post(path=PATHS["post"], response_description=RESPONSE_DES["post"], status_code=status.HTTP_201_CREATED)
def create_contact(request: Request, contact: ImportantContact = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return create_one(COLLECTION_NAME, request, contact, EXCEPTION_404_NOT_FOUND)


@router.put(path=PATHS["put"], response_description=RESPONSE_DES["put"], response_model=ImportantContact)
def update_contact(id: str, request: Request, contact: ImportantContactUpdate = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return update_one(id, COLLECTION_NAME, request, contact, EXCEPTION_404_NOT_FOUND)


@router.delete(path=PATHS["delete"], response_description=RESPONSE_DES["delete"])
def delete_contact(id: str, request:Request, response: Response, api_key: str = Security(get_api_key, scopes=[])):
    return delete_one(id, COLLECTION_NAME, request, response, EXCEPTION_404_NOT_FOUND)


@router.get(path=PATHS["get_all"], response_description=RESPONSE_DES["get_all"], response_model=List[ImportantContact])
def list_contacts(request: Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_all(COLLECTION_NAME, request)


@router.get(path=PATHS["get"], response_description=RESPONSE_DES["get"], response_model=ImportantContact)
def get_contact(id: str, request: Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_one(id, COLLECTION_NAME, request, EXCEPTION_404_NOT_FOUND)
