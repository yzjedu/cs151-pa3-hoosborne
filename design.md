* Purpose: Take user choice for type of ASCII art.
* Name: user_choice_input
* Parameters: none
* Return: choice
* Algorithm:
  1. Prompt user to enter whether they would like to randomly generate an ASCII art, create a custom, or create a circle. (random, custom, circle)
  2. Check if choice does not equal random, custom, circle,
     1. Re-prompt user to enter a valid choice 
     2. Return choice


* Purpose: randomly generate an integer to pick a random design
* Name: random_design_generate 
* Parameters: none
* Return: none
* Algorithm:
  1. Generate a random integer between 1 and 3
  2. Check if random_int equals 1:
     1. call print_design_1 function
  3. Check if random_int equals 2:
     1. Call print_design_2 function
  4. Check if random_int equals 3
     1. Call print_design_3 function


* Purpose: print out 1st random design
* Name: print_design_1 
* Parameters: none
* Return: none
* Algorithm:
  1. Output "^      ^" with 10 spaces centered
  2. Output "(  \__/  )" with 10 spaces centered
  3. Output "[  0  0  ]   $" with 10 spaces centered 
  4. Output "/  \/  \   /" with 14 spaces centered
  5. Output "/_u____u_\ /" with 10 spaces centered
  6. Output "^      ^" with 10 spaces centered


* Purpose: print out 2nd random design
* Name: print_design_2 
* Parameters: none
* Return: none
* Algorithm:
  1. Output "_____" with 10 spaces centered
  2. Output "_|___|_   %" with 14 spaces centered
  3. Output "(( ^_^ )) /" with 10 spaces centered 
  4. Output "_/   \__/" with 10 spaces centered
  5. Output "/_____\" with 10 spaces centered
  6. Output "_|   |_" with 10 spaces centered


* Purpose: print out 3rd random design
* Name: print_design_3 
* Parameters: none
* Return: none
* Algorithm:
  1. Output "_\/_" with 12 spaces centered
  2. Output "/\" with 12 spaces centered
  3. Output "/\" with 12 spaces centered 
  4. Output "/  \" with 12 spaces centered
  5. Output "/~~\o" with 12 spaces centered
  6. Output "/o   \" with 12 spaces centered
  7. Output "/~~*~~~\" with 12 spaces centered
  8. Output "o/    o \" with 12 spaces centered
  9. Output "/~~~~~~~~\" with 12 spaces centered
  10. Output "/__*_______\" with 10 spaces centered
  11. Output "||" with 12 spaces centered


* Purpose: Print a circle
* Name: circle_print
* Parameters: none
* Return: choice
* Algorithm:
  1. Set circle_list to equal [6, 12, 14, 14, 12, 6]
  2. for num in circle_list: 
     1. output "*" multiplied by num centered in between 20 spaces
  3. return

  
* Purpose: collect and output user custom design
* Name: user_custom_input
* Parameters: none
* Return: none
* Algorithm:
  1. set variable count to equal zero
  2. Prompt user to enter the character they would like to use
  3. Prompt user to enter the number of columns they want
  4. Call error_int_function
  5. Prompt user to enter the number of rows they want 
  6. Call error_int_function
  7. While count < rows:
     1. Output (character * columns)
     2. Add 1 to count
  8. return


* Purpose: check if a variable is an valid integer
* Name: error_check_int
* Parameters: amount
* Return: amount
* Algorithm:
  1. while not amount is digit:
     2. prompt user to enter a valid integer
  3. return


* Purpose: display ASCII art and string decorations to the user.
* Name: Main
* Parameters: none
* Return: none
* Algorithm:
  1. Print welcome message and program purpose
  2. Set continue_choice to be an empty string
  3. While continue_choice doesn't equal yes or no
     4. Re-prompt user to enter continue_choice
  3. While continue_choice doesn't equal no:
     1. Call user_choice_input function
     2. Check if user_choice equals 'random':
        1. Call random_design_generate function
     3. Otherwise, Check if user_choice equals 'circle':
        1. Call circle_print function
     4. Otherwise, Check if user_choice equals 'custom'
        1. Call user_custom_input function
  4. Output a thanks/ending message 

1. Run Main
_____________________________________________________________________________________





       ^      ^
      (  \__/  )
      [  0  0  ]   $
       /  \/  \   /
      /_u____u_\ /
      0        0
design 1

        _____
       _|___|_   %
      (( ^_^ )) /
      __/   \__/ 
       /_____\
       _|   |_
design 2


        _\/_
         /\
         /\
        /  \
        /~~\o
       /o   \
      /~~*~~~\
     o/    o \
     /~~~~~~~~\~`
    /__*_______\
         ||
design 3

        ******    
     ************
    **************  
    **************
     ************
        ******

circle design 