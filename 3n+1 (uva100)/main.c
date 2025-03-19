#include <stdio.h>

int main() {
    int start = 0, end = 0, step = 0, stepmax = 0;
    while (scanf("%d%d", &start, &end) != EOF) {
        printf("%d %d ", start, end);
        if (end < start) {
            int temp = start;
            start = end;
            end = temp;
        }
        for (int i = start; i <= end; i++) {
            int n = i;
            while (n != 1) {
                if (n % 2 != 0) {
                    n = 3 * n + 1;
                } else if (n % 2 == 0) {
                    n = n / 2;
                }
                step++;
            }
            if (stepmax < step++) {
                stepmax = step;
            }
            step = 0;
        }
        printf("%d\n", stepmax);
        stepmax = 0;
    }
}