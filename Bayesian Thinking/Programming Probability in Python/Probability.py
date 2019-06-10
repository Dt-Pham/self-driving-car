def probability_of_collision(car_1, car_2):
    probability = 0.0;

    prob = {};
    prob["LL"] = 0.5
    prob["SS"] = 0.02
    prob["RR"] = 0.01
    prob["LS"] = prob["SL"] = 0.25
    prob["LR"] = prob["RL"] = 0.1
    prob["SR"] = prob["RS"] = 0.1

    return prob[car_1 + car_2]
