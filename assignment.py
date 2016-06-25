def main():
    f = open("C:\\cp949\\cp949\\user.txt", "r")
    lis = []
    while True:
        a = f.readline()
        a = a[0:-1]
        if not a: break
        f.readline()
        b = f.readline()
        b = b[0:-1]
        user = {'Id number': a, 'screen name': b}
        f.readline()
        lis.append(user)

    f.close()
    f = open("C:\\cp949\\cp949\\friend.txt", "r")
    for i in range(len(lis)):
        lis[i]['friends'] = []
    while True:
        a = f.readline()
        a = a[0:-1]
        b = f.readline()
        b = b[0:-1]
        f.readline()
        i = 0
        if not a: break
        for i in range(len(lis)):
            h = lis[i].get('Id number')

            if a == h:
                lis[i]['friends'].append(b)  # 친구관계 저장
                break
    f.close()

    f = open("C:\\cp949\\cp949\\word.txt", "r")
    for i in range(len(lis)):
        lis[i]["tweet"] = []
    while True:
        a = f.readline()
        a = a[0:-1]
        if not a: break
        f.readline()
        b = f.readline()
        b = b[0:-1]
        f.readline()
        for i in range(len(lis)):
            h = lis[i].get('Id number')
            if a == h:
                lis[i]['tweet'].append(b)
                break
    f.close()

    word_temp = ''
    while True:
        print("""0. Read data files
    1. display statistics
    2. Top 5 most tweeted words
    3. Top 5 most tweeted users
    4. Find users who tweeted a word (e.g., ’연세대’)
    5. Find all people who are friends of the above users
    6. Delete all mentions of a word
    7. Delete all users who mentioned a word
    8. Find strongly connected components
    9. Find shortest path from a given user
    99. Quit
    Select Menu:""", end='')
        a = input()
        if a == '0':
            fn = 0
            for i in range(len(lis)):
                w = len(lis[i]['friends'])
                fn += w
                for j in range(len(lis[i]['friends'])):
                    s = lis[i].get('friends')
                    idn = lis[i].get('Id number')
                    sd = s[j]
                    for y in range(i + 1, len(lis) - 1):
                        if lis[y].get('Id number') == sd and idn in lis[y]['friends']:
                            fn -= 1  # 겹치는거 뺀 총 친구관계 fn
            tw = 0
            for i in range(len(lis)):
                e = len(lis[i]['tweet'])
                tw += e  # 총트위트수
            print("Total users: %s" % len(lis))
            print("Total friendship records: %s" % fn)
            print("Total tweets: %s" % tw)
        elif a == '1':
            tw = 0
            for i in range(len(lis)):
                e = len(lis[i]['tweet'])
                tw += e  # 총트위트수
            atw = tw / len(lis)
            arrangeTw = []
            for i in range(len(lis)):
                e = len(lis[i]['tweet'])
                arrangeTw.append(e)
            arrangeTw.sort()
            fn = 0
            arrangeFn = []
            for i in range(len(lis)):
                w = len(lis[i]['friends'])
                fn += w
                for j in range(len(lis[i]['friends'])):
                    s = lis[i].get('friends')
                    idn = lis[i].get('Id number')
                    sd = s[j]
                    for y in range(i + 1, len(lis) - 1):
                        if lis[y].get('Id number') == sd and idn in lis[y]['friends']:
                            fn -= 1  # 겹치는거 뺀 총 친구관계 fn
                arrangeFn.append(w)
            arrangeFn.sort()
            anf = fn / len(lis)
            print('Average number of friends: %s' % anf)
            print('Minimum friends: %s' % arrangeFn[0])
            print('Maximum number of friends: %s' % arrangeFn[len(lis)-1])
            print('')
            print('Average tweets per user: %s' % atw)
            print('Minium tweets per user: %s' % arrangeTw[0])
            print('Maximu tweets per user: %s' % arrangeTw[len(lis)-1])
        elif a == '2':
            arrangeTw = []
            Tw = []
            for i in range(len(lis)):
                e = len(lis[i]['tweet'])
                arrangeTw.append(e)
            arrangeTw.sort()
            for i in range(len(lis)):
                for j in range(len(lis[i]['tweet'])):
                    Tw.append(lis[i]['tweet'][j])
            Tw.sort()
            s = 0
            Tlist = []
            Tnumb = 0
            for i in range(len(Tw)):
                if i == len(Tw) - 1:
                    Tnumb += 1
                    Tdict = {'word': Tw[s], 'number': Tnumb}
                    Tlist.append(Tdict)
                elif Tw[s] == Tw[i]:
                    Tnumb += 1
                else:  # Tw[s] != Tw[i]
                    Tdict = {'word': Tw[s], 'number': Tnumb}
                    Tlist.append(Tdict)
                    s = i
                    Tnumb = 1
            for i in range(len(Tlist)):
                for j in range(i + 1, len(Tlist) - 1):
                    if Tlist[i]['number'] < Tlist[j]['number']:
                        Tlist[i], Tlist[j] = Tlist[j], Tlist[i]
            print('단어: %s 개수: %s' % (Tlist[0].get('word'), Tlist[0].get('number')))
            print('단어: %s 개수: %s' % (Tlist[1].get('word'), Tlist[1].get('number')))
            print('단어: %s 개수: %s' % (Tlist[2].get('word'), Tlist[2].get('number')))
            print('단어: %s 개수: %s' % (Tlist[3].get('word'), Tlist[3].get('number')))
            print('단어: %s 개수: %s' % (Tlist[4].get('word'), Tlist[4].get('number')))
        elif a == '3':
            mtu = []  # most tweeted users
            for i in range(len(lis)):
                usertweet = {'Id': lis[i].get('screen name'), 'Twn': len(lis[i].get('tweet'))}
                mtu.append(usertweet)
            for i in range(len(mtu)):
                for j in range(i + 1, len(mtu)):
                    if mtu[i]['Twn'] < mtu[j]['Twn']:
                        mtu[i], mtu[j] = mtu[j], mtu[i]
            print('닉네임: %s 트윗 수: %s' % (mtu[0].get('Id'), mtu[0].get('Twn')))
            print('닉네임: %s 트윗 수: %s' % (mtu[1].get('Id'), mtu[1].get('Twn')))
            print('닉네임: %s 트윗 수: %s' % (mtu[2].get('Id'), mtu[2].get('Twn')))
            print('닉네임: %s 트윗 수: %s' % (mtu[3].get('Id'), mtu[3].get('Twn')))
            print('닉네임: %s 트윗 수: %s' % (mtu[4].get('Id'), mtu[4].get('Twn')))
        elif a == '4' or a == '5':
            if a == '4':
                word = input()
                wordusers = []
                for i in range(len(lis)):
                    for j in range(len(lis[i]['tweet'])):
                        if lis[i]['tweet'][j] == word:
                            ha = {'nick': lis[i]['screen name'], 'fri': lis[i]['friends']}
                            wordusers.append(ha)
                            break
                word_temp = word
                for i in range(len(wordusers)):
                    print(wordusers[i]['nick'])
            elif a == '5':
                if word_temp != '':
                    for i in range(len(wordusers)):

                        print("닉네임: %s 친구: %s" % (wordusers[i]['nick'], wordusers[i]['fri']))
                else:
                    print("입력값이 없습니다. 4를 입력 후 찾고싶은 word를 적어주세요")
        elif a == '6':
            delword = input()
            for i in range(len(lis)):
                t = len(lis[i]['tweet'])
                h = []
                for j in range(t):
                    if delword == lis[i]['tweet'][j]:
                        h.append(lis[i]['tweet'][j])
                for k in range(len(h)):
                    lis[i]['tweet'].remove(h[k])
        elif a == '7':
            deluser = input()
            ht = []
            for i in range(len(lis)):
                t = len(lis[i]['tweet'])
                for j in range(t):
                    if deluser == lis[i]['tweet'][j]:
                        ht.append(lis[i])
                        break
            for k in range(len(ht)):
                lis.remove(ht[k])
        elif a == '8':
            pass
        elif a == '9':
            pass
        elif a == '99':
            break
main()