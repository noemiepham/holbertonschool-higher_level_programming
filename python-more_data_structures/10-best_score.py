#!/usr/bin/python3
def best_score(a_diction):
    if a_diction is None:
        return None
    max_key = max(a_diction, key=a_diction.get)

    return max_key
