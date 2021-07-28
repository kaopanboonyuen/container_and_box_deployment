# Revised: May 2021

from code import Packer, Container, Box

#Step1 
NewPacker = Packer()

#Step2 add Container        # name, width, height, depth, max_weight
NewPacker.add_bin(Container('Container1', 500, 250, 500, 2500.0))

#Step3 add Box
#						# name, width, height, depth, weight
NewPacker.add_item(Box('[Box 1]', 50, 50, 50, 50)) 
NewPacker.add_item(Box('[Box 2]', 50, 50, 50, 50))
NewPacker.add_item(Box('[Box 3]', 50, 50, 50, 50))
NewPacker.add_item(Box('[Box 4]', 50, 50, 50, 50)) 
NewPacker.add_item(Box('[Box 5]', 80,  100, 80, 80))
NewPacker.add_item(Box('[Box 6]', 80, 100, 80, 80)) 
NewPacker.add_item(Box('[Box 7]', 80, 50, 80, 80))
NewPacker.add_item(Box('[Box 8]', 80, 50, 80, 80)) 
NewPacker.add_item(Box('[Box 9]', 100, 100, 100, 100))
NewPacker.add_item(Box('[Box 10]', 100, 100, 100, 100)) 
NewPacker.add_item(Box('[Box 11]', 100, 100, 100, 100)) 
NewPacker.add_item(Box('[Box 12]', 50, 50, 150, 50))
NewPacker.add_item(Box('[Box 13]', 50, 50, 150, 50))
NewPacker.add_item(Box('[Box 14]', 100, 150, 150, 80)) 
NewPacker.add_item(Box('[Box 15]', 100, 100, 150, 80))
NewPacker.add_item(Box('[Box 16]', 100, 100, 150, 80)) 
NewPacker.add_item(Box('[Box 17]', 100, 100, 150, 80))
NewPacker.add_item(Box('[Box 18]', 100, 50, 100, 50)) 
NewPacker.add_item(Box('[Box 19]', 100, 50, 100, 50))
NewPacker.add_item(Box('[Box 20]', 100, 50, 100, 50))
NewPacker.add_item(Box('[Box 21]', 100, 100, 100, 50)) 
NewPacker.add_item(Box('[Box 22]', 50, 50, 50, 100))
NewPacker.add_item(Box('[Box 23]', 50, 50, 50, 100))
NewPacker.add_item(Box('[Box 24]', 100, 150, 150, 100)) 
NewPacker.add_item(Box('[Box 25]', 100, 100, 150, 100))
NewPacker.add_item(Box('[Box 26]', 100, 100, 150, 80)) 
NewPacker.add_item(Box('[Box 27]', 100, 100, 150, 80))
NewPacker.add_item(Box('[Box 28]', 100, 50, 100, 50)) 
NewPacker.add_item(Box('[Box 29]', 100, 50, 100, 50))
NewPacker.add_item(Box('[Box 30]', 100, 50, 100, 50))


NewPacker.pack(sorting_by_size=True)

for b in NewPacker.bins:
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")
