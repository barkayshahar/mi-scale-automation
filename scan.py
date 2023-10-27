import asyncio
import logging

from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic

from parsing import parse_body_composition_message

BODY_COMPOSITION_MEASUREMENT_UUID = "00002a9c-0000-1000-8000-00805f9b34fb"

logger = logging.getLogger(__name__)


async def find_miscale_device():
    return await BleakScanner().find_device_by_name("MIBFS")


def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    """parses body composition data and logs it"""
    message = parse_body_composition_message(data)

    logger.debug(message)

    if message.stabilized and message.measurement.impedance < 3000:
        """when the measurement is stable and the impedance is below 3000 ohm, the measurement is valid"""
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
            BODY_COMPOSITION_MEASUREMENT_UUID, notification_handler
        )
        await disconnected_event.wait()


async def main():
    logger.info("starting scan")
    while True:
        await connect_and_measure()
        logger.info("restarting scan")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
    )

    asyncio.run(main())
