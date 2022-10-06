# BOT assistent
# CLI - Command Line Interface
#              Architecture :
#                   - command`s parser
#                   - decorator --> Rise exceptions
#                   - command`s processing functions (Handlers):
#                           - hello_func                            --- first greeting
#                           - add_func         --> add_record       --- create new contact
#                           - change_func      --> edit_phone       --- change  telephone number for existed contact
#                           - phone_func                            --- show telephone number
#                           - show_func                             --- show all contacts (name telephone number)
# update+                   - see_func                              --- show n records (you could use this command several times)
#                           - addnum_func      --> add_phone        --- add aditional tel number for certain contact
#                           - del_func         --> del_phone        --- del tel number for certain contact
#                           - birth_func                            --- add date of birthday in data format
#                           - nextbirth_func   --> days_to_birthday --- show how many days left up to next birthday
#                           - help_func                             --- bot show commands explanations
#                           - save_func                             --- save data base in file: name (without extention)
#                           - load_func                                       --- load data base from file: name (without extention)
#                           - lookup_func                                     --- find text in records (no difference which case of characters)
#                           - good_buy_func                                   --- bot stops work and messege "Good bye!"
# new_func+                  - del_record_hand     --> del_record              --- delete record from AddressBook
# new_func+                  - add_email_head      --> add_email               --- add email to record (with regex check)
# new_func+                  - add_adress_head     --> add_adress              --- add adress to record
# new_func+                  - add_notes_head      --> add_notes               --- add notes to record
# new_func+                  - find_notes_by_tages_head --> find_notes_by_tages --- looking up notes by tages (#tage#)
# new_func+                  - sort_notes_by_tages_head --> sort_notes_by_tages --- sorting up notes by tages (#tage#)
# new_func+                  - del_notes_by_tages_head --> sort_notes_by_tages --- del notes by tages (#tage#)
# new_func+                  - change_notes_by_tages_head --> sort_notes_by_tages --- change notes by tages (#tage#)
# new_func+                  - sort_files                                       --- sort files in folder
# new_func+                  - guess_command                                    --- analizing taping and try to guess command
# new_func+                  - birthday_in_days_hand    --> birthday_in_days    --- display list of contacts, who have birthday in x days
#
#
#                   - request-answear loop

# Input - dict(name: telephone number)
# Requirements:
#              - telephone number format: 0675223345 - 10 digits;
#              - bot undestands commands:
#                          - "hello" - answear: "How can I help you?"
#                          - "add' name telephone number" - save new contact
#                          - "change' name telephone number" - change telephone number for existed contact
#                          - "phone' name" - show telephone number
#                          - "show all" - show all contacts (name telephone number)
#                          - "see' n" - show n records (you could use this command several times)
#                          - "addnum' name telephone number" - add aditional tel number for certain contact
#                          - "del' name telephone number" - del tel number for certain contact
#                          - "addbirth" name birthday - add date of birthday in data format
#                          - "nextbirth" name - show how many days left up to next birthday
#                          - "help" - bot show commands explanations
#                          - "save" name - save data base in file: name (without extention)
#                          - "load name" - load data base from file: name (without extention)
#                          - "lookup' text" - find text in records (no difference which case of characters)
# new+                      - "delrec' name" - delete record from AddressBook
# new+                      - "addemail' name email" - add email to record
# new+                      - "changeemail" name new_email - change all emails on new one
# new+                      - "addadress' name text" - add adress to record
# new+                      - "addnotes' name text" - add notes to record
# new+                      - "findtag' teg_text" - looking up notes by tages (#tage#)
# new+                      - "sortnotes' teg_text" - sorting up notes by tages (#tage#)
# new+                      - "delnotes' teg_text" - del notes by tages (#tage#)
# new+                      - "changenotes' teg_text" - change notes by tages (#tage#)
# new+                      - "sortfiles' folder_path" - sort files in folder
# new+                      - "guess'    - switch on guess mode ---> analizing taping and try to guess command
# new+                      - "checkbirth' days_number - display list of contacts, who have birthday in x days
#                           - "good bye" or "close" or "exit" - bot stops work and messege "Good bye!"
#
#
# Class_structure:
#                  UserDict Class:
#                         -user has Book of Contacts (AddressBook Class):
# new+                             |__> required (Notes Class) - one or more
#
#                                 |__> records (Record Class): --> dict {Record.name.value: value}
#                                                              --> Name object - separated atribute
#                                                              --> Phone objects - separated atribute
# new+                                                          --> Notes objects - separated atribute
# new+                                                          --> Email objects - separated atribute
# new+                                                          --> Adress objects - separated atribute
#
#                                          |__> fields (Field Class):
#                                                      - required (Name Class) - only one
#                                                      - optional (Phone Class) - one or more
#                                                      - optional (Birthday Class) - only one
# new+                                                  - required (Email Class) - one or more
# new+                                                  - required (Adress Class) - only one
#
#
#
#                AdressBook methods:

#                                - add_record --> add Record in self.data
#new_func+                       - del_record <-- del_record_hand
#                                - iterator - return --> generator by records -N records for 1 step
# new_func+                       - find_notes_by_tages <-- find_notes_by_tages_head - looking up notes by tages (#tage#) in []
# new_func+                       - sort_notes_by_tages <-- sort_notes_by_tages_head - sorting up notes by tages (#tage#) in []
# new_func+                       - birthday_in_days    <-- birthday_in_days_head - display list of contacts, who have birthday in x days
# new_func+                       - add_notes           <-- add_notes_head - add notes to record
#
#
#                                           Notes methods:
# new_func+                                         - change_notes  <-- change_notes_head - change notes in record
# new_func+                                         - del_notes     <-- del_notes_head -    delete notes in record
#
#                                           Record methods:
#                                                 - add_phone <-- addnum_func - add aditional tel number for certain contact (with regex check)
#                                                 - del_phone <-- del_func - del tel number for certain contact
#                                                 - edit_phone <-- change_func - change telephone number for existed contact
#                                                 - days_to_birthday <-- nextbirth_func - show how many days left up to next birthday
# new_func+                                        - add_email <-- add_email_head - add email to record (with regex check)
# new_func+                                        - add_adress<-- add_adress_head - add adress to record
#
#
#                                                  Phone methods:
#                                                         - setter - check tel. num format (7777777777)
#
#                                                  Birthday methods:
#                                                         - setter - check birthday format (28.05.1978)

#
#                                                  Email methods:
# new_func+                                                - change_email <-- change_email_head - change email in record (with regex check)
#
#
#                                                  Adress methods:
# new_func (not relevant)                                  - change_adress <-- change_adress_head - change adress in record
#
#