import pymongo
client = pymongo.MongoClient("mongodb+srv://nikhath:n777@cluster0.skblxqv.mongodb.net/?retryWrites=true&w=majority")
db = client.virtusa

records=db.superwomen

d={"name":input("enter name"),"ph":int(input("enter phone")),"mail":input("email")}
records.insert_one(d)
print("inserted successsfully")
read=records.find()
for x in read:
    print(x)