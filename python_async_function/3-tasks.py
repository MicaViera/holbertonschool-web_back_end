#!/usr/bin/env python3
"""Write a function that takes an integer max_delay."""
import asynciol
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns a asyncio.Task"""
    return (asyncio.Task(wait_random(max_delay)))
