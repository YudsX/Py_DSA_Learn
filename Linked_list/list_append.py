list4 = [10,20,30]

print("Sebelum ditambah")
print("List:",  list4)


list4.append(40)
list4.append(50)

list4.insert(1, 15)
list4.insert(2, 25)
list4.insert(3, 17)

list4.extend((45, 55))

print("\nsetelah Ditambah")
print("list4: ", list4)