input_data = open("input.txt","r")
data = input_data.read()
data = list(data)
c = (data[0]) + (data[1]) + (data[2])
c = int(c)
h = c + 1
x = h * c 
x = str(x)
i = str(25)
end = x + i
output_data = open("output.txt","w")
output_data.write(end)
input_data.close()
output_data.close()

