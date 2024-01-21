from sys import stdin

def optimal_value(capacity, weights, values):
    if capacity == 0:
        return 0
    weight_count = 0
    max_value = 0
    fraction_dic = {}
    for i in range(len(weights)):
        fraction_dic[i] = values[i]/weights[i]

    sorted_fractions = dict(sorted(fraction_dic.items(), key=lambda item: item[1], reverse=True))
    
    for f in sorted_fractions:
        if weight_count < capacity:
            if weight_count+weights[f] <= capacity:
                max_value+=values[f]
                weight_count+=weights[f]
            else:
                diff = capacity-weight_count
                max_value += sorted_fractions[f]*diff
                weight_count+=diff
    return max_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
