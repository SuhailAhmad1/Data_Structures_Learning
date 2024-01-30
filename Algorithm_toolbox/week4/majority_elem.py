def majority_element_naive(elements):
    dic = {}
    for elem in elements:
        if elem in dic:
            dic[elem]+=1
        else:
            dic[elem] = 1
    
    for k in dic:
        if dic[k] > len(elements)/2:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))