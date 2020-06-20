# import json

# data = json.loads(
# """
# {"colors":
#     [
#         {
#             "color": "black",
#             "category": "hue",
#             "type": "primary",
#             "code":
#                 {
#                     "rgba": [255, 255, 255, 1],
#                     "hex": "#000"}
#                 }
#     ]
# }""")
# # print(data["colors"][0]["color"])
# # print(data["colors"][0]["code"]["rgba"][0])
# # print(data["colors"][0]["code"]["hex"])

# # black
# # 255
# # 000

# # Вот пример JSON, который возвращает вк апи по страничке: Выведите:

# # ID пользователя
# # Город
# # ID страны
# # Название первой по порядку школы
# import json

# r = json.loads("""{
#     "response": [{
#             "id": 181178506,
#             "first_name": "Олег",
#             "last_name": "Галичкин",
#             "is_closed": false,
#             "can_access_closed": true,
#             "city": {
#                 "id": 2,
#                 "title": "Санкт-Петербург"
#             },
#             "country": {
#                 "id": 1,
#                 "title": "Россия"
#             },
#             "verified": 0,
#             "schools": [{
#                 "id": "187",
#                 "country": 1,
#                 "city": 2,
#                 "name": "Школа №419",
#                 "year_from": 2016,
#                 "year_to": 2018,
#                 "class": "а"
#             }, {
#                 "id": "87390",
#                 "country": 1,
#                 "city": 242,
#                 "name": "Петергофская гимназия императора Александра II (бывш. Школа № 415)",
#                 "year_from": 2007,
#                 "year_to": 2017,
#                 "type": 1,
#                 "type_str": "Гимназия"
#             }]
#     }]
#     }
# """)
# # print(str(r['response'][0]["id"])+' '+r['response'][0]["city"]["title"]+' '+str(r['response'][0]["country"]["id"])+' '+r['response'][0]["schools"][0]["name"])

# # напишите свой код тут

# import json
# t = """
# {
#     "src":
#         {
#         "12":[1,2],
#         "hf": "gl_hf", 
#         "u":[1,2,3,4,5]
#         }, 
#     "gl":
#         {
#             "hf": "gl_hf", 
#             "u":
#             [
#                 [1,2,3,4,5],
#                 {"cont":
#                     {"data":
#                     [1,2,3,4,5,6,7]
#                     }
#                 },
#                 {"conti":
#                     {
#                         "dataf":
#                         [
#                                     [
#                                         1,
#                                         [2, 3, 88], 
#                                         3, 
#                                         4, 
#                                         [2, 4, 3, 88], 
#                                         [2, 4, 3, 87], 
#                                         5, 
#                                         6, 
#                                         9
#                                     ]
#                         ]
#                     }
#                 }
#             ]
#         }
# }"""
# # items= впишите, при условии, что len(items)==9 и items[-1]==9.
# items = json.loads(t)["gl"]["u"][2]["conti"]["dataf"][0]
# result = []
# for i in items:
#     if type(i) != int and len(i) > 1 and i[2] == 3 and str(i[-1])[-1] != '8':
#         result.append(i)
# result = result[0]
# print(result)
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'car':['Lada', 'VW', 'Volga'], 'year': ['1960', '1980','1970'], 'days': [5,7,np.nan]})
df2 = pd.DataFrame({'car':['BMW','Lada','Volga'],'price':['3000$', '700$', '500$']})

pd.concat([pd.merge(df1, df2, how = "left", left_on = "car", right_on = "car"), pd.merge(df1, df2, how="right", left_on = "car", right_on = "car")], ignore_index=True)