import copy
import math

import numpy
from PIL import Image

def png_read(filepath):
    img = Image.open(filepath)
    assert len(img.size)==2 # skala szarosci, nie RGB
    return (numpy.array(img)/255).reshape(img.size[1], img.size[0]).tolist()

def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img)*255).astype(numpy.int8), 'L')
    img.save(filepath)

def rozjasnianie(A):
    B = copy.deepcopy(A)
    for i in range(0, len(B)):
        for j in range(0, len(B[0])):
            b = 0.5
            B[i][j] += b
            if B[i][j] > 1:
                B[i][j] = 1
            if B[i][j] < 0:
                B[i][j] = 0
    png_write(B, "output2.png")

def negatyw(A):
    B = copy.deepcopy(A)
    for i in range(0, len(B)):
        for j in range(0, len(B[0])):
            B[i][j] = 1 - B[i][j]
    png_write(B, "output3.png")

def konwersja(A):
    B = copy.deepcopy(A)
    for i in range(0, len(B)):
        for j in range(0, len(B[0])):
            p = 0.5
            if B[i][j] > p:
                B[i][j] = 1
            else:
                B[i][j] = 0
    png_write(B, "output4.png")

def kontrast(A):
    B = copy.deepcopy(A)
    for i in range(0, len(B)):
        for j in range(0, len(B[0])):
            theta = 10
            B[i][j] = 1 / (1 + math.e ** (-theta * (B[i][j] - 0.5)))
    png_write(B, "output5.png")

def convolution(A,B):
    k = int((len(B) - 1) / 2)
    C = copy.deepcopy(A)
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            C[i][j] = 0
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    if not 1 <= i <= len(A):
                        C[i][j] += 0
                    elif not 1 <= j <= len(A[0]):
                        C[i][j] += 0
                    else:
                        C[i][j] += (A[i + u][j + v] * B[u + k + 1][v + k + 1])
    return C




def main():
    A = png_read("skimage_astronaut.png")
    png_write(A, "output1.png")
    min = 1
    max = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if A[i][j] >= max:
                max = A[i][j]
            if A[i][j] <= min:
                min = A[i][j]
    print(f"Max={max}")
    print(f"Min={min}")
    rozjasnianie(A)
    negatyw(A)
    konwersja(A)
    kontrast(A)
    k = 3
    B = [[0] * (2 * k + 1)] * (2 * k + 1)
    for i in range(0, len(B)):
        for j in range(0, (len(B[0]))):
            B[i][j] = (1 / (2 * k + 1) ** 2)
    C = convolution(A, B)
    png_write(C, "output6.png")

if __name__ == '__main__':
    main()