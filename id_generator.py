def unique_id_generator(start=1):
    """
    Yields sequential integer IDs starting from `start`.
    - Each call yields the next unique integer (no repetition in a single run).
    - Handles at least 2,000 IDs easily (no fixed upper bound).
    - IDs are integers (usable as primary keys).
    """
    current = start
    while True:
        yield current
        current += 1