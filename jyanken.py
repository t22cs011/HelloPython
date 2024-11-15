import random

# 手を文字列に変換する関数
def get_hand_name(hand):
    hands = ["グー", "チョキ", "パー"]
    return hands[hand]

# 一対一の勝敗判定
def judge_winner(a_hand, b_hand):
    if a_hand == b_hand:
        return "引き分け"
    elif (a_hand - b_hand) % 3 == 1:
        return "Aの勝ち"
    else:
        return "Bの勝ち"

# 複数プレイヤーの勝敗判定
def judge_winner_multiple(players_hands):
    unique_hands = set(players_hands)
    
    if len(unique_hands) == 1 or len(unique_hands) == 3:
        return "引き分け", -1  # 引き分けの時は勝者なし
    elif players_hands.count(0) > 0 and players_hands.count(1) > 0 and players_hands.count(2) == 0:
        return "勝者はプレイヤー1", 0  # グーの勝ち
    elif players_hands.count(1) > 0 and players_hands.count(2) > 0 and players_hands.count(0) == 0:
        return "勝者はプレイヤー2", 1  # チョキの勝ち
    elif players_hands.count(2) > 0 and players_hands.count(0) > 0 and players_hands.count(1) == 0:
        return "勝者はプレイヤー3", 2  # パーの勝ち
    else:
        return "引き分け", -1

# 一対一のじゃんけん
def play_janken():
    a_hand = random.randint(0, 2)
    b_hand = random.randint(0, 2)
    
    a_hand_name = get_hand_name(a_hand)
    b_hand_name = get_hand_name(b_hand)
    
    result = judge_winner(a_hand, b_hand)
    
    print(f"プレイヤーAの手: {a_hand_name} v.s. プレイヤーBの手: {b_hand_name} → {result}")

# 一対一の3回勝負
def play_janken_best_of_three():
    a_wins = 0
    b_wins = 0
    rounds = 0
    
    while a_wins < 2 and b_wins < 2 and rounds < 3:
        a_hand = random.randint(0, 2)
        b_hand = random.randint(0, 2)
        
        a_hand_name = get_hand_name(a_hand)
        b_hand_name = get_hand_name(b_hand)
        
        result = judge_winner(a_hand, b_hand)
        print(f"第{rounds + 1}回: プレイヤーAの手: {a_hand_name} v.s. プレイヤーBの手: {b_hand_name} → {result}")
        
        if result == "Aの勝ち":
            a_wins += 1
        elif result == "Bの勝ち":
            b_wins += 1
        
        rounds += 1
    
    if a_wins > b_wins:
        print("最終結果: Aの勝利")
    elif b_wins > a_wins:
        print("最終結果: Bの勝利")
    else:
        print("最終結果: 引き分け")

# プレイヤーが複数いるじゃんけん
def play_janken_multiple(players):
    players_hands = [random.randint(0, 2) for _ in range(players)]
    
    for i, hand in enumerate(players_hands):
        print(f"プレイヤー{i + 1}の手: {get_hand_name(hand)}")
    
    result, winner_hand = judge_winner_multiple(players_hands)
    
    if winner_hand != -1:  # 勝者がいる場合
        winners = [i + 1 for i, hand in enumerate(players_hands) if hand == winner_hand]
        winners_str = "、".join([f"プレイヤー{winner}" for winner in winners])
        print(f"結果: {result} ({winners_str}の勝ち)")
    else:  # 引き分けの場合
        print(f"結果: {result}")

# 3人以上のプレイヤーで3回勝負
def play_janken_best_of_three_multiple(players, player_names):
    wins = [0] * players  # 各プレイヤーの勝利数を記録
    rounds = 0
    
    while rounds < 3:
        players_hands = [random.randint(0, 2) for _ in range(players)]
        
        for i, hand in enumerate(players_hands):
            print(f"プレイヤー{player_names[i]}の手: {get_hand_name(hand)}")
        
        result, winner_hand = judge_winner_multiple(players_hands)
        print(f"第{rounds + 1}回の結果: {result}")
        
        if winner_hand != -1:
            for i, hand in enumerate(players_hands):
                if hand == winner_hand:
                    wins[i] += 1
        
        rounds += 1
    
    max_wins = max(wins)
    
    # 勝利数を基に最終結果を判断
    winners = [i + 1 for i, win in enumerate(wins) if win == max_wins]
    
    if max_wins == 3:
        print(f"最終結果: プレイヤー{player_names[winners[0] - 1]}の勝利！")
    elif max_wins == 2:
        print(f"最終結果: プレイヤー{player_names[winners[0] - 1]}の勝利！")
    elif max_wins == 1 and len(winners) == 1:
        print(f"最終結果: プレイヤー{player_names[winners[0] - 1]}の勝利！")
    else:
        print("最終結果: 引き分け！")

    # 各プレイヤーの勝利数を表示
    for i, count in enumerate(wins):
        print(f"プレイヤー{player_names[i]}の勝った回数: {count}")

# 実行例
player_names = ["1", "2", "3"]  # プレイヤーの名前
print("\n3人以上での3回勝負:")
play_janken_best_of_three_multiple(3, player_names)
