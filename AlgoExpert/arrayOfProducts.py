def arrayOfProducts(array):
    # Write your code here.
	products = []
	product = 1
    for i in range(len(array)):
        for j in range(len(array)):
			if i ==j:
				continue
			product *= array[j]
			print(product)
		products.append(product)
		product = 1
	return products 
