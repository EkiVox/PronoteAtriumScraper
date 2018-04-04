# Start server
cd Hosted
python -m SimpleHTTPServer 8000 &> /dev/null &
pid=$!

# Give server time to start up
sleep 1