function solve(input) {
    let movies = [];
    for (const line of input) {
        if (line.includes('addMovie')) {
            let name = line.split('addMovie ')[1];

            movies.push({
                name,
            });
        } else if (line.includes('directedBy')) {
            let name = line.split(' directedBy ')[0];
            let director = line.split(' directedBy ')[1];

            movies.forEach(movie => {
                if (Object.values(movie).includes(name)) {
                    movie['director'] = director;
                }
            });

        } else if (line.includes('onDate')) {
            let name = line.split(' onDate ')[0];
            let date = line.split(' onDate ')[1];

            movies.forEach(movie => {
                if (Object.values(movie).includes(name)) {
                    movie['date'] = date;
                }
            });
        }
    }

    let filteredMovies = movies.filter(movie => Object.keys(movie).includes('director') && Object.keys(movie).includes('date'));

    return filteredMovies.map(movie => JSON.stringify(movie)).join('\n');
}
