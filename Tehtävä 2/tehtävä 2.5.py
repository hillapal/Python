leiviska = float(input("anna leiviskät ="))
naula = float(input("anna naulat ="))
luoti = float(input("anna luodit ="))

leiviskat_grammoina = 32 * leiviska * 20 * 13,3
naulat_grammoina =  32 * naula * 13,3
luodit_grammoina= luoti * 13,3

massa_grammoina = leiviskat_grammoina + naulat_grammoina + luodit_grammoina

print(f" massa on {massa_grammoina}")
