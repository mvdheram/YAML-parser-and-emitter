import yaml
import argparse

#open a file and dump yaml
def dump(fname,data):
    with open(fname, "w") as f:
        dump = yaml.dump(data, f,default_flow_style=False)
        return dump

#add new data to file
#def add(fname,arg.name,arg.phone_number,arg.city,arg.email):
    newdata = load(fname)
    newdata[arg.name]={"phone_number" : arg.phone_number,"city":arg.city,"Email":arg.email}
    dump(fname,newdata)

#load a file and return a python object
def load(fname):
    with open(fname) as f:
        data = yaml.load(f)
        return data

#list the contents of a file
def list(fname):
    with open(fname,'r') as f:
        print(f.read())

#search and print contact
def show(fname,fdata):
    data = load(fname)
    for key,value in data.items():
        if  fdata in key :
            print (str(value))



def Main():
    fname = "C:\Proj\YAML-parser-and-emitter\data1.yaml" #filepath to load from or dump to
    dct1 = {"kimum": {"phone_number": 3, "city": "Karvina","Email":"kim@x-uni.com"}, "Davidum": {"phone_number": 33, "city": "Brno","Email":"d@uni.de"}}
    #parser = argparse.ArgumentParser(description='Yaml file loader and dumper for contacts')
    #parser.add_argument('-n','--name',type = string, help ='Name of the contact')
    #parser.add_argument('-ph','--phone_number',type = int, help = 'phone number of contact')
    #parser.add_argument('-c','--city',type = string, help ='city of contact')
    #parser.add_argument('-em','--email',type= string, help = 'email of the contact')
    #args = parser.parse_args();
    dump(fname, dct1)
    load(fname)
    list(fname)
    show(fname,"Davidum")


if __name__ == "__main__":
    Main()
