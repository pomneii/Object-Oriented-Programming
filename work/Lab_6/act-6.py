
"""
    ภาค 1 :
        1. ธนาคารให้บริการ User เปิดบัญชี โดยมีบัญชีประเภทเดียว คือ ออมทรัพย์ โดย User 1 คนจะเปิดกี่บัญชีก็ได้
        โดยข้อมูลของ User ประกอบด้วย 
            1) เลขประจําตัวประชาชน (สมมติ) 2) ชื่อ-นามสกุล 
        ส่วนข้อมูลของบัญชีประกอบด้วย 
            1) หมายเลขบัญชี 2) เจ้าของบัญชี (instance)
        2. ใน 1 บัญชี สามารถขอบัตร ATM ได้ 1 บัตร เพื่อใช้กับเครื่อง ATM ได้ 
        โดยบัตร ATM จะมีหมายเลขบัตรและข้อมูลในบัตร ได้แก่ 
            1) หมายเลขบัตร 2) PIN Number
        3. ธนาคารจะมีหลักเกณฑ์และอัตราต่างๆ ได้แก่
            1) บัตร ATM จะมีค่าธรรมเนียมรายปี 150 บาท 2) บัตร ATM จะเบิกเงินสูงสุดต่อวันไม่เกิน 40,000 บาท
        4. ผู้ใช้สามารถใช้บัตรกับเครื่อง ATM โดยตู้ ATM จะมีข้อมูลคือ 
            1) หมายเลขตู้ 2) เงินที่มีในตู้ กําหนดให้ค่าเริ่มต้นคือ 1,000,000 บาท
        5. การทํากิจกรรมกับธนาคารให้ทําผ่านเครื่อง ATM เท่านั้น กิจกรรมที่ทํากับเครื่อง ATM ได้ประกอบด้วย
            1) การฝากเงิน (Deposit) 2) การถอนเงิน (Withdraw) และการโอนเงิน (Transfer) 
           โดยการถอนเงินและการโอนเงิน จะต้องไม่เกิน อัตราเบิกเงินสูงสุดต่อวัน และการจัดการยอดเงินในบัญชีต้องทำในบัญชีเท่านั้น
        6. ในการทํารายการแต่ละครั้งต้องมีการบันทึกได้แก่ 
            1) ประเภทรายการ (D=Deposit, W=Withdraw,T=Transfer) 2) จํานวนเงิน 3) วัน-เวลา 4) หมายเลขตู้ ATM 5) กรณีโอนจะเก็บเลขบัญชีที่โอนด้วย

        คําสั่ง
        1. ให้เขียน Class Diagram ที่แสดงถึงระบบข้างต้น
        2. ให้เขียนโปรแกรม ที่ทํางานตาม Class Diagram ที่เขียนขึ้น โปรแกรมจะต้องเป็นไปตามข้อกําหนดดังนี้
            - ห้ามใช้ dictionary ในการเก็บข้อมูล
            - ห้ามเก็บข้อมูลนอกคลาส และ ห้ามเก็บข้อมูลซ้ำซ้อน และ ทุกข้อมูลต้องเป็น private
            - ในการสร้างคลาสให้กําหนดว่าจะเก็บข้อมูลใด และ ห้ามมิให้เก็บข้อมูลที่ไม่ใช่ข้อมูลที่เกี่ยวข้องกับ
            คลาสนั้น หากไม่สามารถเก็บลงในคลาสใดได้เลย ให้พิจารณาสร้างคลาสใหม่
            - ในคลาสไม่ให้มีการ Input ค่าหรือ print ค่าโดยตรง ให้ส่งข้อมูล parameter เข้าไปและได้ข้อมูล
            กลับมาเท่านั้น (ให้มอง class เป็น service)
            - ข้อมูลที่เก็บในคลาสที่ไม่ใช่คลาสพื้นฐาน จะต้องเก็บข้อมูลเป็น Instance ของคลาสพื้นฐานเท่านั้น
            และ function ที่เกี่ยวข้องกับข้อมูลใน class ต้องเป็น method เท่านั้น
            - ข้อมูลที่จะเก็บสู่ Class ต้องมี Validation
        3. ในการสร้าง instance ให้มีข้อมูลของ
            - User จํานวน 2 คน กําหนดให้ Citizen ID เป็น 1-1101-12345-nn-0 โดย nn เป็นรหัส 2 ตัว
            สุดท้ายของรหัส นศ. สําหรับคนที่ 2 ให้ใช้ nn+1
            - บัญชี จํานวน 1 บัญชีต่อคน ให้เลขบัญชี 10 หลัก
            - บัตร ATM 1 บัตรต่อ 1 บัญชี สําหรับ Pin ให้ใช้เป็น 1234
            - ตู้ ATM จํานวน 2 ตู้
        4. Test Case จะมี 7 Test Case
            - Test Case #1 : สอดบัตร เข้าตู้ ATM
            - Test Case #2 : ฝากเงิน
            - Test Case #3 : ฝากเงิน แต่ส่งค่าติดลบ
            - Test Case #4 : ถอนเงิน
            - Test Case #5 : ถอนเงิน มากกว่าเงินในบัญชี
            - Test Case #6 : โอนเงิน
            - Test Case #7 : แสดง statement
    
    ภาค 2
        1. ในเวลาต่อมา ธนาคารได้ออกผลิตภัณฑ์ใหม่ โดยเป็น Debit Card โดยมีความสามารถเหมือนกับ ATM
           Card ทุกประการ และสามารถใช้ในการซื้อสินค้าได้ด้วย โดยรายการซื้อสินค้าจะใช้รหัส P (Paid)
        2. ธนาคารได้เพิ่มบัญชีแบบฝากประจํา ซึ่งไม่สามารถมีบัตร ATM ได้ แต่จะมีดอกเบี้ยเมื่อครบปี
        
        คําสั่ง
        1. ให้ปรับปรุง Class Diagram ที่แสดงถึงระบบข้างต้น
        2. ให้ defector code เพื่อให้สามารถรับรายการซื้อของโดยใช้บัตร Debit ได้ด้วย และ สามารถเปิดบัญชีฝากประจําได้
"""

class Bank :
    def __init__(self) :
        self.__users_list = []
        self.__atms_list = []

    # add user
    def add_user(self, user) : 
        if not isinstance(user, User) :
            return False
        self.__users_list.append(user)

    # add atm
    def add_atm(self, atm) : 
        if not isinstance(atm, ATM) :
            return False
        self.__atms_list.append(atm)

    def get_list_of_users(self) :
        return self.__users_list
    
    def get_list_of_atms(self) :
        return self.__atms_list

class User :
    def __init__(self, person_ID, name) :
        self.__person_ID = person_ID
        self.__name = name   
    # User 1 --> more than 1 account
        self.__account_list = []
        
    # add account
    def add_account(self, accounts) :
        if not isinstance(accounts, Account) :
            return False
        self.__account_list.append(accounts)

    def get_accounts_list(self) :
        return self.__account_list

    def get_name(self) :
        return self.__name  

class Account :
    # ส่วนข้อมูลของบัญชีประกอบด้วย 1) หมายเลขบัญชี 2) เจ้าของบัญชี (instance)
    def __init__(self, acc_ID, user, balance) :
        self.__acc_ID = acc_ID
        self.__user_own = user
        self.__balance = balance
        self.__transactions = []

    # ใน 1 บัญชี สามารถขอบัตร ATM ได้ 1 บัตร -> list card (atm, debit, credit, etc.)
        self.__card_list = []
    
    def add_Card(self, cards) : 
        if not isinstance(cards, ATM_Card) :
            return False
        self.__card_list.append(cards)

    def add_Transactions(self, transaction) :
        self.__transactions.append(transaction)

    def deposit_in_account(self, account, amount) :
        if not isinstance(account, Account) or amount <= 0 :
            return "Error"
        self.__balance += amount

    def withdraw_in_account(self, account, amount) :
        if not isinstance(account, Account) or amount <= 0 or amount > account.get_balance_in_account() :
            return "Error"
        self.__balance -= amount

    def transfer_in_account(self, first_account, second_account, amount) :
        if not isinstance(first_account, Account) or not isinstance(second_account, Account) or amount <= 0 or amount > first_account.get_balance_in_account() :
            return "Error"
        first_account.withdraw_in_account(first_account, amount)
        second_account.deposit_in_account(second_account, amount)

    def get_cards_list(self) :
        return self.__card_list

    def get_account_id(self) :
        return self.__acc_ID

    def get_user_own(self) :
        return self.__user_own
    
    def get_balance_in_account(self) :
        return self.__balance
    
    def get_transactions_account(self) :
        return self.__transactions
    
    def __str__(self) :
        name_account = self.__user_own.get_name()
        transact = "\n".join([f"{name_account} transaction : {transacts}" for transacts in self.__transactions])
        return transact

class ATM :
    # โดยตู้ ATM จะมีข้อมูลคือ 1) หมายเลขตู้ 2) เงินที่มีในตู้
    def __init__(self, atm_no, balance) :
        self.__atm_no = atm_no
        self.__balance = balance

    def check_card_atm(self, bank, enter_atm_card, pin_number) :
        for user in bank.get_list_of_users() :
            for account in user.get_accounts_list() :
                for atm_card in account.get_cards_list() :
                    if atm_card.get_card_ID() == enter_atm_card and atm_card.get_pin() == pin_number :
                        return account
        return None
    
    def deposit_in_atm(self, account, amount, atm_number) :
        if not isinstance(account, Account) or amount <= 0 :
            return "Error"
        self.__balance += amount
        account.deposit_in_account(account, amount)
        account.add_Transactions(f"D-ATM:{atm_number}-{str(amount)}-{str(account.get_balance_in_account())}")
        return "Success"
    
    def withdraw_in_atm(self, account, amount, atm_number) :
        if not isinstance(account, Account) or amount <= 0 or amount > account.get_balance_in_account() :
            return "Error"
        self.__balance -= amount
        account.withdraw_in_account(account, amount)
        account.add_Transactions(f"W-ATM:{atm_number}-{str(amount)}-{str(account.get_balance_in_account())}")
        return "Success"
    
    def transfer_in_atm(self, first_account, second_account, amount, atm_number) :
        if not isinstance(first_account, Account) or not isinstance(second_account, Account) or amount <= 0 or amount > first_account.get_balance_in_account() :
            return "Error"
        first_account.transfer_in_account(first_account, second_account, amount)
        first_account.add_Transactions(f"T-ATM:{atm_number}--{str(amount)}-{str(first_account.get_balance_in_account())}")
        second_account.add_Transactions(f"T-ATM:{atm_number}-+{str(amount)}-{str(second_account.get_balance_in_account())}")
        return "Success"

    def get_atm_no(self) :
        return self.__atm_no
    
    def get_balance_in_atm(self) :
        return self.__balance

class Card :
    pass

class ATM_Card :
    # โดยบัตร ATM จะมีหมายเลขบัตรและข้อมูลในบัตร ได้แก่ 1) หมายเลขบัตร 2) PIN Number
    atm_card_fee = 150
    def __init__(self, account, card_ID) :
        self.__acc_data = account
        self.__card_ID = card_ID
        self.__pin_number = 1234

    def get_card_ID(self) :
        return self.__card_ID
    
    def get_pin(self) :
        return self.__pin_number

# Class Code

##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM, จำนวนเงิน ]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance จากข้อมูล Dictionary
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
    

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 3 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card 3) entered Pin ที่ user input ให้เครื่อง ATM
# TODO     return ถ้าบัตร และ Pin ถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 3 ตัว คือ 
# TODO     1) instance ของ account ตนเอง 2) instance ของ account ที่โอนไป 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm = {'1001':1000000,'1002':200000}

def create_bank(users, atms) :

    bank = Bank()
    
    for per_ID, value in users.items() :
        user = User(per_ID, value[0])
        account = Account(value[1], user, value[3])
        atm_card = ATM_Card(account, value[2])

        account.add_Card(atm_card)
        user.add_account(account)
        bank.add_user(user)

    for atm_no, value in atms.items() :
        atm = ATM(atm_no, value)
        bank.add_atm(atm)
    return bank

banks = create_bank(user, atm)

# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

print("Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harryและ Pin ที่รับมา")
print("Ans : 12345, 1234567890, Success")
pin = int(input("Enter PIN number : "))
test_1 = banks.get_list_of_atms()[0].check_card_atm(banks, '12345', pin)
if test_1 != None :
    print(f"{test_1.get_cards_list()[0].get_card_ID()}, {test_1.get_account_id()}, Success")
else :
    print("Invalid Card")
print('')

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
    
print("Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท")
print("Ans : Hermione account before test : 1000 Hermione account after test : 2000")
Hermione_account = banks.get_list_of_users()[1].get_accounts_list()[0]
before_deposit = Hermione_account.get_balance_in_account()
deposit = banks.get_list_of_atms()[1].deposit_in_atm(Hermione_account, 1000, banks.get_list_of_atms()[1].get_atm_no())
after_deposit = Hermione_account.get_balance_in_account()
print("Hermione account before test :", before_deposit)
# print(deposit)
print("Hermione account after test :", after_deposit)
print('')

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error

print("Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท")
print("Ans : Error")
deposit = banks.get_list_of_atms()[1].deposit_in_atm(Hermione_account, -1, banks.get_list_of_atms()[1].get_atm_no())
print(deposit)
print('')

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

print("Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท")
print("Ans : Hermione account before test : 2000 Hermione account after test : 1500")
before_withdraw = Hermione_account.get_balance_in_account()
withdraw = banks.get_list_of_atms()[1].withdraw_in_atm(Hermione_account, 500, banks.get_list_of_atms()[1].get_atm_no())
after_witdraw = Hermione_account.get_balance_in_account()
print("Hermione account before test :", before_withdraw)
# print(withdraw)
print("Hermione account after test :", after_witdraw)
print('')

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

print("Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท")
print("Ans : Error")
withdraw = banks.get_list_of_atms()[1].withdraw_in_atm(Hermione_account, 2000, banks.get_list_of_atms()[1].get_atm_no())
print(withdraw)
print('')

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500

print("Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2")
print("Ans : Harry account before test : 20000 Harry account after test : 10000 Hermione account before test : 1500 Hermione account after test : 11500")
Harry_account = banks.get_list_of_users()[0].get_accounts_list()[0]
harry_before = Harry_account.get_balance_in_account()
hermione_before = Hermione_account.get_balance_in_account()
transfer = banks.get_list_of_atms()[1].transfer_in_atm(Harry_account, Hermione_account, 10000, banks.get_list_of_atms()[1].get_atm_no())
harry_after = Harry_account.get_balance_in_account()
hermione_after = Hermione_account.get_balance_in_account()
print("Harry account before test :", harry_before)
print("Harry account after test :", harry_after)
print("Hermione account before test :", hermione_before)
print("Hermione account after test :", hermione_after)
print('')

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test case #7 : แสดง transaction ของ Hermione ทั้งหมด")
print("Ans : # Hermione transaction : D-ATM:1002-1000-2000 Hermione transaction : W-ATM:1002-500-1500 Hermione transaction : T-ATM:1002-+10000-11500")
print(Hermione_account.__str__())
print('')
