from tkinter import *
import pymysql
import tkinter.messagebox

def main():
    root = Tk()
    app = Window1(root)


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Talent Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle1 = Label(self.frame, text='Talent Management System', font=('arial', 50, 'bold'), bd=20)
        self.LabelTitle1.grid(row=0, column=0, columnspan=2, pady=40)

        self.LoginFrame = Frame(self.frame, width=1010, height=500, bd=20, relief='ridge')
        self.LoginFrame.grid(row=1, column=0)

        self.LabelTitle2 = Label(self.LoginFrame, text='Login', font=('arial', 50, 'bold', UNDERLINE), bd=20)
        self.LabelTitle2.grid(row=0, column=0, columnspan=2, pady=20, sticky='W')

        self.LoginLabel1 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="Enter Username: ")
        self.LoginLabel1.grid(row=1, column=0)
        self.LoginEntry1 = Entry(self.LoginFrame, font=('arial', 30), bd=22, textvariable=self.Username)
        self.LoginEntry1.grid(row=1, column=1)

        self.LoginLabel2 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="Enter Password: ")
        self.LoginLabel2.grid(row=2, column=0)
        self.LoginEntry2 = Entry(self.LoginFrame, font=('arial', 30), show="*", bd=22, textvariable=self.Password)
        self.LoginEntry2.grid(row=2, column=1)

        self.LoginBtn1 = Button(self.LoginFrame, font=('arial', 20, 'bold'), width=17, padx=18, pady=8, text="Login",
                                command=self.Login)
        self.LoginBtn1.grid(row=3, column=1, sticky='W')

        self.LoginLabel3 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="New User? ")
        self.LoginLabel3.grid(row=4, column=0)

        self.LoginBtn2 = Button(self.LoginFrame, font=('arial', 20, 'bold'), width=17, padx=18, pady=8, text="Register",
                                command=self.Registration)
        self.LoginBtn2.grid(row=4, column=1, sticky='W')

    def Login(self):
        usr = self.Username.get()
        passwd = self.Password.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("SELECT TYPE, USERNAME, PASSWORD FROM LOGIN_INFO WHERE USERNAME='%s' \
                    AND PASSWORD='%s'"
                    % (usr, passwd))
        success = cur.fetchall()
        if success:
            for i in success:
                if i[0] == 'ADMIN':
                    self.Username.set("")
                    self.Password.set("")
                    tkinter.messagebox.showinfo("Success!", "Logged in as Admin")
                    self.Admin()
                    con.commit()
                elif i[0] == 'USER':
                    self.Username.set("")
                    self.Password.set("")
                    tkinter.messagebox.showinfo("Success!", "Logged in as User")
                    self.User()
                    con.commit()
        else:
            con.commit()
            self.Username.set("")
            self.Password.set("")
            tkinter.messagebox.showinfo("Failed", "Invalid Username or Password")
        return

    def Registration(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Admin(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)

    def User(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Talent Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LID = IntVar()
        self.UID = IntVar()
        self.Type = StringVar()
        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text='Register', font=('arial', 50, 'bold', UNDERLINE), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20, sticky='W')

        self.LoginFrame = Frame(self.frame, width=1010, height=500, bd=20, relief='ridge')
        self.LoginFrame.grid(row=1, column=0)

        self.RegLabel1 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="Enter LID: ")
        self.RegLabel1.grid(row=0, column=0)
        self.RegEntry1 = Entry(self.LoginFrame, font=('arial', 30), bd=22, textvariable=self.LID)
        self.RegEntry1.grid(row=0, column=1)

        self.RegLabel3 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="Enter User Type: ")
        self.RegLabel3.grid(row=2, column=0)
        self.RegEntry3 = Entry(self.LoginFrame, font=('arial', 30), bd=22, textvariable=self.Type)
        self.RegEntry3.grid(row=2, column=1)

        self.RegLabel4 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="Enter Username: ")
        self.RegLabel4.grid(row=3, column=0)
        self.RegEntry4 = Entry(self.LoginFrame, font=('arial', 30), bd=22, textvariable=self.Username)
        self.RegEntry4.grid(row=3, column=1)

        self.RegLabel5 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="Enter Password: ")
        self.RegLabel5.grid(row=4, column=0)
        self.RegEntry5 = Entry(self.LoginFrame, font=('arial', 30), bd=22, textvariable=self.Password)
        self.RegEntry5.grid(row=4, column=1)

        self.RegLabel2 = Label(self.LoginFrame, font=('arial', 30, 'bold'), text="Enter UID: ")
        self.RegLabel2.grid(row=1, column=0)
        self.RegEntry2 = Entry(self.LoginFrame, font=('arial', 30), bd=22, textvariable=self.UID)
        self.RegEntry2.grid(row=1, column=1)

        self.Btn = Button(self.LoginFrame, font=('arial', 20, 'bold'), width=17, padx=18, pady=8, text="Register",
                          command=self.Reg)
        self.Btn.grid(row=5, column=1, sticky='W')

    def Reg(self):
        lid = self.LID.get()
        uid = self.UID.get()
        type = self.Type.get()
        usr = self.Username.get()
        passwd = self.Password.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("INSERT INTO LOGIN_INFO VALUES(%d, '%s', '%s', '%s', '%s')" % (lid, type, usr, passwd, uid))
        con.commit()

        self.LID.set("")
        self.UID.set("")
        self.Type.set("")
        self.Username.set("")
        self.Password.set("")

        self.Exit()

    def Exit(self):
        tkinter.messagebox.showinfo("Success!", "Registration Successful!")
        self.master.destroy()
        return


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Talent Management System")
        self.master.geometry('1920x1080+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.talent = StringVar()
        self.LID = IntVar()
        self.Type = StringVar()
        self.Username = StringVar()
        self.Password = StringVar()
        self.UID = IntVar()
        self.FName = StringVar()
        self.LName = StringVar()
        self.Phone = IntVar()
        self.City = StringVar()
        self.MailID = StringVar()
        self.SID = IntVar()
        self.Skill = StringVar()
        self.NoProject = IntVar()
        self.NoCertificate = IntVar()
        self.CID = IntVar()
        self.PlaceSecured = IntVar()
        self.CertificateDescription = StringVar()
        self.PID = IntVar()
        self.ProjectDescription = StringVar()

        self.LabelTitle = Label(self.frame, text='Talent Management System', font=('arial', 30, 'bold', UNDERLINE),
                                bd=10)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # --------------------------------------------------------------------------------------------------------------

        self.TalentFrame = Frame(self.frame, bd=20, relief='ridge')
        self.TalentFrame.grid(row=1, column=0, sticky='W')

        self.LabelTalentTitle = Label(self.TalentFrame, text='Search Talent', font=('arial', 20, 'bold', UNDERLINE))
        self.LabelTalentTitle.grid(row=0, column=0, sticky='W')

        self.LabelTalent = Label(self.TalentFrame, text='Enter Talent To search in Database: ',
                                 font=('arial', 15, 'bold'))
        self.LabelTalent.grid(row=1, column=0)
        self.LabelTalentEntry = Entry(self.TalentFrame, font=('arial', 15, 'bold'), bd=15, textvariable=self.talent)
        self.LabelTalentEntry.grid(row=1, column=1)

        self.LabelTalentButton = Button(self.TalentFrame, font=('arial', 20, 'bold'), width=17, padx=18, pady=8,
                                        text="Search", command=self.SearchTalent)
        self.LabelTalentButton.grid(row=2, column=1, sticky='W')

        # --------------------------------------------------------------------------------------------------------------

        self.DBMSFrame = Frame(self.frame, bd=20, relief='ridge')
        self.DBMSFrame.grid(row=2, column=0, sticky='W')

        self.DBMSTableFrame2 = Frame(self.DBMSFrame, bd=10, relief='ridge')
        self.DBMSTableFrame2.grid(row=0, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.BasicInfoTitle = Label(self.DBMSTableFrame2, text='Basic Info', font=('arial', 20, 'bold', UNDERLINE))
        self.BasicInfoTitle.grid(row=0, column=0, sticky='W')

        self.BasicInfoLabel1 = Label(self.DBMSTableFrame2, font=('arial', 15, 'bold'), text="Enter UID: ")
        self.BasicInfoLabel1.grid(row=1, column=0, sticky='W')
        self.BasicInfoEntry1 = Entry(self.DBMSTableFrame2, font=('arial', 10), bd=5, textvariable=self.UID)
        self.BasicInfoEntry1.grid(row=1, column=1)

        self.BasicInfoLabel2 = Label(self.DBMSTableFrame2, font=('arial', 15, 'bold'), text="Enter First Name: ")
        self.BasicInfoLabel2.grid(row=2, column=0, sticky='W')
        self.BasicInfoEntry2 = Entry(self.DBMSTableFrame2, font=('arial', 10), bd=5, textvariable=self.FName)
        self.BasicInfoEntry2.grid(row=2, column=1)

        self.BasicInfoLabel3 = Label(self.DBMSTableFrame2, font=('arial', 15, 'bold'), text="Enter Last Name: ")
        self.BasicInfoLabel3.grid(row=3, column=0, sticky='W')
        self.BasicInfoEntry3 = Entry(self.DBMSTableFrame2, font=('arial', 10), bd=5, textvariable=self.LName)
        self.BasicInfoEntry3.grid(row=3, column=1)

        self.BasicInfoLabel4 = Label(self.DBMSTableFrame2, font=('arial', 15, 'bold'), text="Enter Phone Number: ")
        self.BasicInfoLabel4.grid(row=4, column=0, sticky='W')
        self.BasicInfoEntry4 = Entry(self.DBMSTableFrame2, font=('arial', 10), bd=5, textvariable=self.Phone)
        self.BasicInfoEntry4.grid(row=4, column=1)

        self.BasicInfoLabel5 = Label(self.DBMSTableFrame2, font=('arial', 15, 'bold'), text="Enter City: ")
        self.BasicInfoLabel5.grid(row=5, column=0, sticky='W')
        self.BasicInfoEntry5 = Entry(self.DBMSTableFrame2, font=('arial', 10), bd=5, textvariable=self.City)
        self.BasicInfoEntry5.grid(row=5, column=1)

        self.BasicInfoLabel6 = Label(self.DBMSTableFrame2, font=('arial', 15, 'bold'), text="Enter Mail ID: ")
        self.BasicInfoLabel6.grid(row=6, column=0, sticky='W')
        self.BasicInfoEntry6 = Entry(self.DBMSTableFrame2, font=('arial', 10), bd=5, textvariable=self.MailID)
        self.BasicInfoEntry6.grid(row=6, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.DBMSTableFrame1 = Frame(self.DBMSFrame, bd=10, relief='ridge')
        self.DBMSTableFrame1.grid(row=0, column=0, sticky='W')

        # -------------------------------------------------------------------------------------------------------------

        self.LoginInfoTitle = Label(self.DBMSTableFrame1, text='Login Info', font=('arial', 20, 'bold', UNDERLINE))
        self.LoginInfoTitle.grid(row=0, column=0, sticky='W')

        self.LoginInfoLabel1 = Label(self.DBMSTableFrame1, font=('arial', 15, 'bold'), text="Enter Login ID: ")
        self.LoginInfoLabel1.grid(row=1, column=0, sticky='W')
        self.LoginInfoEntry1 = Entry(self.DBMSTableFrame1, font=('arial', 10), bd=5, textvariable=self.LID)
        self.LoginInfoEntry1.grid(row=1, column=1)

        self.LoginInfoLabel3 = Label(self.DBMSTableFrame1, font=('arial', 15, 'bold'), text="Enter Admin/User: ")
        self.LoginInfoLabel3.grid(row=2, column=0, sticky='W')
        self.LoginInfoEntry3 = Entry(self.DBMSTableFrame1, font=('arial', 10), bd=5, textvariable=self.Type)
        self.LoginInfoEntry3.grid(row=2, column=1)

        self.LoginInfoLabel4 = Label(self.DBMSTableFrame1, font=('arial', 15, 'bold'), text="Enter Username: ")
        self.LoginInfoLabel4.grid(row=3, column=0, sticky='W')
        self.LoginInfoEntry4 = Entry(self.DBMSTableFrame1, font=('arial', 10), bd=5, textvariable=self.Username)
        self.LoginInfoEntry4.grid(row=3, column=1)

        self.LoginInfoLabel5 = Label(self.DBMSTableFrame1, font=('arial', 15, 'bold'), text="Enter Password: ")
        self.LoginInfoLabel5.grid(row=4, column=0, sticky='W')
        self.LoginInfoEntry5 = Entry(self.DBMSTableFrame1, font=('arial', 10), bd=5, textvariable=self.Password)
        self.LoginInfoEntry5.grid(row=4, column=1)

        self.LoginInfoLabel2 = Label(self.DBMSTableFrame1, font=('arial', 15, 'bold'), text="Enter UID: ")
        self.LoginInfoLabel2.grid(row=5, column=0, sticky='W')
        self.LoginInfoEntry2 = Entry(self.DBMSTableFrame1, font=('arial', 10), bd=5, textvariable=self.UID)
        self.LoginInfoEntry2.grid(row=5, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.DBMSTableFrame3 = Frame(self.DBMSFrame, bd=10, relief='ridge')
        self.DBMSTableFrame3.grid(row=0, column=2)

        # -------------------------------------------------------------------------------------------------------------

        self.SkillsTitle = Label(self.DBMSTableFrame3, text='Skills', font=('arial', 20, 'bold', UNDERLINE))
        self.SkillsTitle.grid(row=0, column=0, sticky='W')

        self.SkillsLabel2 = Label(self.DBMSTableFrame3, font=('arial', 15, 'bold'), text="Enter Skill ID: ")
        self.SkillsLabel2.grid(row=1, column=0, sticky='W')
        self.SkillsEntry2 = Entry(self.DBMSTableFrame3, font=('arial', 10), bd=5, textvariable=self.SID)
        self.SkillsEntry2.grid(row=1, column=1)

        self.SkillsLabel3 = Label(self.DBMSTableFrame3, font=('arial', 15, 'bold'), text="Enter Skill: ")
        self.SkillsLabel3.grid(row=2, column=0, sticky='W')
        self.SkillsEntry3 = Entry(self.DBMSTableFrame3, font=('arial', 10), bd=5, textvariable=self.Skill)
        self.SkillsEntry3.grid(row=2, column=1)

        self.SkillsLabel4 = Label(self.DBMSTableFrame3, font=('arial', 15, 'bold'), text="Enter No. of Projects: ")
        self.SkillsLabel4.grid(row=3, column=0, sticky='W')
        self.SkillsEntry4 = Entry(self.DBMSTableFrame3, font=('arial', 10), bd=5, textvariable=self.NoProject)
        self.SkillsEntry4.grid(row=3, column=1)

        self.SkillsLabel5 = Label(self.DBMSTableFrame3, font=('arial', 15, 'bold'), text="Enter No. of Certificates: ")
        self.SkillsLabel5.grid(row=4, column=0, sticky='W')
        self.SkillsEntry5 = Entry(self.DBMSTableFrame3, font=('arial', 10), bd=5, textvariable=self.NoCertificate)
        self.SkillsEntry5.grid(row=4, column=1)

        self.SkillsLabel1 = Label(self.DBMSTableFrame3, font=('arial', 15, 'bold'), text="Enter UID: ")
        self.SkillsLabel1.grid(row=5, column=0, sticky='W')
        self.SkillsEntry1 = Entry(self.DBMSTableFrame3, font=('arial', 10), bd=5, textvariable=self.UID)
        self.SkillsEntry1.grid(row=5, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.DBMSTableFrame4 = Frame(self.DBMSFrame, bd=10, relief='ridge')
        self.DBMSTableFrame4.grid(row=1, column=0)

        # -------------------------------------------------------------------------------------------------------------

        self.SkillCertTitle = Label(self.DBMSTableFrame4, text='Skill Certification', font=('arial', 20, 'bold',
                                                                                            UNDERLINE))
        self.SkillCertTitle.grid(row=0, column=0, sticky='W')

        self.SkillCertLabel2 = Label(self.DBMSTableFrame4, font=('arial', 15, 'bold'), text="Enter Certificate ID: ")
        self.SkillCertLabel2.grid(row=1, column=0, sticky='W')
        self.SkillCertEntry2 = Entry(self.DBMSTableFrame4, font=('arial', 10), bd=5, textvariable=self.CID)
        self.SkillCertEntry2.grid(row=1, column=1)

        self.SkillCertLabel3 = Label(self.DBMSTableFrame4, font=('arial', 15, 'bold'), text="Enter Place Secured: ")
        self.SkillCertLabel3.grid(row=2, column=0, sticky='W')
        self.SkillCertEntry3 = Entry(self.DBMSTableFrame4, font=('arial', 10), bd=5, textvariable=self.PlaceSecured)
        self.SkillCertEntry3.grid(row=2, column=1)

        self.SkillCertLabel4 = Label(self.DBMSTableFrame4, font=('arial', 15, 'bold'), text="Enter Certificate Desc.: ")
        self.SkillCertLabel4.grid(row=3, column=0, sticky='W')
        self.SkillCertEntry4 = Entry(self.DBMSTableFrame4, font=('arial', 10), bd=5,
                                     textvariable=self.CertificateDescription)
        self.SkillCertEntry4.grid(row=3, column=1)

        self.SkillCertLabel1 = Label(self.DBMSTableFrame4, font=('arial', 15, 'bold'), text="Enter User Skill ID: ")
        self.SkillCertLabel1.grid(row=4, column=0, sticky='W')
        self.SkillCertEntry1 = Entry(self.DBMSTableFrame4, font=('arial', 10), bd=5, textvariable=self.SID)
        self.SkillCertEntry1.grid(row=4, column=1)

        self.SkillsLabel1 = Label(self.DBMSTableFrame4, font=('arial', 15, 'bold'), text="Enter UID: ")
        self.SkillsLabel1.grid(row=5, column=0, sticky='W')
        self.SkillsEntry1 = Entry(self.DBMSTableFrame4, font=('arial', 10), bd=5, textvariable=self.UID)
        self.SkillsEntry1.grid(row=5, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.DBMSTableFrame5 = Frame(self.DBMSFrame, bd=10, relief='ridge')
        self.DBMSTableFrame5.grid(row=1, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.SkillProTitle = Label(self.DBMSTableFrame5, text='Skill Project', font=('arial', 20, 'bold', UNDERLINE))
        self.SkillProTitle.grid(row=0, column=0, sticky='W')

        self.SkillProLabel2 = Label(self.DBMSTableFrame5, font=('arial', 15, 'bold'), text="Enter Project ID: ")
        self.SkillProLabel2.grid(row=1, column=0, sticky='W')
        self.SkillProEntry2 = Entry(self.DBMSTableFrame5, font=('arial', 10), bd=5, textvariable=self.PID)
        self.SkillProEntry2.grid(row=1, column=1)

        self.SkillProLabel3 = Label(self.DBMSTableFrame5, font=('arial', 15, 'bold'), text="Enter Project Desc.: ")
        self.SkillProLabel3.grid(row=2, column=0, sticky='W')
        self.SkillProEntry3 = Entry(self.DBMSTableFrame5, font=('arial', 10), bd=5,
                                    textvariable=self.ProjectDescription)
        self.SkillProEntry3.grid(row=2, column=1)

        self.SkillProLabel1 = Label(self.DBMSTableFrame5, font=('arial', 15, 'bold'), text="Enter User Skill ID: ")
        self.SkillProLabel1.grid(row=3, column=0, sticky='W')
        self.SkillProEntry1 = Entry(self.DBMSTableFrame5, font=('arial', 10), bd=5, textvariable=self.SID)
        self.SkillProEntry1.grid(row=3, column=1)

        self.SkillsLabel1 = Label(self.DBMSTableFrame5, font=('arial', 15, 'bold'), text="Enter UID: ")
        self.SkillsLabel1.grid(row=4, column=0, sticky='W')
        self.SkillsEntry1 = Entry(self.DBMSTableFrame5, font=('arial', 10), bd=5, textvariable=self.UID)
        self.SkillsEntry1.grid(row=4, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.ButtonFrame1 = Frame(self.frame, bd=20, relief='ridge')
        self.ButtonFrame1.grid(row=2, column=1, sticky='W')

        # -------------------------------------------------------------------------------------------------------------

        self.btn1 = Button(self.ButtonFrame1, text='Add User/Admin', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.AddUA)
        self.btn1.grid(row=0, column=0)

        self.btn2 = Button(self.ButtonFrame1, text='View Database', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.ViewDB)
        self.btn2.grid(row=1, column=0)

        self.btn3 = Button(self.ButtonFrame1, text='View User/Admin', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.ViewUA)
        self.btn3.grid(row=2, column=0)

        self.btn4 = Button(self.ButtonFrame1, text='View User/Admin Skills', font=('arial', 10, 'bold'), width=20,
                           padx=10, pady=5, command=self.ViewUAS)
        self.btn4.grid(row=3, column=0)

        self.btn5 = Button(self.ButtonFrame1, text='View All Skills', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.ViewS)
        self.btn5.grid(row=4, column=0)

        self.btn6 = Button(self.ButtonFrame1, text='Delete User/Admin', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.Delete)
        self.btn6.grid(row=5, column=0)

        self.btn7 = Button(self.ButtonFrame1, text='Clear Data', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.ClearData)
        self.btn7.grid(row=6, column=0)

        self.btn8 = Button(self.ButtonFrame1, text='Exit', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.Exit)
        self.btn8.grid(row=7, column=0)

        # -------------------------------------------------------------------------------------------------------------

        self.ButtonFrame2 = Frame(self.frame, bd=20, relief='ridge')
        self.ButtonFrame2.grid(row=2, column=2, sticky='W')

        # -------------------------------------------------------------------------------------------------------------

        self.btn10 = Button(self.ButtonFrame2, text='Update Basic_Info', font=('arial', 10, 'bold'), width=20, padx=10,
                            pady=5, command=self.UpdateB)
        self.btn10.grid(row=0, column=0)

        self.btn11 = Button(self.ButtonFrame2, text='Update Login_Info', font=('arial', 10, 'bold'), width=20, padx=10,
                            pady=5, command=self.UpdateL)
        self.btn11.grid(row=1, column=0)

        self.btn12 = Button(self.ButtonFrame2, text='Update Skills', font=('arial', 10, 'bold'), width=20, padx=10,
                            pady=5, command=self.UpdateS)
        self.btn12.grid(row=2, column=0)

        self.btn13 = Button(self.ButtonFrame2, text='Update Skill_Certification', font=('arial', 10, 'bold'), width=20,
                            padx=10, pady=5, command=self.UpdateSC)
        self.btn13.grid(row=3, column=0)

        self.btn14 = Button(self.ButtonFrame2, text='Update Skill_Project', font=('arial', 10, 'bold'), width=20,
                            padx=10, pady=5, command=self.UpdateSP)
        self.btn14.grid(row=4, column=0)

        # -------------------------------------------------------------------------------------------------------------

        self.OutputFrame = Frame(self.frame, bd=20, relief='ridge')
        self.OutputFrame.grid(row=3, column=0, sticky='W')

        self.OutputTitle = Label(self.OutputFrame, text='Results: ', font=('arial', 20, 'bold', UNDERLINE))
        self.OutputTitle.grid(row=0, column=0, sticky='W')

        self.ScrollBar = Scrollbar(self.OutputFrame)
        self.ScrollBar.grid(row=1, column=1, sticky='NS')

        self.ListBox = Listbox(self.OutputFrame, width=130, height=10, font=('arial', 12, 'bold'),
                               xscrollcommand=self.ScrollBar.set)
        self.ListBox.grid(row=1, column=0, padx=8)
        self.ScrollBar.config(command=self.ListBox.xview)

    def SearchTalent(self):
        tal = self.talent.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("SELECT BASIC_INFO.UID, FNAME, SKILL, NO_OF_CERTIFICATES, NO_OF_PROJECTS FROM BASIC_INFO,\
                             SKILLS WHERE SKILL='%s' AND BASIC_INFO.UID=SKILLS.UID ORDER BY NO_OF_CERTIFICATES \
                             OR NO_OF_PROJECTS" % tal)
        f = cur.fetchall()
        con.commit()
        self.ListBox.delete(0, END)
        self.ListBox.insert(END, str("The top most person is best suitable for the requested talent"))
        for i in f:
            self.ListBox.insert(END, '--------------------------------------------')
            self.ListBox.insert(END, i)
        self.ListBox.insert(END, '--------------------------------------------')

    def AddUA(self):
        lid = self.LID.get()
        type = self.Type.get()
        username = self.Username.get()
        password = self.Password.get()
        uid = self.UID.get()
        fname = self.FName.get()
        lname = self.LName.get()
        phone = self.Phone.get()
        city = self.City.get()
        mailid = self.MailID.get()
        sid = self.SID.get()
        skill = self.Skill.get()
        nopro = self.NoProject.get()
        nocer = self.NoCertificate.get()
        cid = self.CID.get()
        placesec = self.PlaceSecured.get()
        cerdesc = self.CertificateDescription.get()
        pid = self.PID.get()
        prodesc = self.ProjectDescription.get()

        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS TMS")
        cur.execute("CREATE TABLE IF NOT EXISTS BASIC_INFO(UID INTEGER PRIMARY KEY, FNAME VARCHAR(20), \
                    LNAME VARCHAR(20), PHONE_NO BIGINT(10), CITY VARCHAR(20), MAILID VARCHAR(50))")
        cur.execute("CREATE TABLE IF NOT EXISTS LOGIN_INFO(LID INTEGER PRIMARY KEY, TYPE VARCHAR(20), \
                    USERNAME VARCHAR(20), PASSWORD VARCHAR(20), UID INTEGER, FOREIGN KEY(UID) REFERENCES \
                    BASIC_INFO(UID) ON DELETE CASCADE)")
        cur.execute("CREATE TABLE IF NOT EXISTS SKILLS(SID INTEGER PRIMARY KEY, SKILL VARCHAR(20), \
                    NO_OF_CERTIFICATES INTEGER, NO_OF_PROJECTS INTEGER, UID INTEGER, FOREIGN KEY(UID) REFERENCES \
                    BASIC_INFO(UID) ON DELETE CASCADE)")
        cur.execute("CREATE TABLE IF NOT EXISTS SKILL_CERTIFICATION(CID INTEGER PRIMARY KEY, PLACE_SECURED INTEGER, \
                    CERTIFICATE_DESCRIPTION VARCHAR(20), SID INTEGER, UID INTEGER, FOREIGN KEY(SID) REFERENCES \
                    SKILLS(SID) ON DELETE CASCADE, FOREIGN KEY(UID) REFERENCES BASIC_INFO(UID) ON DELETE CASCADE)")
        cur.execute("CREATE TABLE IF NOT EXISTS SKILL_PROJECT(PID INTEGER PRIMARY KEY, \
                    PROJECT_DESCRIPTION VARCHAR(20),SID INTEGER, UID INTEGER, FOREIGN KEY(SID) REFERENCES SKILLS(SID) \
                    ON DELETE CASCADE, FOREIGN KEY(UID) REFERENCES BASIC_INFO(UID) ON DELETE CASCADE)")
        cur.execute("INSERT INTO BASIC_INFO VALUES(%d, '%s', '%s', %d, '%s', '%s')"
                    % (uid, fname, lname, phone, city, mailid))
        cur.execute("INSERT INTO LOGIN_INFO VALUES(%d, '%s', '%s', '%s', %d)"
                    % (lid, type, username, password, uid))
        cur.execute("INSERT INTO SKILLS VALUES(%d, '%s', %d, %d, %d)"
                    % (sid, skill, nopro, nocer, uid))
        cur.execute("INSERT INTO SKILL_CERTIFICATION VALUES(%d, %d, '%s', %d, %d)"
                    % (cid, placesec, cerdesc, sid, uid))
        cur.execute("INSERT INTO SKILL_PROJECT VALUES(%d, '%s', %d, %d)"
                    % (pid, prodesc, sid, uid))
        con.commit()

        self.LID.set("")
        self.Type.set("")
        self.Username.set("")
        self.Password.set("")
        self.UID.set("")
        self.FName.set("")
        self.LName.set("")
        self.Phone.set("")
        self.City.set("")
        self.MailID.set("")
        self.SID.set("")
        self.Skill.set("")
        self.NoProject.set("")
        self.NoCertificate.set("")
        self.CID.set("")
        self.PlaceSecured.set("")
        self.CertificateDescription.set("")
        self.PID.set("")
        self.ProjectDescription.set("")

    def ViewDB(self):
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("SELECT * FROM BASIC_INFO")
        a = cur.fetchall()
        cur.execute("SELECT * FROM LOGIN_INFO")
        b = cur.fetchall()
        cur.execute("SELECT * FROM SKILLS")
        c = cur.fetchall()
        cur.execute("SELECT * FROM SKILL_CERTIFICATION")
        d = cur.fetchall()
        cur.execute("SELECT * FROM SKILL_PROJECT")
        e = cur.fetchall()
        con.commit()
        self.ListBox.delete(0, END)
        self.ListBox.insert(END, str("BASIC_INFO"))
        for i in a:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')
        self.ListBox.insert(END, str("LOGIN_INFO"))
        for i in b:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')
        self.ListBox.insert(END, str("SKILLS"))
        for i in c:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')
        self.ListBox.insert(END, str("SKILL_CERTIFICATION"))
        for i in d:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')
        self.ListBox.insert(END, str("SKILL_PROJECT"))
        for i in e:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')

    def ViewUA(self):
        uid = self.UID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("SELECT * FROM LOGIN_INFO, BASIC_INFO WHERE %d=BASIC_INFO.UID=LOGIN_INFO.UID " % uid)
        a = cur.fetchall()
        con.commit()
        self.ListBox.delete(0, END)
        for i in a:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')

    def ViewUAS(self):
        uid = self.UID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("select basic_info.uid, basic_info.fname, skills.* from basic_info, skills where \
                    %d=basic_info.uid=skills.uid;" % uid)
        a = cur.fetchall()
        con.commit()
        self.ListBox.delete(0, END)
        for i in a:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')

    def ViewS(self):
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("SELECT BASIC_INFO.UID, BASIC_INFO.FNAME, SKILLS.* FROM BASIC_INFO, SKILLS WHERE \
                    BASIC_INFO.UID=SKILLS.UID ORDER BY SID")
        a = cur.fetchall()
        self.ListBox.delete(0, END)
        for i in a:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')

    def UpdateL(self):
        lid = self.LID.get()
        uid = self.UID.get()
        type = self.Type.get()
        username = self.Username.get()
        password = self.Password.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        ex = tkinter.messagebox.askyesno("UPDATE?", "Confirm that you Want to Update table 'LOGIN_INFO'")
        if ex > 0:
            cur.execute("UPDATE LOGIN_INFO SET TYPE='%s', USERNAME='%s', PASSWORD='%s', UID=%d \
                         WHERE LID=%d" % (type, username, password, uid, lid))
            con.commit()
            return
        self.LID.set("")
        self.UID.set("")
        self.Type.set("")
        self.Username.set("")
        self.Password.set("")

    def UpdateB(self):
        uid = self.UID.get()
        fname = self.FName.get()
        lname = self.LName.get()
        phone = self.Phone.get()
        city = self.City.get()
        mailid = self.MailID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        ex = tkinter.messagebox.askyesno("UPDATE?", "Confirm that you Want to Update table 'BASIC_INFO'")
        if ex > 0:
            cur.execute("UPDATE BASIC_INFO SET FNAME='%s', LNAME='%s', PHONE_NO=%d, CITY='%s', MAILID='%s' \
                         WHERE UID=%d" % (fname, lname, phone, city, mailid, uid))
            con.commit()
            return
        self.UID.set("")
        self.FName.set("")
        self.LName.set("")
        self.Phone.set("")
        self.City.set("")
        self.MailID.set("")

    def UpdateS(self):
        sid = self.SID.get()
        skill = self.Skill.get()
        nopro = self.NoProject.get()
        nocer = self.NoCertificate.get()
        uid = self.UID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        ex = tkinter.messagebox.askyesno("UPDATE?", "Confirm that you Want to Update table 'SKILLS'")
        if ex > 0:
            cur.execute("UPDATE SKILLS SET SID=%d, SKILL='%s', NO_OF_PROJECTS=%d, NO_OF_CERTIFICATES=%d \
                                                WHERE UID=%d AND SID=%d" % (sid, skill, nopro, nocer, uid, sid))
            con.commit()
            return
        self.SID.set("")
        self.Skill.set("")
        self.NoProject.set("")
        self.NoCertificate.set("")
        self.UID.set("")

    def UpdateSC(self):
        cid = self.CID.get()
        placesec = self.PlaceSecured.get()
        cerdesc = self.CertificateDescription.get()
        sid = self.SID.get()
        uid = self.UID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        ex = tkinter.messagebox.askyesno("UPDATE?", "Confirm that you Want to Update table 'SKILL_CERTIFICATION'")
        if ex > 0:
            cur.execute("UPDATE SKILL_CERTIFICATION SET PLACE_SECURED=%d, CERTIFICATE_DESCRIPTION='%s' \
                         WHERE SID=%d AND UID=%d AND CID=%d" % (placesec, cerdesc, sid, uid, cid))
            con.commit()
            return
        self.CID.set("")
        self.PlaceSecured.set("")
        self.CertificateDescription.set("")
        self.SID.set("")
        self.UID.set("")

    def UpdateSP(self):
        pid = self.PID.get()
        prodesc = self.ProjectDescription.get()
        sid = self.SID.get()
        uid = self.UID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        ex = tkinter.messagebox.askyesno("UPDATE?", "Confirm that you Want to Update table 'SKILL_PROJECT'")
        if ex > 0:
            cur.execute("UPDATE SKILL_PROJECT SET PROJECT_DESCRIPTION='%s' \
                         WHERE SID=%d AND UID=%d AND PID=%d" % (prodesc, sid, uid, pid))
            con.commit()
            return
        self.CID.set("")
        self.PlaceSecured.set("")
        self.CertificateDescription.set("")
        self.SID.set("")
        self.UID.set("")

    def Delete(self):
        uid = self.UID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("DELETE FROM BASIC_INFO WHERE UID=%d" % uid)
        con.commit()

    def ClearData(self):
        self.LID.set("")
        self.Type.set("")
        self.Username.set("")
        self.Password.set("")
        self.UID.set("")
        self.FName.set("")
        self.LName.set("")
        self.Phone.set("")
        self.City.set("")
        self.MailID.set("")
        self.SID.set("")
        self.Skill.set("")
        self.NoProject.set("")
        self.NoCertificate.set("")
        self.CID.set("")
        self.PlaceSecured.set("")
        self.CertificateDescription.set("")
        self.PID.set("")
        self.ProjectDescription.set("")

    def Exit(self):
        ex = tkinter.messagebox.askyesno("EXIT?", "Confirm that you Want to Exit")
        if ex > 0:
            self.master.destroy()
            return


# ---------------------------------------------------------------------------------------------------------------------


class Window4:
    def __init__(self, master):
        self.master = master
        self.master.title("Talent Management System")
        self.master.geometry('1920x1080+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LID = IntVar()
        self.Type = StringVar()
        self.Username = StringVar()
        self.Password = StringVar()
        self.UID = IntVar()
        self.FName = StringVar()
        self.LName = StringVar()
        self.Phone = IntVar()
        self.City = StringVar()
        self.MailID = StringVar()
        self.SID = StringVar()
        self.Skill = StringVar()
        self.NoProject = IntVar()
        self.NoCertificate = IntVar()
        self.CID = StringVar()
        self.PlaceSecured = IntVar()
        self.CertificateDescription = StringVar()
        self.PID = StringVar()
        self.ProjectDescription = StringVar()

        self.LabelTitle1 = Label(self.frame, text='Talent Management System', font=('arial', 30, 'bold', UNDERLINE),
                                 bd=10)
        self.LabelTitle1.grid(row=0, column=0, columnspan=2, pady=10)

        self.UserFrame1 = Frame(self.frame, bd=20, relief='ridge')
        self.UserFrame1.grid(row=1, column=0, sticky='W')

        # --------------------------------------------------------------------------------------------------------------

        self.LabelTitle = Label(self.UserFrame1, text='Login', font=('arial', 20, 'bold', UNDERLINE))
        self.LabelTitle.grid(row=0, column=0, columnspan=2, sticky='W')

        self.LoginLabel1 = Label(self.UserFrame1, font=('arial', 15, 'bold'), text="Enter Username: ")
        self.LoginLabel1.grid(row=1, column=0)
        self.LoginEntry1 = Entry(self.UserFrame1, font=('arial', 15), bd=5, textvariable=self.Username)
        self.LoginEntry1.grid(row=1, column=1)

        self.LoginLabel2 = Label(self.UserFrame1, font=('arial', 15, 'bold'), text="Enter Password: ")
        self.LoginLabel2.grid(row=2, column=0)
        self.LoginEntry2 = Entry(self.UserFrame1, font=('arial', 15), bd=5, textvariable=self.Password)
        self.LoginEntry2.grid(row=2, column=1)

        self.LoginBtn = Button(self.UserFrame1, font=('arial', 20, 'bold'), width=17, padx=18, pady=8, text="Login",
                               command=self.Login)
        self.LoginBtn.grid(row=3, column=1, sticky='W')

        # --------------------------------------------------------------------------------------------------------------

        self.UserFrame2 = Frame(self.frame, bd=20, relief='ridge')
        self.UserFrame2.grid(row=2, column=0, sticky='W')

        self.UserFrame21 = Frame(self.UserFrame2, bd=10, relief='ridge')
        self.UserFrame21.grid(row=0, column=0, sticky='W')

        # --------------------------------------------------------------------------------------------------------------

        self.LoginInfoTitle = Label(self.UserFrame21, text='Login Info', font=('arial', 20, 'bold', UNDERLINE))
        self.LoginInfoTitle.grid(row=0, column=0, sticky='W')

        self.LoginInfoLabel1 = Label(self.UserFrame21, font=('arial', 15, 'bold'), text="Enter Login ID: ")
        self.LoginInfoLabel1.grid(row=1, column=0, sticky='W')
        self.LoginInfoEntry1 = Entry(self.UserFrame21, font=('arial', 10), bd=5, textvariable=self.LID, state=DISABLED)
        self.LoginInfoEntry1.grid(row=1, column=1)

        self.LoginInfoLabel3 = Label(self.UserFrame21, font=('arial', 15, 'bold'), text="Enter Admin/User: ")
        self.LoginInfoLabel3.grid(row=3, column=0, sticky='W')
        self.LoginInfoEntry3 = Entry(self.UserFrame21, font=('arial', 10), bd=5, textvariable=self.Type, state=DISABLED)
        self.LoginInfoEntry3.grid(row=3, column=1)

        self.LoginInfoLabel4 = Label(self.UserFrame21, font=('arial', 15, 'bold'), text="Enter Username: ")
        self.LoginInfoLabel4.grid(row=4, column=0, sticky='W')
        self.LoginInfoEntry4 = Entry(self.UserFrame21, font=('arial', 10), bd=5, textvariable=self.Username)
        self.LoginInfoEntry4.grid(row=4, column=1)

        self.LoginInfoLabel5 = Label(self.UserFrame21, font=('arial', 15, 'bold'), text="Enter Password: ")
        self.LoginInfoLabel5.grid(row=5, column=0, sticky='W')
        self.LoginInfoEntry5 = Entry(self.UserFrame21, font=('arial', 10), bd=5, textvariable=self.Password)
        self.LoginInfoEntry5.grid(row=5, column=1)

        self.LoginInfoLabel2 = Label(self.UserFrame21, font=('arial', 15, 'bold'), text="Enter UID: ")
        self.LoginInfoLabel2.grid(row=2, column=0, sticky='W')
        self.LoginInfoEntry2 = Entry(self.UserFrame21, font=('arial', 10), bd=5, textvariable=self.UID, state=DISABLED)
        self.LoginInfoEntry2.grid(row=2, column=1)

        # --------------------------------------------------------------------------------------------------------------

        self.UserFrame22 = Frame(self.UserFrame2, bd=10, relief='ridge')
        self.UserFrame22.grid(row=0, column=1, sticky='W')

        # --------------------------------------------------------------------------------------------------------------

        self.BasicInfoTitle = Label(self.UserFrame22, text='Basic Info', font=('arial', 20, 'bold', UNDERLINE))
        self.BasicInfoTitle.grid(row=0, column=0, sticky='W')

        self.BasicInfoLabel1 = Label(self.UserFrame22, font=('arial', 15, 'bold'), text="Enter User ID: ")
        self.BasicInfoLabel1.grid(row=1, column=0, sticky='W')
        self.BasicInfoEntry1 = Entry(self.UserFrame22, font=('arial', 10), bd=5, textvariable=self.UID, state=DISABLED)
        self.BasicInfoEntry1.grid(row=1, column=1)

        self.BasicInfoLabel2 = Label(self.UserFrame22, font=('arial', 15, 'bold'), text="Enter First Name: ")
        self.BasicInfoLabel2.grid(row=2, column=0, sticky='W')
        self.BasicInfoEntry2 = Entry(self.UserFrame22, font=('arial', 10), bd=5, textvariable=self.FName)
        self.BasicInfoEntry2.grid(row=2, column=1)

        self.BasicInfoLabel3 = Label(self.UserFrame22, font=('arial', 15, 'bold'), text="Enter Last Name: ")
        self.BasicInfoLabel3.grid(row=3, column=0, sticky='W')
        self.BasicInfoEntry3 = Entry(self.UserFrame22, font=('arial', 10), bd=5, textvariable=self.LName)
        self.BasicInfoEntry3.grid(row=3, column=1)

        self.BasicInfoLabel4 = Label(self.UserFrame22, font=('arial', 15, 'bold'), text="Enter Phone Number: ")
        self.BasicInfoLabel4.grid(row=4, column=0, sticky='W')
        self.BasicInfoEntry4 = Entry(self.UserFrame22, font=('arial', 10), bd=5, textvariable=self.Phone)
        self.BasicInfoEntry4.grid(row=4, column=1)

        self.BasicInfoLabel5 = Label(self.UserFrame22, font=('arial', 15, 'bold'), text="Enter City: ")
        self.BasicInfoLabel5.grid(row=5, column=0, sticky='W')
        self.BasicInfoEntry5 = Entry(self.UserFrame22, font=('arial', 10), bd=5, textvariable=self.City)
        self.BasicInfoEntry5.grid(row=5, column=1)

        self.BasicInfoLabel6 = Label(self.UserFrame22, font=('arial', 15, 'bold'), text="Enter Mail ID: ")
        self.BasicInfoLabel6.grid(row=6, column=0, sticky='W')
        self.BasicInfoEntry6 = Entry(self.UserFrame22, font=('arial', 10), bd=5, textvariable=self.MailID)
        self.BasicInfoEntry6.grid(row=6, column=1)

        # -------------------------------------------------------------------------------------------------------------

        self.ButtonFrame = Frame(self.frame, bd=20, relief='ridge')
        self.ButtonFrame.grid(row=2, column=1, sticky='W')

        # -------------------------------------------------------------------------------------------------------------

        self.btn1 = Button(self.ButtonFrame, text='Clear All Entries', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.ClearData, state=DISABLED)
        self.btn1.grid(row=0, column=0)

        self.btn2 = Button(self.ButtonFrame, text='Update LOGIN_Info', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.UpdateL, state=DISABLED)
        self.btn2.grid(row=1, column=0)

        self.btn3 = Button(self.ButtonFrame, text='Update BASIC_Info', font=('arial', 10, 'bold'), width=20, padx=10,
                           pady=5, command=self.UpdateB, state=DISABLED)
        self.btn3.grid(row=2, column=0)

        self.btn4 = Button(self.ButtonFrame, text='Compare Skills', font=('arial', 10, 'bold'), width=20,
                           padx=10, pady=5, command=self.Compare, state=DISABLED)
        self.btn4.grid(row=3, column=0)

        self.btn5 = Button(self.ButtonFrame, text='View Skills', font=('arial', 10, 'bold'), width=20,
                           padx=10, pady=5, command=self.ViewS, state=DISABLED)
        self.btn5.grid(row=4, column=0)

        # -------------------------------------------------------------------------------------------------------------

        self.OutputFrame = Frame(self.frame, bd=20, relief='ridge')
        self.OutputFrame.grid(row=3, column=0, sticky='W')

        self.OutputTitle = Label(self.OutputFrame, text='Results: ', font=('arial', 20, 'bold', UNDERLINE))
        self.OutputTitle.grid(row=0, column=0, sticky='W')

        self.ScrollBar = Scrollbar(self.OutputFrame)
        self.ScrollBar.grid(row=1, column=1, sticky='NS')

        self.ListBox = Listbox(self.OutputFrame, width=80, height=18, font=('arial', 12, 'bold'),
                               xscrollcommand=self.ScrollBar.set)
        self.ListBox.grid(row=1, column=0, padx=8)
        self.ScrollBar.config(command=self.ListBox.xview)

        # -------------------------------------------------------------------------------------------------------------

    def Login(self):
        usr = self.Username.get()
        passwd = self.Password.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("SELECT * FROM LOGIN_INFO WHERE USERNAME='%s' AND PASSWORD='%s'" % (usr, passwd))
        success = cur.fetchall()
        if success:
            for i in success:
                if i[1] == 'USER':
                    lid = i[0]
                    type = i[1]
                    uid = i[4]
                    self.LoginEntry1.config(state=DISABLED)
                    self.LoginEntry2.config(state=DISABLED)
                    tkinter.messagebox.showinfo("Success!", "Welcome '%s'" % i[2])
                    con = pymysql.connect("localhost", "root", "root123", "tms")
                    cur = con.cursor()
                    cur.execute("SELECT * FROM LOGIN_INFO, BASIC_INFO WHERE BASIC_INFO.UID=%d AND LOGIN_INFO.UID=%d"
                                % (uid, uid))
                    a = cur.fetchall()
                    con.commit()
                    self.ListBox.delete(0, END)
                    for i in a:
                        self.ListBox.insert(END, '--------------------------------------------')
                        for j in i:
                            self.ListBox.insert(END, j)
                    self.ListBox.insert(END, '--------------------------------------------')
                    self.UID.set(uid)
                    self.LID.set(lid)
                    self.Type.set(type)
                    con.commit()
                    self.btn1.config(state=NORMAL)
                    self.btn2.config(state=NORMAL)
                    self.btn3.config(state=NORMAL)
                    self.btn4.config(state=NORMAL)
                    self.btn5.config(state=NORMAL)
                else:
                    con.commit()
                    self.Username.set("")
                    self.Password.set("")
                    tkinter.messagebox.showinfo("Failed", "Invalid Username or Password")
        else:
            con.commit()
            self.Username.set("")
            self.Password.set("")
            tkinter.messagebox.showinfo("Failed", "Invalid Username or Password")

    def ClearData(self):
        self.Username.set("")
        self.Password.set("")
        self.FName.set("")
        self.LName.set("")
        self.Phone.set("")
        self.City.set("")
        self.MailID.set("")

    def UpdateL(self):
        lid = self.LID.get()
        uid = self.UID.get()
        type = self.Type.get()
        username = self.Username.get()
        password = self.Password.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        ex = tkinter.messagebox.askyesno("UPDATE?", "Confirm that you Want to Update table 'LOGIN_INFO'")
        if ex > 0:
            cur.execute("UPDATE LOGIN_INFO SET TYPE='%s', USERNAME='%s', PASSWORD='%s', UID=%d \
                         WHERE LID=%d" % (type, username, password, uid, lid))
            con.commit()
            return
        self.LID.set("")
        self.UID.set("")
        self.Type.set("")
        self.Username.set("")
        self.Password.set("")

    def UpdateB(self):
        uid = self.UID.get()
        fname = self.FName.get()
        lname = self.LName.get()
        phone = self.Phone.get()
        city = self.City.get()
        mailid = self.MailID.get()
        lid = self.LID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        ex = tkinter.messagebox.askyesno("UPDATE?", "Confirm that you Want to Update table 'BASIC_INFO'")
        if ex > 0:
            cur.execute("UPDATE BASIC_INFO SET FNAME='%s', LNAME='%s', PHONE_NO=%d, CITY='%s', MAILID='%s' \
                         WHERE UID=%d" % (fname, lname, phone, city, mailid, uid))
            con.commit()
            return
        self.UID.set("")
        self.FName.set("")
        self.LName.set("")
        self.Phone.set("")
        self.City.set("")
        self.MailID.set("")
        self.LID.set("")

    def Compare(self):
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("select basic_info.uid, basic_info.fname, skills.skill, skills.no_of_certificates, \
                    skills.no_of_projects from basic_info, skills where basic_info.uid=skills.uid")
        a = cur.fetchall()
        con.commit()
        self.ListBox.delete(0, END)
        for i in a:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')

    def ViewS(self):
        uid = self.UID.get()
        con = pymysql.connect("localhost", "root", "root123", "tms")
        cur = con.cursor()
        cur.execute("SELECT BASIC_INFO.UID, BASIC_INFO.FNAME, SKILLS.* FROM BASIC_INFO, SKILLS WHERE \
                    BASIC_INFO.UID=%d AND SKILLS.UID=%d ORDER BY SID" % (uid, uid))
        a = cur.fetchall()
        self.ListBox.delete(0, END)
        for i in a:
            self.ListBox.insert(END, '--------------------------------------------')
            for j in i:
                self.ListBox.insert(END, j)
        self.ListBox.insert(END, '--------------------------------------------')


if __name__ == '__main__':
    main()
    mainloop()
