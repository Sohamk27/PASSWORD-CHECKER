import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def read(answer, tail):
    sen = answer.text
    # print(sen)
    li = sen.split()
    password = li
    j = 0
    for i in password:
        tup = tuple(i.split(':'))
        if(tup[0] == tail):
            return tup[1]
            # print('not safe')
            # print(f'password has been hacked {tup[1]} times')
            # print(i)
            # j = 1
            # break
    return 0 


def pwnew_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #print(sha1password)
    firstfive, tail = sha1password[0:5], sha1password[5:]
    #print(firstfive)
    answer = request_api_data(firstfive)
    #print(answer)
    output = read(answer, tail)
    if output != 0:
        print(f'{password} is not safe')
        print(f'this has been hacked {output} times')
    else:
        print(f'{password} is safe to use')

    
       
   
# password = list(input('enter passwrod to be checked\n').split())
# for x in password:
#     pwnew_api_check(x)

pw = sys.argv[1:]
for item in pw:
    pwnew_api_check(item)
