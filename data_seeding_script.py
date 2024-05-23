from frappeclient import FrappeClient
from frappe import log_error
from decouple import config # for protecting the credentials I used python-decouple
from configurator import configurator
# protecting the credentials
#server 1
#3server1 = str(input("Enter the source server name: "))
server1_username = config("SERVER1_USERNAME")
server1_password = config("SERVER1_PASSWORD")
#server 2
#server2 = str(input("Enter the destination server name: "))
server2_username = config("SERVER2_USERNAME")
server2_password = config("SERVER2_PASSWORD")
# http://development.localhost:8000
# http://development2.localhost:8000

# openning connection with the server 1
conn = FrappeClient("http://development.localhost:8000", server1_username, server1_password)


# openning connection with the server 2
conn2 = FrappeClient("http://development2.localhost:8000", server2_username, server2_password)

def process_configurator():
    result_set = []
    for conf in configurator:
        fetch_insert_data_set(conf, result_set)

def fetch_insert_data_set(conf, result_set):
        documents = conn.get_list(conf["doctype"], fields=conf["fields"])             # getting the list of all the documents of all the doctypes
        for doc in documents:                             # looping through all the documents of all the doctypes
            doc["doctype"] = conf["doctype"]                  # setting the doctype to it's type
            doc_already_exists = conn2.get_value(conf["doctype"], {"name": doc["name"]})
            doc_already_exists_name = conn2.get_value(conf["doctype"], {"name": doc["name"]})         # getting the name of the document that already exists
            match not doc_already_exists:
                  case True:                  # True here means if the document does not exist
                        print(conn2.insert(doc))                               # handling the duplicate documents with Match Case this feature is new in python 3.10 
                  case False:
                        doctype = conn2.get_doc(conf["doctype"], doc["name"]).get("doctype")                        # getting the doctype of the document                   # False here means if the document already exists
                        print(f"The document --{doctype}-- that you tried to insert already exists {doc_already_exists_name} in the destination server. Skipping")   # printing the message that the document already exists
            result_set.append({"Doctype": doc["doctype"], "name": doc["name"]})   # appending the doctype and the name of the document to the result_set
        







if __name__ == "__main__":
    process_configurator( )


