from pytest import mark

from src.constants import Constants


@mark.parametrize(
    "input, expected", [
        # snake case should be converted to camel case
        ("snake_case", "snakeCase"),
        ("camelCase", "camelCase")
    ]
)
def test_to_camel_case_given_string_value_returns_string_in_camel_case(
    input,
    expected
):
    assert Constants.snake_to_camel_case(input) == expected
