import Player
import Judge

if __name__ == '__main__':
    judge = Judge.Judge()
    playerA = Player.Player('山本')
    playerB = Player.Player('鈴木')
    judge.start_janken(playerA,playerB)