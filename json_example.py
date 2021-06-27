import json
class Stock_detail:
    def insert_data(self,name,weight,qty):
        l=[]
        d={}
        found=0
        for i in self.data[0]["stock_detail"]:
            #found=1
            if i[0]["item_name"]==name and i[0]["item_weight"]==weight:
                found=1
                i[0]["qty"]=str(int(i[0]["qty"])+int(qty))
        if found==0:
            d["item_name"]=name
            d["item_weight"]=weight
            d["qty"]=qty
            l.append(d)
            self.data[0]["stock_detail"].append(l)
        f=open('e:/nayan project 1/stock_detail.json','w')
        f.write(json.dumps(self.data))
        f.close()
    def get_data(self,name,weight):
        for i in self.data[0]["stock_detail"]:
            if name==i[0]["item_name"] and weight==i[0]["item_weight"]:
                return i[0]
        return None
    def get_all_data(self):
        return self.data[0]["stock_detail"]
    
    
    def __init__(self):
        f = open('e:/nayan project 1/stock_detail.json')
        self.data = json.loads(f.read())
        f.close()
        #print(self.data)
class Customer_detail:
    #insert data
    def insert_data(self,name,add,pending_amount,bill_no,mob_no):
        l=[]
        d={}
        found=0
        id1="0"
        for i in self.data[0]["customer_detail"]:
            #print(i[0])
            if name==i[0]["name"]:
                found=1
                id1=i[0]["id"]
                pending_amount=str(int(pending_amount)+int(i[0]["pending_amount"]))
                bil_no=i[0]["bill no's list"]+","+bill_no
                i[0]["name"]=name
                i[0]["add"]=add
                i[0]["pending_amount"]=pending_amount
                i[0]["bill no's list"]+=","+bill_no
                i[0]["mob_no"]=mob_no
                break
            else:
                id1=i[0]["id"]
        if found==0:
            d["id"]=int(id1)+1
            d["name"]=name
            d["add"]=add
            d["pending_amount"]=pending_amount
            d["bill no's list"]=bill_no
            d["mob_no"]=mob_no
            l.append(d)
            self.data[0]["customer_detail"].append(l)
        f=open('e:/nayan project 1/customer_detail.json','w')
        f.write(json.dumps(self.data))
        #print(self.data)
        f.close()
    
    
    #get data
    def get_data(self,name):
        for i in self.data[0]["customer_detail"]:
            if name==i[0]["name"]:
                return i[0]
    def get_all_data(self):
        return self.data[0]["customer_detail"]
    
    #update data
    def update_data(self,name,add,pending_amount,mob_no):
         for i in self.data[0]["customer_detail"]:
                #print(i[0])
            if name==i[0]["name"]:
                found=1
                id1=i[0]["id"]
                pending_amount=str(int(pending_amount)+int(i[0]["pending_amount"]))
                bil_no=i[0]["bill no's list"]+","+bill_no
                i[0]["name"]=name
                i[0]["add"]=add
                i[0]["pending_amount"]=pending_amount
                i[0]["mob_no"]=mob_no
                f=open('e:/nayan project 1/customer_detail.json','w')
                f.write(json.dumps(self.data))
                #print(self.data)
                f.close()
        
    #delete data
    def delete_data(self,name):
        for i in self.data[0]["customer_detail"]:
            if i[0]["name"]==name:
                self.data[0]["customer_detail"].remove(i)
            #if name==i[0]["name"]:
        f=open('e:/nayan project 1/customer_detail.json','w')
        f.write(json.dumps(self.data))
        print(self.data)
        f.close()
        
        
    # constructor
    def __init__(self):
        f = open('e:/nayan project 1/customer_detail.json')
        self.data = json.loads(f.read())
        f.close()
        #print(self.data)

class Bill:
    #insert data
    def insert_data(self,bill_no,cid):
        l=[]
        d={}
        id1="0"
        d["bill_no"]=bill_no
        d["cid"]=cid
        d["location"]="e:/nayan project 1/"+bill_no+".pdf"
        l.append(d)
        self.data[0]["bill"].append(l)
        f=open('e:/nayan project 1/bill.json','w')
        f.write(json.dumps(self.data))
        #print(self.data)
        f.close()
        print(self.data)
    def get_new_bill_no(self):
        return int(self.data[0]["bill"][-1][0]["bill_no"])+1
     
    # constructor
    def __init__(self):
        f = open('e:/nayan project 1/bill.json')
        self.data = json.loads(f.read())
        f.close()
        #print(self.data)

'''class Buying_item:
    #insert data
    def insert_data(self,name,weight,price):
        l=[]
        d={}
        d["item_name"]=name
        d["item_weight"]=weight
        d["item_price"]=price
        l.append(d)
        self.data[0]["Buying_item"].append(l)
        f=open('e:/nayan project 1/Buying_item.json','w')
        f.write(json.dumps(self.data))
        print(self.data)
        f.close()
    
    
    #get data
    def get_qty(self,name,weight):
        count=0
        for i in self.data[0]["Buying_item"]:
            if name==i[0]["item_name"] and weight==i[0]["item_weight"]:
               count+=1
        return count
    #delete data
        
        
    # constructor
    def __init__(self):
        f = open('e:/nayan project 1/Buying_item.json')
        self.data = json.loads(f.read())
        f.close()
        #print(self.data)
                 
c=Customer_detail()
b=Bill()
b.insert_data(str(b.get_new_bill_no()),"1")
print(b.get_new_bill_no())
'''
s=Stock_detail()
s.insert_data("payjab","200","10")
print(s.data)