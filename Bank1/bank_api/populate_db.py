import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V9ba12r#",
    database="now"
)

cursor = db.cursor()

clients = range(1, 11)
products = [
    ('Сберегательный счет', random.randint(1, 10)),
    ('Кредитная карта', random.randint(1, 10)),
    ('Ипотека', random.randint(1, 10)),
    ('Автокредит', random.randint(1, 10)),
    ('Потребительский кредит', random.randint(1, 10)),
]

for client in clients:
    random_products = random.sample(products, 3)
    for product, score in random_products:
        cursor.execute(
            "INSERT INTO clientrecommendations (client_id, product_name, recommendation_score) VALUES (%s, %s, %s)",
            (client, product, score)
        )

db.commit()
cursor.close()
db.close()