void quick_sort(int* v, int init, int end);
int partition(int* v, int init, int end);

void quick_sort(int* v, int init, int end) {
    if (end > init) {
        int p = partition(v, init, end);
        quick_sort(v, init, p - 1);
        quick_sort(v, p + 1, end);
    }
}

int partition(int* v, int init, int end) {
    int left, right, pivo, aux;
    left = init;
    right = end;
    pivo = v[init];
    while (left < right) {
        while (left < end && v[left] <= pivo) {
            left++;
        }
        while (right > init && v[right] > pivo) {
            right--;
        }
        if (left < right) {
            aux = v[left];
            v[left] = v[right];
            v[right] = aux;
        }
    }
    v[init] = v[right];
    v[right] = pivo;
    return right;
}