var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'IOOS National Glider DAC' });
});

router.get('/benefits', function(req, res, next) {
  res.render('benefits', {title: 'Benefits'});
});

router.get('/metrics', function(req, res, next) {
  res.render('metrics', {title: 'metrics'});
});

module.exports = router;
