import uuid

def unique_id_generator():
    """Generates unique UUID4 strings indefinitely."""
    while True:
        yield str(uuid.uuid4())
