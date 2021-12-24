from random import randint

from models.roll import Result


def mount_chars(_chars):
    chars = []
    for char in _chars:
        chars.append({'name': char.name, 'attribute': char.attribute, 'adventure': char.adventure})
    return chars

def roll_dices(_type, _qtd, _attribute):
    results = []
    for i in range(0, _qtd):
        result = randint(1, 6)
        results.append(Result.create_result(result, get_success(result, _type, _attribute)))
    return results

def get_success(_result, _type, _attribute):
    if _type == 'fisico':
        return 'critico' if _result == _attribute else 'sucesso' if _result < _attribute else 'falha'
    elif _type == 'mental':
        return 'critico' if _result == _attribute else 'sucesso' if _result > _attribute else 'falha'

def mount_rolls(_results):
    results = []
    for result in _results:
        results.append({'name': result.char_name, 'results': [res.to_mongo().to_dict() for res in result.results]})
    return results
