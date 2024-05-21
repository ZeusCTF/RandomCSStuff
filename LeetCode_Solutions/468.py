def main(queryIP):

    def ipv4(IP):
        IP += '.'
        s = ''
        for byte in IP:
            if byte != '.':
                s += byte
            else:
                count += 1
                if s.isdigit() and int(s) >= 0 and int(s) < 255:
                    print('valid octet')
                    print(s)
                    s = ''
                else:
                    print('wack')
                    return False
        
            
    def ipv6(IP):
        pass


    if '.' in queryIP:
        ipv4(queryIP)
    if ':' in queryIP:
        ipv6(queryIP)


#main('12c.0.0.1')

def test(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    for octet in ip:
        if octet.isdigit() and octet >= 0 and octet < 255:


test("192.168.1.1")