from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Болит голова')],
    [KeyboardButton(text='Болит живот')],
    [KeyboardButton(text='Болит горло')]
    [KeyboardButton(text='Болит зуб')]],
    resize_keyboard=True)