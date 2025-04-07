from collections import deque

def solution(bridge_length, max_weight, truck_weights):
    answer = 0
    
    num_of_trucks = len(truck_weights)
    bridge_queue = deque([0]*bridge_length)
    truck_queue = deque(truck_weights)
    sum_bridge = 0
    
    
    while truck_queue:
        truck = truck_queue.popleft()
        
        while True:
            something = bridge_queue.popleft()
            answer += 1
            
            if something != 0:  # it's truck!
                sum_bridge -= something
            
            if sum_bridge + truck <= max_weight:
                sum_bridge += truck
                bridge_queue.append(truck)
                break
            else:
                bridge_queue.append(0)
        
    answer += bridge_length         
    
    return answer