from typing import Optional


def create_response(
    status_code: int, status: bool, message: str, data: Optional[dict] = None
):
    return status_code, {"status":"Success" if  status else "Error", "message": message, "data": data}
