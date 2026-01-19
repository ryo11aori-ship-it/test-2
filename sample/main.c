// sample/main.c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    printf("C sample: Hello from main.c\n");

    // create a tiny artifact file to prove run-to-completion
    FILE *f = fopen("sample_c_artifact.txt", "w");
    if (f) {
        fprintf(f, "c_ok\n");
        fclose(f);
        printf("Wrote sample_c_artifact.txt\n");
    } else {
        fprintf(stderr, "Failed to write artifact\n");
        return 2;
    }

    return 0;
}
