from typing import List, Optional, Union
from pydantic import BaseModel, Field, EmailStr

class Candidate(BaseModel):
    """Represents a candidate's personal, contact, and professional details."""
    honorifics: Optional[str] = Field(default=None, description="Honorific title (e.g., Dr., Prof.)")
    first_name: Optional[str] = Field(default=None, description="Candidate's given first name")
    middle_name: Optional[str] = Field(default=None, description="Middle name if applicable")
    last_name: Optional[str] = Field(default=None, description="Surname or family name")
    suffix: Optional[str] = Field(default=None, description="Suffix (e.g., Jr., Sr.)")
    phone_no: Optional[str] = Field(default=None, description="Primary contact number")
    mobile_no: Optional[str] = Field(default=None, description="Mobile phone number")
    fax: Optional[str] = Field(default=None, description="Fax number")
    email: Optional[EmailStr] = Field(default=None, description="Valid email address")
    address1: Optional[str] = Field(default=None, description="Primary street address")
    address2: Optional[str] = Field(default=None, description="Secondary address line")
    city: Optional[str] = Field(default=None, description="City of residence")
    state: Optional[str] = Field(default=None, description="State or province")
    country: Optional[str] = Field(default=None, description="Country of residence")
    zip_code: Optional[str] = Field(default=None, description="Postal/ZIP code")
    dr_degree: Optional[str] = Field(default=None, description="Doctorate degree (e.g., PhD, MD)")

class Education(BaseModel):
    institution_name: Optional[str] = Field(default=None, description="Educational institution name")
    degree_diploma: Optional[str] = Field(default=None, description="Degree or diploma obtained")
    specialty: Optional[str] = Field(default=None, description="Field of study or specialty")
    completion_year: Optional[int] = Field(default=None, description="Year of completion")
    completion_month: Optional[str] = Field(default=None, description="Month of completion")

class License(BaseModel):
    issuer: Optional[str] = Field(default=None, description="Issuing organization or authority")
    license_type: Optional[str] = Field(default=None, description="Type of license issued")
    license_no: Optional[str] = Field(default=None, description="Unique license number")
    state: Optional[str] = Field(default=None, description="State where the license is issued")
    country: Optional[str] = Field(default=None, description="Country of issuance")
    issue_date: Optional[str] = Field(default=None, description="License issue date")
    exp_date: Optional[str] = Field(default=None, description="License expiration date")

class OrganizationAffiliation(BaseModel):
    organization_name: Optional[str] = Field(default=None, description="Name of the affiliated organization")
    address: Optional[str] = Field(default=None, description="Address of the organization")
    role: Optional[str] = Field(default=None, description="Role within the organization")
    status: Optional[str] = Field(default=None, description="Current status of the affiliation")

class Training(BaseModel):
    course_title: Optional[str] = Field(default=None, description="Title of the training course")
    provider: Optional[str] = Field(default=None, description="Training provider or organization")
    completion_date: Optional[str] = Field(default=None, description="Date of course completion")
    expiration_date: Optional[str] = Field(default=None, description="Date of certification expiration")
    status: Optional[str] = Field(default=None, description="Current certification status")

class Experience(BaseModel):
    organization_name: Optional[str] = Field(default=None, description="Name of the organization")
    job_role: Optional[str] = Field(default=None, description="Job role or position held")
    start_year: Optional[int] = Field(default=None, description="Year the job started")
    start_month: Optional[str] = Field(default=None, description="Month the job started")
    completion_year: Optional[int] = Field(default=None, description="Year the job ended")
    completion_month: Optional[str] = Field(default=None, description="Month the job ended")

class Resume(BaseModel):
    """Structured resume information"""
    candidate_details: Candidate = Field(..., description="Candidate details")
    education: List[Education] = Field(default_factory=list, description="List of education entries")
    experience: List[Experience] = Field(default_factory=list, description="List of work experiences")
    skills: Optional[List[OrganizationAffiliation]] = Field(default_factory=list, description="List of skills or affiliations")
    certifications: List[Training] = Field(default_factory=list, description="List of certifications")

class ConversationalResponse(BaseModel):
    response: str = Field(..., description="Conversational response to the user")

class FinalResponse(BaseModel):
    final_output: Union[Resume, ConversationalResponse]
