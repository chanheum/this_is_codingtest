input_data = list(map(str, input()))
input_data.sort()

result_num = 0
result_str = str()

for i in range(len(input_data)):
    if input_data[i] >= '1' and input_data[i] <= '9':
        result_num += int(input_data[i])
    else:
        result_str += input_data[i]

if result_num > 0:
    print(result_str + str(result_num))
else:
    print(result_str)
