from pydantic import BaseModel

class MtrDocumentRequest(BaseModel):
    # is_active: bool
    document_type_id: int
    brand_id: int
    profit_center_id: int
    transaction_type_id: int
    bank_company_id: int
    reset_frequency_id: int
    document_name: str
    document_format: str
    document_reference: bool
    signature_employee_1: int
    signature_title_1: str
    signature_employee_2: int
    signature_title_2: str
    signature_employee_3: int
    signature_title_3: str
    signature_employee_4: int
    signature_title_4: str
    document_source_doc_prefix: str
    document_brand_prefix: str
    document_profit_cost_center_prefix: str
    document_transaction_type_prefix: str
    document_bank_acc_prefix: str
    document_auto_number: bool

    

class MtrDocumentSchema(MtrDocumentRequest):
    is_active: bool
    document_id: int

    class Config:
        orm_mode = True