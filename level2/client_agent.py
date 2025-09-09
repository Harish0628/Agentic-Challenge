import asyncio
from fastmcp import Client
from google import genai
from google.genai import types

#----------------------------------------------------------------------------------
client_mcp = Client("http://127.0.0.1:8000/mcp")

async def call_tool(city: str):
    async with client_mcp:
        result = await client_mcp.call_tool("get_weather", {"city": city})
        return str(result) 

#----------------------------------------------------------------------------------
prompt=input("Enter the prompt: ")

client_llm = genai.Client()

response = client_llm.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_mime_type="application/json",   
        response_schema={
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    )
)

city=response.text[10:len(response.text)-2]

weather_data=asyncio.run(call_tool(city=city))
data_bytes=weather_data.encode("UTF-8")
#----------------------------------------------------------------------------------
response1 = client_llm.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(
            data=data_bytes,
            mime_type="text/plain"   
        ),
        prompt+" Mention source(API,json file etc)"
    ]
)

print("AI Response:\n",response1.text)