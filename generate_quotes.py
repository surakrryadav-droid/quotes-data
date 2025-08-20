import json
import random

# Famous seed quotes
famous_quotes = [
    {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"text": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
    {"text": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
    {"text": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"},
    {"text": "Happiness depends upon ourselves.", "author": "Aristotle"},
    {"text": "Injustice anywhere is a threat to justice everywhere.", "author": "Martin Luther King Jr."},
    {"text": "That which does not kill us makes us stronger.", "author": "Friedrich Nietzsche"},
    {"text": "I think, therefore I am.", "author": "René Descartes"},
    {"text": "The journey of a thousand miles begins with a single step.", "author": "Lao Tzu"},
    {"text": "Knowledge is power.", "author": "Francis Bacon"}
]

# Custom S Kumar quotes
s_kumar_quotes = [
    "Dreams are the sketches of our future.",
    "Your patience is the silent architect of success.",
    "Every small step is a giant leap when done consistently.",
    "Silence is sometimes louder than words.",
    "Endings are just doors to new beginnings.",
    "Smile is the cheapest gift you can give.",
    "Hope is the fuel of human life.",
    "Kindness echoes longer than fame.",
    "Courage is not absence of fear, but walking with it.",
    "Failures are footprints toward greatness."
]

quotes = []
for i in range(50000):
    if i % 10 == 0:
        quotes.append({"text": random.choice(s_kumar_quotes), "author": "S Kumar"})
    else:
        quotes.append(random.choice(famous_quotes))

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)

print("✅ quotes.json generated with", len(quotes), "quotes!")



