def machine():
    mode=[0,1,2,9999]
    drinks={'포도 주스':800,'오렌지 주스':800,'콜라':1000,'사이다':1000,'몬스터':2000}
    menu=list(drinks.keys())
    count={'포도 주스':0,'오렌지 주스':0,'콜라':0,'사이다':0,'몬스터':0}
    cash={'잔돈':0,'매출':0}
    while True:
        buttons=int(input("무엇이 하고 싶은가요? 1: 자판기 이용 2: 내가 뽑은 음료수 현황/ 자판기에 넣은 금액 확인 0:종료 9999:관리자 모드"))
        if buttons not in mode:
            print("잘못 입력하셨습니다.")
            continue
        if buttons==0:
            print("프로그램을 종료합니다")
            break
        elif buttons==1:
            for k,v in drinks.items():
                print(k,'₩',v)
            money=int(input('돈을 넣어주세요'))
            if money==0:
                print("안녕히가세요. 거스름돈은 {}원입니다.".format(cash['잔돈']))
                cash['잔돈']=0
                continue
            cash['잔돈']=cash.get('잔돈')+money
            print("현재 잔액: {}".format(cash['잔돈']))
            try:
                x,y=map(int,input("음료수 종류 1:포도 주스 2:오렌지 주스 3:콜라 4:사이다 5:몬스터 를 정하고 갯수를 입력하세요 ").split())
                print(f"{menu[x-1]} {y}개가 맞습니까? 총 {drinks.get(menu[x-1])*y}원입니다.")
                cash['매출']+=(drinks.get(menu[x-1])*y)
                if money< (drinks.get(menu[x-1])*y):
                    print("돈이 부족합니다. 돈을 더 넣어주세요")
                    continue
                else:
                    count[menu[x-1]]=count.get(menu[x-1])+y
                    cash['잔돈']-=(drinks.get(menu[x-1])*y)
                    print("감사합니다. 현재 남은 돈은 {}원입니다".format(cash['잔돈']))
            except:
                print("잘못입력하셨습니다. 거스름돈은 {}원입니다.".format(cash['잔돈']))
                cash['매출']-=cash['잔돈']
                cash['잔돈']=0
                continue
        elif buttons==2:
            for k,v in count.items():
                print(k,v,'개')
            print("현재 기기에 남은 돈은 {}원입니다".format(cash['잔돈']))
        elif buttons==9999:
            while True:
                print("관리자 모드 입니다.")
                try:
                    control= int(input("1:메뉴 추가 2:메뉴 수정 3:메뉴 삭제 4:금일 매출 0:종료"))
                    if control==1:
                        name=input("추가 할 메뉴이름을 적으세요")
                        cost=int(input("새로운 메뉴의 값을 정해주세요"))
                        drinks[name]=cost
                        count[name]=0
                        print("새로운 메뉴:")
                        for k,v in drinks.items():
                            print(k,'₩',v)
                    elif control==2:
                        name=input("수정할 메뉴를 고르세요")
                        if name in drinks.keys():
                            cost=int(input("가격을 새로 정해주세요"))
                            drinks[name]=cost
                            print("수정된 메뉴:")
                            for k,v in drinks.items():
                                print(k,'₩',v)
                        else:
                            print("없는 메뉴입니다")
                            continue
                    elif control==3:
                        name=input("삭제할 메뉴를 고르세요")
                        if name in drinks.keys():
                            del(drinks[name])
                            del(count[name])
                            print("수정된 메뉴:")
                            for k,v in drinks.items():
                                print(k,'₩',v)
                        else:
                            print("없는 메뉴입니다.")
                            continue
                    elif control==4:
                        print("오늘 팔린 음료수 갯수:")
                        for k,v in count.items():
                            print(k,v,'개')
                        print(f"총 {sum(count.values())}개, 총{cash['매출']}원")
                    elif control==0:
                        print("관리자 모드를 종료합니다")
                        break
                except:
                    print("잘못 입력하셨습니다")
                    continue


machine()