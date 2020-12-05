from typing import List


class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            result.append(products[:3])
        return result


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()

        for k, v in enumerate(searchWord):
            currentWord = searchWord[:k + 1]
            currentList = []

            for product in products:
                if product.startswith(currentWord):
                    currentList.append(product)
                    if len(currentList) == 3:
                        break

            result.append(currentList)

        return result


if True:
    s = Solution()
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    res = s.suggestedProducts(products, searchWord)
    print("Result ", res)

if True:
    s = Solution()
    products = ["havana"]
    searchWord = "havana"
    res = s.suggestedProducts(products, searchWord)
    print("Result ", res)

if True:
    s = Solution()
    products = ["bags", "baggage", "banner", "box", "cloths"]
    searchWord = "bags"
    res = s.suggestedProducts(products, searchWord)
    print("Result ", res)

if True:
    s = Solution()
    products = ["havana"]
    searchWord = "tatiana"
    res = s.suggestedProducts(products, searchWord)
    print("Result ", res)

