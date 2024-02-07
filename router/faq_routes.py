from fastapi import APIRouter, Body, Request, Response, status, Security
from typing import List
from models.FAQ import FAQ
from models.FAQUpdate import FAQUpdate
from router.default import PATHS, exception_404, response_descriptions
from router.default_functions import create_one, update_one, get_one, get_all, delete_one
from api_keys import get_api_key


COLLECTION_NAME = "faqs"
EXCEPTION_404_NOT_FOUND = exception_404("FAQ")
RESPONSE_DES = response_descriptions("FAQ")

router = APIRouter()


@router.post(path=PATHS["post"], response_description=RESPONSE_DES["post"], status_code=status.HTTP_201_CREATED)
def create_faq(req: Request, faq: FAQ = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return create_one(COLLECTION_NAME, req, faq, EXCEPTION_404_NOT_FOUND)


@router.put(path=PATHS["put"], response_description=RESPONSE_DES["put"], response_model=FAQ)
def update_faq(id: str, req: Request, faq: FAQUpdate = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    return update_one(id, COLLECTION_NAME, req, faq, EXCEPTION_404_NOT_FOUND)


@router.delete(path=PATHS["delete"], response_description=RESPONSE_DES["delete"])
def delete_faq(id: str, req: Request, res: Response, api_key: str = Security(get_api_key, scopes=[])):
    return delete_one(id, COLLECTION_NAME, req, res, EXCEPTION_404_NOT_FOUND)


@router.get(path=PATHS["get_all"], response_description=RESPONSE_DES["get_all"], response_model=List[FAQ])
def get_all_FAQs(req: Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_all(COLLECTION_NAME, req)


@router.get(path=PATHS["get"], response_description=RESPONSE_DES["get"], response_model=FAQ)
def get_faq(id: str, req: Request, api_key: str = Security(get_api_key, scopes=[])):
    return get_one(id, COLLECTION_NAME, req, EXCEPTION_404_NOT_FOUND)
