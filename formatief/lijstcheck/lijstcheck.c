#include <stdio.h>

// Tel hoevaak een getal voorkomt in een array.
int count(int arr[], int num, int len) {
  int c = 0;

  for (int i = 0; i < len; i++) {

    // Check of het getal op index i in array hetzelfde is als het gezochte getal.
    if(arr[i] == num) {
      // Debugging
      // printf("%d\n", i);
      c++;
    }
  }

  return c;
}

// Bereken het grootste verschil tussen twee elementen in een array.
int diff(int arr[], int len){

  int high = 0;

  for (int i = 1; i < len; i++) {
    int num = 0;

    // Bereken eerst het verschil tussen twee getallen.
    if (arr[i] > arr[i-1]) {
      num = arr[i] - arr[i-1];
      // Debugging
      // printf("%d\n", num);
    } else {
      num = arr[i+1] - arr[i];
      // Debugging
      // printf("%d\n", num);
    }

    // Check of nieuw verschil groter is dan het grootste oude verschil.
    if (num > high) {
      high = num;
    }
  }

  return high;
}

int rule(int arr[], int len){

  int zeros = count(arr, 0, len);

  if (zeros > 11){
    return 0;

  } else {
    int ones = count(arr, 1, len);

    if (ones > zeros){
      return 1;

    } else {
      return 0;
    }
  }

}

int main() {

  int num = 5;

  int arr[] = {4, 5, 6, 7, 2, 5, 3, 4};

  int len = sizeof(arr)/sizeof(arr[0]);

  int c = count(arr, num, len);

  printf("Het getal %d komt %d keer voor in de array.\n", num, c);

  int d = diff(arr, len);

  printf("Het grootste verschil tussen twee opeenvolgende getallen is %d\n", d);

  int ones_and_zeros[] = {1, 1, 0, 1, 1, 0, 1, 1, 0, 0};

  len = sizeof(ones_and_zeros)/sizeof(ones_and_zeros[0]);

  int result = rule(ones_and_zeros, len);

  printf("%d\n", result);

  return 0;
}
