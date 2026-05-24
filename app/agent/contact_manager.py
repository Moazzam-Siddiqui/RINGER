import json

with open("contacts.json", "r", encoding="utf-8") as file:
    contacts = json.load(file)

# def get_contact(name):

#     return contacts.get(
#         name,
#         {
#             "relation": "unknown",
#             "tone": "neutral"
#         }
#     )

def get_contact(name):

    name = name.lower()

    for contact_name, info in contacts.items():

        if name in contact_name.lower():

            return info

    return {
        "relation": "unknown",
        "tone": "neutral"
    }
