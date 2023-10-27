import asyncio
import logging

from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic

from parsing import parse_body_composition_message

DEVICE_INFORMATION_UUID = "0000180a-0000-1000-8000-00805f9b34fb"
BODY_COMPOSITION_UUID = "0000181b-0000-1000-8000-00805f9b34fb"
GENERIC_ATTRIBUTE_UUID = "00001801-0000-1000-8000-00805f9b34fb"
SCALE_CONFIGURATION_UUID = "00001530-0000-3512-2118-0009af100700"

logger = logging.getLogger(__name__)
miscale_device = None


async def find_miscale_device():
    return await BleakScanner().find_device_by_name("MIBFS")


def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    """Simple notification handler which prints the data received."""
    message = parse_body_composition_message(data)
    logger.debug(message)

    if message.stabilized and message.measurement.impedance < 3000:
        logger.info(message)


async def connect_and_measure():
    disconnected_event = asyncio.Event()

    def disconnected_callback(client):
        logger.info("disconnected callback")
        disconnected_event.set()

    device = await find_miscale_device()
    if not device:
        return

    client = BleakClient(device, disconnected_callback=disconnected_callback)

    async with client:
        await client.start_notify(
            "00002a9c-0000-1000-8000-00805f9b34fb", notification_handler
        )
        await disconnected_event.wait()


async def main():
    while True:
        await connect_and_measure()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
    )

    asyncio.run(main())
