# THE HUMAN-AI SYNERGY ARCHITECTURE: CORE-ANALYTICS-ENGINE

An enterprise framework integrating AI as the computational Brain with human execution as the Heart & Nervous System. Features advanced SQL analytics for real-time finance auditing, dynamic inventory reorder controls, and end-to-end supply chain optimization. The ultimate blueprint for next-gen business scalability. 🚀📊

---

## 🏛️ 1. SYSTEM ARCHITECTURE (Ang Buhay na Sistema)

Ang framework na ito ay binuo bilang isang Buhay na Organismo kung saan ang tao at teknolohiya ay nagkakaisa para sa pinakamataas na antas ng kahusayan:

* **The Human as the HEART (Ang Puso):** Ang nagpapasya, nagtatakda ng vision, etika, at nagbibigay ng "buhay" at organic connection sa brand na hindi kayang tularan ng sintetikong algorithm.
* **The AI as the BRAIN (Ang Utak):** Ang taga-analisa ng malalaking data, taga-kwenta ng komplikadong formulas, at tagapamahala ng digital automation sa loob ng ilang segundo upang maalis ang human error.
* **The Human as the NERVOUS & VASCULAR SYSTEM (Ang mga Ugat):** Ang daloy ng buhay na nagpapakilos sa kapital, nagpapatakbo sa supply chain, nakikipag-ugnayan sa mga supplier, at nagpapatupad ng mga digital na stratehiya sa totoong buhay.

---

## 🗂️ 2. DATABASE SCHEMA DESIGN (PostgreSQL)

```sql
-- 1. INVENTORY MODULE (Raw Materials & Stocks)
CREATE TABLE inventory_stocks (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    current_qty INT NOT NULL DEFAULT 0,
    reorder_point INT NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    supplier_contact VARCHAR(100)
);

-- 2. SALES MODULE (GCash Transactions Only)
CREATE TABLE sales_orders (
    order_id SERIAL PRIMARY KEY,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    customer_name VARCHAR(100),
    customer_contact VARCHAR(15),
    delivery_location VARCHAR(150),
    payment_method VARCHAR(20) DEFAULT 'GCash Only',
    gcash_ref_no VARCHAR(50) UNIQUE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    order_status VARCHAR(20) DEFAULT 'Pending'
);

-- 3. ORDER DETAILS (Breakdown of Items Sold)
CREATE TABLE order_details (
    detail_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES sales_orders(order_id),
    item_name VARCHAR(100),

SELECT 
    item_name, 
    category, 
    current_qty, 
    reorder_point,
    (reorder_point - current_qty) AS shorted_quantity,
    CASE 
        WHEN current_qty <= (reorder_point * 0.2) THEN 'CRITICAL: RESTOCK IMMEDIATELY'
        ELSE 'WARNING: LOW STOCK'
    END AS nervous_system_action
FROM inventory_stocks
WHERE current_qty <= reorder_point
ORDER BY current_qty ASC;

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


    quantity INT NOT NULL,
    selling_price DECIMAL(10, 2) NOT NULL
);


---

## 🚀 4. CORE AUTOMATION LAYER (Python Integration)

Para sa tunay na operasyon ng "AI bilang Utak", ang repository na ito ay may kasamang **`report_generator.py`**. Ang Python script na ito ay awtomatikong kumokonekta sa PostgreSQL database, pinatatakbo ang financial engine, at nagluluwa ng isang organisado at petsadong **Excel Financial Report** para sa management decision-making.

### Tech Stack Used:
* **Python 3**
* **Pandas & OpenPyXL** (Data manipulation at Excel formatting)
* **Psycopg2** (PostgreSQL database driver)

---

## 👥 CONTRIBUTORS

* **Wilfredo Bolbes** — *Lead Systems Engineer & Operations Architect*
