class MovieCompany:
    def __init__(self, movieCold, movieCompanyName, awards, noOfMovies, movieCategory):
        self.movieCold = movieCold
        self.movieCompanyName = movieCompanyName
        self.awards = awards
        self.noOfMovies = noOfMovies
        self.movieCategory = movieCategory


class MovieSolution:
    def __init__(self, movieList):
        self.movieList = movieList

    def getSecondLargestNoOfmoviesInCategory(self, catName):
        newDict = {}
        for movie in self.movieList:
            for key, value in enumerate(movie.movieCategory):
                count = 0
                if value.lower() == catName.lower():
                    count += 1
                    newDict[movie] = count
        return sorted(newDict.values())[-2].movieCompanyName if len(newDict) >= 2 else None

    def getMovieInCategory(self, catName):
        count = 0
        for val in self.movieList:
            for key, value in enumerate(val.movieCategory):
                if catName.lower() == value.lower():
                    count += 1
        return count if count > 0 else None


MovieCompanyList = []
noOfMovieComp = int(input())
for i in range(noOfMovieComp):
    movieId = input()
    movieCompanyName = input()
    awards = input()
    noOfMovies = int(input())
    movieCategory = {}
    for j in range(noOfMovies):
        movieCategoryName = input()
        movieName = input()
        movieCategory[movieName] = movieCategoryName

    MovieCompanyList.append(MovieCompany(
        movieId, movieCompanyName, awards, noOfMovies, movieCategory))

movieSolutionObject = MovieSolution(MovieCompanyList)
catName = input()
moviesInCat = movieSolutionObject.getMovieInCategory(catName)

if moviesInCat == None:
    print("No movies found in this category")
else:
    print(moviesInCat)

secondLargest = movieSolutionObject.getSecondLargestNoOfmoviesInCategory(
    catName)

if secondLargest == None:
    print("Not enough companies found in this category")
else:
    print(secondLargest)
