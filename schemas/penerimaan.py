#schemas membantu serialize dan juga convert mongodb format ke json

def penerimaanEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "kd_akun" : db_item["kd_akun"],
        "jumlah" : db_item["jumlah"],
        "tgl_transaksi" : db_item["tgl_transaksi"]
    }

def listOfPenerimaanEntity(db_item_list) -> list:
    list_penerimaan_entity = []
    for item in db_item_list:
        list_penerimaan_entity.append(penerimaanEntity(item))
    return list_penerimaan_entity