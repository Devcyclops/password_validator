<h1><b>Password_validator</b></h1>
A password validator package for python apps(web, desktop and cmd).

<b>Requirements</b>
Before you continue, ensure you have met the following requirements:
* You have python3 installed

<h2>Getting started</h2>

<pre>
from validator import (
    password_is_common, username_in_password, contains_alphanumeric_and_symbols, confirm_password,
    is_minimum_length,
)
validate = Validator(username, password)
</pre>

Check if password is common

<pre>
validator.password_is_common()
</pre>


Check if password is similar to username
<pre>
validator.username_in_password()

</pre>


Check if password is up to the required minimum length
<pre>
validator.is_minimum_length(length)
where length is the minimum length of your choice
</pre>



Check if password contains letters, numbers and symbols
<pre>
validator.contains_alphanumeric_and_symbols()
</pre>


Check if password and confirm password are the same
<pre>
validator.confirm_password(password2)
where password2 is the second password
</pre>


