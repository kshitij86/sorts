import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import algorithms

if __name__ == "__main__":
    N = int(input("Enter number of integers: "))
    eff = []
      
    # Generate the list an shuffle it thororughly. 
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

#1__________________________________
    fig, ax = plt.subplots()
    ax.set_title()
        
    bar_rects = ax.bar(range(len(A)), A, align="edge")
        
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f'# of operations: {iteration[0]}')

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=getattr(algorithms, "bubblesort")(A), interval=1,
        repeat=False)
    eff.append(iteration[0])
    plt.show()


#2__________________________________
    fig, ax = plt.subplots()
    ax.set_title()
        
    bar_rects = ax.bar(range(len(A)), A, align="edge")
        
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f'# of operations: {iteration[0]}')

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=getattr(algorithms, "insertionsort")(A), interval=1,
        repeat=False)
    eff.append(iteration[0])
    plt.show()

#3__________________________________
    fig, ax = plt.subplots()
    ax.set_title()
        
    bar_rects = ax.bar(range(len(A)), A, align="edge")
        
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f'# of operations: {iteration[0]}')

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=getattr(algorithms, "mergesort")(A, 0, len(A)-1), interval=1,
        repeat=False)
    eff.append(iteration[0])
    plt.show()

#4__________________________________
    fig, ax = plt.subplots()
    ax.set_title()
        
    bar_rects = ax.bar(range(len(A)), A, align="edge")
        
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f'# of operations: {iteration[0]}')

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=getattr(algorithms, "quicksort")(A, 0, len(A)-1), interval=1,
        repeat=False)
    eff.append(iteration[0])
    plt.show()

#5__________________________________
    fig, ax = plt.subplots()
    ax.set_title()
        
    bar_rects = ax.bar(range(len(A)), A, align="edge")
        
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f'# of operations: {iteration[0]}')

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=getattr(algorithms, "selectionsort")(A), interval=1,
        repeat=False)
    eff.append(iteration[0])
    plt.show()