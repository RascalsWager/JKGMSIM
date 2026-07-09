import random
from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


APP_TITLE = 'Jester King Market Lord'

ITEMS = {'Satyr Pilsner': (45, 130), 'Nani Rice Lager': (40, 120), 'Sasha IPA': (50, 150), 'Atrial Rubicite': (55, 180), 'Wild Yeast': (80, 260), 'Texas Malt': (35, 110), 'NZ Hops': (90, 300), 'Oak Barrels': (120, 420), 'Pizza Dough': (20, 70), 'Pepperoni': (25, 90), 'Mushrooms': (18, 75), 'Goat Walks': (35, 140), 'Hibiscus Tea': (12, 55), 'Lemonade': (10, 45), "Bobby's Brewery Tour": (15, 65), 'Hay Bales': (30, 115), 'Goat Experience Tickets': (40, 160)}

GOATS = ['oysOld Dirty Bastard', 'Sasha', 'a Goat', 'Banjo the goat', 'Frat Boy Ted', 'Dumpling', 'Biscuit', 'Sasha', 'Ozzy', 'Ozzy', 'Sasha', 'One of the boy goats']

LOCATIONS = ['Beer Garden', 'Pole Barn', 'Pizzeria', 'Goat Pen', 'Barrel Room', 'Brewhouse', 'QR Pickup', 'the wedding']

RANKS = [(0, 'trainee'), (1000, 'barback'), (5000, 'pizza slinger'), (10000, 'cellar hand'), (25000, 'yeast wrangler'), (50000, 'goat whisperer'), (100000, 'GM aka God Mode')]

EVENTS = ['A wedding party just bought every keg of {item}. Prices exploded.', 'The goats escaped and ate the label stock. {item} prices got weird.', '{goat} headbutted a vendor cart. {item} is suddenly hard to find.', '{goat} became famous on Instagram. Goat Walk Tickets are hot today.', 'A goat walk crowd rolled through thirsty and hungry. The market tightened.', '{goat} stole a bag of Goat Treats. Treat prices jumped.', 'The goat pen needed emergency Hay Bales. Hay got expensive fast.', 'A thunderstorm scared off the crowd. The market is soft today.', 'A beer nerd convention rolled in. Everyone wants {item}.', 'The pizza oven is ripping hot. {item} is moving fast.', 'A fresh batch hit the board. {item} is cheaper than usual.', 'The barrel room smells incredible. Demand for {item} jumped.', 'A private event bought heavy. You feel the market tighten.', 'Someone started a rumor about {item}. The price is all over the place.', 'The crowd is thirsty, hungry, and surrounded by goats. Good luck keeping up.', 'A wedding party just bought every keg of {item}. Prices exploded.', 'The goats escaped and ate the label stock. {item} prices got weird.', '{goat} headbutted a vendor cart. {item} is suddenly hard to find.', '{goat} became famous on Instagram. Goat Walk Tickets are hot today.', 'A goat walk crowd rolled through thirsty and hungry. The market tightened.', '{goat} stole a bag of Goat Treats. Treat prices jumped.', 'The goat pen needed emergency Hay Bales. Hay got expensive fast.', 'A thunderstorm scared off the crowd. The market is soft today.', 'A beer nerd convention rolled in. Everyone wants {item}.', 'The pizza oven is ripping hot. {item} is moving fast.', 'A fresh batch hit the board. {item} is cheaper than usual.', 'The barrel room smells incredible. Demand for {item} jumped.', 'A private event bought heavy. You feel the market tighten.', 'Someone started a rumor about {item}. The price is all over the place.', 'The crowd is thirsty, hungry, and surrounded by goats. Good luck keeping up.', 'A party bus of sorority girls rolled in and bought every light beer and cider in sight. {item} prices went feral.', 'Sasha knocked over a tray of food and somehow started a bidding war over {item}.', '{goat} got loose during a wedding toast and the crowd panic-bought Goat Walk Tickets.', 'A bachelor party tried to pay for {item} with poker chips. The confusion made prices spike.', "Someone yelled 'limited release' and nobody checked if it was true. {item} vanished fast.", 'A pizza influencer posted one blurry slice and now Pizza Dough is basically gold.', 'The goats formed a blockade near the Goat Pen. Hay Bales are moving like emergency currency.', 'A bus full of beer nerds asked for the weirdest thing on the board. {item} immediately got expensive.', 'A kid dropped a lemonade and six adults somehow blamed the market. Lemonade prices jumped.', 'The Pole Barn TV started playing goat footage on loop. Goat Treats went nuclear.', 'A wedding DJ accidentally announced a fake last call. The Beer Market lost its mind.', "Someone said the word 'spontaneous' too loudly and Wild Yeast doubled before lunch.", 'A mysterious man in a linen shirt bought every Oak Barrel he could find.', 'The pizzeria ran out of pepperoni and the staff stared into the void. Pepperoni prices exploded.', '{goat} ate a printed event contract. Nobody knows what was ordered, so everyone is hoarding {item}.', "A corporate group demanded 'the authentic farmhouse experience' and bought all the Farmhouse Ale.", 'A thunderstorm hit, then immediately became a beautiful sunset. The crowd bought everything twice.', 'A bachelorette party adopted {goat} emotionally and bought all the Goat Walk Tickets.', 'A food runner slipped, saved the tray, and became a legend. Goat Cheese prices shot up for no reason.', 'A rumor spread that Nelson Hops were cursed. Collectors bought them anyway.', 'A visiting brewer winked at the wrong person and now Texas Malt is impossible to find.', 'The line at the Pizzeria got so long people started trading Pizza Dough like concert tickets.', "A man in jorts declared Satyr Pilsner 'the people's beer.' It sold out instantly.", 'A cider fan club appeared with matching hats. Cider-adjacent goods got weirdly valuable.', 'A goat stared into a barrel for nine minutes. Oak Barrels spiked because people called it a sign.', 'A private event asked for extra ranch and somehow crashed the whole market.', 'Someone brought a tiny cowboy hat for {goat}. Goat Treats are now a luxury good.', "The bartender said 'we might run out' and that was all it took. {item} went vertical.", 'A dadcore BBQ crew showed up and cleaned out light beer, lager, and anything cold.', 'The merch line got confused with the beer line. Hibiscus Tea became a status symbol.', 'A wedding guest tried to Venmo a goat. Goat Walk Tickets spiked from the publicity.', 'The oven burped smoke like a dragon and everyone ordered pizza at once.', "A cryptic chalkboard note said '{item} knows what it did.' Sales tripled.", 'The goats staged what looked like a union meeting. Hay Bales are now strategic assets.', 'A jazz trio played one funky chord and the crowd bought every Farmhouse Ale.', 'A tourist asked if Wild Yeast was a petting zoo add-on. Wild Yeast prices went insane.', "A server whispered 'barrel pull' and the Beer Garden turned into a treasure hunt.", "Somebody dropped the word 'allocation' and beer nerds started sweating.", 'A rogue picnic table became VIP seating. Everyone near it started buying {item}.', 'A goat sneezed on a clipboard and accidentally approved a massive {item} order.', 'A wedding planner demanded calm. The market responded with violence.', 'A bus driver said they had exactly 17 minutes. The group bought everything portable.', "A man asked for 'the cleanest beer' and accidentally created a run on Satyr Pilsner.", "A spilled tray of mushrooms became 'the mushroom incident.' Mushrooms are now somehow rare.", 'A goat named Sasha charged the food pickup window and knocked over a tray of food. Chaos pricing engaged.', "A local chef tasted Goat Cheese and whispered 'oh no.' Goat Cheese is gone everywhere.", 'A heat wave hit the Beer Garden. Lemonade and Hibiscus Tea became survival equipment.', 'A cold front hit the Pole Barn. Everybody suddenly wanted big beer and pizza.', 'A magician at a private event made a keg disappear. Nobody is laughing. {item} prices jumped.', 'Someone saw Bobby with a clipboard and assumed a secret event was coming. The market panicked.']

RUMOR_TEMPLATES = ['Word is {location} needs {item} around day {day}.', '{goat} heard staff whispering about a {item} shortage on day {day}.', 'Someone at {location} is quietly buying up {item}. Watch day {day}.', 'A private party may clean out {item} on day {day}.', 'The goats seem obsessed with {item}. That usually means trouble around day {day}.', 'A vendor mentioned {item} could spike near day {day}.', 'No promises, but {item} may be the move around day {day}.', '{goat} knocked over a clipboard. It said {item}, day {day}, big order.', 'Word is {location} needs {item} around day {day}.', '{goat} heard staff whispering about a {item} shortage on day {day}.', 'Someone at {location} is quietly buying up {item}. Watch day {day}.', 'A private party may clean out {item} on day {day}.', 'The goats seem obsessed with {item}. That usually means trouble around day {day}.', 'A vendor mentioned {item} could spike near day {day}.', 'No promises, but {item} may be the move around day {day}.', '{goat} knocked over a clipboard. It said {item}, day {day}, big order.', 'Party bus chatter says light beer and cider vanish around day {day}.', '{goat} overheard sorority girls planning to clean out {item} on day {day}.', 'Sasha has been circling the food pickup window. {item} may spike near day {day}.', "A wedding planner's clipboard says {item}, {location}, day {day}, urgent.", 'Beer nerds are whispering about {item}. Could get ugly on day {day}.', 'Someone at {location} keeps asking if {item} is allocated. Watch day {day}.', 'The goats are standing in a circle around {item}. That usually means day {day}.', 'A party bus deposit just hit. {item} may disappear around day {day}.', 'The pizzeria prep list has {item} underlined three times for day {day}.', "A private event wants 'a ton of something easy.' Might be {item} on day {day}.", '{goat} ate half a receipt but left the words {item} and day {day}.', "A bartender said 'do not tell anyone about {item} on day {day}.' So obviously everyone knows.", 'A DJ request sheet says the drop hits when {item} spikes on day {day}.', 'The farm radio crackled: {location}, {item}, day {day}. Then it went dead.', 'A goat walk group asked about bulk pricing for {item}. Check day {day}.', 'A bachelor party is pre-gaming the market. {item} may rip on day {day}.', 'A bachelorette party has matching shirts and a plan for {item} on day {day}.', "Someone wrote '{item} emergency' on a napkin and left it at {location}. Day {day}.", 'The wedding seating chart has one table named {item}. Suspicious. Day {day}.', '{goat} knocked over a chalkboard and it landed on {item}. Day {day} feels cursed.', 'A distributor text mentioned {item}, but only around day {day}.', 'A chef said {item} is the sleeper play near day {day}.', 'The goats refused treats unless paid in {item}. Could spike day {day}.', 'A table of dads in cargo shorts is targeting {item} around day {day}.', 'The staff meal rumor mill says {item} will matter on day {day}.', 'A kid asked if {item} was rare, and adults started acting weird. Day {day}.', 'Someone at {location} is building a mountain of {item} boxes for day {day}.', "A guest asked for 'whatever is about to sell out.' They were pointed toward {item}. Day {day}.", 'A goat named {goat} is sleeping beside {item}. Market omen for day {day}.', 'The private event BEO has coffee stains over everything except {item} and day {day}.', 'A drummer asked to be paid in {item}. That never ends normal. Day {day}.', 'A cooler count came back short on {item}. Watch day {day}.', 'The Pole Barn whisper network says {item} gets spicy on day {day}.', 'A goat selfie line is forming. Somehow {item} is involved around day {day}.', 'A mystery van unloaded decorations at {location}. {item} could pop day {day}.', 'A regular said they saw this exact {item} setup before. Day {day} was a bloodbath.', 'A tourist asked if {item} was the famous one. Could be by day {day}.', 'A server hid three cases of {item} behind a plant. Day {day} is the tell.', "The event radio said 'copy that, all {item}' around day {day}.", 'A goat tried to eat the {item} label. Demand follows chaos. Day {day}.', 'A vendor booth is trading art for {item}. Check day {day}.', 'A group chat screenshot leaked: {item}, {location}, day {day}.', "Someone wrote 'DO NOT RUN OUT OF {item}' in all caps for day {day}.", 'The weather app says hot, but the market says {item} on day {day}.', 'A cider crew is coming through and may drag {item} up with them on day {day}.', 'A pizza panic is brewing. {item} could be the hinge on day {day}.', 'A goat blocked the path to {location}. People may hoard {item} around day {day}.', 'A man in a Hawaiian shirt asked too many questions about {item}. Day {day}.', "A staff note says 'Sasha incident backup plan: {item}' for day {day}.", 'Nobody knows why, but {item} has bad moon energy around day {day}.']

STARTING_INFO = "Here's the situation:\nAfter one failed job after another, you decide to become a Jester King employee. You scrape together your last $5000, but it really isn't enough to get started. The good news is that Bobby spots you an extra $1000 in house credit. The bad news is that the loan shark will soon want his money back.\n\nBuy beer, yeast, hops, pizza supplies, goat treats, hay bales, and goat walk tickets. Travel around the property, watch the market, listen to the street rumors, survive the goats, pay down debt, and make it to day 30."


def sp_safe(size):
    return size


class Game:
    def __init__(self):
        self.day = 1
        self.max_days = 30
        self.location = random.choice(LOCATIONS)
        self.cash = 5000
        self.bank = 0
        self.debt = 1150
        self.health = 100
        self.capacity = 15
        self.inventory = {name: 0 for name in ITEMS}
        self.market = {}
        self.message = STARTING_INFO
        self.rumors = []
        self.future_spikes = {}
        self.generate_market(first=True)
        self.seed_starting_rumors()

    @property
    def pocket_count(self):
        return sum(self.inventory.values())

    @property
    def net_worth(self):
        inv_value = sum(self.inventory[name] * self.market.get(name, {}).get("price", 0) for name in ITEMS)
        return self.cash + self.bank + inv_value - self.debt

    @property
    def rank(self):
        worth = self.net_worth
        current = RANKS[0][1]
        for threshold, name in RANKS:
            if worth >= threshold:
                current = name
        return current

    def seed_starting_rumors(self):
        for _ in range(3):
            self.create_future_opportunity(min_offset=2, max_offset=6)

    def create_future_opportunity(self, min_offset=2, max_offset=7):
        if self.day >= self.max_days - 1:
            return

        target_day = min(self.max_days, self.day + random.randint(min_offset, max_offset))
        item = random.choice(list(ITEMS.keys()))
        location = random.choice(LOCATIONS)
        goat = random.choice(GOATS)
        multiplier = random.uniform(2.0, 4.5)

        self.future_spikes.setdefault(target_day, [])
        self.future_spikes[target_day].append({
            "item": item,
            "location": location,
            "goat": goat,
            "multiplier": multiplier,
        })

        rumor = random.choice(RUMOR_TEMPLATES).format(
            item=item,
            location=location,
            goat=goat,
            day=target_day
        )

        self.rumors.append(rumor)
        self.rumors = self.rumors[-8:]

    def generate_market(self, first=False):
        market = {}
        for name, (low, high) in ITEMS.items():
            qty = random.randint(0, 10)
            price = random.randint(low, high)

            if not first and random.random() < 0.12:
                price = int(price * random.uniform(1.8, 3.5))
            elif not first and random.random() < 0.12:
                price = max(1, int(price * random.uniform(0.25, 0.55)))

            market[name] = {"qty": qty, "price": price}

        self.market = market
        self.apply_scheduled_opportunities()

    def apply_scheduled_opportunities(self):
        if self.day not in self.future_spikes:
            return

        notes = []
        for spike in self.future_spikes[self.day]:
            item = spike["item"]
            self.market[item]["price"] = int(self.market[item]["price"] * spike["multiplier"])
            self.market[item]["qty"] = max(0, self.market[item]["qty"] - random.randint(2, 7))
            notes.append(f"The rumor was true: {item} spiked at {spike['location']}.")

        if notes:
            self.message = "\n".join(notes)

        del self.future_spikes[self.day]

    def travel(self, new_location=None):
        if self.day >= self.max_days:
            self.message = "The season is over. Final score time."
            return False

        self.day += 1
        if new_location:
            self.location = new_location
        else:
            choices = [loc for loc in LOCATIONS if loc != self.location]
            self.location = random.choice(choices)

        self.debt = int(self.debt * 1.08)
        self.generate_market()

        if random.random() < 0.65:
            self.create_future_opportunity()

        self.trigger_random_event()
        return True

    def trigger_random_event(self):
        item = random.choice(list(ITEMS.keys()))
        goat = random.choice(GOATS)
        event = random.choice(EVENTS).format(item=item, goat=goat)

        if "Goat Walk Tickets are hot" in event and "Goat Walk Tickets" in self.market:
            self.market["Goat Walk Tickets"]["price"] = int(self.market["Goat Walk Tickets"]["price"] * random.uniform(2.0, 4.0))
        elif "Goat Treats" in event and "Goat Treats" in self.market:
            self.market["Goat Treats"]["price"] = int(self.market["Goat Treats"]["price"] * random.uniform(2.0, 4.0))
        elif "Hay Bales" in event and "Hay Bales" in self.market:
            self.market["Hay Bales"]["price"] = int(self.market["Hay Bales"]["price"] * random.uniform(2.0, 4.0))

        roll = random.random()
        if roll < 0.22:
            self.market[item]["price"] = int(self.market[item]["price"] * random.uniform(1.7, 3.2))
        elif roll < 0.42:
            self.market[item]["price"] = max(1, int(self.market[item]["price"] * random.uniform(0.35, 0.7)))
        elif roll < 0.55:
            lost = min(self.cash, random.randint(25, 250))
            self.cash -= lost
            event += f"\nYou lost ${lost} in the chaos."
        elif roll < 0.68:
            found = random.randint(50, 300)
            self.cash += found
            event += f"\nYou found ${found} in forgotten event change."
        elif roll < 0.83:
            damage = random.randint(5, 20)
            self.health = max(0, self.health - damage)
            event += f"\n{goat} got loose and clipped your knee. You lost {damage} health."

        if self.debt > 0 and random.random() < 0.18:
            pressure = random.randint(50, 200)
            self.debt += pressure
            event += f"\nThe loan shark added ${pressure} in pressure fees."

        if self.message and self.message.startswith("The rumor was true"):
            self.message += "\n\n" + event
        else:
            self.message = event

    def rumor_ticker_text(self):
        if not self.rumors:
            return "Word on the Street: Nothing yet."
        return "  |  ".join(self.rumors)


class JKAppLayout(BoxLayout):
    ticker_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=dp(4), padding=dp(6), **kwargs)
        self.game = Game()
        self.selected_market_item = None
        self.selected_inventory_item = None
        self.ticker_offset = 0
        self.build_ui()
        self.refresh()
        Clock.schedule_interval(self.animate_ticker, 0.08)

    def build_ui(self):
        title = Label(
            text="[b]Jester King Market Lord[/b]",
            markup=True,
            font_size=sp_safe(22),
            size_hint_y=None,
            height=dp(40),
        )
        self.add_widget(title)

        self.info = Label(
            text="",
            font_size=sp_safe(13),
            color=(0.85, 0.95, 1, 1),
            markup=True,
            halign="left",
            valign="top",
            size_hint_y=None,
            height=dp(118),
        )
        self.info.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        self.add_widget(self.info)

        self.ticker = Label(
            text="",
            font_size=sp_safe(13),
            color=(0.2, 1, 0.2, 1),
            markup=True,
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=dp(34),
        )
        self.ticker.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        self.add_widget(self.ticker)

        middle = BoxLayout(orientation="horizontal", spacing=dp(5))
        self.add_widget(middle)

        left = BoxLayout(orientation="vertical", spacing=dp(3))
        middle.add_widget(left)
        left.add_widget(Label(text="[b]Beer Market[/b]", markup=True, size_hint_y=None, height=dp(28)))
        self.market_scroll = ScrollView()
        self.market_list = GridLayout(cols=1, spacing=dp(2), size_hint_y=None)
        self.market_list.bind(minimum_height=self.market_list.setter("height"))
        self.market_scroll.add_widget(self.market_list)
        left.add_widget(self.market_scroll)

        center = BoxLayout(orientation="vertical", spacing=dp(4), size_hint_x=None, width=dp(125))
        middle.add_widget(center)

        for text, callback in [
            ("Buy", self.buy_selected),
            ("Sell", self.sell_selected),
            ("Dump", self.dump_selected),
            ("Travel", self.travel_popup),
            ("Stay", self.stay_here),
            ("Bank", self.bank_popup),
            ("Debt", self.pay_debt_popup),
            ("Info", self.info_popup),
        ]:
            center.add_widget(Button(text=text, size_hint_y=None, height=dp(42), on_release=callback))

        right = BoxLayout(orientation="vertical", spacing=dp(3))
        middle.add_widget(right)
        self.inv_title = Label(text="[b]Apron Pocket 0/10[/b]", markup=True, size_hint_y=None, height=dp(28))
        right.add_widget(self.inv_title)
        self.inv_scroll = ScrollView()
        self.inv_list = GridLayout(cols=1, spacing=dp(2), size_hint_y=None)
        self.inv_list.bind(minimum_height=self.inv_list.setter("height"))
        self.inv_scroll.add_widget(self.inv_list)
        right.add_widget(self.inv_scroll)

        self.status = Label(
            text="",
            font_size=sp_safe(13),
            markup=True,
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=dp(98),
        )
        self.status.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        self.add_widget(self.status)

    def animate_ticker(self, dt):
        full_text = "   Word on the Street: " + self.game.rumor_ticker_text() + "   "
        if len(full_text) < 160:
            full_text = full_text * 3
        self.ticker_offset = (self.ticker_offset + 2) % len(full_text)
        display = full_text[self.ticker_offset:] + full_text[:self.ticker_offset]
        self.ticker.text = f"[color=33ff33]{display[:115]}[/color]"

    def market_button(self, item, qty, price):
        selected = item == self.selected_market_item
        prefix = "> " if selected else ""
        btn = Button(
            text=f"{prefix}{item}\nQty {qty}    ${price}",
            font_size=sp_safe(12),
            size_hint_y=None,
            height=dp(54),
            halign="left",
        )
        btn.bind(on_release=lambda instance, name=item: self.select_market(name))
        return btn

    def inventory_button(self, item, qty, price):
        selected = item == self.selected_inventory_item
        prefix = "> " if selected else ""
        btn = Button(
            text=f"{prefix}{item}\nQty {qty}    Market ${price}",
            font_size=sp_safe(12),
            size_hint_y=None,
            height=dp(54),
            halign="left",
        )
        btn.bind(on_release=lambda instance, name=item: self.select_inventory(name))
        return btn

    def select_market(self, item):
        self.selected_market_item = item
        self.selected_inventory_item = None
        self.refresh()

    def select_inventory(self, item):
        self.selected_inventory_item = item
        self.selected_market_item = None
        self.refresh()

    def ask_qty_popup(self, title, message, maximum, callback):
        content = BoxLayout(orientation="vertical", spacing=dp(8), padding=dp(8))
        content.add_widget(Label(text=f"{message}\nMax: {maximum}", font_size=sp_safe(16)))
        buttons = GridLayout(cols=3, spacing=dp(4), size_hint_y=None, height=dp(180))

        values = [1, 2, 3, 5, 10, maximum]
        clean_values = []
        for value in values:
            value = min(value, maximum)
            if value >= 1 and value not in clean_values:
                clean_values.append(value)

        popup = Popup(title=title, content=content, size_hint=(0.85, 0.55))

        def choose(value):
            popup.dismiss()
            callback(value)

        for value in clean_values:
            buttons.add_widget(Button(text=str(value), on_release=lambda instance, v=value: choose(v)))

        content.add_widget(buttons)
        content.add_widget(Button(text="Cancel", size_hint_y=None, height=dp(42), on_release=lambda instance: popup.dismiss()))
        popup.open()

    def buy_selected(self, instance=None):
        name = self.selected_market_item
        if not name:
            self.popup_message("Buy", "Pick something from the Beer Market first.")
            return
        data = self.game.market[name]
        max_by_cash = self.game.cash // data["price"]
        max_by_space = self.game.capacity - self.game.pocket_count
        maximum = min(data["qty"], max_by_cash, max_by_space)
        if maximum <= 0:
            self.popup_message("Buy", "You do not have enough cash, inventory space, or market quantity.")
            return

        def do_buy(qty):
            self.game.cash -= qty * data["price"]
            self.game.inventory[name] += qty
            self.game.market[name]["qty"] -= qty
            self.game.message = f"You bought {qty} {name} for ${qty * data['price']}."
            self.refresh()

        self.ask_qty_popup("Buy", f"How many {name}?", maximum, do_buy)

    def sell_selected(self, instance=None):
        name = self.selected_inventory_item
        if not name:
            self.popup_message("Sell", "Pick something from your apron pocket first.")
            return
        maximum = self.game.inventory[name]
        if maximum <= 0:
            return

        def do_sell(qty):
            price = self.game.market[name]["price"]
            self.game.cash += qty * price
            self.game.inventory[name] -= qty
            self.game.message = f"You sold {qty} {name} for ${qty * price}."
            self.refresh()

        self.ask_qty_popup("Sell", f"How many {name}?", maximum, do_sell)

    def dump_selected(self, instance=None):
        name = self.selected_inventory_item
        if not name:
            self.popup_message("Dump", "Pick something from your apron pocket first.")
            return
        maximum = self.game.inventory[name]
        if maximum <= 0:
            return

        def do_dump(qty):
            self.game.inventory[name] -= qty
            self.game.message = f"You dumped {qty} {name}."
            self.refresh()

        self.ask_qty_popup("Dump", f"Dump how many {name}?", maximum, do_dump)

    def travel_popup(self, instance=None):
        content = BoxLayout(orientation="vertical", spacing=dp(4), padding=dp(8))
        popup = Popup(title="Where to tomorrow?", content=content, size_hint=(0.85, 0.8))
        for loc in LOCATIONS:
            if loc == self.game.location:
                continue
            content.add_widget(Button(text=loc, size_hint_y=None, height=dp(44),
                                      on_release=lambda instance, l=loc: self.travel_to(l, popup)))
        content.add_widget(Button(text="Cancel", size_hint_y=None, height=dp(44), on_release=lambda instance: popup.dismiss()))
        popup.open()

    def travel_to(self, location, popup):
        popup.dismiss()
        self.game.travel(location)
        self.check_end_conditions()
        self.refresh()

    def stay_here(self, instance=None):
        self.game.travel(self.game.location)
        self.check_end_conditions()
        self.refresh()

    def bank_popup(self, instance=None):
        content = BoxLayout(orientation="vertical", spacing=dp(8), padding=dp(8))
        content.add_widget(Label(text=f"Cash: ${self.game.cash}\nBank: ${self.game.bank}", font_size=sp_safe(16)))
        popup = Popup(title="Bank", content=content, size_hint=(0.85, 0.45))

        def deposit_all(btn):
            amount = self.game.cash
            self.game.cash = 0
            self.game.bank += amount
            self.game.message = f"You deposited ${amount}."
            popup.dismiss()
            self.refresh()

        def withdraw_all(btn):
            amount = self.game.bank
            self.game.bank = 0
            self.game.cash += amount
            self.game.message = f"You withdrew ${amount}."
            popup.dismiss()
            self.refresh()

        content.add_widget(Button(text="Deposit All Cash", size_hint_y=None, height=dp(44), on_release=deposit_all))
        content.add_widget(Button(text="Withdraw All Bank", size_hint_y=None, height=dp(44), on_release=withdraw_all))
        content.add_widget(Button(text="Cancel", size_hint_y=None, height=dp(44), on_release=lambda instance: popup.dismiss()))
        popup.open()

    def pay_debt_popup(self, instance=None):
        if self.game.debt <= 0:
            self.popup_message("Debt", "You are debt free.")
            return
        maximum = min(self.game.cash, self.game.debt)
        if maximum <= 0:
            self.popup_message("Debt", "You need cash to pay debt.")
            return

        def do_pay(amount):
            self.game.cash -= amount
            self.game.debt -= amount
            self.game.message = f"You paid ${amount} toward the loan shark."
            self.refresh()

        self.ask_qty_popup("Pay Debt", "Pay how much debt?", maximum, do_pay)

    def info_popup(self, instance=None):
        self.popup_message(
            "How to Play",
            "Buy low, sell high, travel around Jester King, and survive 30 days.\n\n"
            "Watch the Word on the Street ticker. It hints at future price spikes.\n\n"
            "Goats affect the market. Tickets, tours, and Hay Bales can spike hard.\n\n"
            "Debt grows every day, so pay it down when you can.\n\n"
            f"Your apron pocket holds {self.game.capacity} items."
        )

    def popup_message(self, title, message):
        content = BoxLayout(orientation="vertical", spacing=dp(8), padding=dp(8))
        label = Label(text=message, font_size=sp_safe(15), halign="center", valign="middle")
        label.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        content.add_widget(label)
        popup = Popup(title=title, content=content, size_hint=(0.85, 0.55))
        content.add_widget(Button(text="OK", size_hint_y=None, height=dp(44), on_release=lambda instance: popup.dismiss()))
        popup.open()

    def check_end_conditions(self):
        if self.game.health <= 0:
            self.popup_message("Game Over", f"The goats got you.\nFinal net worth: ${self.game.net_worth}")
        elif self.game.day >= self.game.max_days:
            self.popup_message("Season Over", f"Day {self.game.max_days} is over.\nFinal net worth: ${self.game.net_worth}\nRank: {self.game.rank}")

    def refresh(self):
        self.info.text = f"[color=d6ecff]{self.game.message}[/color]"

        self.market_list.clear_widgets()
        for name, data in sorted(self.game.market.items()):
            self.market_list.add_widget(self.market_button(name, data["qty"], data["price"]))

        self.inv_list.clear_widgets()
        for name, qty in sorted(self.game.inventory.items()):
            if qty > 0:
                self.inv_list.add_widget(self.inventory_button(name, qty, self.game.market[name]["price"]))

        self.inv_title.text = f"[b]Apron Pocket {self.game.pocket_count}/{self.game.capacity}[/b]"

        self.status.text = (
            f"[b]Location:[/b] {self.game.location}    "
            f"[b]Health:[/b] {self.game.health}%    "
            f"[b]Day:[/b] {self.game.day}/{self.game.max_days}\n"
            f"[b]Rank:[/b] {self.game.rank}\n"
            f"[b]Cash:[/b] ${self.game.cash}    "
            f"[b]Bank:[/b] ${self.game.bank}    "
            f"[b]Debt:[/b] ${self.game.debt}    "
            f"[b]Net:[/b] ${self.game.net_worth}"
        )


class JesterKingMarketLordApp(App):
    def build(self):
        self.title = APP_TITLE
        return JKAppLayout()


if __name__ == "__main__":
    JesterKingMarketLordApp().run()
