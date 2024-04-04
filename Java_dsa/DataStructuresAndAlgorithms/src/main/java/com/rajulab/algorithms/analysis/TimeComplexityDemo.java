package com.rajulab.algorithms.analysis;

public class TimeComplexityDemo {

    public static  void  main(String[] args) {
        System.out.println("Time complexity");

        double now = System.currentTimeMillis();
        System.out.println(findSum(99999));


        System.out.println("Time taken - by  findSum is " + (System.currentTimeMillis() -now) + " millisecond.");

        System.out.println("Time taken - by findSumV2 is  " + (System.currentTimeMillis() -now) + " millisecond.");

    }

    public  static int findSum(int n){
        return  n* (n + 1)/2;
    }


    public  static int findSumV2(int n){
        int sum =0;

        for (int i=0; i<=n; i++){
            sum = sum +1;
        }
        return  sum;
    }
}
