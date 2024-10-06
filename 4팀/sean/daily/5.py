import json

def solution(input_list):
    n = len(input_list)
    if n % 2 != 0:
        return []
    config = {}
    for i in range(0, n, 2):
        key = input_list[i]
        value = input_list[i+1]
        config[key] = value

    resolved_config = {}
    resolved = {}
    try:
        for key in config.keys():
            resolving = set()
            resolved_value = resolve(config, key, resolving, resolved)
            resolved_config[key] = resolved_value
    except Exception:
        return []
    output = []
    for key in sorted(resolved_config.keys()):
        output.append(key)
        output.append(resolved_config[key])
    return output

def resolve(config, key, resolving, resolved):
    if key in resolved:
        return resolved[key]
    if key in resolving:
        raise Exception('Cycle detected')
    resolving.add(key)
    value = config.get(key, '')
    import re
    pattern = re.compile(r'\{([^{}]*)\}')
    while True:
        matches = pattern.findall(value)
        if not matches:
            break
        new_value = value
        for match in matches:
            if match == key:
                raise Exception('Cycle detected')
            replacement = resolve(config, match, resolving, resolved)
            if replacement is None:
                replacement = ''
            new_value = new_value.replace('{' + match + '}', replacement)
        if new_value == value:
            break
        value = new_value
    resolving.remove(key)
    resolved[key] = value
    return value

# 테스트 입력
input_list = ["test", "{hello}", "test2", "{{test}}"]

# 결과 출력
output = solution(input_list)
print(output)