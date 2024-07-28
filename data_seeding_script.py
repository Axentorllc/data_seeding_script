from frappeclient import FrappeClient
from frappe import log_error
from decouple import config # for protecting the credentials I used python-decouple
from configurator import configurator
# protecting the credentials
#server 1
#server1 = str(input("Enter the source server name: "))
server1_username = config("SERVER1_USERNAME")
server1_password = config("SERVER1_PASSWORD")
#server 2
#server2 = str(input("Enter the destination server name: "))
server2_username = config("SERVER2_USERNAME")
server2_password = config("SERVER2_PASSWORD")
# http://development.localhost:8000
# http://development2.localhost:8000

# openning connection with the server 1
conn = FrappeClient('http://development.localhost:8000', server1_username, server1_password)


# openning connection with the server 2
conn2 = FrappeClient('http://development2.localhost:8000', server2_username, server2_password)

def process_configurator():

    result_set = []

    for conf in configurator:

        fetch_insert_data_set(conf, result_set)





def fetch_insert_data_set(conf, result_set):
        
        documents = conn.get_list(conf["doctype"], fields=conf["fields"])

        method = "baraka_customization.api_test.our_custom_get_doc"
        _meta = conn.post_api(method, {"doctype": "Item"})
        print("from_response", _meta)
        # for doc in documents:

        #     doc["doctype"] = conf["doctype"]

        #     print(conn.get_meta("Item"))
            

        #     doc_already_exists = conn2.get_value(conf["doctype"], {"name": doc["name"]})

        #     match not doc_already_exists: 
                                          
        #           case True:                  
        #                 print(conn2.insert(doc))  

        #           case False:                     
        #                 doctype = conn2.get_doc(conf["doctype"], doc["name"]).get("doctype")                                         
        #                 print(f"The document -- {doctype} -- that you tried to insert already exists {doc_already_exists} in the destination server. Skipping") 


        #     result_set.append({"Doctype": doc["doctype"], "name": doc["name"]})   
        







if __name__ == "__main__":
    process_configurator( )


