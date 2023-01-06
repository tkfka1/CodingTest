def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 1초에 한대씩 가는게 맞는가.
    timer = 0
    truck = 0
    dic = {}
    for i in range(len(truck_weights)):
        dic[i] = 0
    temp_weight = weight
    while True:
        timer += 1
        # 올라가있는 트럭이있다면
        for key, value in dic.items():
            if value:
                dic[key] += 1
            if value == bridge_length:
                temp_weight += truck_weights[key]
                dic[key] = 0
                if key == len(truck_weights) - 1:
                    return timer

        # 다리에 트럭올리기 된다면
        if not truck == len(truck_weights):
            if truck_weights[truck] <= temp_weight:
                temp_weight -= truck_weights[truck]
                dic[truck] = 1
                truck += 1
