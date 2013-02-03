Title: Tracking Outbound Links with Rails 3
Date: 2011-02-28 05:45
Author: gmwils
Category: Ruby

To gain some insight on what interests users, I want to be able to track
which links they click on.

</p>

There were a number of options I considered, and finally settled on
using Javascript to update an underlying Click model. For analytics, I
intend to aggregate the data offline. Thus the current aim is capture
only.

</p>

To store the data, I created a simple model using:

</p>

<p>
    rails g model Click url:string request_ip:string user_agent:string user_id:string

</p>

I decided not to store the all the request data, and instead just track
the following:

</p>

-   **URL** - these are already normalized
-   **Request IP** - I aim to use this to figure out geo-location at a
    later date
-   **User Agent** - which browser used
-   **User ID** - a unique hash for the user, kept in a cookie

</p>

Rails kindly adds in the created\_at column, which is the final key
piece of data.

</p>

To generate the click data, I added the following into my
[application.js][]:

</p>

<p>
      $("a").live("click", function() {    params = { click: { url: this.href } };    $.post("/clicks", params);    setTimeout('document.location = "' + this.href + '"', 100);    return false;  });

</p>

This posts the click through to the [Click controller][]. In the
controller, I added in the following:

</p>

<p>
      def create    @click = Click.new(params[:click])            @click.request_ip = request.remote_addr    @click.user_agent = request.user_agent    @click.user_id = cookies[:uid]        respond_to do |format|      if @click.save        format.js { render :json => @click }      else        format.js { render :json => @click.errors }      end    end  end

</p>

To generate the tracking cookie, I included the following in
[application.js][]:

</p>

<p>
      if($.cookie("uid") == null) {    var tracking_id = $.md5($.now() + "-" + Math.ceil(Math.random() * 314159)); // Current time + random seed    $.cookie("uid", tracking_id, { expires: 365 * 20, path: "/" });      }

</p>

By using an MD5 hash of the current time and a random number, I am
comfortable enough that it is unique enough for tracking purposes.

</p>

In this example, I am tracking all clicks on the application. For
production use, I'll filter this down to only the outbound article
titles.

</p>

I've included a skeleton Rails 3 app that includes the code on
[GitHub][]. I used a jQuery plugin for cookies and MD5 hash generation,
and these are included in the [public/javascripts][] directory.

</p>

There are a few things that this misses, such as links clicked via RSS,
via Twitter, and a heap of tests. I'm looking into Feedburner and bit.ly
to see if I they fill in the missing metrics.

</p>

  [application.js]: https://github.com/gmwils/clicks/blob/master/public/javascripts/application.js
  [Click controller]: https://github.com/gmwils/clicks/blob/master/app/controllers/clicks_controller.rb#L42
  [GitHub]: https://github.com/gmwils/clicks/
  [public/javascripts]: https://github.com/gmwils/clicks/tree/master/public/javascripts/jquery
