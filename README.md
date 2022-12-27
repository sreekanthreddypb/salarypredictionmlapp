# salarypredictionmlapp

run flask locally(install module required for this application) or run using docker

docker run -p 0.0.0.0:5000:5000 sreekanthreddypb/salaryapp:latest

for testing
GET http://localhost:5000/hi




POST http://127.0.0.1:5000/api
{
    "exp":10
}
it will give expected salary for 10 years of experience
