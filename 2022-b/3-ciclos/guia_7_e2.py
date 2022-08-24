init_temp = int(input('ingrese la temp inicial (F)'))
final_temp = int(input('ingrese la temp final (F)'))
step = int(input('ingrese el salto de grados'))

print('Temperature:')
print('F\t\tC')
for t in range(init_temp, final_temp+step, step):
    c = (t - 32) * (5/9)
    print(f'{t:.2f}\t\t{c:.2f}')

