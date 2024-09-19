from typing import Optional

def create_response(status_code: int, status: str, message: str, data: Optional[dict] = None):
    return status_code, {"status": status, "message": message, "data": data}
