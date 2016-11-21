var gulp = require('gulp');
var rename = require('gulp-rename');

/* Bower components are hardcoded just beacause this is a small thing */


gulp.task('bower-css', function () {
    return gulp.src('./bower_components/bootstrap/dist/css/bootstrap.min.css')
        .pipe(rename('vendor.css'))
        .pipe(gulp.dest('./public/css/'))
});

gulp.task('bower-fonts', function () {
    return gulp.src('./bower_components/bootstrap/fonts/*')
        .pipe(gulp.dest('./public/fonts/'))
});