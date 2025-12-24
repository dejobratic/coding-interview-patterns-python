from typing import Any, cast


def assert_lists_equivalent(actual: Any, expected: Any) -> None:
    """Assert that two structures are equivalent with order-insensitive comparison.

    Compares lists using multiset semantics at all nesting levels:
    - [1, 2, 3] == [3, 1, 2]
    - [[1, 2], [3, 4]] == [[3, 4], [1, 2]]
    - [[2, 1], [4, 3]] == [[1, 2], [3, 4]]

    Args:
        actual: The actual value from the test
        expected: The expected value to compare against

    Raises:
        AssertionError: If the structures are not equivalent
    """
    def _canonicalize(obj: Any) -> Any:
        if isinstance(obj, list):
            return tuple(sorted(_canonicalize(i) for i in obj))  # type: ignore
        return obj

    canonical_actual = _canonicalize(actual)
    canonical_expected = _canonicalize(expected)

    assert canonical_actual == canonical_expected, (
        f"Lists not equivalent:\n"
        f"  Actual:   {actual}\n"
        f"  Expected: {expected}"
    )


def to_list(obj: Any) -> list[Any]:
    """Convert various list-like structures to a Python list.

    Handles:
    - Regular Python lists (returns as-is)
    - Linked lists (converts by traversing nodes)
    - Other iterables (converts via list())

    Args:
        obj: A list-like structure or iterable

    Returns:
        A Python list containing the values
    """
    if obj is None:
        return []

    if hasattr(obj, 'val') and hasattr(obj, 'next'):
        result: list[Any] = []
        current = obj
        while current:
            result.append(current.val)
            current = current.next
        return result

    if isinstance(obj, list):
        return cast(list[Any], obj)

    return list(obj)
