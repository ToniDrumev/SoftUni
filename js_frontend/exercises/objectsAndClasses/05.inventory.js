function solve(input) {
    const heroes = []

    for (const line of input) {
        let [heroName, level, items] = line.split(' / ');
        
        let hero = {
            name: heroName,
            level: Number(level),
            items: items.split(', '),
        }

        heroes.push(hero);
    }

    const filretedHeroes = heroes.slice().sort((a, b) => a.level - b.level);

    for (const hero of filretedHeroes) {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items.join(', ')}`);
    }
}
