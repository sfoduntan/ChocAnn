from enum import Enum

class MemberActiveStatus(Enum):
    ACTIVE =  True
    INACTIVE = False

class ProviderActiveStatus(Enum):
    ACTIVE =  True
    INACTIVE = False

class Member(object):
    def __init__(self, memberID, name, socialSecurityNumber):
        self.memberID = memberID
        self.name = name
        self.socialSecurityNumber = socialSecurityNumber
        self.email =  "\0" * 25
        self.streetAddress =  "\0" * 25
        self.city = "\0" * 14
        self.state = "\0" * 2
        self.zipcode = "\0" * 10
        self.status = MemberActiveStatus.ACTIVE

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email
    
    def set_address(self, address):
        self.streetAddress = address

    def get_address(self):
        return self.address

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def get_zipcode(self):
        return self.zipcode

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

class Provider(object):
    def __init__(self, providerID, name):
        self.providerID = memberID
        self.name = name
        self.email =  "\0" * 25
        self.streetAddress =  "\0" * 25
        self.city = "\0" * 14
        self.state = "\0" * 2
        self.zipcode = "\0" * 10
        self.status = ProviderActiveStatus.ACTIVE
        self.services = {}

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email
    
    def set_address(self, address):
        self.streetAddress = address

    def get_address(self):
        return self.address

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def get_zipcode(self):
        return self.zipcode

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
    
    def add_service_code(self, service_code):
        self.services.add(service_code)

    def remove_service_code(self, service_code):
        self.services.remove(service_code)

    def get_services(self):
        return self.services

class ServiceCode(object):
    def __init__(self, serviceCodeID,serviceCodeName):
        self.serviceCodeID = serviceCodeID
        self.serviceCodeName = serviceCodeName

class ProviderDirectoryEntry(object):
    def __init__(self, aProvider, aServiceCode):
        self.provider = aProvider
        self.service = aServiceCode

    def setFee(self, fee):
        self.serviceFee = fee
    
    def getFee(self):
        return self.fee
        
class ProviderDirectory(object):
    def __init__(self):
        providers_directory = []

class Service(object):
    def __init__(self, aProvider, aMember, aServiceCode, aDate, aFee):
        self.provider = aProvider
        self.member =  aMember
        self.serviceCode = aServiceCode
        self.dateOfService = aDate
        self.fee = aFee

    def set_provider(self, provider):
        self.set_provider = provider

    def get_provider(self):
        return self.provider
    
    def set_member(self, member):
        self.set_member = member

    def get_provider(self):
        return self.provider

class  Operator(object):
    def __init__(self, anEployeeID, anEmployeeName, aSupervisor):
        self.employeeID =  anEployeeID
        self.employeeName = anEmployeeName
        self.supervisor = aSupervisor

        def get_employee_ID(self):
            return self.employeeID

        def get_employee_name(self):
            return self.employeeName

class Manager(Operator):
    def __init__(self):
        self.projectID = "\0" * 10

class ChocAnn(object):
    def __init__(self):
        self.members = []
        self.providers = []
        self.provider_directory = ProviderDirectory()

    def get_members(self):
        return self.members

    def get_providers(self):
        return self.providers


