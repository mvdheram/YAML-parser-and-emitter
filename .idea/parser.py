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
        f.close()
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
            return (key,value)
            break
        else:
            continue



def Main():
    fname = "data.yaml"
parser = argparse.ArgumentParser(description='Yaml file loader and dumper for contacts')
parser.add_argument('-a','--add_name',metavar = '', help ='Name of the contact')
parser.add_argument('-ph','--phone_number',type = int,metavar = '', help = 'phone number of contact')
parser.add_argument('-c','--city',metavar = '', help ='city of contact')
parser.add_argument('-em','--email',metavar = '', help = 'email of the contact')
parser.add_argument('-sh','--show',metavar = '', help = 'show the contact')
group = parser.add_mutually_exclusive_group()
group.add_argument('-ls','--list',action = 'store_true',help = 'print  list')
group.add_argument('-v','--verbose',action = 'store_true',help = 'print verbose list ')
args = parser.parse_args()
data = add(args.add_name,args.phone_number,args.city,args.email,fname)

if args.show:
    print(show(fname,args.show))

if args.list:
    print(list(fname))
elif args.verbose:
    print ("\nlist of contacts in file name: " + fname + " are:\n\n"  + list(fname))


if __name__ == "__main__":
    Main()
