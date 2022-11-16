def get_params(request_type, excluded):
    return {
        key: value for key, value in request_type.items()
        if key not in excluded
    }
