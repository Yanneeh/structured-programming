#include <stdio.h>

// Piramid functie die gebruik maakt van for-loops
void piramid_for(int n){

  // Eerste for-loop die een regel sterren schrijft met een lengte van i.
  // Stopt bij waarde n.
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      printf("*");
    }
    printf("\n");
  }

  // Print een regel sterren n keer.
  for (int i = 0; i < n; i++) {
    printf("*");
  }
  printf("\n");

  // Tweede for-loop die het proces in de eerste for-loop omgekeerd herhaalt.
  // Stopt bij 0.
  for (int i = n; i > 0; i--) {
    for (int j = 0; j < i; j++) {
      printf("*");
    }
    printf("\n");
  }
}

void piramid_while(int n) {

  // Init iterator.
  int i = 0;

  // Eerste while-loop die een regel sterren schrijft met een lengte van i.
  // Stopt bij waarde n.
  while (i < n) {
    for (int j = 0; j < i; j++) {
      printf("*");
    }
    printf("\n");

    i++;
  }

  // Print * keer hoogte n
  for (int i = 0; i < n; i++) {
    printf("*");
  }
  printf("\n");

  // Verander iterator naar n.
  i = n;

  // Tweede while-loop die het proces in de eerste for-loop omgekeerd herhaalt.
  while (i > 0) {
    for (int j = 0; j < i; j++) {
      printf("*");
    }
    printf("\n");

    i--;
  }
}


// Main program
int main() {

  int i;

  printf("Enter a value : ");
  scanf("%d", &i);

  printf("Piramid for functie ...\n");

  piramid_for(i);

  printf("Piramid while functie ...\n");

  piramid_while(i);

  return 0;
}
