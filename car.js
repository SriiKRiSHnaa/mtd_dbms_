const car = {
    brand: "Toyota",
    model: "Innova",
    color: "White",
    price: 2500000
};

console.log("Original Object:");
console.log(car);

console.log("\nObject Properties:");

for (let key in car) {
    console.log(key + " : " + car[key]);
}

// Delete second property (model)
delete car.model;

console.log("\nAfter Deleting Second Property:");
console.log(car);

// Get length of object
const length = Object.keys(car).length;

console.log("\nLength of Object:");
console.log(length);