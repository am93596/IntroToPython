# Dictionaries

# Dictionary = Key-Value Pairs

sre = {
    "course name": "Deloitte SRE",
    "length": 12,
    "trainees": ["Ioana", "Kieron", "William"],
    "topics": ("Linux", "Python"),
    "outline": {
        "Week 1": "Business Week",
        "Week 2": "Linux",
        "Week 3": "Python"
    }
}

print(sre)
print(sre.keys())
print(sre.values())
print(sre.items())

print("length" in sre)
print(12 in sre.values())
