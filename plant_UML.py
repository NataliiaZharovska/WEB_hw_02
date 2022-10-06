
# +----------+
# |  Field   |
# |----------|
# |          |
# +----------+
#     .
#    /_\
#     |                [ Field ]            [ Field ]             [ Field ]            [ Field ]
#     |                    .                    .                     .                   .
#     |                   /_\                  /_\                   /_\                 /_\
#     |                    |                    |                     |                   |
#     |                    |                    |                     |                   |
# +----------+       +--------------+       +----------+       +---------------+       +-------+
# | Birthday |       |    Email     |       |  Phone   |       |     Adress    |       |  Name |
# |----------|       |--------------|       |----------|       |---------------|       |-------|
# | __value  |       | value        |       | __value  |       | value         |       | value |
# | value    |       |--------------|       | value    |       |---------------|       +-------+
# |----------|       | __init__     |       |----------|       | __init__      |
# | __init__ |       | change_email |       | __init__ |       | change_adress |
# +----------+       +--------------+       +----------+       +---------------+
#
#
#
#
# +-----------------------+
# |       Exception       |
# |-----------------------|
# |                       |
# +-----------------------+
#            .
#           /_\
#            |                             [ Exception ]                          [ Exception ]                 [ Exception ]
#            |                                   .                                      .                             .
#            |                                  /_\                                    /_\                           /_\
#            |                                   |                                      |                             |
#            |                                   |                                      |                             |
# +-----------------------+       +--------------------------------+       +---------------------------+       +---------------+
# | NameDoesNotExistError |       | BirthdayDoesNotMathFormatError |       | TelDoesNotMathFormatError |       | TryAgainError |
# |-----------------------|       |--------------------------------|       |---------------------------|       |---------------|
# | status                |       | status                         |       | status                    |       | status        |
# +-----------------------+       +--------------------------------+       +---------------------------+       +---------------+
#
#
#
#
# +---------------------+
# |       UserDict      |
# |---------------------|
# |                     |
# +---------------------+
#           .
#          /_\
#           |
#           |
#           |
#           |
#           |
# +---------------------+
# |     AddressBook     |
# |---------------------|
# | data                |  ---->  [ Record ]
# | note                |
# | notes_data          |
# | phone               |
# | tag                 |
# |---------------------|
# | __init__            |
# | add_notes           |
# | add_record          |
# | birthday_in_days    |
# | del_record          |
# | find_notes_by_tages |
# | iterator            |
# | sort_notes_by_tages |
# +---------------------+
#
#
#
#
# +--------------+       +------------------+
# |    Notes     |       |      Record      |
# |--------------|       |------------------|
# | note         |       | adress           |  ---->  [ Adress ]
# | result       |       | email            |  ---->  [ Email ]
# | tag          |       | name             |  ---->  [ Name ]
# |--------------|       | phone            |  ---->  [ Phone ]
# | change_notes |       | record_dict      |
# | del_notes    |       |------------------|
# +--------------+       | __init__         |
#                        | add_adress       |
#                        | add_email        |
#                        | add_phone        |
#                        | days_to_birthday |
#                        | del_phone        |
#                        | edit_phone       |
#                        +------------------+
