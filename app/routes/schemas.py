from pydantic import BaseModel, field_validator



class RequestChat(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def msgLength(cls, message):
        if len(message) > 1000:
            # summarize the input 
            # need to finish the function
            pass
        return message

class ResponseChat(BaseModel):
    message: str
    
