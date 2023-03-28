import pytest
from main import check_same_elems


@pytest.mark.parametrize('arr1, arr2, result', [
    (["elem1", "elem2", "elem3", "elem4"], ["elem5", "elem1", "elem3", "elem2"], ["elem1", "elem2","elem3"]),
     ([1, 2, 4], [5, 6, 1], [1]),
])
def test_check_same_elems(arr1, arr2, result):
    expected = check_same_elems(arr1, arr2)
    assert expected == result