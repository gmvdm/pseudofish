Title: Machinist, AuthLogic & Cucumber
Date: 2010-03-21 02:40
Author: gmwils
Category: programming

For a Rails app, I wanted to define rules about authentication using
[Cucumber][] and a bit of BDD. This went well, until I added in
[Pickle][], [Machinist][], and [AuthLogic][]; a few too many new things
at once.

I first ran afoul of defining users and then password confirmation. This
is easy to fix, as a Machinist spec is Ruby code:

    :::ruby
    Sham.email { Faker::Internet.email }
    Sham.username { Faker::Internet.user_name }
    User.blueprint do
      username
      email
      password 'secret'
      password_confirmation { password }
    end

I also created a named admin user:

    :::ruby
    User.blueprint(:admin) do
      username { Sham.username + " -admin-"}
      admin { true }
    end

I can then add some user specific step definitions for Cucumber using
[Webrat][]:

    :::ruby
    def user
      @user ||= User.make
    end

    def admin_user
      @admin_user ||= User.make(:admin)
    end

    def login(user)
      user
      visit '/login'
      fill_in("Username", :with => user.username)
      fill_in("Password", :with => user.password)
      click_button("Log in")
    end

    def logout
      visit '/logout'
    end

    Given /^I am a logged in user$/ do
      login(user)
    end

    Given /^I am logged in as an admin$/ do
      begin
        login(admin_user)
      rescue
        save_and_open_page
        raise
      end
    end

    Given /^I am not logged in$/ do
      logout
    end


The three behaviors I want to define are for guest, non-admin and admin
users. This gives me the following:

    Scenario: Can't see new entry as guest
      Given I am not logged in
      When I go to path "/entries"
      Then I should not see "New entry"

    Scenario: Can't see new entry as non admin
      Given I am a logged in user
      When I go to path "/entries"
      Then I should not see "New entry"

    Scenario: Can see new entry as admin
      Given I am logged in as an admin
      When I go to path "/entries"
      Then I should see "New entry"

In writing this blog post, I cleaned up some of the features and found a
few missing authentication paths. One further thing to ponder is what
happens when someone visits your controller directly. I think you should
also add defined behaviours for this, such as:

    Scenario: Can't add new entry as non admin via controller
      Given I am not logged in
      When I go to path "/entries/new"
      Then I should be on the home page

A big thank you to [Railscasts][]. Ryan has done several casts on
[Cucumber][1] and [AuthLogic][2] that really helped get me started.

If you need to sham a Paperclip file with Machinist, check out [Tim
Riley's blog][]. [This article][]was also useful, although I found after
I had most things working.

  [Cucumber]: http://cukes.info/
  [Pickle]: http://github.com/ianwhite/pickle
  [Machinist]: http://github.com/notahat/machinist
  [AuthLogic]: http://github.com/binarylogic/authlogic
  [Webrat]: http://wiki.github.com/brynary/webrat/
  [Railscasts]: http://railscasts.com/
  [1]: http://railscasts.com/episodes?search=cucumber
  [2]: http://railscasts.com/episodes?search=AuthLogic
  [Tim Riley's blog]: http://openmonkey.com/articles/2009/07/machinist-paperclip
  [This article]: http://itsignals.cascadia.com.au/?p=30/
