void merge_sort(int* v, int init, int end);
void merge(int* v, int init, int m, int end);

void merge_sort(int *v, int init, int end) {
    int m;
    if (init < end) {
        m = (init + end) / 2;
        merge_sort(v, init, m);
        merge_sort(v, m + 1, end);
        merge(v, init, m, end);
    }
}

void merge( int* v, int init, int m, int end) {
    int tam = end - init + 1;
    int* w = (int *)malloc(tam * sizeof(int));
    int i = init;
    int j = m + 1;
    for (int k = 0; k < tam; k++) {
        if (j > end || (i < m && v[i] < v[j])) {
            w[k] = v[i];
            i++;
        }
        else {
            w[k] = v[j];
            j++;
        }
    }
    for (int p = 0; p < tam; p++)
    v[init + p] = w[p];
}