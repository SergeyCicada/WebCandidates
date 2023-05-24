from function import *


class candidates:

    def __init__(self, path):
        self.path = path

    def all_candidates(self):
        candidates = load_candidates(self.path)
        str_candidates = '<pre>'
        for candidate in candidates.values():
            str_candidates += f"\n{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
        str_candidates += "</pre>"
        return str_candidates

    def profile_candidates(self, uid):
        candidates = load_candidates(self.path)
        str_candidates = '<pre>'
        candidates_uid = candidates[uid]
        str_candidates += f"\n<img src={candidates_uid['picture']}>\n{candidates_uid['name']} \n{candidates_uid['position']} \n{candidates_uid['skills']}\n\n"
        str_candidates += "</pre>"
        return str_candidates

    def skills_candidates(self, skills):
        candidates = load_candidates(self.path)
        str_candidates = '<pre>'
        for candidate in candidates.values():
            if skills.lower() in candidate['skills'].lower():
                str_candidates += f"\n{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
        str_candidates += '</pre>'
        return str_candidates


