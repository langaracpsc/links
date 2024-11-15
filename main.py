from flask import Flask, redirect

app = Flask(__name__)

# Define the links in a dictionary for easy management
referral_code = "linkspage"

links = {
    "register": f"https://lu.ma/g2q0djtw?utm_source={referral_code}",
    "hiring": f"https://forms.gle/hdojrJcQXKLxU14W7",
    # Add more links here as needed
}




@app.route('/')
def redirect_to_linktree():
    return redirect("https://linktr.ee/langaracpsc?utm_source=" + referral_code)  # Hardcoded linktree URL with ref


@app.route('/<path:path>')
def redirect_link(path):
    # Check if the path exists in the links dictionary
    if path in links:
        return redirect(links[path])
    else:
        return "Link not found", 404


if __name__ == '__main__':
    app.run(debug=True)
