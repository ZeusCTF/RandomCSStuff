def main(emails):
    res = []
    for email in emails:
        email = email.split('@')
        user = email[0].replace('.','')
        user = user.split('+')
        e = user[0]  + '@' + email[-1]
        res.append(e)
    
    print(set(res))


main(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])