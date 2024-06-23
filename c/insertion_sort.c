void insertion_sort(int* v, unsigned int n) {
    int i, j, k;
    for (i = 1; i < n; i++) {
        k = v[i];
        j = i - 1;
        while (j > 0 && v[j] > k) {
            v[j + 1] = v[j];
            j = j - 1;
        }
        v[j + 1] = k;
    }
}