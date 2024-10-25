def solution(scores):
    answer = 0
    # Add index to each score to keep track of original positions
    indexed_scores = [(i, score[0], score[1]) for i, score in enumerate(scores)]
    # Sort by work_attitude_score decreasing, then by peer_evaluation_score increasing
    indexed_scores.sort(key=lambda x: (-x[1], x[2]))

    max_peer_evaluation = 0
    eliminated = set()
    for idx, work_attitude, peer_evaluation in indexed_scores:
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