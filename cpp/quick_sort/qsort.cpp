#include <iostream>

using namespace std;




// Function to compute our partition
int partition(int *arr, int beg, int end){
  int store_ind=beg;
  int tmp;
  int piv_ind = (beg+end)/2;
  int piv_val = arr[piv_ind]; // we make a naive/crappy choice of pivot, a better one might be 1/2 val

  // store the pivot value at the end where it wont interfere
  tmp = arr[piv_ind];
  arr[piv_ind] = arr[end];
  arr[end] = tmp;

  for(int i=beg; i < end; i++){
    if(arr[i] < piv_val){
      tmp = arr[i];
      arr[i] = arr[store_ind];
      arr[store_ind] = tmp;
      store_ind++;
    }
  }  

  // Store the pivot value in its place
  tmp = arr[store_ind];
  arr[store_ind] = arr[end];
  arr[end] = tmp;

  return store_ind;
}


// an implementation ogf quicksort
void qsort(int* arr, int beg, int end){
  if(beg < end){
    int piv = partition(arr, beg, end);
    //recursive call to LHS of list
    qsort(arr, beg, piv-1);
    //recursive call to RHS of list
    qsort(arr, piv+1, end);
  }
}



int main(int argc, char* argv[]){
  int l1[9] = {9,8,7,6,5,4,3,2,1};
  int l2[4] = {9,8,7,6};


  cout << "Unsorted list 1: ";
  for(int i=0; i < 9; i++){
    cout << l1[i];
  }
  cout << endl;
  
  cout << "Unsorted list 2: ";
  for(int i=0; i < 4; i++){
    cout << l2[i];
  }
  cout << endl;

  qsort(l1,0,8);
  qsort(l2,0,3);

  cout << "Sorted list 1: ";
  for(int i=0; i < 9; i++){
    cout << l1[i];
  }
  cout << endl;
  
  cout << "Sorted list 2: ";
  for(int i=0; i < 4; i++){
    cout << l2[i];
  }
  cout << endl;

  return 0;
}
