# BlockChain_eVoting <br/>

### Blockchain Based E-Voting using Rest APIs

It a blockchain based python app that provide eVoting using Rest API.

> It uses FastAPI for API developement

> How to run => `python3 main.go`

> After running, Go to `127.0.0.1:8000/` for voting.

## Features:

- Support admin access using access token
- Support Organisation registration for voting
- Support Organisatio based vote counting

## Awailable API routes:

`/admin/start` => POST | For starting the voting

`/admin/stop` => POST | For stoping the voting

`/voter/vote` => POST | For casting the vote

`/getvotes` => GET | For getting total casted votes

`/getvotesbyorg` => GET | For getting votes count for each organisation

> Use `\docs` for swagger API documentation
