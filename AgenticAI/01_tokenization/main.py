import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")
my_prompt = "Hey my name is Vaibhav Sharma , how are you ?"


encodedText =encoder.encode(my_prompt)
print("Encoded Text", encodedText)


decode = encoder.decode(encodedText)

print("Decoded Message : - "+ decode)

