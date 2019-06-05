# Desenvolvido  por: Artur de Souza Amorim - 3048, Thomas Sonobe Moreira Chang - 3052 e Victor Hugo Rezende dos Santos - 3510
# Desenvolvido com Windows 10, Visual Studio Code v1.33.1 e Python v3.7

import time
typeR = [
    "add",
    "sub",
    "or",
    "nor",
    "and",
    "sll",
    "slr"
]

typeI = [
    "addi",
    "andi",
    "ori"
]
#dicionario com as funct e seus respectivos binarios
Funct={ 
    "add": "100000",#Intruções do tipo R
    "sub": "100010",
    "and": "100100",
    "or": "100101",
    "nor": "100111",
    "sll": "000000",
    "srl": "000010",
    "addi": "001000",#Intruções do tipo I
    "andi": "001100",
    "ori": "001101"
}

def ConvertFunct(funct):#converte o tipo funct para binario
    return Funct[funct]

#dicionario com os registradores e seus respectivos binarios
Registers={
    "$zero": "00000",
    "$at": "00001",
    "$v0": "00010",
    "$v1": "00011",
    "$a0": "00100",
    "$a1": "00101",
    "$a2": "00110",
    "$a3": "00111",
    "$t0": "01000",
    "$t1": "01001",
    "$t2": "01010",
    "$t3": "01011",
    "$t4": "01100",
    "$t5": "01101",
    "$t6": "01110",
    "$t7": "01111",
    "$s0": "10000",
    "$s1": "10001",
    "$s2": "10010",
    "$s3": "10011",
    "$s4": "10100",
    "$s5": "10101",
    "$s6": "10110",
    "$s7": "10111",
    "$t8": "11000",
    "$t9": "11001",
    "$k0": "11010",
    "$k1": "11011",
    "$gp": "11100",
    "$sp": "11101",
    "$fp": "11110",
    "$ra": "11111",
}

def Trans5B(num): #Transforma a entrada em um numero binario de 5 bits
    num = int(num)
    bits = 5
    s = bin(num & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


def Trans16B(num): #Transforma a entrada em um numero binario de 16 bits
    num = int(num)
    bits = 16
    s = bin(num & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def ConvertRegister(register): #converte o registrador para binario
    return Registers [register]

def Montador(nomeArqEntrada):
    arquivo = open(nomeArqEntrada, 'r')

    for input_instruction in arquivo:

        input_instruction = input_instruction.replace(",","") #Substitui toda ',' por um espaço em branco, de modo a facilitar o uso do split
        input_instruction = input_instruction.replace("\n","")
        split_instruction = input_instruction.split(" ") # separa as instruções por espaço

        print("Instrução -> ", split_instruction)

        instruction = split_instruction[0]
        print("\tComando -> ", instruction)
        OutputFile = open("saida.txt", 'a')
        if instruction in typeR:#se a instrucao for do tipo R ela terá opcode 000000
            opcode = '000000'
            if ((instruction == "sll") or (instruction == "srl")):
                shamt = Trans5B(split_instruction[3])
                rs = '00000'
                rt = ConvertRegister(split_instruction[2])
                rd = ConvertRegister(split_instruction[1])
                funct = ConvertFunct(split_instruction[0])
                print("\topcode {} rs {} rt {} rd {} shamt {} funct {}\n".format(opcode, rs, rt, rd, shamt, funct))
                OutputFile.write("{}{}{}{}{}{}\n".format(opcode, rs, rt, rd, shamt, funct))

            elif ((instruction == "add") or (instruction == "sub") or (instruction == "and") or (instruction == "or") or  (instruction == "nor")): # se a instrucao for alguma dessas o shamt será 00000
                shamt = '00000'
                rs= ConvertRegister(split_instruction[2])
                rt= ConvertRegister(split_instruction[3])
                rd= ConvertRegister(split_instruction[1])
                funct =  ConvertFunct(split_instruction[0])
                print("\topcode {} rs {} rt {} rd {} shamt {} funct {}\n".format(opcode, rs, rt, rd, shamt, funct))
                OutputFile.write('{}{}{}{}{}{}\n'.format(opcode, rs, rt, rd, shamt, funct))        
        elif instruction in typeI:
            if (instruction == "addi"):
                opcode ="001000"
                imm = Trans16B(split_instruction[3])
                rs = ConvertRegister(split_instruction[2])
                rt = ConvertRegister(split_instruction[1])
                print('\topcpde {} rs {} rt {} imm {}\n'.format(opcode, rs, rt, imm))
                OutputFile.write('{}{}{}{}\n'.format(opcode, rs, rt, imm))
            elif (instruction == "andi"):
                opcode ="001100"
                imm = Trans16B(split_instruction[3])
                rs = ConvertRegister(split_instruction[2])
                rt = ConvertRegister(split_instruction[1])
                print('\topcpde {} rs {} rt {} imm {}\n'.format(opcode, rs, rt, imm))
                OutputFile.write('{}{}{}{}\n'.format(opcode, rs, rt, imm))
            elif (instruction == "ori"):
                opcode ="001101"
                imm = Trans16B(split_instruction[3])
                rs = ConvertRegister(split_instruction[2])
                rt = ConvertRegister(split_instruction[1])
                print('\topcpde {} rs {} rt {} imm {}\n'.format(opcode, rs, rt, imm))
                OutputFile.write('{}{}{}{}\n'.format(opcode, rs, rt, imm))

    arquivo.close()
    OutputFile.close()
    return

def menu():
    opc = 1
    while (opc != 0):
        print("\t********************\tMENU\t********************\n\n")
        print("\t1 - Entrar com o nome do arquivo a ser lido.\n")
        print("\t2 - Montar saida em linguagem de máquina.\n")
        print("\t0 - Sair e fechar arquivo de saida\n")
        print("\t***Se o arquivo nao for fechado, nada sera escrito nele\n")
        opc = int(input("\tDigite uma opcao: \n\n\n"))
        if(opc == 1):
            nomeArqEntrada = input("Digite o nome do arquivo com a extensão ")
        elif(opc == 2):
            Montador(nomeArqEntrada)
        elif(opc == 0):
            return 0
            time.sleep(2)
        else:
            print("\t**Opcão inválida!**")
            time.sleep(2)

menu()