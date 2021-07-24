import json
import csv


json_list = []
user_count = 0
book_count = 0
list_of_all_books = []


class ObjectIterator:
    def __init__(self, itter_object, counter):
        self.counter = counter
        self.iter_object = iter(itter_object)

    def return_object_by_counter(self):
        asd = []
        step_cout = 0
        while step_cout < self.counter:
            asd.append(next(self.iter_object))
            step_cout += 1
        return asd

    def set_count(self, new_value):
        self.counter = new_value


with open("files/users.json", "r", encoding="utf-8") as f:
    text = json.load(f)
    for i in text:
        user_dict = {}
        user_count += 1
        user_dict.update(name=i["name"])
        user_dict.update(gender=i["gender"])
        user_dict.update(address=i["address"])
        user_dict.update(age=i["age"])
        json_list.append(user_dict)
    f.close()


with open("files/books.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, restkey="data")
    for row in reader:
        book_count += 1
        del row["Publisher"]
        key_list = [x.lower() for x in row.keys()]
        value_list = [x for x in row.values()]
        key_list.append(key_list.pop(2))
        value_list.append(value_list.pop(2))
        a = dict(zip(key_list, value_list))
        book_dict = {key.lower(): value for key, value in row.items()}
        book_dict.update({"genre": book_dict["genre"]})
        list_of_all_books.append(book_dict)
    f.close()
users_who_have_more_book = book_count % user_count
min_count_of_book = int((book_count - users_who_have_more_book) / user_count)
min_users_with_books = ObjectIterator(list_of_all_books, min_count_of_book + 1)
for i in json_list:
    if users_who_have_more_book != 0:
        i["books"] = min_users_with_books.return_object_by_counter()
        users_who_have_more_book -= 1
    else:
        min_users_with_books.set_count(min_count_of_book)
        i["books"] = min_users_with_books.return_object_by_counter()
with open("result.json", "w") as f:
    json.dump(json_list, f, indent=4)
    f.close()
