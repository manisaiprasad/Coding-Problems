def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)

	backRow = "blue" if redShirtHeights[0] < blueShirtHeights[0] else "red"

	for height in range(len(redShirtHeights)):
		if backRow == "blue":
			if redShirtHeights[height] >= blueShirtHeights[height]:
				return False
		if backRow == "red":
			if blueShirtHeights[height] >= redShirtHeights[height]:
				return False
    return True
