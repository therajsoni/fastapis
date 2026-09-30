def ResponseSuccess(success=200, message="", data=None, other=None):
    return {
        "success": success,
        "message": message,
        "data": data,
        "other": other
    }


def ResponseFailure(success=500, message="", other=None):
    return {
        "success": success,
        "message": message,
        "other": other
    }