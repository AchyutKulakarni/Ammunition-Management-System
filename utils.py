import re
from models import Ammunition

def compare_ammunition(a1: Ammunition, a2: Ammunition):
    diffs = {}
    fields = ['caliber', 'ammo_type', 'quantity', 'manufacturer', 'price', 'date_manufactured', 'expiry_date']
    for field in fields:
        v1 = getattr(a1, field)
        v2 = getattr(a2, field)
        if v1 != v2:
            diffs[field] = {'old': v1, 'new': v2}
    return diffs

def regex_search(ammo_list, field, pattern, ignore_case=True):
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags)
    results = []
    for ammo in ammo_list:
        value = getattr(ammo, field)
        if regex.search(str(value)):
            results.append(ammo)
    return results

def sort_ammo(ammo_list, key, descending=False):
    return sorted(ammo_list, key=lambda x: getattr(x, key), reverse=descending)
