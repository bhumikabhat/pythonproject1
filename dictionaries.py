# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals)) 

#print(capitals.get("India"))
#print(capitals.get("Japan"))

#if capitals.get("japan"):
#    print("That capital exist")
#else:
#    print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()
#print(keys)

#for key in capitals.keys():
#    print(key)

#print(capitals)

#values = capitals.values()

#for value in capitals.values():
#    print(value)

#items = capitals.items()

#for item in capitals.items():
#   print(item)

for key, value in capitals.items():
    print(f"{key}: {value}")