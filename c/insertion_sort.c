#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>
#include <time.h>


//Insertion sort function
void insertion_sort(int *a, unsigned int s) {
    int i, j, k; //Declaration of variables

    for (i = 1; i < s; i++) {
        k = a[i]; //Stores the value of the current element
        j = i - 1;

        //Moves elements greater than k to the front position
        while (j > 0 && a[j] > k) {
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j + 1] = k; //Insert k in the correct position
    }
}