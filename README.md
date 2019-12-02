# Iba
//from Iba
heroku container:push web -a ibachatbot
heroku container:release web -a ibachatbot

//From actions
heroku container:push worker -a ibachatbot
heroku container:release worker -a ibachatbot