# LPRecon-LPFinder
Artificial License Plate Recognition with Node.js webserver endpoints.

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Getting Started
### Install openALPR (Ubuntu 14.04+)

```bash
# Install prerequisites
sudo apt-get install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
sudo apt-get install liblog4cplus-dev libcurl3-dev

# If using the daemon, install beanstalkd
sudo apt-get install beanstalkd

# Clone the latest code from GitHub
git clone https://github.com/openalpr/openalpr.git

# Setup the build directory
cd openalpr/src
mkdir build
cd build

# setup the compile environment
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..

# compile the library
make

# Install the binaries/libraries to your local system (prefix is /usr)
sudo make install

# Test the library
wget http://plates.openalpr.com/h786poj.jpg -O lp.jpg
alpr lp.jpg
```

### Requirements
```bash
# Python requirements
pip install -r requirements.txt

# Node.js modules
npm install
```

#### Before running
```bash
# .env variables
PORT = *port*
CLIENT_ID = *imgur api key*
PASS = *mongoDB pass*
COLLECTION = *mongoDB collection*

# Start server
npm start
```

### API Endpoints

#### Getting License Plate Number

This endpoint takes an Imgur image ID in 'imgur_image_id', the api will then return openALPR's results for the license plate.

```bash
GET https://localhost:3000/api/getLP/*imgur_image_id*

{
    "license" : "ABC123"
}
```

#### Getting Customer Information

This endpoint takes a license plate number in 'license_number', the api will then run a mongoDB query and if the license plate matches any customer then it returns the data of the customer.

```bash
GET https://localhost:3000/api/getCustomer/*license_number*

{
    "name" : "John Smith"
}
```
