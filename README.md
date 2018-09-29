# YAML-parser-and-emitter

A Yaml parser & emitter for managing contacts

Operations:

1.Adding contact

2.List all the contact
  - Quite 
  - Verbose
  
3.Show a perticular contact

# CLI for YAML-Parser-emitter:

Variable : `fname` specify the file path to dump or to load from 

Usage: `parser.py [-h] [-a] [-ph] [-c] [-em] [-sh] [-ls | -v]`

Yaml file loader and dumper for contacts

optional arguments:

  -h, --help            show this help message and exit
  
  -a , --add_name       Name of the contact
  
  -ph , --phone_number  phone number of contact
  
  -c , --city           city of contact
  
  -em , --email         email of the contact
  
  -sh , --show          show the contact
  
  -ls, --list           print list
  
  -v, --verbose         print verbose list
  
  # Results:

Add:
```C:\>python parser.py -[add_name|a] Meher -[phone_number|ph] 7 -[city|c] meherabad -[email|em] gm```
 
Show: 
C:\>python test5.py --[show|sh] Meher
>>('Meher', {'Email': 'gm', 'city': 'meherabad', 'phone_number': 7})

List:
C:\t>python test5.py -[list|ls]

>>Meher:
  >> Email: gm
  >>city: meherabad
  >>phone_number: 7
>>kim:
  >>Email: null
  >>city: null
  >>phone_number: 888

Verbose:
C:\>python test5.py -[verbose|v]

>>list of contacts in file name: data.yaml are:

>>Meher:
  >>Email: gm
  >>city: meherabad
  >>phone_number: 7
>>kim:
  >>Email: null
  >>city: null
  >>phone_number: 888"
