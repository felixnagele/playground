package io.github.felixnagele.calculatorplusplus;

import java.util.Scanner;

public class Calculator
{

	public Calculator()
	{

	}

	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);				// +,-,*,/ 1 Number, 2 Number

		int number1;
		int number2;
		String operator;
		long sum;
		long difference;
		long product;
		double quotient;

		System.out.println("Please enter the first number:");
		number1 = scan.nextInt();
		System.out.println("Please enter the second number:");
		number2 = scan.nextInt();
		System.out.println("Please enter the operator (+, -, *, /):");
		operator = scan.next();

		if(operator.equals("+"))			// sum
		{
			sum = number1 + number2;
			System.out.println(sum);
		}
		if(operator.equals("-"))			// difference
		{
			difference = number1 - number2;
			System.out.println(difference);
		}
		if(operator.equals("*"))			// product
		{
			product = number1 * number2;
			System.out.println(product);
		}
		if(operator.equals("/"))			// quotient
		{
			quotient = (double)number1 / (double)number2;
			System.out.println(quotient);
		}

		scan.close();

	}

}
