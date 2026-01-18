"""Quick script to inspect the register page HTML"""
import sys
sys.path.insert(0, '/Users/najib/Desktop/nopCommerceApp2')

from utilities.readProperties import ReadConfig
from utilities.customLogger import LoggerFactory
from utilities.antiDetectionDriver import AntiDetectionDriver
import time

logger = LoggerFactory.get_logger(__name__)

# Setup driver
driver = AntiDetectionDriver.create_driver()

try:
    # Navigate to register page
    base_url = ReadConfig.get("APPLICATION", "base_url")
    register_url = f"{base_url}register"
    
    logger.info(f"Navigating to {register_url}")
    driver.get(register_url)
    time.sleep(3)
    
    # Get page source and search for FirstName element
    page_source = driver.page_source
    
    # Check for common input id patterns
    if 'FirstName' in page_source:
        logger.info("✓ Found 'FirstName' in page source")
    else:
        logger.warning("✗ 'FirstName' NOT found in page source")
    
    if 'id="FirstName"' in page_source:
        logger.info("✓ Found id='FirstName' in page source")
    else:
        logger.warning("✗ id='FirstName' NOT found in page source")
    
    # Check for first-name variations
    if 'first-name' in page_source.lower():
        logger.info("✓ Found 'first-name' pattern in page")
    
    if 'first_name' in page_source.lower():
        logger.info("✓ Found 'first_name' pattern in page")
    
    # List all input fields
    logger.info("\nSearching for all input fields...")
    import re
    inputs = re.findall(r'<input[^>]*id=["\']([^"\']+)["\'][^>]*>', page_source)
    if inputs:
        logger.info(f"Found {len(inputs)} input elements with IDs:")
        for input_id in inputs[:20]:  # Show first 20
            logger.info(f"  - {input_id}")
    else:
        logger.warning("No input elements with id attributes found")
    
finally:
    driver.quit()
    logger.info("Driver closed")
