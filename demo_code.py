# Revised: May 2021

from code import Packer, Container, Box

#Step1
NewPacker = Packer()

#Step2 add Container        # name, width, height, depth, max_weight
NewPacker.add_bin(Container('Container1', 1000, 1000, 1000, 700.0))

#Step3 add Box
#						# name, width, height, depth, weight
NewPacker.add_item(Box('50g [Box 1]', 50, 50, 50, 50)) 
NewPacker.add_item(Box('100g [Box 2]', 100, 100, 100, 100))
NewPacker.add_item(Box('200g [Box 3]', 200, 200, 200, 200))

NewPacker.add_item(Box('150g [Box 4]', 150, 150, 150, 150)) 
NewPacker.add_item(Box('300g [Box 5]', 300, 300, 300, 300))
NewPacker.add_item(Box('350g [Box 6]', 350, 350, 350, 350)) 


# NewPacker.add_item(Box('250g [Box 4]', 150, 150, 250, 5))
# NewPacker.add_item(Box('250g [Box 5]', 150, 150, 250, 5))
# NewPacker.add_item(Box('250g [Box 6]', 150, 150, 250, 5))
# NewPacker.add_item(Box('250g [Box 7]', 150, 150, 250, 5))
# NewPacker.add_item(Box('250g [Box 8]', 150, 150, 250, 5))
# NewPacker.add_item(Box('250g [Box 9]', 149, 149, 249, 5))
# NewPacker.add_item(Box('250g [Box 10]', 150, 150, 250, 5))
# NewPacker.add_item(Box('250g [Box 11]', 150, 150, 250, 5))
# NewPacker.add_item(Box('250g [Box 12]', 150, 150, 250, 5))


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
