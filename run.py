#!/usr/bin/env python3
"""
DevOps Dashboard Entry Point
Run the Flask application with configuration
"""

import os
import sys
import logging
from app import create_app
from prometheus_metrics import start_metrics_collection

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.txt'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main application entry point"""
    try:
        # Create Flask application
        app = create_app()
        
        # Start background metrics collection
        start_metrics_collection()
        
        # Get configuration from environment
        host = os.environ.get('FLASK_HOST', '0.0.0.0')
        port = int(os.environ.get('FLASK_PORT', 5000))
        debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
        
        logger.info(f"Starting DevOps Dashboard on {host}:{port}")
        logger.info(f"Debug mode: {debug}")
        logger.info(f"GitHub repos configured: {app.config.get('GITHUB_REPOS', [])}")
        logger.info(f"Log paths configured: {app.config.get('LOG_PATHS', [])}")
        
        # Run the application
        app.run(
            host=host,
            port=port,
            debug=debug,
            threaded=True
        )
        
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Failed to start application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()