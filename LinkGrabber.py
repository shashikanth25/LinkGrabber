import urllib.request
import re
def main():
    i=1;  
    print("hello \n")
    ass=urllib.request.urlopen("https://python.org")
    hulk=ass.read().decode('utf-8')
    links=re.findall('"((https|http)://.*?)"', hulk)
    for i in links:
        print(i) 
        print("\n") 

main()


