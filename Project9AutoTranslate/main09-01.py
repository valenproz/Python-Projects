import googletrans

translator = googletrans.Translator()

str1 = "como vai"
result1 = translator.translate(str1, dest='en', src='auto')
print(f"como vai => {result1.text}")

str2 = "how are you"
result2 = translator.translate(str2, dest='pt', src='en')
print(f"how are you => {result2.text}")