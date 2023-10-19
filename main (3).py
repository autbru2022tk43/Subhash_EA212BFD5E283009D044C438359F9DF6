


def lenearSearchProduct(productList, targetproduct):
  indices = []

  for index, product in enumerate(productList):
   if product == targetproduct:
     indices.append(index)

  return indices


# Example usage:
product = ["shoes", "boot", "loafer", "shoes", "sandles", "shoes"]
target = "shoes"
result = lenearSearchProduct(product, target)
print(result)
  