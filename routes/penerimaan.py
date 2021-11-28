from fastapi import APIRouter
from models.penerimaan import Penerimaan
from config.database import connection
from schemas.penerimaan import penerimaanEntity, listOfPenerimaanEntity
from bson import ObjectId


penerimaan_router = APIRouter()

#getting all penerimaan
@penerimaan_router.get('/penerimaan')
async def find_all_penerimaan():
    return listOfPenerimaanEntity(connection.local.penerimaan.find())

#get one penerimaan with matching id
@penerimaan_router.get('/penerimaan/{penerimaanId}')
async def find_penerimaan_by_id(penerimaanId):
    return penerimaanEntity(connection.local.penerimaan.find_one({"_id": ObjectId(penerimaanId)}))

#create a penerimaan
@penerimaan_router.post('/penerimaan')
async def create_penerimaan(penerimaan: Penerimaan):
    connection.local.penerimaan.insert_one(dict(penerimaan))
    return listOfPenerimaanEntity(connection.local.penerimaan.find())
    
#update
@penerimaan_router.put('/penerimaan/{penerimaanId}')
async def update_penerimaan(penerimaanId, penerimaan: Penerimaan):
# find the penerimaan and then update it with new penerimaan data
    connection.local.penerimaan.find_one_and_update(
        {"_id": ObjectId(penerimaanId)},
        {"$set": dict(penerimaan)}
    )
    return penerimaanEntity(connection.local.penerimaan.find_one({"_id": ObjectId(penerimaanId)}))

#delete penerimaan
@penerimaan_router.delete('/penerimaan/{penerimaanId}')
async def delete_penerimaan(penerimaanId):
    #finds the penerimaan, delete it and also return the same penerimaan object
    return penerimaanEntity(connection.local.penerimaan.find_one_and_delete({"_id": ObjectId(penerimaanId)}))

