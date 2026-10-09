# EasyTool compact GUI template

This template links every requested module to `main.py` using Tkinter buttons. It contains no business logic.

## Run

```bash
python main.py
```

## Add your logic

Add each feature's code inside its `execute_*()` function. Leave the GUI callback wrapped by `run_gui_action()` so exceptions are logged to `log/Log.txt` and displayed safely to the user.

## Included standards

- Module-level loggers using `logging.getLogger(__name__)`
- Rotating UTF-8 log file at `log/Log.txt`
- Common expected and unexpected exception handling
- User-friendly message boxes
- Fatal startup error logging
- Keyboard interrupt handling
- Patching submenu linked to A2L, CPS, HEX, and CFA modules
- No application-specific processing logic
