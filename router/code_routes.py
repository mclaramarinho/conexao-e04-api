from fastapi import APIRouter, Body, Request, Response, status, Security
from typing import List
from fastapi import HTTPException, status
from database import db
from router.default import PATHS, exception_404, response_descriptions
from router.default_functions import create_one
from api_keys import get_api_key
from models.Code import Code, OnlyCode

COLLECTION_NAME = "creation_codes"
EXCEPTION_404_NOT_FOUND = exception_404("Code")
RESPONSE_DES = response_descriptions("code")

router = APIRouter()


@router.post(path=PATHS["post"], response_description=RESPONSE_DES["post"], status_code=status.HTTP_201_CREATED)
def create_code(request: Request, input_code: Code = Body(...), api_key: str = Security(get_api_key, scopes=[])):
    uid = input_code.uid
    user = db["admins"].find_one({"firebase_uid": uid})
    if user is not None:
        if input_code.role == 'admin' or input_code.role == 'owner':
            return create_one(COLLECTION_NAME, request, input_code, EXCEPTION_404_NOT_FOUND)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The role is not valid.")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"This user does not exist")


@router.delete(path="/delete/{id}/{uid}", response_description=RESPONSE_DES["delete"],  status_code=status.HTTP_204_NO_CONTENT)
def delete_class(id: str, uid: str, request: Request, response: Response, api_key: str = Security(get_api_key, scopes=[])):
    print(id)
    print(uid)
    dr = db[COLLECTION_NAME].delete_one({"_id": id, "uid": uid})
    print(dr)
    if dr.deleted_count > 0:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    else:
        raise EXCEPTION_404_NOT_FOUND


@router.get(path="/all/{uid}/{exp}", response_description=RESPONSE_DES["get_all"], response_model=List[Code])
def get_all_ccdes(uid: str, exp: bool, request: Request, api_key: str = Security(get_api_key, scopes=[])):
    user = db["admins"].find_one({"firebase_uid": uid})
    if user is not None:
        res = list(db[COLLECTION_NAME].find({"uid": uid, "expired": exp},limit=100))
        return res
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"This user does not exist")


@router.put(path="/expire-code/{id}", response_description="Mark a code as expired", response_model=Code)
def update_code_validity(id: str, req: Request, res: Response, input_content=Body(...),
                         api_key: str = Security(get_api_key, scopes=[])):

    pr = db[COLLECTION_NAME].update_one({"_id": id}, {"$set": {
        "expired": True
    }})

    if (existing_class := db[COLLECTION_NAME].find_one({"_id": id})) is not None:
        return existing_class

    raise EXCEPTION_404_NOT_FOUND

@router.post(path="/validate", response_model=Code, status_code=status.HTTP_202_ACCEPTED)
def validate_code(req: Request, input_content:OnlyCode=Body(...), api_key: str = Security(get_api_key, scopes=[])):

    codes = list(db[COLLECTION_NAME].find({"code": input_content.code}))
    is_valid = False
    valid_code:Code = None

    for code in codes:
        if code["expired"] == False:
            valid_code = code
            is_valid = True
            break
    print(valid_code)
    if is_valid:
        try:
            pr = db[COLLECTION_NAME].update_one({"_id": valid_code['_id']}, {"$set": {
                "expired": True
            }})
            print(pr)
            if pr.modified_count > 0:
                return valid_code
            else:
                raise
        except:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="The code is not valid")