def countSeniors( details):
        res = 0
        senior = ''
        for citizen in details:
            senior = str(citizen[11]) + str(citizen[12])
            if int(senior) > 60:
                res += 1
        return res