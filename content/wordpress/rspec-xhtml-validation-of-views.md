Title: RSpec XHTML Validation of Views
Date: 2010-06-19 16:02
Author: gmwils
Category: programming

A great way to learn is to read other people's code. And in that vein,
Chris Lowe has a [great post][] on suggested OSS Rails apps to [look
into][great post].

One technique I picked up from [simply\_agile][] is to validate the HTML
output by your views. That way, bad HTML isn't introduced.

To start with, you need to install the [assert\_valid\_xhtml][] plugin
and the libxml-ruby gem.

In your [spec/spec\_helper.rb][] file, add the following inside the
config block:

    config.include ValidateXhtml

And at the end of the file, outside the config block, include the
following:

    describe "a standard view", :shared => true do
      it "should be successful" do
        response.should be_success
      end
      it "should be valid" do
        response.should be_valid_xhtml
      end
    end

Now in your [view specs][], include the following line:

    it_should_behave_like "a standard view"

And that's it. Now each view will be tested for valid xhtml when you run
your specs.

There are a lot of other great techniques scattered through the projects
mentioned in the [original post][great post]. And if you want more
details on good practices for RSpec, check out the [RSpec Book][].

  [great post]: http://blog.chrislowis.co.uk/2010/05/31/five-rails-apps-to-study-and-learn-from.html
  [simply\_agile]: http://github.com/camelpunch/simply_agile
  [assert\_valid\_xhtml]: http://github.com/camelpunch/simply_agile/tree/master/vendor/plugins/assert_valid_xhtml/
  [spec/spec\_helper.rb]: http://github.com/camelpunch/simply_agile/blob/master/spec/spec_helper.rb
  [view specs]: http://github.com/camelpunch/simply_agile/tree/master/spec/views
  [RSpec Book]: http://www.pragprog.com/titles/achbd/the-rspec-book
