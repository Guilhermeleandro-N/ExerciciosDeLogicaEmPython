import time
arr=[48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
    91, 78, 72, 51, 75, 15, 80, 90, 89, 10,48, 19, 21, 52, 92, 24, 16, 74, 73, 41,
    85, 22, 62, 11, 29, 39, 93, 60, 33, 47,
    88, 17, 26, 94, 45, 13, 27, 37, 99, 54,
    49, 56, 12, 71, 68, 64, 35, 53, 95, 79,
    31, 18, 25, 81, 70, 87, 42, 76, 55, 14,
    30, 97, 50, 23, 34, 65, 86, 61, 77, 63,
    38, 40, 20, 69, 44, 43, 96, 36, 67, 46,
    59, 98, 82, 28, 83, 57, 32, 84, 58, 66,
 ]
time_init=time.perf_counter()
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
time_end=time.perf_counter()
tempo_fim=time_end-time_init

print(arr,tempo_fim)