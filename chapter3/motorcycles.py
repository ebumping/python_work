motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(1, 'harley')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")