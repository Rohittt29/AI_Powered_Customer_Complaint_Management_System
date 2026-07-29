"""
Database seed script – Inserts realistic demo data for development and testing.
Usage: python -m scripts.seed_data
"""
import uuid
from datetime import date, datetime


DEMO_COMPLAINTS = [
    {
        "complaint_number": "CMP-2026-0001",
        "complaint_description": "Broken tablets found in blister packaging. Batch BT24051 from Mumbai warehouse. Customer reported approximately 30% of tablets were crumbled upon opening.",
        "complaint_category": "Product Defect",
        "complaint_source": "Customer Call",
        "complaint_date": "2026-07-15",
        "customer": {
            "customer_name": "Rajesh Sharma",
            "email": "rajesh.sharma@healthcorp.in",
            "phone": "+91 9876543210",
            "customer_type": "Distributor",
            "country": "India",
        },
        "product": {
            "product_name": "Aspirin 500mg",
            "batch_number": "BT24051",
            "manufacturing_date": "2026-05-01",
            "expiry_date": "2028-05-01",
        },
    },
    {
        "complaint_number": "CMP-2026-0002",
        "complaint_description": "Discoloration observed in liquid suspension. Color shifted from white to pale yellow. Batch LS24033 stored under recommended conditions.",
        "complaint_category": "Stability Issue",
        "complaint_source": "Quality Audit",
        "complaint_date": "2026-07-18",
        "customer": {
            "customer_name": "Global Pharma Distributors",
            "email": "qa@globalpharma.com",
            "phone": "+1 555-234-5678",
            "customer_type": "Wholesaler",
            "country": "United States",
        },
        "product": {
            "product_name": "Amoxicillin Suspension 250mg/5ml",
            "batch_number": "LS24033",
            "manufacturing_date": "2026-03-15",
            "expiry_date": "2027-03-15",
        },
    },
    {
        "complaint_number": "CMP-2026-0003",
        "complaint_description": "Incorrect labeling on outer carton. The dosage printed reads 100mg instead of 200mg. Affects entire shipment of 5000 units.",
        "complaint_category": "Labeling Error",
        "complaint_source": "Distributor Report",
        "complaint_date": "2026-07-20",
        "customer": {
            "customer_name": "MedSupply GmbH",
            "email": "complaints@medsupply.de",
            "phone": "+49 30 1234567",
            "customer_type": "Distributor",
            "country": "Germany",
        },
        "product": {
            "product_name": "Metformin HCl 200mg",
            "batch_number": "MF24072",
            "manufacturing_date": "2026-07-01",
            "expiry_date": "2028-07-01",
        },
    },
    {
        "complaint_number": "CMP-2026-0004",
        "complaint_description": "Patient reported allergic reaction after taking medication. Suspected cross-contamination with peanut-derived excipient. Requires immediate investigation.",
        "complaint_category": "Adverse Event",
        "complaint_source": "Hospital Report",
        "complaint_date": "2026-07-22",
        "customer": {
            "customer_name": "City General Hospital",
            "email": "pharmacovigilance@citygeneral.org",
            "phone": "+44 20 7946 0958",
            "customer_type": "Hospital",
            "country": "United Kingdom",
        },
        "product": {
            "product_name": "Cetirizine 10mg",
            "batch_number": "CT24065",
            "manufacturing_date": "2026-06-15",
            "expiry_date": "2028-06-15",
        },
    },
    {
        "complaint_number": "CMP-2026-0005",
        "complaint_description": "Temperature excursion during transit. Cold-chain shipment reached 12°C for 4 hours. Insulin batch requires efficacy re-validation.",
        "complaint_category": "Storage/Transport",
        "complaint_source": "Logistics Alert",
        "complaint_date": "2026-07-25",
        "customer": {
            "customer_name": "PharmaCold Logistics",
            "email": "ops@pharmacold.com",
            "phone": "+1 800-555-0199",
            "customer_type": "Logistics Partner",
            "country": "United States",
        },
        "product": {
            "product_name": "Insulin Glargine 100 IU/ml",
            "batch_number": "IG24088",
            "manufacturing_date": "2026-07-10",
            "expiry_date": "2027-01-10",
        },
    },
]


def seed():
    """
    Print demo data to stdout. When database persistence is implemented,
    this function should use SQLAlchemy to insert records.
    """
    print("=" * 60)
    print("  QMS AI COPILOT – SEED DATA")
    print("=" * 60)
    for i, complaint in enumerate(DEMO_COMPLAINTS, 1):
        print(f"\n--- Complaint {i}: {complaint['complaint_number']} ---")
        print(f"  Category   : {complaint['complaint_category']}")
        print(f"  Source     : {complaint['complaint_source']}")
        print(f"  Customer   : {complaint['customer']['customer_name']}")
        print(f"  Product    : {complaint['product']['product_name']}")
        print(f"  Batch      : {complaint['product']['batch_number']}")
        print(f"  Description: {complaint['complaint_description'][:80]}...")

    print(f"\n✅ {len(DEMO_COMPLAINTS)} demo complaints ready for insertion.")
    print("   Connect to database and run `seed()` with SQLAlchemy session to persist.")


if __name__ == "__main__":
    seed()
