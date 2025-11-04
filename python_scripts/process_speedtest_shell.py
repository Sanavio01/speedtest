#!/usr/bin/env python3
import json
import sys
import os

#!/usr/bin/env python3
import json
import sys
import os

# Add Home Assistant paths
sys.path.insert(0, '/usr/src/homeassistant')

try:
    # Read speedtest results
    with open('/config/speedtest_result.json', 'r') as f:
        data = json.load(f)
    
    # Import Home Assistant after path is set
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers import config_validation as cv
    
    # Simple file-based approach - write to a temp file that HA will read
    result = {
        'download': data.get('download', 0),
        'upload': data.get('upload', 0),
        'ping': data.get('ping', 0),
        'server_name': data.get('server', {}).get('sponsor', '') + ' - ' + data.get('server', {}).get('name', ''),
        'timestamp': data.get('timestamp', '')
    }
    
    with open('/config/speedtest_processed.json', 'w') as f:
        json.dump(result, f)
    
    print('SUCCESS')
    
except Exception as e:
    print(f'ERROR: {str(e)}')
    sys.exit(1)