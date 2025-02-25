def kidsWithCandies(self, candies, extraCandies):
        if len(candies) < 1: 
            return []

        maxNCandies = candies[0]
        for kid in candies:
            maxNCandies = max(maxNCandies, kid)
        
        result = []
        for i, kid in enumerate(candies):
            if kid + extraCandies >= maxNCandies:
                result.append(True)
                continue
            result.append(False)

        return result