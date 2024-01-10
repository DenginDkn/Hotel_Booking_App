from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import User

dummy_user = {'name': 'Dengin Diken', 'authenticated': True}

hotels = [
    {
        'city':'istanbul',
        'id': 0,
        'name': 'Nex Hotel Istanbul City Center',
        'explanation': 'Istanbul merkezli spa, açık havuz olan otel.',
        'rating': 10.0,
        'reviews': 5,
        'price_original': 8909,
        'price_discounted': 6236,
        'price': 7000,
        'date_range': '22 Ara - 24 Ara',
        'nightly_price': 3118,
        'taxes_and_fees_included': True,
        'member_price_available': True,
        'image': 'nex_hotel.jpg',
        'location': 'Nex+Hotels+Istanbul',
        'location_exp': 'Bozkurt, Dolapdere Cd. No:209, 34375 Şişli/İstanbul',
        'amenities': ['Free Wi-Fi', 'Swimming Pool', 'Spa', 'Gym', 'Restaurant', 'Bar']
    },
    {
        'city':'bodrum',
        'id': 1,
        'name': 'Casa Nonna Bodrum - Adult Only',
        'explanation': 'Bodrum merkezinde sadece yetişkinlere özel otel.',
        'rating': 9.4,
        'reviews': 46,
        'price_original': 20472,
        'price_discounted': 13818,
        'price': 6000,
        'nightly_price': 6909,
        'taxes_and_fees_included': True,
        'member_price_available': True,
        'image': 'casa_nonna.jpg',
        'location': 'Casa+Nonna+Bodrum',
        'location_exp': 'Yalı Mahallesi İçmeler Mevkii No:60, 48400 Bodrum/Muğla',
        'amenities': ['Free Wi-Fi', 'Swimming Pool', 'Beach Access', 'Spa', 'Adults Only', 'Bar']
    },
    {
        'city':'fethiye',
        'id': 2,
        'name': 'Sundia Exclusive By Liberty Fethiye',
        'explanation': 'Fethiye de denize ve tatile doyacağınız mükemmel bir otel.',
        'rating': 7.8,
        'reviews': 10,
        'price_original': 16238,
        'price_discounted': 9414,
        'nightly_price': 4707,
        'price': 5000,
        'taxes_and_fees_included': True,
        'discount_percentage': 42,
        'image': 'sundia.jpg',
        'location': 'Sundia+Exclusive+by+Liberty+Fethiye',
        'location_exp': 'Foça, 1085. Sk., 48300 Fethiye/Muğla',
        'amenities': ['Free Wi-Fi', 'Swimming Pool', 'Spa', 'Beach Access', 'Fitness Center', 'Restaurant']
    }
]


@app.route('/special-prices')
def special_prices():
    # Fetch special hotel prices (you can replace this with actual logic)
    special_prices_data = [
        {
            'id':1,
            'name': 'Casa Nonna Bodrum - Adult Only',
            'rating': 9.4,
            'reviews': 46,
            'price': 7000,
            'taxes_and_fees_included': True,
            'member_price_available': True,
            'image': 'casa_nonna.jpg'
        },
        {
            'id':0,
            'name': 'Nex Hotel Istanbul City Center',
            'rating': 10.0,
            'reviews': 5,
            'price':5000,
            'date_range': '22 Ara - 24 Ara',
            'taxes_and_fees_included': True,
            'member_price_available': True,
            'image': 'nex_hotel.jpg'
        }
    ]

    return render_template('special_prices.html', user=dummy_user, special_prices=special_prices_data)

@app.route('/')
def home():
    return render_template('home.html', hotels=hotels, user=dummy_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') 
        password = request.form.get('password')
        authenticated_user = User.query.filter_by(email=email, password=password).first()
        if authenticated_user:
            user_data = {'name': authenticated_user.name, 'authenticated': True}
            return render_template('home.html', user=user_data)

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        surname = request.form['surname']
        country = request.form['country']
        city = request.form['city']

        new_user = User(email=email, password=password, name=name, surname=surname, country=country, city=city)
        db.session.add(new_user)
        db.session.commit()

    return render_template('register.html')

@app.route('/search-results', methods=['GET', 'POST'])
def search_results():
    query = request.args.get('q', '')
    results = [hotel for hotel in hotels if query.lower() in hotel['city'].lower() or query.lower() in hotel['name'].lower()]

    if request.method == 'POST':
        return render_template('search_results.html', hotels=results, query=query)

    return render_template('search_results.html', hotels=results, query=query)



@app.route('/hotel-detail/<int:hotel_id>')
def hotel_detail(hotel_id):
    selected_hotel = next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)

    if selected_hotel:
        return render_template('hotel_detail.html', hotel=selected_hotel, user=dummy_user)
    else:
        return redirect(url_for('home'))
    
    

