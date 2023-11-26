# Edit this One AI API call using our studio at https://studio.oneai.com/?pipeline=BWmA6j&share=true

import requests
api_key = 
url = "https://api.oneai.com/api/v0/pipeline"

user_input = input("Type a paragraph: ")

headers = {
  "api-key": api_key, 
  "content-type": "application/json"
}
payload = {
  "input": user_input,
  "input_type": "article",
	"output_type": "json",
  "multilingual": {
    "enabled": True
  },
  "steps": [
      {
      "skill": "sentiments"
    },
    {
      "skill": "emotions"
    }
  ],
}

r = requests.post(url, json=payload, headers=headers)
data = r.json()
print(data)
