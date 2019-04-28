vals = [None]*10
count = input("Quantos valores quer guardar no array? ")
for i in range(0, count):
    vals[i] = count-i
which = input("Que valor deseja recuperar? ")
print 'O valor e ', str(vals[which])

