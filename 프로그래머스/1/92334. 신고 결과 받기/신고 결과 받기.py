def solution(id_list, report, k):
    report = set(report)
    
    reported_count = {}
    for r in report:
        reporter, reported = r.split()
        
        if reported not in reported_count:
            reported_count[reported] = 1
        else:
            reported_count[reported] += 1
    
    suspended = []
    for user in reported_count:
        if reported_count[user] >= k:
            suspended.append(user)
    
    mail_count = {}
    for user in id_list:
        mail_count[user] = 0
    
    for r in report:
        reporter, reported = r.split()
        if reported in suspended:
            mail_count[reporter] += 1
    
    result = []
    for user in id_list:
        result.append(mail_count[user])
    
    return result
