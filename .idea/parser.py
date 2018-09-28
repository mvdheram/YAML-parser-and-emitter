import yaml
import argparse

#open a file and dump yaml
def dump(fname,data):
    with open(fname, "w") as f:
        dump = yaml.safe_dump(data, f,default_flow_style=False)
        f.close()
        return dump
#load a file and return a python object of dictionary
def load(fname):
    with open(fname) as f:
        data = yaml.safe_load(f)
        #f.close()
        return data

#add new data to file
def add(Nname,phnumber,city,email,fname):
    data = load(fname)
    data[Nname] ={"phone_number" : phnumber, "city" : city, "Email": email }
    dump(fname,data)

#list the contents of a file
def list(fname):
    with open(fname,'r') as f:
        return (f.read())

#search and print contact
def show(fname,fdata):
    data = load(fname)
    for key,value in data.items():
        if fdata == key :
            print (key,value)
            break
        else:
            continue



def Main():
    fname = "C:\Proj\YAML-parser-and-emitter\.idea\data1.yaml" #filepath to load from or dump to
    dct1 = {"kimum": {"phone_number": 3, "city": "Karvina","Email":"kim@x-uni.com"}, "Davidum": {"phone_number": 33, "city": "Brno","Email":"d@uni.de"}}
    parser = argparse.ArgumentParser(description='Yaml file loader and dumper for contacts')
    parser.add_argument('-n','--name',metavar = '',required = True, help ='Name of the contact')
    parser.add_argument('-ph','--phone_number',type = int,metavar = '',required = True, help = 'phone number of contact')
    parser.add_argument('-c','--city',metavar = '',required = True, help ='city of contact')
    parser.add_argument('-em','--email',metavar = '',required = True, help = 'email of the contact')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q','--quite',action = 'store_true',help = 'print quite')
    group.add_argument('-v','--verbose',action = 'store_true',help = 'print verbose')
    args = parser.parse_args()
    add(args.name,args.phone_number,args.city,args.email,fname)
    if args.quite :
        print (list(fname))
    elif args.verbose:
        print ("\nlist of contacts in file name: " + fname + " are:\n\n"  + list(fname))
    else:
        print ("\nlist :\n\n" + list(fname))


if __name__ == "__main__":
    Main()
    # dump(fname, dct1)
    # load(fname)
    print (list(fname))
    show(fname,"kimum")
