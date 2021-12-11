# Write an algorithm to compute distance between two images. It should work for any sizes of images, even two images can be of different size.
def computeDistance(img1, img2):
    # Convert to grayscale
    img1 = cv2.cvtColor(img1, COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, COLOR_BGR2GRAY)

    # Convert to floating point
    img1 = float32(img1)
    img2 = float32(img2)

    # Flattern the images
    img1 = img1.flatten()
    img2 = img2.flatten()

    # Generating the Count-Histogram-Vector
    RH1 = zeros(256)
    RH2 = zeros(256)
    for i in range(len(img1)):
        RH1[img1[i]] += 1
    for i in range(len(img2)):
        RH2[img2[i]] += 1

    # Calculating the distance
    distance = 0
    for i in range(len(RH1)):
        distance += (RH1[i] - RH2[i])**2
    return distance**0.5
