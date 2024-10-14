from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Function to convert Roman numeral to integer
def roman_to_integer(roman):

    # Dictionary to hold Roman numeral values
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


# Define a Pydantic model for input validation
class RomanInput(BaseModel):
    roman_numeral: str


# API endpoint to convert Roman numeral to intege
@app.post('/convert/')
async def convert_roman_to_integer(input:RomanInput):
    roman_numeral = input.roman_numeral

    # Validate the input Roman numeral
    if not all(char in 'IVXLCDM' for char in roman_numeral):
        raise HTTPException(status_code=400,detail='Invalid Roman numeral')

    # Convert the Roman numeral to an integer
    integer_value = roman_to_integer(roman_numeral)

    return {'integer_value': integer_value}
