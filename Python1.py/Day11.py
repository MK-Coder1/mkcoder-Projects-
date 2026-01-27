#string
name = "Mohit"

# apple = ("He said , \"I want to eat an apple")
print("Hello, " + name)
# apple = ('He said , \"I want to eat an apple')

# print(apple)

apple = (''' He said,
hi mohit
how are you 
i am happy 
and you''')
print(apple)

# st = ("""What is DMA?
# Direct Memory Access (DMA) is a technology in computers that allows certain devices (like hard drives, graphics cards, and network adapters) to transfer data directly to and from the system's main memory (RAM) without relying solely on the central processing unit (CPU). This significantly improves overall system performance.
# Why is DMA Important?
# Imagine the CPU as the manager of a busy office. Without DMA, the CPU would be responsible for every single task of moving data between devices and memory. This would be incredibly slow and inefficient, especially for large data transfers. With DMA, the CPU can delegate this task to a specialized assistant, the DMA controller (DMAC). This frees up the CPU to focus on other crucial tasks, leading to a smoother and faster running computer.
# How Does DMA Work?
# Here's a step-by-step breakdown of the DMA process:
# 1.	Initiation: The CPU sets up the DMA transfer by providing instructions to the DMAC. This includes details like the source (where the data is coming from), the destination (where it's going), and the amount of data to be transferred.
# 2.	Data Transfer: The DMAC takes over""")

# print(st)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])thrown an arror.
# sbi character ki couning ke liye.use below lines 
for character in apple:
    print(character)