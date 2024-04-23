import pytest
from src.widget import mask_info, convert_date

@pytest.mark.parametrize("x, answer", [("Maestro 1596837868705199", "Maestro 159683******5199")])
def test_mask_info(x, answer):
    assert mask_info(x) == answer
