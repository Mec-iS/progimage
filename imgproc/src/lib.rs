extern crate image;
extern crate libc;

use libc::c_char;
use std::ffi::{CString, CStr};
use std::ptr;

use image::ImageFormat;
use image::imageops::FilterType;
use std::fmt;
use std::fs::File;
use std::time::{Duration, Instant};
use std::os::raw::c_int;

struct Elapsed(Duration);

impl Elapsed {
    fn from(start: &Instant) -> Self {
        Elapsed(start.elapsed())
    }
}

impl fmt::Display for Elapsed {
    fn fmt(&self, out: &mut fmt::Formatter) -> Result<(), fmt::Error> {
        match (self.0.as_secs(), self.0.subsec_nanos()) {
            (0, n) if n < 1000 => write!(out, "{} ns", n),
            (0, n) if n < 1000_000 => write!(out, "{} µs", n / 1000),
            (0, n) => write!(out, "{} ms", n / 1000_000),
            (s, n) if s < 10 => write!(out, "{}.{:02} s", s, n / 10_000_000),
            (s, _) => write!(out, "{} s", s),
        }
    }
}

//
// Example for resizing. FFI to be called from Python
//
#[no_mangle]
pub extern "C" fn rs_resize_1024(input: *const c_char) -> c_int {
    let path = unsafe { CStr::from_ptr(input).to_bytes() };
    let tiny = image::open(path).unwrap();
    for &(name, filter) in [
        ("near", FilterType::Nearest),
        ("tri", FilterType::Triangle),
        ("xcmr", FilterType::CatmullRom),
        ("ygauss", FilterType::Gaussian),
        ("zlcz2", FilterType::Lanczos3),
    ].iter() {
        let timer = Instant::now();
        let scaled = tiny.resize(1024, 768, filter);
        println!("Scaled by {} in {}", name, Elapsed::from(&timer));
        let mut output = File::create(&format!("../../fs/up2-{}.png", name)).unwrap();
        scaled.write_to(&mut output, ImageFormat::Png).unwrap();

        let timer = Instant::now();
        let scaled = tiny.resize(48, 48, filter);
        println!("Scaled by {} in {}", name, Elapsed::from(&timer));
        let mut output = File::create(&format!("up3-{}.png", name)).unwrap();
        scaled.write_to(&mut output, ImageFormat::Png).unwrap();
    }

    0
  }
