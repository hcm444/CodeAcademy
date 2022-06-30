//adds total of odd and even values of an array

#include <iostream>
#include <vector>
int main() {
  int total_even = 0;
  int product_odd = 1;
  std::vector<int> vector = {1, 2, 3, 4, 5};
  for (int i = 0; i < vector.size(); i++) {
  if ((i+1) % 2 == 0){
    std::cout << "even";
    total_even = total_even + vector[i];
  }
  else{
    std::cout << "odd";
    product_odd = product_odd * vector[i];
  }
  
}
  std::cout << "\n";
  std::cout << "Sum of even: " << total_even << "\n";
  std::cout << "Product of odd: " << product_odd;
};
  
