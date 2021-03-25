var inputData = [
    {
        id: 1,
        title: 'hippo',
        faveFood: 'carrots'
    },
    {
        id: 2,
        title: 'Cat',
        faveFood: 'carrots'
    },
    {
        id: 3,
        title: 'ducks',
        faveFood: 'breadcrumbs'
    },
]

findAnimal = function(args) {
    for(x=0; x<3; x++) {
        if(inputData[x].title == args) {
            var answer = inputData[x].faveFood
        }
    }
    return answer
}

console.log(findAnimal('hippo'))