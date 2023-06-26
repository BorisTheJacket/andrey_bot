# 1. импорт класса апи
# 1.1 запустить цикл с парамтрами
# 2. вызвать функцию get_all_contacts
# 2.1 resp['_embedded']['contacts']
# 3. положить данные в DataFrame
# 4. сохраняешь их в эксель

list_of_contacts = []

for i in range(1, 100):
    resp = api.get_all_contacts(i)
    list_of_contacts.append(resp)


    resp = self.session.get(f'{self.URL}/api/v4/contacts', params=i)
    if resp.status_code != 200:
        print(resp.status_code)
        raise Exception('Попытка загрузить пользователя по ID завершилось с ошибкой')
    return(resp.json())