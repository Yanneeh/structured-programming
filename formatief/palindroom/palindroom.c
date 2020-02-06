#include <stdio.h>
#include <string.h>

/*

Ik heb geleerd in deze opdracht dat functies in c anders
werken dan in andere programmeertalen. Een array kan niet als return type uit een functie geretourneerd worden.
Een functie kan arrays wel modificeren. Daarom heeft de reverse functie geen return type,
omdat de functie direct de globale arrays aanpast.

*/

int count_str(char str[], int len){
  int count = 0;

  for(int i = 0; i < len; i++){
    if (str[i] == '\0'){
      break;
      // Debuging
      // printf("%d\n", i);
    } else {
      count++;
    }
  }

  count--;

  return count;
}

void reverse(char str[], char reversed_str[], int len){
  int index = 0;

  int count = count_str(str, len);

  for (int i = count; i >= 0; i--){
    reversed_str[index] = str[i];
    index++;

    // Debugging
    // printf("%s\n", reversed_str);
  }
}

int main(){

  int len = 100;

  char str[len];
  char reversed_str[len];

  printf("%s", "Typ een woord: ");

  scanf("%s", str);

  reverse(str, reversed_str, len);

  printf("Omgekeerd woord: %s\n", reversed_str);

  int palindroom = 1;

  int count = count_str(str, len);

  for (int i = 0; i <= count; i++) {
    if (str[i] != reversed_str[i]){
      palindroom = 0;
      break;
    }
  }

  if (palindroom == 1) {
    printf("Het woord is palindroom\n");
  } else {
    printf("Het woord is niet palindroom\n");
  }

  return 0;
}
