#----------------Importing modules----------------
from google import genai
from google.genai import types

#----------------Seting up client----------------
client=genai.Client() 


#----------------Getting Response----------------
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain about bits pilani in 3 lines",

)
print(response.text)

