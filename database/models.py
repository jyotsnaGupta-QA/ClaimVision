from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    NVARCHAR,
    func,
)
from sqlalchemy.orm import relationship

from database.db import Base


class Customer(Base):
    __tablename__ = "Customers"

    CustomerId = Column(Integer, primary_key=True, index=True)
    FullName = Column(NVARCHAR(100), nullable=False)
    Email = Column(NVARCHAR(100))
    PhoneNumber = Column(NVARCHAR(20))
    CreatedDate = Column(DateTime, server_default=func.now())

    vehicles = relationship("Vehicle", back_populates="customer")
    claims = relationship("Claim", back_populates="customer")


class Vehicle(Base):
    __tablename__ = "Vehicle"

    VehicleId = Column(Integer, primary_key=True, index=True)
    CustomerId = Column(Integer, ForeignKey("Customers.CustomerId"))

    VehicleNumber = Column(NVARCHAR(20))
    VehicleBrand = Column(NVARCHAR(50))
    VehicleModel = Column(NVARCHAR(50))
    VehicleYear = Column(Integer)
    InsurancePolicyNumber = Column(NVARCHAR(50))

    customer = relationship("Customer", back_populates="vehicles")
    claims = relationship("Claim", back_populates="vehicle")


class Claim(Base):
    __tablename__ = "Claims"

    ClaimId = Column(Integer, primary_key=True, index=True)

    CustomerId = Column(Integer, ForeignKey("Customers.CustomerId"))
    VehicleId = Column(Integer, ForeignKey("Vehicle.VehicleId"))

    AccidentDate = Column(DateTime)
    AccidentLocation = Column(NVARCHAR(200))
    Description = Column(NVARCHAR(500))

    Status = Column(NVARCHAR(50))
    CreatedDate = Column(DateTime, server_default=func.now())

    customer = relationship("Customer", back_populates="claims")
    vehicle = relationship("Vehicle", back_populates="claims")

    images = relationship("UploadedImage", back_populates="claim")
    assessments = relationship("DamageAssessment", back_populates="claim")


class UploadedImage(Base):
    __tablename__ = "UploadedImages"

    ImageId = Column(Integer, primary_key=True, index=True)
    ClaimId = Column(Integer, ForeignKey("Claims.ClaimId"))

    ImagePath = Column(NVARCHAR(300))
    UploadedDate = Column(DateTime, server_default=func.now())

    claim = relationship("Claim", back_populates="images")


class DamageAssessment(Base):
    __tablename__ = "DamageAssessment"

    AssessmentId = Column(Integer, primary_key=True, index=True)
    ClaimId = Column(Integer, ForeignKey("Claims.ClaimId"))

    DamageType = Column(NVARCHAR(100))
    Severity = Column(NVARCHAR(50))
    EstimatedCost = Column(Numeric(10, 2))
    FraudScore = Column(Float)
    Recommendation = Column(NVARCHAR(200))
    Confidence = Column(Float)

    ProcessedImagePath = Column(NVARCHAR(300))
    CreatedDate = Column(DateTime,server_default=func.now())

    claim = relationship("Claim", back_populates="assessments")
    
  