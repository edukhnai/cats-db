import shelve as sh

"""
	Библиотека методов для работы с даннами из БД
	Автор: Магомедов Шамиль и Духнай Екатерина
"""

cats = [["Лесная кошка", "Felis", 7, "Серо-коричневый", "Европа"],
		["Степная кошка", "Felis", 6, "Серый", "Азия"],
		["Каракал", "Caracal", 20, "Песочный", "Африка"],
		["Калимантанская кошка", "Catopuma", 4.5, "Коричневый", "Калимантан"],
		["Ириомотейская кошка", "Felis", 3, "Коричневый", "Япония"],
		["Онцилла", "Leopardus", 2.8, "Охристый", "Южная Америка"],
		["Ягуарунди", "Herpailurus", 9, "Рыжий", "Южная Америка"],
		["Кошка Жоффруа", "Oncifelis", 4.2, "Охристый", "Южная Америка"],
		["Андская кошка", "Oreailurus", 4, "Серебристо-серый", "Анды"],
		["Дымчатый леопард", "Neofelis", 20, "Светло-желтый", "Азия"],
		["Лев", "Panthera", 190, "Темно-золотой", "Африка"],
		["Пума", "Puma", 100, "Желто-бурый", "Африка"],
		["Леопард", "Panthera", 70, "Золотистый", "Азия"],
		["Бенгальский кот", "Prionailurus", 8, "Серо-желтый", "Азия"],
		["Рысь", "Lynx", 15, "Рыжий", "Сибирь"],

		["Сервал", "Leptailurus", 18, "Желтый", "Северная Африка"],
		["Оцелот", "Leopardus", 10, "Песчаный", "Южная Америка"],
		["Манул", "Otocolobus", 4.5, "Желтый", "Азия"],
		["Суматранская кошка", "Prionailurus", 2.1, "Коричневый", "Океания"],
		["Африканская золотая кошка", "Profelis", 11, "Золотой", "Африка"],
		["Кошка Темминка", "Catopuma", 12.3, "Коричневый", "Азия"],
		["Китайская кошка", "Felis", 9, "Песочный", "Китай"],
		["Маргай", "Leopardus", 3, "Коричнево-желтый", "Северная Америка"],
		["Пампасская кошка", "Oncifelis", 8, "Желтовато-серый", "Южная Америка"],
		["Онза", "Puma", 27, "Темно-рыжий", "Мексика"],
		["Тигр", "Panthera", 300, "Рыжий", "Азия"],
		["Ягуар", "Panthera", 100, "Темно-рыжий", "Южная Африка"],
		["Гепард", "Acinonyx", 50, "Песочный", "Африка"],
		["Снежный барс", "Uncia", 70, "Дымчатый", "Средняя Азия"],
		["Мраморная кошка", "Pardofelis", 3, "Коричневый", "Азия"]]

fields = ['name', 'genus', 'weight', 'colour', 'habitat']
db_path = '../Data/data'
count_field = 'count'


def create_db_from_dict(cats, db_name):
	"""
		Создает БД (db_name) из словаря (cats)
		Параметры: dict cats, str db_name
		Автор: Магомедов Шамиль
	"""
	db = sh.open('../Data/' + db_name)
	index = 0
	for cat in cats:
		db[str(index)] = cats[cat]
		index += 1
	db[count_field] = index
	db.close()


def from_txt_to_db(file_path, db_name):
	"""
		Записыввает котов из файла (file_path) в файл базы данных с именем db_name
		Параметры: str file_path, str db_name
		Автор: Духнай Екатерина
	"""
	file = open(file_path, 'r')
	db = sh.open('../Data/' + db_name)
	index = 0
	for line in file:
		db[str(index)] = dict(zip(fields, line.rstrip('\n').split(' | ')[1:]))
		index += 1
	db[count_field] = str(index)
	db.close()


def from_ls_to_dict(cats_list):
	"""
		Преобразовывает список котов в словарь котов
		Параметры: list cats_arr
		Автор: Магомедов Шамиль
	"""
	cats_dict = {}
	for index in range(len(cats_list)):
		cats_dict[index] = dict(zip(fields, cats_list[index]))
	return cats_dict


def print_dict_to_txt(file_name, cats_dict):
	"""
		Записыввает словарь котов в файл [file_name].txt
		Параметры: str file_name, dict cats_dict
		Автор: Духнай Екатерина
	"""
	file = open('../Output/' + file_name + '.txt', 'w')
	for index in cats_dict:
		print("%d" % index, end='', file=file)
		for key in fields:
			print(" | %s" % cats_dict[index][key], end='', file=file)
		print(file=file)
	file.close()


def print_dict(cats_dict):
	"""
		Выводит в консоль словарь котов в правильном виде
		Параметры: dict cats_dict
		Автор: Магомедов Шамиль
	"""
	for index in cats_dict:
		print("%d" % index, end='')
		for key in fields:
			print(" | %s" % cats_dict[index][key], end='')
		print()


def print_all_db(db_path):
	"""
		Выводит в консоль базу данных из db_path
		Параметры: str db_path
		Автор: Духнай Екатерина
	"""
	database = sh.open(db_path)
	for item in database:
		if item != count_field:
			print('-' * 4 + item + '-' * 4)
			for field in database[item]:
				print(str(field) + ' : ' + str(database[item].get(field)))
			print()
	print("Cats count = " + str(database[count_field]))
	database.close()


def search(request, fields, db_path):
	"""
		Находит все совпадения запроса(request) в базе данных(db_path) в полях(fields)
		Параметры: str request, list fields, str db_path
		Возвращает: список совпадений (list)
		Автор: Магомедов Шамиль
	"""
	db = sh.open(db_path)
	matches = []
	for key in db:
		for field in db[key]:
			if field in fields and key not in matches:
				if db[key].get(field).lower().find(request.lower()) != -1:
					matches.append(db[key])
	db.close()
	return matches


def get_cats_by_weight(w1, w2, db_path):
	"""
		Возвращает список котов удовлетворяющих условию: вес
		Параметры: int w1, int w2, str db_path
		Возвращает: список котов (list)
		Автор: Магомедов Шамиль
	"""
	db = sh.open(db_path)
	matches = []
	count = 0
	for item in db:
		if item != count_field:
			# fields[2] - название поля, которое хранит вес кота
			if w1 <= int(db[item][fields[2]]) <= w2:
				matches.append(db[item])
				count += 1
	#	matches.append(count)
	# тут кароч как нить куда нить надо будет запихнуть count, мб сделаю список из списка и int
	db.close()
	return matches


def get_count(db_path):
	"""
		Получает из базы данных (db_path) количество котов
		Параметры: str db_path
		Возвращает: количество котов(int)
		Автор: Духнай Екатерина
	"""
	db = sh.open(db_path)
	count = db[count_field]
	db.close()
	return count


def get_dict_from_db(db_path):
	"""
		Получает из базы данных (db_path) словарь котов
		Параметры: str db_path
		Возвращает: словарь котов(list)
		Автор: Духнай Екатерина
	"""
	dict = {}
	database = sh.open(db_path)
	for item in database:
		dict[item] = database[item]
	database.close()
	return dict


def sort(param, cats_list, reverse):
	"""
		Сортирует котов (cats_list) по определенному параметру (param)
		Параметры: str param, list cats_list, bool reverse
		Возвращает: отсортированный список котов(list)
		Автор: Магомедов Шамиль
	"""
	return sorted(cats_list, key=lambda cat: cat[param], reverse=reverse)


# create_db_from_dict(from_ls_to_dict(cats), 'data')
# print_dict_to_txt('out', from_ls_to_dict(cats))
# from_txt_to_db('../Output/out.txt', 'data')
# create_db_from_dict(from_ls_to_dict(cats), 'data')
# print_all_db(db_path)
# new_ls = sort(fields[1], get_cats_by_weight(4, 6, db_path), False)