class AppController {
  static getHomepage(req, res) {
    res.status(200).type('text').send('Hello Holberton School!');
  }
}

export default AppController;
