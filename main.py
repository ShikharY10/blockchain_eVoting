from pydantic import BaseModel
from fastapi import FastAPI
from blockchain.chain import Chain
from db.userdata import UserData
import utils
import sys

print("Starting Decentralised Voting System")
token = input("Create a access token: ")
orgDetails = utils.takeOrgDetails()

if len(orgDetails.keys()) < 2:
    print("At least two organisation shoudl be registered")
    sys.exit(1)

chain = Chain(10)
userData = UserData()

orgVoteCount: "dict[str, list[str]]" = {}
print("Voting system is ready")

controller = {
    "isStarted": False,
    "isStoped": False
}

app = FastAPI()

@app.post("/admin/start")
def startVoting(item: utils.Token):
    if (item.token == token):
        controller["isStarted"] = True
        print("System is running: Voter can cast there vote")
        return {
            "status": "started"
        }

@app.post("/admin/stop")
def stopVoting(item: utils.Token):
    if item.token == token:
        controller["isStoped"] = True
        print("System is stoped")
        return {
            "status": "stoped"
        }

@app.post("/voter/vote")
def CastVote(item: utils.Vote):
    if controller["isStarted"]:
        if item.userId in userData.data:
            try:
                orgName = orgDetails[item.orgCode]
                chain.add_to_pool(orgName)
                hash: str = chain.mine()
                try:
                    votes = orgVoteCount[orgName]
                    votes.append(hash)
                    orgVoteCount[orgName] = votes
                except KeyError:
                    orgVoteCount[orgName] = [hash]
                return {
                    "status": "successfull"
                }
            except KeyError:
                return {
                    "status": "Invalid Organisation Details"
                }
        else:
            return {
                    "status": "Invalid userId"
                }
    else:
        return {
                    "status": "Voting is closed or it is not started"
                }

@app.get("/getvotes")
def getTotalVotes():
    if not controller["isStoped"]:
        return {
            "total_votes": 0,
            "status": "Voting is currently running"
        }
    return {
        "total_votes" : len(chain.blocks)-1,
        "status": "voting has been stoped"
    }

@app.get("/getvotesbyorg")
def getVotesByOrg():
    if not controller["isStoped"]:
        return {
            "status": "Voting is currently running"
        }
    result = {}
    for i in range(len(orgVoteCount.keys())):
        org = list(orgVoteCount.keys())[i]
        count = len(list(orgVoteCount.values())[i])
        result[org] = count
    return result

# admin/start - POST - secured
# admin/stop - POST - secured
# admin/getTotalVoteCount  - GET - access is possible only after the voting stop

# voter/vote - POST - unsecured
# voter/getTotalVoteCount - GET - access is possible only after the voting stop
