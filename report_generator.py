import os
import psycopg2
import pandas as pd
from datetime import datetime

def generate_financial_report():
    print("🧠 [AI BRAIN] Initializing Automated Financial Audit...")
    
    # 1. Database Connection Configuration
    # In production, these should be securely stored in environment variables
    db_config = {
        "dbname": os.getenv("DB_NAME", "synergy_db"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "your_password"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432")
    }
    
    # 2. Query B: Financial Profit & Performance Analytics
    query = """
    SELECT 
        od.item_name,
        SUM(od.quantity) AS total_units_sold,
        SUM(od.quantity * od.selling_price) AS gross_revenue,
        SUM(od.quantity * (od.selling_price - inv.unit_cost)) AS net_profit,
        ROUND((SUM(od.quantity * (od.selling_price - inv.unit_cost)) / SUM(od.quantity * od.selling_price)) * 100, 2) AS profit_margin_percentage
    FROM order_details od
    JOIN inventory_stocks inv ON od.item_name = inv.item_name
    GROUP BY od.item_name
    ORDER BY net_profit DESC;
    """
    
    try:
        # Establish connection to PostgreSQL
        conn = psycopg2.connect(**db_config)
        
        # Load query results directly into a Pandas DataFrame
        print("📊 [AI BRAIN] Fetching real-time transactional data from PostgreSQL...")
        df = pd.read_sql_query(query, conn)
        
        # Close the database connection
        conn.close()
        
        # 3. Generate the Automated Report
        current_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"Financial_Performance_Report_{current_date}.xlsx"
        
        print(f"💾 [AI BRAIN] Structuring and exporting analytical insights to Excel...")
        
        # Export to Excel using openpyxl backend
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name="Profit Analytics", index=False)
            
        print(f"✅ [NERVOUS SYSTEM] Success! Report generated successfully as: {filename}")
        print("👤 Lead Architect: Wilfredo Bolbes")
        
    except Exception as e:
        print(f"❌ [SYSTEM ERROR] Failed to execute automated report: {str(e)}")

if __name__ == "__main__":
    generate_financial_report()
