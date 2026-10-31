from google import genai

client = genai.Client()
reponse = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents="Dis bonjour en français simple.",
)
print(reponse.text)