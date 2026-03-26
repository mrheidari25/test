import os
import sys

#ignore this comment#Reza commented the following since it fails
from google import genai

#Reza added the following since it works better
#import google.generativeai as genai #Reza commented his own command

# Pass the gemini api key
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)
print("\nReza shows GEMINI_API_KEY= ",api_key)

prompt = sys.stdin.read() # Expects a git diff
print("\nReza shows PROMPT= ",prompt)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Create a concise summary in markdown format of the following git diff of a pull request: \n" + prompt
)

summary = response.text
print("Reza .... summary",summary)

print("\nReza exits summary ...\n\n")
print("Reza....\n\n\n")
exit(0)

# Strip the response from a surrounding markdown code block
if summary.startswith("```markdown"):
    summary = summary.removeprefix("```markdown").strip()
elif summary.startswith("```"):
    summary = summary.removeprefix("```").strip()

if summary.endswith("```"):
    summary = summary.removesuffix("```").strip()

print(summary)
