def count_mean(arr):
    return sum(arr)/len(arr)

def email_validator(email):
    if email.count('@')==1 and email.count('.')==1:
        return True
    else:
        return False 
        
def test_email_validator():
    assert email_validator('julie.lu@se.com') == True
    assert email_validator('julie@lu@se.com') == False
