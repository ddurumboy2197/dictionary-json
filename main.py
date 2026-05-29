import json

def dictionary_to_json(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file, indent=4)

# Misol uchun dictionary
dictionary = {
    "ism": "Ali",
    "yosh": 25,
    "viloyat": "Toshkent"
}

# Dictionaryni JSON faylga saqlash
dictionary_to_json(dictionary, "ma'lumot.json")
```

```python
import json

def json_to_dictionary(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Misol uchun JSON fayl
# ma'lumot.json:
# {
#     "ism": "Ali",
#     "yosh": 25,
#     "viloyat": "Toshkent"
# }

# JSON fayldan dictionary olish
dictionary = json_to_dictionary("ma'lumot.json")
print(dictionary)
