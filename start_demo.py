#!/usr/bin/env python3
import subprocess
import sys
import webbrowser
import time

def start_demo():
    print("🚀 Starting KPI Integration Demo...")
    
    try:
        # Start Streamlit
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "comprehensive_framework_demo.py",
            "--server.port", "8502",
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false"
        ])
        
        print("✅ Demo server starting...")
        print("🌐 Opening browser in 3 seconds...")
        
        time.sleep(3)
        webbrowser.open("http://localhost:8502")
        
        print("📊 Demo ready at: http://localhost:8502")
        print("Press Ctrl+C to stop")
        
        process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Demo stopped")
        process.terminate()

if __name__ == "__main__":
    start_demo()