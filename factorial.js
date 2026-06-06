input_num = 5

console.log(`Input number: ${input_num}`);

factorial_number = 1;

if (input_num == 0 || input_num == 1)
    console.log(`Factorial of ${input_num} is 1`);
else 
    for (let i = 2; i <= input_num; i++) 
        factorial_number *= i;

console.log(`Factorial of ${input_num} is ${factorial_number}`);
