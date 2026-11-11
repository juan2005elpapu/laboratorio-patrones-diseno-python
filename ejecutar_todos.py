"""Ejecuta cada ejemplo aislado y guarda su salida real en UTF-8."""

import os
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent
    examples = sorted(root.glob('[0-9][0-9]_*.py'))
    results = ['LABORATORIO - PATRONES DE DISEÑO', 'Resultados de ejecución', '']
    failures = 0
    for example in examples:
        process = subprocess.run(
            [sys.executable, str(example)],
            capture_output=True,
            text=True,
            encoding='utf-8',
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
            cwd=root,
            timeout=30,
        )
        results.extend([
            f'=== {example.name} ===',
            process.stdout.rstrip(),
            f'Estado: {"OK" if process.returncode == 0 else "ERROR"}',
        ])
        if process.returncode:
            failures += 1
            results.append(process.stderr.rstrip())
        results.append('')
    results.append(f'Resumen: {len(examples) - failures}/{len(examples)} ejemplos ejecutados correctamente.')
    output = root / 'resultados.txt'
    output.write_text('\n'.join(results) + '\n', encoding='utf-8')
    print(f'Resultados guardados en {output.name}')
    print(results[-1])
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
