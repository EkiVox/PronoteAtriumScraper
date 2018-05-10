#!/bin/bash
screen -S handler -d -m python HANDLER.py
screen -S fetcher -d -m python FETCHER.py
