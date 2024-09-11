from flask import Blueprint, render_template, redirect, url_for, flash, request
from . import db
from .models import Book
from .forms import BookForm
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@bp.route('/book/<int:id>', methods=['GET', 'POST'])
def book_detail(id):
    book = Book.query.get_or_404(id)
    return render_template('book_detail.html', book=book)

@bp.route('/create', methods=['GET', 'POST'])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        file = form.cover_photo.data
        filename = file.filename
        file.save(os.path.join('app/static/cover_photos', filename))
        book = Book(title=form.title.data, cover_photo=filename, pages=form.pages.data, description=form.description.data)
        db.session.add(book)
        db.session.commit()
        flash('Book created successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_book.html', form=form)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.pages = form.pages.data
        book.description = form.description.data
        if form.cover_photo.data:
            file = form.cover_photo.data
            filename = file.filename
            file.save(os.path.join('app/static/cover_photos', filename))
            book.cover_photo = filename
        db.session.commit()
        flash('Book updated successfully!', 'success')
        return redirect(url_for('main.book_detail', id=book.id))
    return render_template('edit_book.html', form=form)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('main.index'))
