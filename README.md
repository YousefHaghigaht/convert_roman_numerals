This project implements a FastAPI application that converts Roman numerals to integers. It consists of two main components: a function for converting Roman numerals and an API to handle requests.

▎Part 1: Roman Numeral to Integer Conversion

The roman_to_integer function takes a string representing a Roman numeral and returns its integer equivalent. The function uses a dictionary to map Roman numeral characters to their respective values and processes the string in reverse order to handle subtraction cases.

▎Part 2: Creating an API with FastAPI

The FastAPI framework is used to create a RESTful API. The API includes:

• An input model defined using Pydantic for data validation.

• A POST endpoint /convert/ that accepts a JSON payload with a Roman numeral and returns its integer value.

▎Installation and Running the Project

1. Install FastAPI and Uvicorn:
   Ensure that Python and pip are installed on your system. Then, run the following command to install FastAPI and Uvicorn:

   
   pip install fastapi uvicorn
   

2. Save the Code:
   Save the above code in a file named main.py.

3. Run the Server:
   Use the following command to run the server:

   
   uvicorn main:app --reload
   

4. Test the API:
   After starting the server, you can send a POST request to http://127.0.0.1:8000/convert/ using tools like Postman or curl.

   The request body should look like this:

   
   {
       "roman_numeral": "XXVII"
   }
   

   The expected output will be:

   
   {
       "integer_value": 27
   }
   
