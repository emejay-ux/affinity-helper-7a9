import os
from datetime import datetime

class OutputManager:
    def __init__(self, base_output_path):
        self.base_output_path = base_output_path
        self.ensure_output_directory()

    def ensure_output_directory(self):
        """Ensure the base output directory exists, create if it doesn't."""
        if not os.path.exists(self.base_output_path):
            try:
                os.makedirs(self.base_output_path)
                print(f"Created directory: {self.base_output_path}")
            except Exception as e:
                raise RuntimeError(f"Failed to create output directory: {e}")

    def generate_output_path(self, layer_name):
        """Generate a unique output path for the exported PNG file."""
        sanitized_layer_name = self.sanitize_layer_name(layer_name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file_name = f"{sanitized_layer_name}_{timestamp}.png"
        output_path = os.path.join(self.base_output_path, output_file_name)
        return output_path

    def sanitize_layer_name(self, layer_name):
        """Sanitize the layer name to create a valid filename."""
        # Remove invalid characters for filenames
        invalid_chars = '<>:"/\\|?*'
        sanitized_name = ''.join(c for c in layer_name if c not in invalid_chars)
        return sanitized_name if sanitized_name else "Unnamed_Layer"

    def get_output_directory(self):
        """Return the base output directory."""
        return self.base_output_path

# TODO: Add support for different file formats (e.g., JPEG, TIFF)
# TODO: Implement a method to handle batch exports with progress indication
# TODO: Add logging instead of print statements for better debugging and tracking

# Example usage (to be removed in production):
if __name__ == "__main__":
    output_manager = OutputManager("exports")
    print(output_manager.generate_output_path("My Layer 1"))  # For testing purposes only.
