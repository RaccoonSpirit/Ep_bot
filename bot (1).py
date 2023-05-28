import telebot
from telebot import types
import math
from math import gcd
from sympy import mod_inverse, isprime

bot=telebot.TeleBot('5870332284:AAGlryL10PpTZKJTjlfTxjphRWlSB5iQQFw')

#Функция Старт 
 
@bot.message_handler(commands=['start'])
def start(message):
    list_command= f'Привет, Список команд: \n \n /rsa \n \n /egsa \n \n /dsa \n \n /gost'
    bot.send_message(message.chat.id, list_command , parse_mode='html')

#Функция RSA

@bot.message_handler(commands=['rsa'])
def RSA(message):
  explanation = bot.send_message(message.chat. id, 'Введите число q оно должно быть простым')
  bot.register_next_step_handler(explanation, num_qr)
def num_qr(message):
   try:
       global q;
       q = int(message.text)
       if isprime(q) == False:
           bot.send_message(message.chat. id, 'Вы ввели не  простое число')
           explanation = bot.send_message(message.chat. id, 'Введите число q оно должно быть простым')
           return bot.register_next_step_handler(explanation, num_qr)
       explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
       bot.register_next_step_handler(explanation, num_pr)
   except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_pr(message):
   try:
       global p;
       global n;
       global Fn;
       p = int(message.text)
       if isprime(p) == False:
           explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
           return bot.register_next_step_handler(explanation, num_pr)
       n = p*q
       Fn = (p-1)*(q-1)
       bot.send_message(message.chat. id, f'Fn равна: {Fn}')
       explanation = bot.send_message(message.chat. id, 'Введите число e оно должно быть взаимно простым с Fn и 1<e<=Fn')
       bot.register_next_step_handler(explanation, num_er)
   except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_er(message):
   try:
       global d;
       global e;
       e = int(message.text)
       if Fn%e == 0:
           bot.send_message(message.chat. id, 'Вы ввели e не взаимнопростое с Fn')
           explanation = bot.send_message(message.chat. id, 'Введите число e оно должно быть взаимно простым с Fn и 1<e<=Fn')
           return bot.register_next_step_handler(explanation, num_er)
       elif 1>e or e>Fn:
           bot.send_message(message.chat. id, 'Вы ввели 1>e>=Fn')
           explanation = bot.send_message(message.chat. id, 'Введите число e оно должно быть взаимно простым с Fn и 1<e<=Fn')
           return bot.register_next_step_handler(explanation, num_er)
       d = mod_inverse(e, Fn)
       explanation = bot.send_message(message.chat. id, 'Введите число m в диапазоне 1<m<Fn')
       bot.register_next_step_handler(explanation, num_mr)
   except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_mr(message):
   try:
       m = int(message.text)
       if m<1 or m>Fn:
           bot.send_message(message.chat. id, 'Вы ввели 1>m>Fn')
           explanation = bot.send_message(message.chat. id, 'Введите число m в диапазоне 1<m<Fn')
           return bot.register_next_step_handler(explanation, num_mr)
       c = (m**d)%n
       l = (c**e)%n
       bot.send_message(message.chat. id, f'Электронная подпись: ({m},{c})')
       bot.send_message(message.chat. id, f'L равна: {l}')
       if l == m:
           bot.send_message(message.chat. id, 'Подпись верна L = m')
       else:
            bot.send_message(message.chat. id, f'Подпись не верна')
   except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')

#Функция EGSA

@bot.message_handler(commands=['egsa'])
def EGSA(message):
  explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
  bot.register_next_step_handler(explanation, num_pe)
def num_pe(message):
    try:
        global p;
        p = int(message.text)
        if isprime(p) == False:
           bot.send_message(message.chat. id, 'Вы ввели не  простое число')
           explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
           return bot.register_next_step_handler(explanation, num_pe)
        explanation = bot.send_message(message.chat. id, 'Введите число g  должно быть  p>g')
        bot.register_next_step_handler(explanation, num_ge)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_ge(message):
    try:
        global g;
        g = int(message.text)
        if p<g:
           bot.send_message(message.chat. id, 'p<g')
           explanation = bot.send_message(message.chat. id, 'Введите число g  должно быть  p>g')
           return bot.register_next_step_handler(explanation, num_ge)
        explanation = bot.send_message(message.chat. id, 'Введите число x оно должно в диапазоне 1<x<=(p-1)')
        bot.register_next_step_handler(explanation, num_xe)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_xe(message):
    try:
        global x;
        global y;
        x = int(message.text)
        if x<1 or x>(p-1):
           bot.send_message(message.chat. id, 'Вы ввели 1>x>(p-1)')
           explanation = bot.send_message(message.chat. id, 'Введите число x оно должно в диапазоне 1<x<=(p-1)')
           return bot.register_next_step_handler(explanation, num_xe)
        y = (g**x)%p
        explanation = bot.send_message(message.chat. id, 'Введите число k в диапазоне 0<k<(p-1) и взаимно простое с (p-1)')
        bot.register_next_step_handler(explanation, num_ke)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_ke(message):
    try:
        global k;
        k = int(message.text)
        if k<1 or k>(p-1):
           bot.send_message(message.chat. id, 'Вы ввели 1>k>(p-1)')
           explanation = bot.send_message(message.chat. id, 'Введите число k в диапазоне 0<k<(p-1) и взаимно простое с (p-1)')
           return bot.register_next_step_handler(explanation, num_ke)
        elif gcd(k,(p-1)) != 1:
           bot.send_message(message.chat. id, 'Вы ввели k не взаимнопростое с (p-1)')
           explanation = bot.send_message(message.chat. id, 'Введите число k в диапазоне 0<k<(p-1) и взаимно простое с (p-1)')
           return bot.register_next_step_handler(explanation, num_ke)
        explanation = bot.send_message(message.chat. id, 'Введите число m в диапазоне 1<m<(p-1)')
        bot.register_next_step_handler(explanation, num_me)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_me(message):
    try:
        m = int(message.text)
        if m<1 or m>(p-1):
           bot.send_message(message.chat. id, 'Вы ввели 1>m>(p-1)')
           explanation = bot.send_message(message.chat. id, 'Введите число m в диапазоне 1<m<(p-1)')
           return bot.register_next_step_handler(explanation, num_me)
        a = (g**k)%p
        b = ((m-x*a)%(p-1))*(mod_inverse(k, (p-1)))%(p-1)
        bot.send_message(message.chat. id, f'Электронная подпись: (m: {m},a: {a},b: {b})')
        a1=(y**a)*(a**b)%p
        a2 = (g**m)%p
        bot.send_message(message.chat. id, f'Число A1 равно: {a1}')
        bot.send_message(message.chat. id, f'Число A2 равно: {a2}')
        if a1 == a2:
            bot.send_message(message.chat. id, 'Подпись верна A1 = A2')
        else:
            bot.send_message(message.chat. id, 'Подпись не верна')
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
     
#Функция DSA

@bot.message_handler(commands=['dsa'])
def DSA(message):
  explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
  bot.register_next_step_handler(explanation, num_pd)
def num_pd(message):
    try:
        global p;
        p = int(message.text)
        if isprime(p) == False:
           bot.send_message(message.chat. id, 'Вы ввели не  простое число')
           explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
           return bot.register_next_step_handler(explanation, num_pd)
        explanation = bot.send_message(message.chat. id, 'Введите число q  должно быть простым и  q|(p-1)')
        bot.register_next_step_handler(explanation, num_qd)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_qd(message):
    try:
        global q;
        q = int(message.text)
        if isprime(q) == False:
           bot.send_message(message.chat. id, 'Вы ввели не  простое число')
           explanation = bot.send_message(message.chat. id, 'Введите число q  должно быть простым и  q|(p-1)')
           return bot.register_next_step_handler(explanation, num_qd)
        elif (p-1)%q != 0:
           bot.send_message(message.chat. id, 'Вы q не |(p-1)')
           explanation = bot.send_message(message.chat. id, 'Введите число q  должно быть простым и  q|(p-1)')
           return bot.register_next_step_handler(explanation, num_qd)
        explanation = bot.send_message(message.chat. id, 'Введите g оно должно быть (g^q)mod(p)=1')
        bot.register_next_step_handler(explanation, num_gd)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_gd(message):
    try:
        global g;
        g = int(message.text)
        if isprime(g) == False:
           bot.send_message(message.chat. id, 'Вы ввели не  простое число')
           explanation = bot.send_message(message.chat. id, 'Введите g оно должно быть (g^q)mod(p)=1')
           return bot.register_next_step_handler(explanation, num_gd)
        elif mod_inverse((g**q), p) != 1:
           bot.send_message(message.chat. id, 'Вы вели g не (g^q)mod(p)=1')
           explanation = bot.send_message(message.chat. id, 'Введите g оно должно быть (g^q)mod(p)=1')
           return bot.register_next_step_handler(explanation, num_gd)
        explanation = bot.send_message(message.chat. id, 'Введите число x оно должно в диапазоне 1<x<q')
        bot.register_next_step_handler(explanation, num_xd)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_xd(message):
    try:
        global x;
        global y;
        x = int(message.text)
        if x<1 or x>q:
           bot.send_message(message.chat. id, 'Вы ввели 1>x>q')
           explanation = bot.send_message(message.chat. id, 'Введите число x оно должно в диапазоне 1<x<q')
           return bot.register_next_step_handler(explanation, num_xd)
        y = (g**x)%p
        explanation = bot.send_message(message.chat. id, 'Введите число 1<k<q')
        bot.register_next_step_handler(explanation, num_kd)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_kd(message):
    try:
        global k;
        k = int(message.text)
        if k<1 or k>q:
           bot.send_message(message.chat. id, 'Вы ввели 1>k>q')
           explanation = bot.send_message(message.chat. id, 'Введите число 1<k<q')
           return bot.register_next_step_handler(explanation, num_kd)
        explanation = bot.send_message(message.chat. id, 'Введите число 1<m<q')
        bot.register_next_step_handler(explanation, num_md)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_md(message):
    try:
        m = int(message.text)
        if 1>m and m>q:
           bot.send_message(message.chat. id, 'Вы ввели 1>m>q')
           explanation = bot.send_message(message.chat. id, 'Введите число 1<m<q')
           return bot.register_next_step_handler(explanation, num_md)
        r = ((g**k)%p)%q
        s = ((m+r*x)*(mod_inverse(k, q)))%q
        if r<0 or r>q or s<=0 or s>q:
           bot.send_message(message.chat. id, 'Подпись недействительна')
           explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
           return bot.register_next_step_handler(explanation, num_pd)
        bot.send_message(message.chat. id, f'Цифровая подпись: s = {s}, r = {r}')
        w = mod_inverse(s, q)
        u1 = (m*w)%q
        u2 = (r*w)%q
        v = ((g**u1*y**u2)%p)%q
        bot.send_message(message.chat. id, f'Число v: {v}')
        if v == r:
            bot.send_message(message.chat. id, f'Подпись верна: v = r')
        else:
            bot.send_message(message.chat. id, f'Подпись не верна')   
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')

#Функция GOST

@bot.message_handler(commands=['gost'])
def GOST(message):
  explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
  bot.register_next_step_handler(explanation, num_pg)
def num_pg(message):
    try:
        global p;
        p = int(message.text)
        if isprime(p) == False:
           bot.send_message(message.chat. id, 'Вы ввели не  простое число')
           explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
           return bot.register_next_step_handler(explanation, num_pg)
        explanation = bot.send_message(message.chat. id, 'Введите число  q оно должно быть простым и q|(p-1)')
        bot.register_next_step_handler(explanation, num_qg)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_qg(message):
    try:
        global q;
        q = int(message.text)
        if isprime(q) == False:
           bot.send_message(message.chat. id, 'Вы ввели не  простое число')
           explanation = bot.send_message(message.chat. id, 'Введите число  q оно должно быть простым и q|(p-1)')
           return bot.register_next_step_handler(explanation, num_qg)
        elif (p-1)%q != 0:
           bot.send_message(message.chat. id, 'Вы q не |(p-1)')
           explanation = bot.send_message(message.chat. id, 'Введите число  q оно должно быть простым и q|(p-1)')
           return bot.register_next_step_handler(explanation, num_qg)
        explanation = bot.send_message(message.chat. id, 'Введите g оно должно быть таким что (g^q)mod(p)=1')
        bot.register_next_step_handler(explanation, num_gg)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_gg(message):
    try:
        global g;
        g = int(message.text)
        if mod_inverse((g**q), p) != 1:
           bot.send_message(message.chat. id, 'Вы вели g не (g^q)mod(p)=1')
           explanation = bot.send_message(message.chat. id, 'Введите g оно должно быть таким что (g^q)mod(p)=1')
           return bot.register_next_step_handler(explanation, num_gg)
        explanation = bot.send_message(message.chat. id, 'Введите число x оно должно в диапазоне 1<x<q')
        bot.register_next_step_handler(explanation, num_xg)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_xg(message):
    try:
        global x;
        global y;
        x = int(message.text)
        if x<1 or x>q:
           bot.send_message(message.chat. id, 'Вы ввели 1>x>q')
           explanation = bot.send_message(message.chat. id, 'Введите число x оно должно в диапазоне 1<x<q')
           return bot.register_next_step_handler(explanation, num_xg)
        y = (g**x)%p
        explanation = bot.send_message(message.chat. id, 'Введите число k оно должно быть в диапазоне 1<k<q')
        bot.register_next_step_handler(explanation, num_kg)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_kg(message):
    try:
        global k;
        k = int(message.text)
        if k<1 or k>q:
           bot.send_message(message.chat. id, 'Вы ввели 1>k>q')
           explanation = bot.send_message(message.chat. id, 'Введите число k оно должно быть в диапазоне 1<k<q')
           return bot.register_next_step_handler(explanation, num_kg)
        explanation = bot.send_message(message.chat. id, 'Введите число 1<m<q')
        bot.register_next_step_handler(explanation, num_mg)
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')
def num_mg(message):
    try:
        m = int(message.text)
        if 1>m or m>q:
           bot.send_message(message.chat. id, 'Вы ввели 1>m>q')
           explanation = bot.send_message(message.chat. id, 'Введите число 1<m<q')
           return bot.register_next_step_handler(explanation, num_mg)
        r = ((g**k)%p)%q
        s = (x*r+k*m)%q
        if r<0 or r>q or s<=0 or s>q:
           bot.send_message(message.chat. id, 'Подпись недействительна')
           explanation = bot.send_message(message.chat. id, 'Введите число p оно должно быть простым')
           return bot.register_next_step_handler(explanation, num_pg)
        bot.send_message(message.chat. id, f'Электронная подпись (s: {s},r: {r})')
        w = (m**(q-2))%q
        u1 = (s*w)%q
        u2 = ((q-r)*w)%q
        v = ((g**u1*y**u2)%p)%q
        bot.send_message(message.chat. id, f'Число v: {v}, r: {r}')
        if v == r:
            bot.send_message(message.chat. id, f'Подпись верна: v = r')
        else:
            bot.send_message(message.chat. id, f'Подпись не верна')
    except Exception:
      bot.send_message(message.chat. id, 'Вы ввели не число')

bot.polling(none_stop=True)