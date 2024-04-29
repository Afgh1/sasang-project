import datetime

while True:
    day = input("목표 날짜(YYYYMMDD): ")
    while True:
        if len(day) != 8:
            print("날짜 형식이 잘못되었습니다.\n")
            day = input("목표 날짜(YYYYMMDD): ")
        else:
            break

    diff = int(input("날짜 차이: "))

    day = datetime.date(int(day[0:4]), int(day[4:6]), int(day[6:8]))
    result = day - datetime.timedelta(days=diff)

    print(result)
    while True:
        exit_input = input("\n\'exit\'를 입력하여 종료,\n\'other\'를 입력하여 재시작: ")
        if exit_input.lower() == "exit":
            exit()
        elif exit_input.lower() == "other":
            break
        else:
            print("올바른 입력이 아닙니다.")