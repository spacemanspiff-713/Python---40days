def get_temp():
    with open("bounus_examples/2.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i.strip("\n")) for i in values]
    return values

temp_data = get_temp()
print(temp_data)