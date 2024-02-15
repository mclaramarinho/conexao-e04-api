from fastapi import Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from database import db


def get_one(id: str, collection: str, req: Request, exception: HTTPException):
    if collection == "admins":
        response = db[collection].find_one({"firebase_uid": id})
    else:
        response = db[collection].find_one({"_id": id})

    if response is not None:
        return response

    raise exception


def get_all(collection: str, req: Request):
    response = list(db[collection].find(limit=100))
    return response


def delete_one(id: str, collection: str, req: Request, res: Response,  exception: HTTPException):
    if collection == "admins":
        delete_result = db[collection].delete_one({"firebase_uid": id})
    else:
        delete_result = db[collection].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        res.status_code = status.HTTP_204_NO_CONTENT
        return res

    raise exception


def update_one(id: str, collection: str, req: Request, body, exception: HTTPException):
    body = {
        k: v for k, v in body.dict().items()
        if v is not None
    }

    if len(body) >= 1:
        if collection == "admins":
            update_result = db[collection].update_one(
                {"firebase_uid": id}, {"$set": body}
            )
        else:
            update_result = db[collection].update_one(
                {"_id": id}, {"$set": body}
            )

        if update_result.modified_count == 0:
            raise exception

    if (existing_class := db[collection].find_one({"_id": id})) is not None:
        return existing_class

    raise exception


def create_one(collection: str, req: Request, body, exception: HTTPException):
    body = jsonable_encoder(body)

    new_document = db[collection].insert_one(body)

    created_document = db[collection].find_one({
        "_id": new_document.inserted_id
    })

    return created_document


