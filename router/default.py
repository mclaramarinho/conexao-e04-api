from fastapi import HTTPException, status

PATHS = {
    "post": "/create",
    "put": "/update/{id}",
    "delete": "/delete/{id}",
    "get_all": "/all",
    "get": "/get/{id}",
}


def exception_404(what = ""):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{what} with ID {id} was not found.")


def response_descriptions(what = ""):
    return {
        "post": f"Create a new {what}",
        "put": f"Update an existing {what}",
        "delete": f"Delete an existing {what}",
        "get_all": f"Get all existing {what}",
        "get": f"Get an existing {what}"
    }

