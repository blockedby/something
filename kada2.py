# Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. 
# For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"
def domain_name(url = "http://www.google.co.jp"):
    tLetters = list()
    url = url.split('.')
    if 'www' in url[0]:
        return url[1]
    else:
        myString = str(url[0])
        if "//" in myString:
            return myString.split("//")[1]
        else:
            return myString
    return 0
print(domain_name("https://youtube.com"))