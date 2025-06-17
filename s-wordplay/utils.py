import os

def have_char(word, caractere):
    for char in word:
        if char == caractere:
            return True
        
    return False

def uses_only(palavra, letra_permitida):
    for letra in palavra:
        if not have_char(letra_permitida, letra):
            return False
    return True     

def uses_all(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:
        if not have_char(palavra, letra):
            return False
    return True

def clear_screen():
    os.system('cls')

def is_abecedarian(word):
  anterior = word[0]

  for i in range(1, len(word)):
    atual = word[i]
    if anterior > atual:
      return False
    
    anterior = atual
  
  return True


def has_no_x(word, caractere_proibido):
    for caractere in word:
        if caractere_proibido == caractere:
            return False
    return True

def avoids(word, letter_forbidden):
    for char in word:
        if have_char(letter_forbidden, char):
            return False
        
    return True


def to_lower(text):
  new_text = ''
  for char in text:
    if is_upper_letter(char):
      code = ord(char)
      new_code = code + 32
      lower_char = chr(new_code)
      new_text += lower_char
    else:
      new_text += char

  return new_text


def to_upper(text):
  new_text = ''

  for letter in text:
    if is_lower_letter(letter):
      new_text = new_text + chr(ord(letter) - 32)
    else:
      new_text = new_text + letter
  
  return new_text


def is_upper_letter(char):
  return ord(char) >= 65 and ord(char) <= 90


def is_lower_letter(char):
  return ord(char) >= 97 and ord(char) <= 122


def is_letter(char):
  return is_lower_letter(char) or is_upper_letter(char)


def is_number(char):
  return ord(char) >= 48 and ord(char) <= 57
