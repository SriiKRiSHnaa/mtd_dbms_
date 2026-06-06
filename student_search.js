const { MongoClient } = require('mongodb');
const readline = require('readline');

const url = 'mongodb+srv://<username>:<password>@<host>/';
const client = new MongoClient(url);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function searchStudent() {

    await client.connect();

    const db = client.db('college');
    const collection = db.collection('student');

    rl.question("Enter Partial Name to Search: ", async (partialName) => {

        const result = await collection.find({
            name: { $regex: partialName, $options: 'i' }
        }).toArray();

        console.log("\nMatching Students:");

        console.log(result);

        rl.close();
        client.close();
    });
}

searchStudent();