import frappe
from frappeclient import FrappeClient
from frappe import log_error
from decouple import config # for protecting the credentials I used python-decouple
from configurator import configurator
# protecting the credentials
#server 1
server1 = str(input("Enter the source server name: "))
server1_username = config("SERVER1_USERNAME")
server1_password = config("SERVER1_PASSWORD")
#server 2
server2 = str(input("Enter the destination server name: "))
server2_username = config("SERVER2_USERNAME")
server2_password = config("SERVER2_PASSWORD")
# http://development.localhost:8000
# http://development2.localhost:8000

# openning connection with the server 1
conn = FrappeClient(server1, server1_username, server1_password)


# openning connection with the server 2
conn2 = FrappeClient(server2, server2_username, server2_password)

def process_configurator():

    result_set = []

    for conf in configurator:

        fetch_insert_data_set(conf, result_set)







def getting_the_link_fields(doc):

    method = "baraka_customization.api_test.our_custom_get_doc"

    document_doctype = conn.get_doc(doc["doctype"], doc["name"])

    meta_doctype = conn.post_api(method, {"doctype": document_doctype.get("doctype")})


    doc_already_exists = conn2.get_value(document_doctype.get("doctype"), {"name": doc["name"]})

    if document_doctype and meta_doctype:

        there_is_link_fields = [field for field in meta_doctype.get("fields") if field.get("fieldtype") == "Link"]


    for field in there_is_link_fields:
        field_parent = conn2.get_doc(field.get("parent"), doc["name"])
        if field_parent:
            the_parent_field_value = field_parent.get(field.get("fieldname"))

            match not the_parent_field_value, not doc_already_exists:

                case True, True:
                    print(conn2.insert(doc))

                case False, False:
                    print(f"The doctype --- {field.get('parent')} --- that have link field --- {field.get('fieldname')} --- you tried to insert already exists --- {the_parent_field_value} --- in the destination server. Skipping")
                    print("-------------------------------------------------------------------------------------------------")
                    doctype = conn2.get_doc(doc["doctype"], doc["name"]).get("doctype")                                         
                    print(f"The document --- {doc_already_exists} --- that it's doctype --- {doctype} --- that you tried to insert already exists in the destination server. Skipping")
                    print("-------------------------------------------------------------------------------------------------")
                    print("-------------------------------------------------------------------------------------------------")
                    print("-------------------------------------------------------------------------------------------------")
                    print("-------------------------------------------------------------------------------------------------")
                    print("-------------------------------------------------------------------------------------------------")

                case True, False:
                    doctype = conn2.get_doc(doc["doctype"], doc["name"]).get("doctype")                                         
                    print(f"The document --- {doc_already_exists} --- that it's doctype --- {doctype} --- that you tried to insert already exists in the destination server. Skipping")







def fetch_insert_data_set(conf, result_set):
        
    documents = conn.get_list(conf["doctype"], fields=conf["fields"])

    for doc in documents:


        doc["doctype"] = conf["doctype"]

        doc_already_exists = conn2.get_doc(doc["doctype"], doc["name"])

        match doc_already_exists is not None: 
                                        
            case None:                  
                print(conn2.insert(doc))  

            case _:                     
                getting_the_link_fields(doc)

            


    result_set.append({"Doctype": doc["doctype"], "name": doc["name"]})   
        







if __name__ == "__main__":
    process_configurator( )


