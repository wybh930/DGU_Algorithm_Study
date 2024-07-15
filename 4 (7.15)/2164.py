from collections import deque

def last_card(n):
    # 1부터 N까지의 카드를 덱에 넣는다.
    cards = deque(range(1, n + 1))
    
    while len(cards) > 1:
        # 제일 위에 있는 카드를 버린다.
        cards.popleft()
        # 제일 위에 있는 카드를 제일 아래로 옮긴다.
        cards.append(cards.popleft())
    
    # 마지막으로 남는 카드의 번호를 반환한다.
    return cards[0]

# 입력을 받는다.
N = int(input().strip())
# 마지막으로 남는 카드의 번호를 출력한다.
print(last_card(N))
