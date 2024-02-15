from fastapi import APIRouter, Body, Response, status, Depends, Security
from typing import List
from fastapi.requests import Request

from router.default import PATHS, exception_404, response_descriptions
from router.default_functions import get_one, get_all, delete_one, update_one, create_one
from models.Admin import Admin
from models.AdminUpdate import AdminUpdate
from api_keys import get_api_key


COLLECTION_NAME = "admins"
EXCEPTION_404_NOT_FOUND = exception_404("Admin")
RESPONSE_DES = response_descriptions("admin")

router = APIRouter()


@router.post(path=PATHS["post"], response_description=RESPONSE_DES["post"], status_code=status.HTTP_201_CREATED)
def create_admin(request: Request, user: Admin = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return create_one(COLLECTION_NAME, request, user, EXCEPTION_404_NOT_FOUND)


@router.put(path=PATHS["put"], response_description=RESPONSE_DES["put"], response_model=Admin)
def update_admin(id: str, request: Request, user: AdminUpdate = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return update_one(id, COLLECTION_NAME, request, user, EXCEPTION_404_NOT_FOUND)


@router.delete(path=PATHS["delete"], response_description=RESPONSE_DES["delete"])
def delete_admin(id: str, request: Request, response: Response, api_key: str = Security(get_api_key, scopes=[])):
    return delete_one(id, COLLECTION_NAME, request, response, EXCEPTION_404_NOT_FOUND)


@router.get(path=PATHS["get_all"], response_description=RESPONSE_DES["get_all"], response_model=List[Admin])
def get_all_admins(request: Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_all(COLLECTION_NAME, request)


@router.get(path=PATHS["get"], response_description=RESPONSE_DES["get"], response_model=Admin)
def get_admin(id: str, request:Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_one(id, COLLECTION_NAME, request, EXCEPTION_404_NOT_FOUND)
