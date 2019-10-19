def multi_assert(*args,tp):
    ls = []
    for arg in args:
        ls.append(isinstance(arg,tp))
    return False if False in ls else True

