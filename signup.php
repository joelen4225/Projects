<?php
    include_once 'header.php'
?>
            <div style="margin-bottom:20px"class="form-container">
                <h2 style="color:white">Register</h2>
                <form action="signup.inc.php" method="post">
                    <input type="text" name="name" placeholder="Full Name">
                    <input type="text" name="email" placeholder="E-Mail">
                    <input type="text" name="user" placeholder="Username">
                    <input type="password" name="pass" placeholder="Password">
                    <input type="password" name="pass2" placeholder="Confirm Password">
                    <br>
                    <button class="btn" type="submit" name="submit">Sign Up</button>
                </form>
            </div>
<?php
        include_once 'footer.php'
?>
        <script type="text/javascript">
            var MenuItems = document.getElementById("MenuItems");
            var Cart = document.getElementById("Cart");
            MenuItems.style.maxHeight = "0px"; 
            
            function menuopen()
            {   
                if (MenuItems.style.maxHeight == "0px")
                    {
                        MenuItems.style.maxHeight = "400px";
                        Cart.style.filter = "invert(1)";
                        MenuItems.style.marginTop = "110px";
                    }
                else
                    {
                        MenuItems.style.maxHeight = "0px";
                    }
            }
        </script>
        <script src="https://assets.juicer.io/embed.js" type="text/javascript"></script>