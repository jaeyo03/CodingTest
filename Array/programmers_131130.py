def pick_cards(cards, start_point, opened=None):
    if opened is None:
        opened = [False] * len(cards)
    group = []

    current_picked = cards[start_point]
    opened[start_point] = True
    group.append(current_picked)

    while True:
        if opened[current_picked - 1]:
            return group, opened

        next_picked = cards[current_picked - 1]
        opened[current_picked - 1] = True
        group.append(next_picked)
        current_picked = next_picked

def solution(cards):
    answer = 0
    groups = []
    open_info = []

    for i in range(len(cards)):
        group, opened = pick_cards(cards, i)
        groups.append(group)
        open_info.append(opened)

    for inx, g in enumerate(groups):
        second_groups = []
        starting_points = []

        for card_index, card in enumerate(cards):
            if card not in g:
                starting_points.append(card_index)

        for s in starting_points:
            group, opened = pick_cards(cards, s, open_info[inx])
            if len(g) * len(group) > answer:
                answer = len(g) * len(group)

    return answer