#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 07:04:24 2020

@author: DJ2LS
"""

import array
import base64
import json
import sys
import time
from pprint import pformat

import structlog

sys.path.insert(0, "..")
sys.path.insert(0, "../tnc")
import codec2
import data_handler
import helpers
import modem
import sock
import static


def t_highsnr_arq_short_station2(
    parent_pipe,
    freedv_mode: str,
    n_frames_per_burst: int,
    mycall: str,
    dxcall: str,
    message: str,
    lowbwmode: bool,
):
    log = structlog.get_logger(__name__)
    orig_tx_func: object
    orig_rx_func: object

    def t_transmit(self, mode, repeats: int, repeat_delay: int, frames: bytearray):
        """'Wrap' RF.transmit function to extract the arguments."""
        nonlocal orig_tx_func, parent_pipe

        t_frames = frames
        parent_pipe.send(t_frames)
        log.debug("S2 TX: ", frames=t_frames)
        # frametype = int.from_bytes(t_frames[:1], "big")
        # log.debug("S2 RX: ", frametype=frametype)

        # Apologies for the Python "magic." "orig_func" is a pointer to the
        # original function captured before this one was put in place.
        orig_tx_func(self, mode, repeats, repeat_delay, frames)  # type: ignore

    def t_process_data(self, bytes_out, freedv, bytes_per_frame: int):
        """'Wrap' DATA.process_data function to extract the arguments."""
        nonlocal orig_rx_func, parent_pipe
        t_bytes_out = bytes(bytes_out)
        parent_pipe.send(t_bytes_out)
        log.debug(
            "S2 RX: ",
            bytes_out=t_bytes_out,
            bytes_per_frame=bytes_per_frame,
        )
        frametype = int.from_bytes(t_bytes_out[:1], "big")
        log.debug("S2 RX: ", frametype=frametype)

        # Apologies for the Python "magic." "orig_func" is a pointer to the
        # original function captured before this one was put in place.
        orig_rx_func(self, bytes_out, freedv, bytes_per_frame)  # type: ignore

    # enable testmode
    data_handler.TESTMODE = True
    modem.RXCHANNEL = "/tmp/hfchannel2"
    modem.TESTMODE = True
    modem.TXCHANNEL = "/tmp/hfchannel1"
    static.HAMLIB_RADIOCONTROL = "disabled"
    static.LOW_BANDWIDTH_MODE = lowbwmode
    static.MYGRID = bytes("AA12aa", "utf-8")
    static.RESPOND_TO_CQ = True

    mycallsign = bytes(mycall, "utf-8")
    mycallsign = helpers.callsign_to_bytes(mycallsign)
    static.MYCALLSIGN = helpers.bytes_to_callsign(mycallsign)
    static.MYCALLSIGN_CRC = helpers.get_crc_24(static.MYCALLSIGN)
    static.MYGRID = bytes("AA12aa", "utf-8")
    static.SSID_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    dxcallsign = bytes(dxcall, "utf-8")
    dxcallsign = helpers.callsign_to_bytes(dxcallsign)
    dxcallsign = helpers.bytes_to_callsign(dxcallsign)
    static.DXCALLSIGN = dxcallsign
    static.DXCALLSIGN_CRC = helpers.get_crc_24(static.DXCALLSIGN)

    # Create the TNC
    tnc = data_handler.DATA()
    orig_rx_func = data_handler.DATA.process_data
    data_handler.DATA.process_data = t_process_data

    # Create the modem
    t_modem = modem.RF()
    orig_tx_func = modem.RF.transmit
    modem.RF.transmit = t_transmit

    time.sleep(22)

    log.debug("Info: ", info=static.INFO)
    assert "DATACHANNEL;RECEIVEDOPENER" in static.INFO
    # assert "QRV;SENDING" in static.INFO
    # assert "ARQ;SESSION;CLOSE" in static.INFO
    log.debug("station2: Exiting!")
