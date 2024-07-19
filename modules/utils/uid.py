import uuid

def generate_uid():
    return uuid.uuid4().__str__()