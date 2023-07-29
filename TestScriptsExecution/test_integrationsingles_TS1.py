from Test_scripts.Singlescripts.Authtoken import put_AuthToken_repos, verify_key
from Test_scripts.Singlescripts.CreateBooking import post_CreateBooking_repos, get_BookingIDs
from Test_scripts.Singlescripts.DeletetheBooking import delete_Booking
from Test_scripts.Singlescripts.UpdateBooking import put_UpdateBookingBasedOnBookingId_repos


def test_01_Integration_UpdatingBookingDataWithUpdatingBookingid():
    put_UpdateBookingBasedOnBookingId_repos(post_CreateBooking_repos())


def test_02_Integration_NewbookingDataAndConfirmTheBookingid():
    get_BookingIDs(post_CreateBooking_repos())


def test_03_Integration_DeleteTheBookingidThatwasgenerated():
    delete_Booking(post_CreateBooking_repos(), put_AuthToken_repos())


def test_04_Integration_VerifythetokenidExist():
    verify_key(put_AuthToken_repos())


