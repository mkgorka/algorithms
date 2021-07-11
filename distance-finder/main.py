import math

def tour(friends, friend_towns, home_to_town_distances):
    path_in_order = []
    total_distance = 0

    for friend in friends:
        for friend_loc_pair in friend_towns:
            if friend in friend_loc_pair:
                friend_town = friend_loc_pair[1]
                path_in_order.append(home_to_town_distances[friend_town])
            elif friend not in friend_loc_pair:
                pass
    for idx, path in enumerate(path_in_order):
        target = path_in_order[idx]
        if idx < (len(path_in_order) - 1):
            next_target = path_in_order[idx + 1]
        else:
            break
        start_path = path_in_order[0]
        end_path = path_in_order[-1]
        dist = math.sqrt((next_target ** 2) - (target ** 2))
        total_distance = total_distance + dist
        result = math.floor(total_distance + start_path + end_path)
    return result
