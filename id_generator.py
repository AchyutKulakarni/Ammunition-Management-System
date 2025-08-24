def unique_id_generator(start=1):
    
    current = start
    while True:
        yield current
        current += 1