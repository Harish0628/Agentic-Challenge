from fastmcp import FastMCP
import requests
import os

API_key=os.environ.get("OPENWEATHER_API_KEY")

mcp = FastMCP("My MCP Server")
#------------------------MCP Server----------------------
@mcp.tool
def get_weather(city: str):

    parameters={
        "appid":API_key,
        "q":city
        }

    url="https://api.openweathermap.org/data/2.5/weather"

    response=requests.get(url=url,params=parameters)
    data= response.json()
    
    return data


if __name__=="__main__":
    mcp.run(transport="http",port=8000)

