def size_unit(size: int) -> str:
    if size >= 1000:
        return "kb"
    else:
        return "bytes"