print("Enter q for exit")
print("Enter name to add")
name_list = []

def silentFail():
    while True:
        try:
            name = input("\nEnter:- ").strip()
            if name.lower() == "q":
                break
            
            if name.isdigit():
                raise TypeError()

            if name:
                name_list.append(name)
                print("Name added successfuly")
            else:
                pass
        except KeyboardInterrupt:
            pass
    return name_list

if __name__ == "__main__":
    result = silentFail()
    print(f"Final list: {result}")


