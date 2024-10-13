from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


def roman_to_integer(roman):

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M':1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


app = FastAPI()


class RomanInput(BaseModel):
    roman_numeral: str


@app.post('/convert/')
async def convert_roman_to_integer(input:RomanInput):
    roman_numeral = input.roman_numeral

    if not all(char in 'IVXLCDM' for char in roman_numeral):
        raise HTTPException(status_code=400,detail='Invalid Roman numeral')

    integer_value = roman_to_integer(roman_numeral)

    return {'integer_value': integer_value}
