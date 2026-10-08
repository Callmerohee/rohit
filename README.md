# EasyTool standard template

Python 3.10+ reference implementation with centralized logging, expected-vs-unexpected exception handling, input validation, atomic writes/copies, checksums, and non-zero CLI exit codes.

Examples:

```bash
python main.py --verbose create-work-folder --path ./work
python main.py update-configuration --file config.json --updates updates.json
python main.py patch-a2l --source input.a2l --output patched.a2l
python main.py deliver-to-worm --source patched.a2l --destination ./worm/delivered/patched.a2l
```

Notes:
- The patch modules intentionally add a safe marker only. Replace that line with validated domain-specific A2L/CPS/HEX/CFA patch logic.
- Treat WORM storage permissions and retention as infrastructure controls; application checks alone cannot guarantee immutability.
- Add secrets redaction before logging any production credentials or tokens.
