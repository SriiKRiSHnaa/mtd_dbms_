const { MongoClient } = require('mongodb');
const readline = require('readline');

const url = 'mongodb+srv://srikrishnabiradar2k06_db_user:SriKrishna04@cluster0.mdssd4g.mongodb.net/';
const client = new MongoClient(url);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function insertStudent() {

    await client.connect();

    const db = client.db('college');
    const collection = db.collection('student');

    rl.question("Enter USN: ", (usn) => {

        rl.question("Enter Name: ", (name) => {

            rl.question("Enter Semester: ", (sem) => {

                rl.question("Enter Year of Admission: ", async (year) => {

                    const student = {
                        usn: usn,
                        name: name,
                        sem: parseInt(sem),
                        year_of_admission: parseInt(year)
                    };

                    const result = await collection.insertOne(student);

                    console.log("Student Inserted Successfully");
                    console.log(result);

                    rl.close();
                    client.close();
                });
            });
        });
    });
}

insertStudent();