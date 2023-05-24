import requests


def load_candidates(path):
    data = requests.get(path)
    list_candidates = data.json()
    candidates = {}
    for i in list_candidates:
        candidates[i["id"]] = i
    return candidates
