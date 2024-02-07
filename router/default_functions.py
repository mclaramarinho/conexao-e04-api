from fastapi import Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder


def get_one(id: str, collection: str, req: Request, exception: HTTPException):
    response = req.app.database[collection].find_one({"_id": id})

    if response is not None:
        return response

    raise exception


def get_all(collection: str, req: Request):
    response = list(req.app.database[collection].find(limit=100))
    return response


def delete_one(id: str, collection: str, req: Request, res: Response,  exception: HTTPException):
    delete_result = req.app.database[collection].delete_one({"_id": id})

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
        update_result = req.app.database[collection].update_one(
            {"_id": id}, {"$set": body}
        )

        if update_result.modified_count == 0:
            raise exception

    if (existing_class := req.app.database[collection].find_one({"_id": id})) is not None:
        return existing_class

    raise exception


def create_one(collection: str, req: Request, body, exception: HTTPException):
    body = jsonable_encoder(body)

    new_document = req.app.database[collection].insert_one(body)

    created_document = req.app.database[collection].find_one({
        "_id": new_document.inserted_id
    })

    return created_document


