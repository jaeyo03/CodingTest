from collections import deque

def solution(nodes, edges):
    answer = [0, 0]
    trees = dict()
    node_dict = dict()
    tree_id = 1
    checked = [0] * (max(nodes) + 1)  # 트리 번호를 넣을 array
    change_to = dict()
    # 트리 연결된것 끼리 분리시키기
    for edge in edges:
        if checked[edge[0]] and checked[edge[1]]:  # 두 트리를 연결시킨다면
            _id = checked[edge[1]]
            new_id = checked[edge[0]]
            current_tree = trees[new_id]
            for key in trees[_id]:
                checked[key] = new_id  # id 갱신
                current_tree[key] = trees[_id][key]  # 그래프 합쳐주기
            current_tree[edge[0]].append(edge[1])  # 그래프 합쳐주기
            current_tree[edge[1]].append(edge[0])  # 그래프 합쳐주기
            del trees[_id]
        elif checked[edge[0]] or checked[edge[1]]:  # 어떤 트리에 속해 있다면
            if trees.get(checked[edge[0]]):
                _id = checked[edge[0]]
                current_tree = trees[_id]
                current_tree[edge[0]].append(edge[1])
                current_tree[edge[1]] = [edge[0]]
                checked[edge[1]] = _id
            elif trees.get(checked[edge[1]]):
                _id = checked[edge[1]]
                current_tree = trees[_id]
                current_tree[edge[1]].append(edge[0])
                current_tree[edge[0]] = [edge[1]]
                checked[edge[0]] = _id
        else:  # 처음이라면
            checked[edge[0]] = tree_id
            checked[edge[1]] = tree_id
            trees[tree_id] = dict()
            trees[tree_id][edge[0]] = [edge[1]]
            trees[tree_id][edge[1]] = [edge[0]]
            tree_id += 1

    # node 에만 있고 edges에 없는 거 처리
    for n in nodes:
        if (checked[n] == 0):
            count = 0
            if (n % 2 == 0 and count % 2 == 0) or (n % 2 != 0 and count % 2 != 0):
                answer[0] += 1
            elif (n % 2 == 0 and count % 2 != 0) or (n % 2 != 0 and count % 2 == 0):
                answer[1] += 1

    # 트리마다 루트 노드 변경시키면서 완탐
    for inx in trees.keys():
        tree = trees[inx]

        for node in tree.keys():
            holjjak = 0
            reverse_holjjak = 0
            root = node
            new_tree = dict()
            visited = [False] * (max(nodes) + 1)
            q = deque([(root, 0)])  # 노드번호, level => 0이 최상위
            visited[root] = True
            is_break = False
            while q:
                current_node, level = q.popleft()
                count = 0
                for n in tree[current_node]:
                    if not visited[n]:
                        visited[n] = True
                        count += 1
                        q.append((n, level + 1))
                if (current_node % 2 == 0 and count % 2 == 0) or (current_node % 2 != 0 and count % 2 != 0):
                    holjjak += 1
                elif (current_node % 2 == 0 and count % 2 != 0) or (current_node % 2 != 0 and count % 2 == 0):
                    reverse_holjjak += 1
                if holjjak > 0 and reverse_holjjak > 0:
                    is_break = True
                    break

            if is_break:
                continue

            if holjjak > 0 and reverse_holjjak == 0:
                answer[0] += 1
            elif reverse_holjjak > 0 and holjjak == 0:
                answer[1] += 1

    return answer