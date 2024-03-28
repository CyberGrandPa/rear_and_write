# 1 часть задания
def get_cook_book_from_file():
        
    cook_book ={}

    with open (r"E:\питон\ДЗ\чтение и запись в файл\Cook_Book\recipes.txt", "r", encoding="UTF-8") as f:
    
        for row in f:
    
            if not row.strip():
                return
            dish_name =  row.strip() 
            quantity_ingradients = int(f.readline().strip())
            ingradients = []      
            for item in range(quantity_ingradients):
                ingradient_dict = {}
                ingradient_list = f.readline().strip().split(' | ')
                ingradient_dict['ingredient_name'] = ingradient_list[0]
                ingradient_dict['quantity'] = float(ingradient_list[1])
                ingradient_dict['measure'] = ingradient_list[2]
                ingradients.append(ingradient_dict)
            cook_book[dish_name ] = ingradients
            f.readline()
    return cook_book
cook_book = get_cook_book_from_file()
print(cook_book)
print("*" *60)


# 2 часть задания

def get_shop_list_by_dishes(dishes,person_count):
    cook_book = get_cook_book_from_file()
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            continue
        for item in cook_book[dish]:
           if item ["ingredient_name"] not in shop_list:
            shop_list[item["ingredient_name"]] = {'measure': item['measure'],'quantity': (int(item['quantity']) * person_count)}
           else:
            shop_list[item["ingredient_name"]]['quantity'] += (int(item['quantity']) * person_count)
            
           
    print(shop_list)          
dish_list = ['Омлет','Фахитос']           
get_shop_list_by_dishes(dish_list,5)          






    