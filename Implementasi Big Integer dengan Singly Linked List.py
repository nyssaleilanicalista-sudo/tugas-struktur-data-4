# Definisi Node untuk Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class BigInteger:
    def __init__(self, initValue="0"):
        # Menyimpan digit dari belakang ke depan (Least Significant Digit) 
        self.head = None
        self.tail = None
        
        # Membersihkan string input dan membaliknya
        initValue = str(initValue).strip()
        for char in reversed(initValue):
            self._append_digit(int(char))

    def _append_digit(self, digit):
        """Menambahkan digit di akhir linked list (digit yang lebih signifikan)"""
        new_node = Node(digit)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def toString(self):
        """Mengembalikan representasi string dari angka [cite: 11]"""
        if not self.head:
            return "0"
        
        digits = []
        current = self.head
        while current:
            digits.append(str(current.data))
            current = current.next
        
        # Balikkan kembali untuk menampilkan angka yang benar
        return "".join(reversed(digits))

    def __add__(self, other):
        """Operasi penjumlahan sederhana (+) [cite: 16]"""
        result = BigInteger("")
        curr1 = self.head
        curr2 = other.head
        carry = 0 # Simpanan jika hasil > 9
        
        while curr1 or curr2 or carry:
            val1 = curr1.data if curr1 else 0
            val2 = curr2.data if curr2 else 0
            
            # Hitung total digit dan simpanan (carry)
            total = val1 + val2 + carry
            carry = total // 10
            result._append_digit(total % 10)
            
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
            
        return result

    # Implementasi assignment combo operator += 
    def __iadd__(self, other):
        temp_res = self + other
        self.head = temp_res.head
        self.tail = temp_res.tail
        return self

# Contoh Penggunaan
num1 = BigInteger("45839")
num2 = BigInteger("12345")

print(f"Angka 1: {num1.toString()}") # Output: 45839
print(f"Angka 2: {num2.toString()}") # Output: 12345

# Penjumlahan
hasil = num1 + num2
print(f"Hasil Penjumlahan: {hasil.toString()}") # Output: 58184

# Assignment Operator (+=)
num1 += num2
print(f"Setelah num1 += num2: {num1.toString()}")