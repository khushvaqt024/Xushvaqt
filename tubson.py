from sympy import isprime, factorint

def lucas_test(n):
    """Lucas testi"""
    if n < 2:
        return False, "Son 2 dan kichik, shuning uchun tub emas."

    factors = factorint(n - 1)  # (n-1) sonini faktorlarga ajratamiz
    for q in factors.keys():
        a = 2  # Har bir q uchun a^(n-1)/q mod n != 1 bo'lishini tekshiramiz
        if pow(a, (n - 1) // q, n) == 1:
            return False, f"Lucas testi bajarilmadi: a^(n-1)/{q} mod {n} = 1."

    return True, "Lucas testi bajarildi."

def quadratic_frobenius_test(n):
    """Quadratic Frobenius testi"""
    if n < 2:
        return False, "Son 2 dan kichik, shuning uchun tub emas."

    b, c = 1, 1  # Polinom koeffitsiyentlari (P(x) = x^2 - bx + c)
    discriminant = b ** 2 - 4 * c  # Diskriminant hisoblaymiz

    if pow(discriminant, (n - 1) // 2, n) != 1:
        return False, f"Quadratic Frobenius testi bajarilmadi: diskriminant^{(n-1)//2} mod {n} != 1."

    return True, "Quadratic Frobenius testi bajarildi."

def baillie_psw_test(n):
    """Baillie-PSW testi (Miller-Rabin + Lucas)"""
    if n < 2:
        return False, "Son 2 dan kichik, shuning uchun tub emas."

    # Miller-Rabin testi
    if not isprime(n):
        return False, "Baillie-PSW testi bajarilmadi: Miller-Rabin testi o'tmadi."

    # Lucas testi
    lucas_result, lucas_reason = lucas_test(n)
    if not lucas_result:
        return False, f"Baillie-PSW testi bajarilmadi: {lucas_reason}"

    return True, "Baillie-PSW testi bajarildi."

def check_primality_with_selected_method(n, method):
    """Sonni tublikka tekshiruvchi funksionallik va foydalanuvchi tanlagan metod bo'yicha izoh"""
    explanation_steps = []

    if method == 'Lucas':
        # Lucas testi
        result, reason = lucas_test(n)
        explanation_steps.append("Lucas testi bosqichlari:")
        explanation_steps.append("1. (n-1) sonini faktorlarga ajratamiz.")
        explanation_steps.append("2. Har bir q uchun a^(n-1)//q mod n != 1 bo'lishini tekshiramiz.")
        explanation_steps.append(reason)
        return result, "\n".join(explanation_steps)

    elif method == 'Quadratic Frobenius':
        # Quadratic Frobenius testi
        result, reason = quadratic_frobenius_test(n)
        explanation_steps.append("Quadratic Frobenius testi bosqichlari:")
        explanation_steps.append("1. Diskriminantni hisoblaymiz.")
        explanation_steps.append("2. Diskriminant^(n-1)//2 mod n != 1 bo'lishini tekshiramiz.")
        explanation_steps.append(reason)
        return result, "\n".join(explanation_steps)

    elif method == 'Baillie-PSW':
        # Baillie-PSW testi
        result, reason = baillie_psw_test(n)
        explanation_steps.append("Baillie-PSW testi bosqichlari:")
        explanation_steps.append("1. Miller-Rabin testi o'tkaziladi.")
        explanation_steps.append("2. Lucas testi bajariladi.")
        explanation_steps.append(reason)
        return result, "\n".join(explanation_steps)

    else:
        return False, "Tanlangan metod noto'g'ri."

# Foydalanuvchidan sonni va testni tanlashni so'raymiz
n = int(input("Sonni kiriting: "))
print("Metodlarni tanlang:")
print("1. Lucas testi")
print("2. Quadratic Frobenius testi")
print("3. Baillie-PSW testi")
method_choice = input("Tanlangan metodni kiriting (1, 2, 3): ")

# Tanlangan metodga qarab, sonni tublikka tekshiramiz
if method_choice == '1':
    method = 'Lucas'
elif method_choice == '2':
    method = 'Quadratic Frobenius'
elif method_choice == '3':
    method = 'Baillie-PSW'
else:
    method = ''

result, explanation = check_primality_with_selected_method(n, method)

if result:
    print(f"{n} tub son.\nIzoh:\n{explanation}")
else:
    if n > 1:
        print(f"{n} murakkab son.\nIzoh:\n{explanation}")
    else:
        print(f"{n} tub son emas.\nIzoh:\n{explanation}")
