def main():
    list1 = [10, 20, 30, 20, 10, 10]

    print("list1: ", list1)

    #menghitung banyaknya elemen 10
    list1.count(10)
    #menghitung banyaknya elemen 20
    list1.count(20) 
    #menghitung banyaknya elemen 30
    list1.count(30)

    print("\nlist1.count(10): ", list1.count(10))
    print("list1.count(20): ", list1.count(20))
    print("list1.count(30): ", list1.count(30))

if __name__ == "__name__":
    main()