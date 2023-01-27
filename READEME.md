SITE LINK: https://colorgenerator.onrender.com

So I spent 6 hours figuring out why I couldn't get deployment to work on Render. I tried everything...I even tried switching to another deployment service.
Changing the code, optimizing it to make it faster. Then I realized, the image was too large and it was making it really slow. Therefore, the gunicorn worker was timeing out. I resized it to a smaller image and it started working...so dumb.
