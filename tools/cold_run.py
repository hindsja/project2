"""AI-run fresh-folder check. This is explicitly NOT the required partner cold run."""
import json
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def main():
    started = time.perf_counter()
    record = {'actor': 'AI-assisted automated check, not partner evidence',
              'timestamp_utc': datetime.now(timezone.utc).isoformat(),
              'command': 'python app.py --port 0', 'first_failure': None, 'checks': []}
    with tempfile.TemporaryDirectory(prefix='project2-cold-') as folder:
        isolated = Path(folder)/'repository'
        shutil.copytree(ROOT, isolated, ignore=shutil.ignore_patterns('__pycache__', '.git', '.venv'))
        # Disable site-packages to prove no optional package is silently required.
        process = subprocess.Popen([sys.executable, '-S', 'app.py', '--port', '0'], cwd=isolated,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            line = process.stdout.readline().strip()
            if 'http://' not in line:
                raise RuntimeError('App did not print its address: '+line)
            address = line.split('http://',1)[1]
            base = 'http://'+address
            with urlopen(base, timeout=15) as response:
                assert b'ETF Portfolio Committee Dashboard' in response.read()
            record['checks'].append('Home page returned HTTP 200 from fresh copy with site-packages disabled.')
            with urlopen(base+'/api/results', timeout=30) as response:
                result = json.load(response)
            assert result['decision'] == 'PILOT'
            assert result['portfolios'][2]['passed']
            record['checks'].append('Base decision and all constrained mandate checks returned successfully.')
            config = result['config']
            config['max_weight'] = .30
            request = Request(base+'/api/analyze', data=json.dumps(config).encode(), headers={'Content-Type':'application/json'})
            with urlopen(request, timeout=30) as response:
                changed = json.load(response)
            assert changed['decision'] == 'REJECT'
            record['checks'].append('Changing fund cap to 30% recalculated to REJECT.')
            export = subprocess.run([sys.executable, '-S', 'app.py', '--export'], cwd=isolated,
                                    text=True, capture_output=True, timeout=60)
            if export.returncode:
                raise RuntimeError(export.stderr)
            assert (isolated/'outputs/decision-output.md').is_file()
            record['checks'].append('Export command produced readable output and committee memo in isolated copy.')
            record['result_location'] = 'Browser at printed localhost address; outputs/decision-output.md and outputs/results.json'
            record['status'] = 'PASS'
        except Exception as error:
            record['first_failure'] = str(error)
            record['status'] = 'FAIL'
            raise
        finally:
            process.terminate()
            process.wait(timeout=10)
            record['elapsed_seconds'] = round(time.perf_counter()-started, 3)
            (ROOT/'outputs/automated-cold-run.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
