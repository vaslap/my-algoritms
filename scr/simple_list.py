# Простой пример списка в Python
# Автор: [Лапунов В.К.]

my_list = [1, 2, 3, 4, 5]

print("Весь список:", my_list)
print("Первый элемент:", my_list[0])
print("Последний элемент:", my_list[-1])
print("Длина списка:", len(my_list))

# Добавление элемента
my_list.append(6)
print("После добавления 6:", my_list)

# Удаление элемента
my_list.remove(3)
print("После удаления 3:", my_list)
