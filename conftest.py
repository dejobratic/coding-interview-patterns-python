from typing import Any


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
