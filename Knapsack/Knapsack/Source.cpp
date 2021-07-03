#include <stdio.h>
int items[100] = {2,1,3,2};
int values[100] = {3,2,4,2 };
int dp[100][2001] = { 0 };
int n = 4;
int size = 5;
int max(int a, int b) {
	return a > b ? a : b;
}
int knapsack(int items[], int values[], int size) {
	

	for (int i = 0; i < n; i++) {
		for (int j = 1; j <= size; j++) {
			if (items[i] <= j) {
				dp[i+1][j] = max(dp[i][j],values[i] + dp[i][j - items[i]]);									
			}
			else {
				dp[i+1][j] = dp[i][j];
			}
		}
	}
	return dp[n][size];
}

int main(int argc, char** argv) {
	int n;
	n = knapsack(items, values, size);
	printf("%d\n", n);
	return 0;
}