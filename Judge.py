class Judge:
# 審判クラスのコンストラクタなし
    '''
    じゃんけんの手と数値の対応（クラス定数として定義）
    グー = 0
    チョキ = 1
    パー = 2
    '''

    def print_hand(self, hand):
        if hand == 0:
            return 'グー'
        elif hand == 1:
            return 'チョキ'
        elif hand == 2:
            return 'パー'
        
    '''
    じゃんけんを一回実行して、勝者を返す
    '''
    def judge_janken(self, player1, player2):
        winner = None
        player1Hand = player1.show_hand()
        player2Hand = player2.show_hand()
        print(player1.get_name(),':',Judge.print_hand(self,player1Hand), ' v.s. ', player2.get_name(),';',Judge.print_hand(self, player2Hand) )
        
        if (player1Hand == 0 and player2Hand == 1) or (player1Hand == 1 and player2Hand == 2) or (player1Hand == 2 and player2Hand == 0):
            winner = player1
        elif (player2Hand == 0 and player1Hand == 1) or (player2Hand == 1 and player1Hand == 2) or (player2Hand == 2 and player1Hand == 0):
            winner = player2
        
        return winner
    
    '''
    最終的な勝者を判定する
    '''
    
    def judge_finalwinner(self,player1,player2):
        winner = None
        player1Wincount = player1.get_wincount()
        player2Wincount = player2.get_wincount()
        
        if player1Wincount > player2Wincount:
            winner = player1
        elif player2Wincount > player1Wincount:
            winner = player2
            
        return winner
    
    '''
じゃんけんプログラムの本体
    '''
    def start_janken(self, player1, player2):
        print('【じゃんけん開始】')
        for x in {1,2,3}:
            print('【',x,'回戦目】')
            winner = Judge.judge_janken(self,player1,player2)
        if winner != None:
            print(winner.get_name(),'の勝ち')
            winner.notify_result(True)
        else:
            print('引き分け')
        
        print('\n【じゃんけん終了】')
        finalWinner = Judge.judge_finalwinner(self,player1,player2)
        print(player1.get_wincount(),'対',player2.get_wincount(),'で')
        if finalWinner != None:
            print(finalWinner.get_name(),'の勝ちです')
        else:
            print('引き分けです')