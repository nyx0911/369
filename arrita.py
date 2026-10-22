import random

print("🧮 MIRËSEVINI NË QUIZIN MATEMATIKOR 🧠")
print("Zgjidh nivelin e vështirësisë:\n")
print("1️⃣  Lehtë (numra 1–10)")
print("2️⃣  Mesatar (numra 1–50)")
print("3️⃣  I vështirë (numra 1–100)\n")

# Zgjedh niveli
niveli = input("Shkruaj 1, 2 ose 3: ")

if niveli == "1":
    max_num = 10
elif niveli == "2":
    max_num = 50
elif niveli == "3":
    max_num = 100
else:
    print("❌ Zgjedhje e pavlefshme! Po caktohet niveli mesatar.")
    max_num = 50

# Sa pyetje do ketë quiz-i
numri_pyetjeve = 5
pikë = 0

print("\n📘 Fillojmë quiz-in! Përgjigju saktë në sa më shumë pyetje.\n")

for i in range(numri_pyetjeve):
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    operacion = random.choice(["+", "-", "*", "/"])

    # Përcakto përgjigjen e saktë
    if operacion == "/":
        # për të shmangur ndarjen me 0 dhe për rezultate të thjeshta
        përgjigje_saktë = round(a / b, 2)
    else:
        përgjigje_saktë = eval(f"{a}{operacion}{b}")

    # Kërko përgjigjen nga përdoruesi
    print(f"Pyetja {i+1}: Sa bën {a} {operacion} {b}?")
    try:
        përgjigje = float(input("Përgjigjja jote: "))
        if abs(përgjigje - përgjigje_saktë) < 0.01:
            print("✅ Saktë!\n")
            pikë += 1
        else:
            print(f"❌ Gabim! Përgjigjja e saktë ishte {përgjigje_saktë}\n")
    except ValueError:
        print("⚠️ Ju lutem shkruani një numër të vlefshëm!\n")

# Rezultati final
print("🎯 Quiz i mbaruar!")
print(f"Pikët e tua: {pikë}/{numri_pyetjeve}")

# Mesazh personalizuar sipas performancës
if pikë == numri_pyetjeve:
    print("🏆 Perfekt! Je gjeni i matematikës!")
elif pikë >= numri_pyetjeve * 0.7:
    print("👏 Shumë mirë! Ke njohuri të forta.")
elif pikë >= numri_pyetjeve * 0.4:
    print("🙂 Jo keq, por mund të përmirësohesh!")
else:
    print("😅 Duhet më shumë praktikë... mos u dorëzo!")

print("\nFaleminderit që luajte quiz-in matematikor! 💡")
