function solve(base, increment) {
    let stoneRequired = 0;
    let marbleRequired = 0;
    let lapisLazuliRequired = 0;
    let goldRequired = 0;
    let pyramidHeight = 0;
    let step = 0;

    for (let i = base; i > 0; i -= 2) {
        pyramidHeight += increment;
        step += 1;

        if (base > 2) {
            if (step % 5 === 0) {
                lapisLazuliRequired += (base - 1) * 4 * increment;
            } else {
                marbleRequired += (base - 1) * 4 * increment;
            }

            stoneRequired += ((base - 2) ** 2) * increment;
        } else {
            goldRequired += (base ** 2) * increment;
        }

        base -= 2;
    }

    console.log(`Stone required: ${Math.round(stoneRequired)}`);
    console.log(`Marble required: ${Math.round(marbleRequired)}`);
    console.log(`Lapis Lazuli required: ${Math.round(lapisLazuliRequired)}`);
    console.log(`Gold required: ${Math.round(goldRequired)}`);
    console.log(`Final pyramid height: ${Math.trunc(pyramidHeight)}`);
}

solve(20, 1)