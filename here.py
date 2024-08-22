import os
import pyodbc
from openai import AzureOpenAI


server = 'tasqlserver12345.database.windows.net'
database = 'Techarmy DB'
username = 'hackathon_user'
password = 'Techarmy@123!'
driver = '{ODBC Driver 17 for SQL Server}'



client = AzureOpenAI(
    api_key="b7c3314e81ac4fc191e5bb5f4aa957ee",  
    api_version="2024-05-01-preview",
    azure_endpoint="https://hackathon0000.openai.azure.com/"
)

deployment_name = 'Test'  


system_message = "You are an expert in generating SQL queries from natural language."
start_phrase = "print all the rows from Sports table where the size of the team is 7"

# Combine the system message with the user input
full_prompt = f"{system_message}\nUser: {start_phrase}\nSQL Query:"

# Send a test completion job with adjusted settings
response = client.completions.create(
    model=deployment_name,
    prompt=full_prompt,
    max_tokens=50,           
    temperature=0.2,         
    stop=[";", "\n"],        
    frequency_penalty=0.0,   
    presence_penalty=0.6     
)


print('Input - '+start_phrase )
print('Output - '+response.choices[0].text)
