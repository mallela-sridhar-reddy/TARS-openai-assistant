import os
import openai
from config import apikey

def ai(prompt):
  openai.api_key =apikey
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="write an email to send to my brother?",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  print(response["choices"][0]["text"])
# output
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nSubject: Miss You!\n\nHey Bro,\n\nI miss you so much! I don't think a day goes by that I don't think of you. I remember all of our fun times together and how much I look up to you. In the past few weeks, I've been thinking about all the places we could visit together in the future - when it's safe of course!\n\nI hope you're doing well and continue to stay safe. I can't wait until we can be reunited again and spend quality time together.\n\nLove you,\n\n[Your Name]"
#     }
#   ],
#   "created": 1685023170,
#   "id": "cmpl-7K5n0GpRWysAq0YNkjzggHG8VDc7l",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 123,
#     "prompt_tokens": 9,
#     "total_tokens": 132
#   }
# }