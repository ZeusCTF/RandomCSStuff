def main(queryIP):
        
    def ipv4(IP):
        ip = IP.split('.')
        if len(ip) != 4:
            return False
        for octet in ip:
            if not octet.isdigit() or int(octet) > 255 or str(int(octet)) != octet:
                return False
        return True
        
    def ipv6(IP):

        allowed = ['a','b','c','d','e','f','A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
        ip = IP.split(':')

        if len(ip) != 8:
            return False
        
        for section in ip:
            if len(section) > 4 or len(section) < 1:
                return False
            for char in section:
                if char not in allowed:
                    return False

        return True

    if '.' in queryIP:
        
        if ipv4(queryIP):
            return "IPv4"
        else:
            return "Neither"
        
    elif ':' in queryIP:
        if ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
        
    else:
        return "Neither"

main("2001:db8:85a3:0::8a2E:0370:7334")