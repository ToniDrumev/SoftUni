function solve(stock, orders) {
    let store = {};

    for (let i = 0; i < stock.length; i += 2) {
        let productName = stock[i];
        let quantity = Number(stock[i + 1]);

        store[productName] = quantity;
    }

    for (let i = 0; i < orders.length; i += 2) {
        let productName = orders[i];
        let quantity = Number(orders[i + 1]);

        if (!store[productName]) {
            store[productName] = 0;
        }

        store[productName] += quantity;
    }

    for (const product in store) {
        console.log(`${product} -> ${store[product]}`);
    }
}
