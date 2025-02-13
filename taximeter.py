import time
import sys
import threading

class TaxiMeter:
    def __init__(self):
        
        self.stopped_rate = 0.02  
        self.moving_rate = 0.05   
        
        self.trip_active = False
        self.is_moving = False
        self.start_time = 0
        self.total_fare = 0.0
        self.calculation_thread = None
        self.should_run = False

    def start_trip(self):
       
        if not self.trip_active:
            self.trip_active = True
            self.total_fare = 0.0
            self.start_time = time.time()
            self.should_run = True
            
            self.calculation_thread = threading.Thread(target=self._calculate_fare_continuously)
            self.calculation_thread.daemon = True
            self.calculation_thread.start()
            
            return "Trip started. Meter is running."
        return "Error: Trip already in progress"

    def _calculate_fare_continuously(self):

        last_calculation = time.time()
        
        while self.should_run:
            current_time = time.time()
            elapsed = current_time - last_calculation
            
            rate = self.moving_rate if self.is_moving else self.stopped_rate
            self.total_fare += rate * elapsed
            
            last_calculation = current_time
            time.sleep(0.1)  

    def toggle_movement(self):
       
        if self.trip_active:
            self.is_moving = not self.is_moving
            state = "moving" if self.is_moving else "stopped"
            rate = self.moving_rate if self.is_moving else self.stopped_rate
            return f"Taxi is now {state} (Rate: {rate:.2f}€/second)"
        return "Error: No trip in progress"

    def end_trip(self):
       
        if self.trip_active:
            self.should_run = False
            if self.calculation_thread:
                self.calculation_thread.join()
            
            self.trip_active = False
            self.is_moving = False
            
            duration = time.time() - self.start_time
            
            summary = f"""
Trip Summary:
-----------------
Duration: {int(duration)} seconds
Total fare: {self.total_fare:.2f}€
-----------------"""
            return summary
        return "Error: No trip in progress"

def show_welcome_message():
 
    print("""
   ╔════════════════════════════════════╗
🚕 ║        Welcome to TaxiMeter        ║ 🚕
   ╚════════════════════════════════════╝

🟢 This program calculates taxi fares based on:
🔹 Stopped time: 0.02€ per second
🔹 Moving time: 0.05€ per second

🟢 Available commands:
🔹 start   - Start a new trip
🔹 move    - Toggle between moving/stopped
🔹 status  - Show current status
🔹 end     - End current trip
🔹 quit    - Exit program

""")

def run_cli():
   
    taxi = TaxiMeter()
    show_welcome_message()
    
    while True:
        try:
            command = input("\nEnter command (start/move/status/end/quit): ").lower().strip()
            
            if command == "quit":
                if taxi.trip_active:
                    print("Please end the current trip first!")
                    continue
                print("Thank you for using TaxiMeter!")
                break
                
            elif command == "start":
                print(taxi.start_trip())
                
            elif command == "move":
                print(taxi.toggle_movement())
                
            elif command == "status":
                if taxi.trip_active:
                    state = "moving" if taxi.is_moving else "stopped"
                    print(f"Status: Trip in progress - Taxi is {state}")
                    print(f"Current fare: {taxi.total_fare:.2f}€")
                else:
                    print("No trip in progress")
                    
            elif command == "end":
                result = taxi.end_trip()
                print(result)
                
            else:
                print("Invalid command. Please try again.")
                
        except KeyboardInterrupt:
            if taxi.trip_active:
                print("\nPlease end the trip properly with 'end' command")
            else:
                print("\nThank you for using TaxiMeter!")
                break
                
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cli()