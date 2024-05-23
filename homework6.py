my_list = ["Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун"]
print("List:", my_list)
print("First element:", my_list[0], "\nLast element:", my_list[-1])
print("Sublist:", my_list[3:5])
my_list[3] = "Плутон"
print("Modified list:", my_list, "\n")

my_dict = {"Russia": "Moscow", "Japan": "Tokyo", "USA": "Washington", "China": "Beijing"}
print("Dictionary:", my_dict)
print("Capital:", my_dict["Russia"])
my_dict.update({"Germany": "Berlin"})
print("Modified dictionary:", my_dict)
