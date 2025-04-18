def my_solution(scores):
    answer = 0
    wanho = scores[0]

    scores = [(inx, s[0], s[1]) for inx, s in enumerate(scores)]

    scores.sort(key=lambda x: (-x[2], x[1]))

    max_score = 0
    eliminated = []
    for s in scores:
        inx = s[0]
        score = s[1]
        if score < max_score:
            eliminated.append(inx)
        else:
            max_score = score

    if 0 in eliminated:
        return -1

    new = []

    for s in scores:
        if s[0] in eliminated or s[0] == 0:
            continue
        else:
            new.append([s[1], s[2]])

    wanho.append(0)
    new.append(wanho)
    new.sort(key=lambda x: (x[0] + x[1]))
    w_inx = new.index(wanho)
    answer = len(new) - w_inx

    return answer

def solution(scores):
    answer = 0
    # Add index to each score to keep track of original positions
    indexed_scores = [(i, score[0], score[1]) for i, score in enumerate(scores)]
    # Sort by work_attitude_score decreasing, then by peer_evaluation_score increasing
    indexed_scores.sort(key=lambda x: (-x[1], x[2]))

    max_peer_evaluation = 0
    eliminated = set()
    for idx, work_attitude, peer_evaluation in indexed_scores:
        '''
        위에서 근무 태도 기준으로 정렬하면 동료 평가 점수가 max보다 낮은 사람은 근무 태도 점수는 무조건 낮고,
        동료 평가 점수도 낮은게 보장되므로 등수 산정에서 제외 가능
        '''
        if peer_evaluation < max_peer_evaluation:
            eliminated.add(idx)
        else:
            max_peer_evaluation = max(max_peer_evaluation, peer_evaluation)
    # Check if Wanho is eliminated
    if 0 in eliminated:
        return -1
    # Prepare list of eligible employees with their total scores
    eligible_scores = []
    for idx, work_attitude, peer_evaluation in indexed_scores:
        if idx not in eliminated:
            total = work_attitude + peer_evaluation
            eligible_scores.append((idx, total))
    # Sort eligible employees by total score decreasing
    eligible_scores.sort(key=lambda x: -x[1])
    # Assign ranks
    rank = 0
    same_rank_count = 0
    prev_total = None
    for i, (idx, total) in enumerate(eligible_scores):
        if total != prev_total:
            rank += same_rank_count + 1
            same_rank_count = 0
        else:
            same_rank_count += 1
        if idx == 0:
            answer = rank
            break
        prev_total = total
    return answer
