# # Home work 3.1
# # Список.

# li = [1,2,3,4,5,6,7]

# print("li: ", li)
# print("Длина li:",len(li))

# a = int(input("Введите число:"))
# b = int(input("На какую позицию в списке втсавить?"))

# li.insert(b, a)

# print("li: ", li)

# li.pop()

# print("Удалено послденее значение списка li: ", li)


# # Home work 3.3
# # Сортировка пузырьком.

# # Через цикл for.
# li = [1,2,5,9,2,6,0]

# print("li: ",li)

# for j in range(len(li)):
#     for i in range(len(li) - 1):
    
#         if li[i] > li[i+1]:
#             li[i], li[i+1] = li[i+1], li[i]

# print("Отсортированный список li: ", li) 

# # Через цикл while.
# li = [9,4,6,1,9,2,3,4]

# while i <= len(li)+1:
#     for j in range(len(li)-1):
#         if li[j] > li[j+1]:
#             li[j], li[j+1] = li[j+1], li[j]
#     i +=1

# print("Отсортированный список li: ", li) 
