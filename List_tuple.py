# List index
def main():
    list1 = [10, 20, 30, 30, 40]

    print(f"list: {[list1]}")

    print(f"\n list index ke 0: {list1[0]}")
    print(f"list index ke 2: {list1[2]}")
    print(f"list index ke 4: {list1[4]}")

    # Melihat posisi data berdasarkan index
    print(f"Data posisi 10: {list1.index(10)}")
    print(f"Data posisi 30: {list1.index(30)}")
    print(f"Data posisi 40: {list1.index(40)}")

if __name__ == "__main__":
    main()

# List Insert
def main():
    list1 = [10, 30, 20, 50, 60]

    print(f"Before {list1}")

    # Menambahkan items baru ke dalam list ke index 2
    list1.insert(2, 500)
    print("\nAfter Add")
    print("===========================================")
    print(f"The Result: {list1}")

if __name__ == "__main__":
    main()

# List Append
def main():
    # List
    list1 = [90, 20, 40, 30, 50, 60, 100]

    print(f"==== Before ====")
    print(list1)

    # Add new items to the list
    list1.append(400)
    list1.append(9000)
    list1.insert(2, 676767)
    list1.insert(5, 3030)
    list1.extend(1000, 1)

    print("\n==== After ====")
    print(list1)

# First program
if __name__ == "__main__":
    main()