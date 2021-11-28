from pydantic import BaseModel


class Penerimaan(BaseModel):
    kd_akun : str
    jumlah : str
    tgl_transaksi : str


