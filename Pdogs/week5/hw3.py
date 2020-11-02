def main():
    record_complete = False
    function_complete = False
    records = []
    user_action = []
    """ 輸入紀錄 / 項目 """
    while not record_complete or not function_complete:
        user_input = input()
        if user_input == "RECORDSTOP":
            record_complete = True
        elif user_input == "FUNCTIONSTOP":
            function_complete = True
        else:
            # 紀錄
            if not record_complete:
                data = []
                # [隊伍代號, 球員號碼, 賽季, 打數, 安打數]
                for i in user_input.split(","):
                    # EAFP coding style
                    try:
                        data.append(int(i))
                    # 隊伍代號
                    except ValueError:
                        data.append(i)
                records.append(data)
            # 項目
            else:
                data = user_input.split(" ")
                user_action.append(data)
    answer = solution(records=records, user_action=user_action)
    print(answer)


def solution(records, user_action):
    results_list = []
    for each in user_action:
        mode = int(each[0])
        seasons = [int(i) for i in each[1].split(",")]
        if mode == 1:
            result = player_avg(
                seasons=seasons, records=records, player_number=int(each[2])
            )
        elif mode == 2:
            result = team_avg(seasons=seasons, records=records, team_name=each[2])
        elif mode == 3:
            result = best_player(seasons=seasons, records=records)
        else:
            result = best_team(seasons=seasons, records=records)
        results_list.append(result)
    return "\n".join(str(i) for i in results_list)


def chop(avg):
    avg = int(avg * 100) / 100
    return avg if avg > 0 else 0


def player_avg(seasons, records, player_number):
    """ 球員打擊率 """
    # 打數
    at_bats = 0
    # 安打數
    hits = 0
    # 篩選各季該球員資料
    sub_records = list(
        filter(lambda arr: arr[1] == player_number and arr[2] in seasons, records)
    )
    for each in sub_records:
        at_bats += each[3]
        hits += each[4]
    # 打擊率 = 安打數 / 打數
    batting_average = hits / at_bats
    return chop(avg=batting_average)


def team_avg(seasons, records, team_name):
    """ 球隊打擊率 """
    at_bats = 0
    hits = 0
    # 篩選各季該隊伍資料
    sub_records = list(
        filter(lambda arr: arr[0] == team_name and arr[2] in seasons, records)
    )
    for each in sub_records:
        at_bats += each[3]
        hits += each[4]
    # 打擊率
    batting_average = hits / at_bats
    return chop(avg=batting_average)


def best_player(seasons, records):
    """ 表現最佳球員 """
    result = []
    for season in seasons:
        year_data = []
        # 篩選當季該球員資料
        sub_records = list(filter(lambda arr: arr[2] == season, records))
        for each in sub_records:
            player_number = each[1]
            at_bats = each[3]
            hits = each[4]
            batting_average = hits / at_bats
            # (打擊率, 打數, 球員號碼)
            year_data.append((batting_average, at_bats, player_number))
        # 排序: 較大打擊率 > 較小打數 > 較小球員號碼
        year_data.sort(key=lambda element: (-element[0], element[1], element[2]))
        result.append(year_data[0][2])
    return ",".join(str(i) for i in result)


def best_team(seasons, records):
    """ 表現最佳球隊 """
    result = []
    for season in seasons:
        previous_team = ""
        team_index = 0
        year_data = []
        # 篩選當季該隊伍資料, 並以隊伍名稱排序
        sub_records = sorted(list(filter(lambda arr: arr[2] == season, records)), key=lambda element: ord(element[0]))
        for each in sub_records:
            team = each[0]
            at_bats = each[3]
            hits = each[4]
            if team != previous_team:
                # 非第一筆資料
                if year_data:
                    # 更新上一隊打擊率
                    year_data[team_index].append(year_data[team_index][1] / year_data[team_index][2])
                    team_index += 1
                previous_team = team
                # 新隊伍 : [隊伍代號, 打擊率, 打數]
                year_data.append([team, hits, at_bats])
            else:
                year_data[team_index][1] += hits
                year_data[team_index][2] += at_bats
        # 更新最後一隊打擊率
        year_data[team_index].append(year_data[team_index][1] / year_data[team_index][2])
        # 排序: 較大打擊率 > 較小打數 > 較小隊伍代號
        year_data.sort(key=lambda element: (-element[3], element[2], ord(element[0])))
        result.append(year_data[0][0])
    return ",".join(str(i) for i in result)


if __name__ == "__main__":
    main()
