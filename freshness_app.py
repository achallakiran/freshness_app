from datetime import date
from datetime import datetime

if __name__=="__main__":

    today = date.today()
    current_date = today.strftime("%Y-%m-%d")
    transaction_file_path="transaction.csv"
    product_file_path="product.csv"
    product_dict={}


    cust_name=input("Log in name: ")
    txn_list=open(transaction_file_path,"r")
    product_list=open(product_file_path,"r")

    for product in product_list:
        product_col_list=product.split("|")
        #print(product_col_list)
        product_name=product_col_list[0]
        product_expiry_day_cnt=int(product_col_list[1].strip())

        product_dict[product_name]=product_expiry_day_cnt

    for txn in txn_list:
        txn_col_list=txn.split("|")
        txn_cust_name=txn_col_list[0]
        txn_product_name=txn_col_list[1]
        txn_date=txn_col_list[2].strip()

        if product_dict.get(txn_product_name):
            days_elapsed=(datetime.strptime(current_date, '%Y-%m-%d').date()-datetime.strptime(txn_date, '%Y-%m-%d').date()).days
            if days_elapsed<product_dict.get(txn_product_name):
                print ("Your " + txn_product_name + " will expire in " + str(abs(days_elapsed-product_dict.get(txn_product_name))) + " days!")
            elif days_elapsed==0:
                print ("Your " + txn_product_name + " will expire today!")
            else:
                print ("Your " + txn_product_name + " expired " + str(abs(days_elapsed-product_dict.get(txn_product_name))) + " days ago!")
