geography= {"continets": ["North America", "South America", "Africa", "Antarctica", "Australia", "Asia", "Europe"]}

geography["oceans"] = ["Pacific", "Atlantic", "Indian", "Arctic"]
print(geography)

patient= {"name": "John Doe", "age": 25, "height": 64, "symptoms": "cough" }
patient["height"] = 72
print(patient)

print(patient.items())


print(patient.get("name"))


print(patient.get("weight", 150))


patient.clear()
print(patient)
