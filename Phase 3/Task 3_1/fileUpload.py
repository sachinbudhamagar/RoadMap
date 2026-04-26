import os 
import time
import random
from pathlib import Path

class fileUploadSystem:
    """File Upload System with state management"""
    
    # Configuration
    MAX_FILE_SIZE_MB = 10
    ALLOWED_EXTENSIONS = [".txt", ".pdf", ".docx", ".zip", ".jpg", ".png"]
    
    def __init__(self):
        self.state = "idle"
        self.selected_file = None
        self.error_message = None
        self.system_running = True
    
    def display_message(self, message, message_type = "info"):
        """Display formatted messages"""
        symbols = {
            "info": "i",
            "success": "✅",
            "error": "❌",
            "warning": "⚠️"
        }
        symbol = symbols.get(message_type, "💠")
        print(f"\n{symbol} {message}")
        
    def clear_screen(self):
        """Clear console screen"""
        os.system("cls" if os.name == "nt" else "clear")
        
    def get_user_input(self, prompt, options = None):
        """Get validated user input"""
        while True:
            user_input = input(f"\n{prompt}: ").strip().lower()
            
            if options is None:
                return user_input
            
            if user_input in options:
                return user_input
            else:
                print(f"Invalid input. Please enter one of: {', '.join(options)}")
                
    def select_file(self):
        """Allow user to select a file"""
        file_path = input("\nEnter the file path (or 'exit' to quit): ").strip()
        
        if file_path.lower() == "exit":
            return None
        
        # Remove quotes if present
        file_path = file_path.strip("'").strip("'")
        
        if os.path.isfile(file_path):
            return file_path
        else:
            self.display_message("File not found!")
            return False
        
    def validate_file(self, file_path):
        """
        Validate selected file based on name, size, and type
        
        Returns: tuple (is_Valid, error_message)
        """
        # Check if file exists
        if not os.path.isfile(file_path):
            return False, "File does not exist"
        
        # Get file info
        file_name = os.path.basename(file_path)
        file_ext = Path(file_path). suffix.lower()
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    
        # Validating file extension
        if file_ext not in self.ALLOWED_EXTENSIONS:
            return False, f"File type '{file_ext}' not allowed. Allowed: {', '.join(self.ALLOWED_EXTENSIONS)}"
        
        # Validate file name
        if len(file_name) > 225:
            return False, "File name too long (max 255 characters)"
        
        return True, None
    
    def simulate_upload(self, file_path):
        """
        Simulate file upload with progress bar
        
        Returns: 
            bool: True if successful, False if failed
        """
        file_name = os.path.basename(file_path)
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        
        print(f"\n Uploading: {file_name} ({file_size_mb:.2f}MB)")
        print("=" * 50)
        
        # Simulate upload progress
        for i in range(0, 101, 10):
            # Progress bar 
            filled = "█" * (i // 2)
            empty = "░"*  (50 - i // 2)
            print(f"[{filled}{empty}] {i}%", end="", flush=True)
            time.sleep(0.3) #Simulate network delay
        
        print("\n" + "=" * 50)
        
        # Simulate random failure (10% chance)
        success = random.random() > 0.1
        
        return success
    
    def reset_form(self):
        """Reset form to initial state"""
        self.select_file = None
        self.error_message = None
        
    def run(self):
        """Main state machine loop"""
        print("=" * 50)
        print(" FILE UPLOAD SYSTEM ")
        print("=" * 50)
        
        while self.system_running:
            
            # STATE: IDLE
            if self.state == "idle":
                print("Select a file to upload")
                result = self.select_file()
            
                if result is None: # User wants to exit
                    self.state = "exiting"
                elif result:
                    self.selected_file = result
                    self.state = "file_selected"
                # If result is False, Stay in idle (file not found)
                
            # STATE: FILE SELECTED
            elif self.state == "file_selected":
                self.display_message("Validating file...)", "info")
                
                is_valid, error_msg = self.validate_file(self.selected_file)
                
                if is_valid:
                    self.state = "file_validated"
                    self.display_message("File validation passed!", "success")
                else:
                    self.state = "file_validation_failed"
                    self.error_message = error_msg
                
            # STATE: FILE VALIDATION FAILED 
            elif self.state == "file_validation_failed":
                self.display_message(f"Validation Error: {self.error_message}", "error")
                
                action = self.get_user_input(
                    "Choose action: (s)elect another file or (e)xit",
                    option = ['s', 'e']
                )
                
                if action == 's':
                    self.state = "idle"
                    self.reset_form()
                else:
                    self.state = "exiting"
                    
            # STATE: FILE VALIDATED
            elif self.state == "file_validated":
                file_name = os.path.basename(self.selected_file)
                self.display_message(f"Ready to upload: {file_name}", "success")
                
                action = self.get_user_input(
                    "Press (u)pload, (c)hange file, or (x)cancel",
                    options=["u", "c", "x"]
                )
                
                if action == "u":
                    self.state = "upload_in_progress"
                elif action == "c":
                    self.state = "idle"
                    self.reset_form()
                elif action == "x":
                    self.state = "cancelled"
            
            # STATAE: UPLOAD IN PROGRESS
            elif self.state == "upload_in_progress":
                success = self.simulate_upload(self.selected_file)
                
                if success:
                    self.state = "upload_completed"
                else:
                    self.state = "upload_failed"
                    self.error_message = "Network error: Connection timeout"
            
            # STATE: UPLOAD COMPLETED
            elif self.state == "upload_completed":
                self.display_message("Upload Successful!", "success")
                
                action = self.get_user_input(
                    "Upload another file? (y)es or (n)o",
                    options=["y", "n"]
                )
                
                self.reset_form()
                
                if action == "y":
                    self.state = "idle"
                else:
                    self.state = "exiting"
            
            # STATE: UPLOAD FILED 
            elif self.state == "upload_failed":
                self.display_message(f"Upload Failed: {self.error_message}", "error")
                
                action = self.get_user_input(
                    "Retry or Cancel? (r)etry or (c)ancel",
                    options=["r", "c"]
                )
                
                if action == "r":
                    self.state = "file_validated"
                else:
                    self.state = "cancelled"
                
            # STATE: CANCELLED
            elif self.state == "cancelled":
                self.display_message("Upload cancelled", "warning")
                self.reset_form()
                
                action = self.get_user_input(
                    "Start Over? (y)es or (n)o",
                    options=["y", "n"]
                )
                
                if action == "y":
                    self.state = "idle"
                else:
                    self.state = "exiting"
                
            # STATE: EXITING
            elif self.state == "exiting":
                self.display_message("Thank you for using File Upload System!", "info")
                print("=" * 50)
                self.system_running = False
                break
    
# Run the system
if __name__ == "__main__":
    system = fileUploadSystem()
    system.run()