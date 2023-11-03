def solution(id_list, report, k):
    report_id = {id: [] for id in id_list}
    report_dict = {id: 0 for id in id_list}
    for re in report:
        user, reported_user = re.split(' ')
        if user not in report_id[reported_user]:
            report_dict[reported_user] += 1
            report_id[reported_user].append(user)
    result = {id: 0 for id in id_list}
    for reported_user, report_count in report_dict.items():
        if report_count >= k:
            for user in report_id[reported_user]:
                result[user] += 1
    return list(result.values())