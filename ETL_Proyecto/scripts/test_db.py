from scripts.database import get_connection

try:
    conn = get_connection()
    print("✅ Conexión exitosa a Supabase")
    conn.close()
except Exception as e:
    print("❌ Error:", e)