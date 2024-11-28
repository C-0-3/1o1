def CutRod(prices, n): 
    if n == 0: 
        return 0 
    else: 
        T = [[0] * (n + 1) for _ in range(n)] 
        for i in range(n): 
            for j in range(n + 1): 
                if (i-1) < 0: 
                    if (j - i - 1) < 0: 
                        T[i][j] = 0 
                    else: 
                        T[i][j] = prices[i] + T[i][j-i-1] 
                elif (j - i - 1) < 0: 
                    T[i][j] = T[i-1][j] 
                else: 
                    T[i][j] = max(T[i-1][j], prices[i] + T[i][j-i-1]) 
                    
        for t in T:
            print(t)
            print("Maximum Profit = ", T[len(T)-1][len(T[0])-1]) 
                        
cutPrices = [2, 5, 7, 8] 
# cutPrices = [1, 5, 8, 9, 10, 17, 17, 20] 
# cutPrices = [1, 5, 8, 10, 14, 8, 9, 7, 4, 13] 
cutSize = len(cutPrices) 
CutRod(cutPrices, cutSize)