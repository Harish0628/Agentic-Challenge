#----------------Importing modules----------------
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig

#----------------Calling a client----------------
client=genai.Client() 

prompt=input("Enter a prompt: ")
#----------------Getting Response----------------
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="text/plain"
    )

)
print("Response: \n",response.text)

