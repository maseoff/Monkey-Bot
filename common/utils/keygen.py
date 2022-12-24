import uuid


COMPLEXITY = 5


def keygen() -> str:
    return "".join([str(uuid.uuid4()) for _ in range(COMPLEXITY)])
