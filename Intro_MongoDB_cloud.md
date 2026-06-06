
Code to import 01_transactions.json into your cloud database

mongoimport --uri <your_uri_link> --username  <your username> --collection tranzactions --file "01_transactions.json" --jsonArray


Code to import  Upsert Records from transactions_upsert.json 

mongoimport --uri <your_uri_link> --username  <your username> --collection tranzactions --file "01_transactions_upsert.json" --jsonArray --mode upsert --upsertFields tranzaction_id