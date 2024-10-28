import os
from aiohttp import web
from server import PromptServer
import logging

class LoopLinesSequential:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "jump": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING", "INT", "INT")  # Added INT for line number
    RETURN_NAMES = ("current_line", "remaining_cycles", "current_line_number")
    FUNCTION = "get_next_line"
    CATEGORY = "Bjornulf"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def get_next_line(self, text, jump):
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not lines:
            raise ValueError("No valid lines found in input text")

        counter_file = os.path.join("Bjornulf", "counter_lines.txt")
        os.makedirs(os.path.dirname(counter_file), exist_ok=True)

        try:
            with open(counter_file, 'r') as f:
                current_index = int(f.read().strip())
        except (FileNotFoundError, ValueError):
            current_index = -jump

        next_index = current_index + jump

        if next_index >= len(lines):
            raise ValueError(f"Counter has reached the last line (total lines: {len(lines)}). Reset Counter to continue.")

        with open(counter_file, 'w') as f:
            f.write(str(next_index))

        remaining_cycles = max(0, (len(lines) - next_index - 1) // jump + 1)
        
        return (lines[next_index], remaining_cycles - 1, next_index + 1)  # Added line number (1-based)

# Server routes
@PromptServer.instance.routes.post("/reset_lines_counter")
async def reset_lines_counter(request):
    logging.info("Reset lines counter called")
    counter_file = os.path.join("Bjornulf", "counter_lines.txt")
    try:
        os.remove(counter_file)
        return web.json_response({"success": True}, status=200)
    except FileNotFoundError:
        return web.json_response({"success": True}, status=200)
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

@PromptServer.instance.routes.post("/increment_lines_counter")
async def increment_lines_counter(request):
    counter_file = os.path.join("Bjornulf", "counter_lines.txt")
    try:
        current_index = 0
        try:
            with open(counter_file, 'r') as f:
                current_index = int(f.read().strip())
        except (FileNotFoundError, ValueError):
            pass

        with open(counter_file, 'w') as f:
            f.write(str(current_index + 1))
        return web.json_response({"success": True}, status=200)
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

@PromptServer.instance.routes.post("/decrement_lines_counter")
async def decrement_lines_counter(request):
    counter_file = os.path.join("Bjornulf", "counter_lines.txt")
    try:
        current_index = 0
        try:
            with open(counter_file, 'r') as f:
                current_index = int(f.read().strip())
        except (FileNotFoundError, ValueError):
            pass

        # Prevent negative values
        new_index = max(-1, current_index - 1)
        with open(counter_file, 'w') as f:
            f.write(str(new_index))
        return web.json_response({"success": True}, status=200)
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)

@PromptServer.instance.routes.get("/get_current_line")
async def get_current_line(request):
    counter_file = os.path.join("Bjornulf", "counter_lines.txt")
    try:
        with open(counter_file, 'r') as f:
            current_index = int(f.read().strip())
        return web.json_response({"success": True, "value": current_index + 1}, status=200)
    except (FileNotFoundError, ValueError):
        return web.json_response({"success": True, "value": 0}, status=200)
    except Exception as e:
        return web.json_response({"success": False, "error": str(e)}, status=500)