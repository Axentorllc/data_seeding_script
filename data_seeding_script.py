from frappeclient import FrappeClient
from decouple import config # for protecting the credentials I used python-decouple

# protecting the credentials
#server 1
server1_username = config("SERVER1_USERNAME")
server1_password = config("SERVER1_PASSWORD")
#server 2
server2_username = config("SERVER2_USERNAME")
server2_password = config("SERVER2_PASSWORD")
# openning connection with the server 1
conn = FrappeClient("http://development.localhost:8000", server1_username, server1_password)


# openning connection with the server 2
conn2 = FrappeClient("http://development2.localhost:8000", server2_username, server2_password)


# getting item from the server 1
item_list = conn.get_list("Item", fields=["name"])
print(item_list)
print("=======================================================================================================================================================================")
item = conn.get_doc("Item", "SKU001")
print(item)
print("=======================================================================================================================================================================")
# getting item filtered with item_group from the server 1
item_group = conn.get_list("Item", filters={"item_group": "Demo Item Group"}, fields=["name"])
print(item_group)
print("=======================================================================================================================================================================")
print("=======================================================================================================================================================================")

#getting item price from the server 1
item_price_list = conn.get_list("Item Price")
print(item_price_list)
print("=======================================================================================================================================================================")
print("=======================================================================================================================================================================")

item_price_list_by_brand = conn.get_list("Item Price", filters={"brand": "Demo Brand"}, fields=["name"])
print(item_price_list_by_brand)