#include <stdio.h>
#define STR_SIZE 255

// Bereken de index waar twee characters verschillen in een array.
int get_index(char str_1[], char str_2[], int l){

  // Note: while loop zou efficienter werken door minder geheugen op te slaan.

  int index;

  for (int i = 0; i < l; i++) {

    // Stel huidige return index gelijk aan de huidige loop index.
    index = i;

    // Check de verschillen tussen de characters op index i.
    if (str_1[i] == str_2[i]) {
      continue;
    } else {
      break;
    }
  }

  return index;
}

int main() {

  // Zinnen kunnen op dit moment maximaal str_size aantal characters hebben.
  char str_1[STR_SIZE];
  char str_2[STR_SIZE];

  printf("First sentence: ");
  fgets(str_1, STR_SIZE, stdin);

  printf("Second sentence: ");
  fgets(str_2, STR_SIZE, stdin);

  // Debugging print statements
  // printf("%s\n", str_1);
  //
  // printf("%s\n", str_2);

  // Bereken index.
  int index = get_index(str_1, str_2, STR_SIZE);

  printf("Het verschil zit op index: %d\n", index);

  // succes
  return 0;
}
