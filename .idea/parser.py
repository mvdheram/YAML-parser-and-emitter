import yaml
import argparse

#open a file and dump yaml
def dump(fname,data):
    with open(fname, "w") as f:
        dump = yaml.dump(data, f,default_flow_style=False)
        return dump
#load a file and return a python object
def load(fname):
    with open(fname) as f:
        newdata = yaml.load(f)
        return newdata

def Main():
    fname = "C:\Proj\YAML-parser-and-emitter\data1.yaml"
    dct1 = {"kimum": {"phone_number": 3, "city": "Karvina","Email":"kim@x-uni.com"}, "Davidum": {"phone_number": 33, "city": "Brno","Email":"d@uni.de"}}
    dump(fname,dct)
    newdct = load(fname)
    newdct["k"] = {"phone_number": 170, "city": "Stockholm","Email":"k.k"}
    dump (fname,newdct)
    load(fname)

if __name__ == "__main__":
    Main()
