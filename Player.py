import random
class Player:
    '''
    プレイヤークラスのコンストラクタ
    引数： name プレイヤーの名前
    '''
    def __init__(self, name):
        self._name = name
        self._wincount = 0
    '''
    じゃんけんの手を出す関数：
    0, 1, 2 をランダムに出力する
    '''
    def show_hand(self):
        return random.randrange(3)
    
    '''
    審判から勝敗を聞く
    '''
    
    def notify_result(self, result):
        if True == result:
            self._wincount += 1
    
    '''
    自分の勝ちの数を答える
    '''
    def get_wincount(self):
        return self._wincount
    
    '''
    名前を答える(表示する)
    '''
    
    def get_name(self):
        return self._name
