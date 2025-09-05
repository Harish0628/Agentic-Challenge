from pypdf import PdfReader
from google import genai
from google.genai import types
import pathlib
import UI


client=genai.Client()

path_pdf= rf"{UI.path_var}"

client = genai.Client()
filepath = pathlib.Path(path_pdf)


prompt = "What is the minimum cgpa required to pass, also format the output" 

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)