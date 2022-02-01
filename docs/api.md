
# Kalkulators Applikation programming interface (API)

## Eksempel

```python

from typing import (
    Callable,
    Tuple,
    Union,
)

import kalk


def options(line: str) -> Tuple[Callable, List[float]]:
    first, *remaining = line.strip().split()
    operation = getattr(kalk, first)
    arguments = [float(a) for a in remaining]
    return operation, arguments


def main():
    with open('tal.dat', encoding='utf-8') as f:
        lines = f.read().splitlines()

    prepared = (options(line) for line in line)
    for operation, arguments in prepared:
        print(operation, operation(*arguments))

```
