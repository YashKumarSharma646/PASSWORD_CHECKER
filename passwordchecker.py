import requests
import hashlib
import sys
def request_api_data(query_check):
    url="https://api.pwnedpasswords.com/range/" + query_check
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error Fetching {res.status_code}')
    return res
    
def get_passwords_leak_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check.upper():
            return count
    return 0

def password_checker(password):
    sha1_password=hashlib.sha1(password.encode('utf-8')).hexdigest()
    first5_character,tail=sha1_password[:5],sha1_password[5:]
    response=request_api_data(first5_character)
    print(response)
    return get_passwords_leak_count(response,tail)

def main(args):
    for password in args:
        count=password_checker(password)
        if count:
            print(f"{password} was found {count} times. You should change the password.")
        else:
            print(f"This {password} has no match found. Carry on with the same password.")
if __name__=="__main__":
    sys.exit(main(sys.argv[1:]))