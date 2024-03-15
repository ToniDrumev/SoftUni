function solve(catsArray) {
    class Cat {
        constructor(catName, catAge) {
            this.catName = catName;
            this.catAge = catAge;
        }

        meow() {
            console.log(`${this.catName}, age ${this.catAge} says Meow`);
        }
    }

    let cats = catsArray.map(str => {
        let [name, age] = str.split(' ');
        return new Cat(name, age);
    });

    cats.forEach(cat => {
        cat.meow();
    });
}
