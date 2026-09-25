from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Room, Booking

booking_bp = Blueprint("booking", __name__, url_prefix="/booking")


@booking_bp.route("/rooms")
@login_required
def rooms():
    all_rooms = Room.query.all()
    return render_template("booking/rooms.html", rooms=all_rooms)


@booking_bp.route("/book/<int:room_id>", methods=["GET", "POST"])
@login_required
def book_room(room_id):
    room = Room.query.get_or_404(room_id)

    if request.method == "POST":
        check_in = datetime.strptime(request.form["check_in"], "%Y-%m-%d").date()
        check_out = datetime.strptime(request.form["check_out"], "%Y-%m-%d").date()

        if check_out <= check_in:
            flash("Check-out date must be after check-in date.", "error")
            return redirect(url_for("booking.book_room", room_id=room.id))

        booking = Booking(
            guest_id=current_user.id,
            room_id=room.id,
            check_in=check_in,
            check_out=check_out,
        )
        room.status = "booked"
        db.session.add(booking)
        db.session.commit()
        flash("Room booked successfully!", "success")
        return redirect(url_for("booking.my_bookings"))

    return render_template("booking/book_room.html", room=room)


@booking_bp.route("/my-bookings")
@login_required
def my_bookings():
    bookings = Booking.query.filter_by(guest_id=current_user.id).all()
    return render_template("booking/my_bookings.html", bookings=bookings)


@booking_bp.route("/cancel/<int:booking_id>", methods=["POST"])
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.guest_id != current_user.id and current_user.role != "admin":
        flash("Not authorized.", "error")
        return redirect(url_for("booking.my_bookings"))

    booking.status = "cancelled"
    booking.room.status = "available"
    db.session.commit()
    flash("Booking cancelled.", "success")
    return redirect(url_for("booking.my_bookings"))


@booking_bp.route("/pay/<int:booking_id>", methods=["POST"])
@login_required
def pay_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    booking.payment_status = "paid"
    db.session.commit()
    flash("Payment recorded.", "success")
    return redirect(url_for("booking.my_bookings"))
