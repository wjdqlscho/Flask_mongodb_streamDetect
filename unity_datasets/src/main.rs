use std::fs::OpenOptions;
use std::io::{self, Write};
use std::sync::mpsc;
use std::thread;
use std::time::{Duration, SystemTime};
use rand::random;
use serde_json::json;

fn main() {
    println!("이 프로그램은 10초마다 집중하는 학생 수를 시뮬레이션합니다 (10초는 1분에 해당).");
    println!("프로그램을 중지하려면 'exit'을 입력하고 Enter 키를 누르세요.");

    let students = 100;
    let start_time = SystemTime::now();
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let mut input = String::new();
        while io::stdin().read_line(&mut input).is_ok() {
            if input.trim() == "exit" {
                tx.send(()).unwrap();
                break;
            }
            input.clear();
        }
    });

    loop {
        thread::sleep(Duration::from_secs(10));
        let focused_students = random::<u32>() % students;
        let elapsed_time = start_time.elapsed().unwrap().as_secs() / 10;
        let data = json!({
            "total_students": students,
            "focused_students": focused_students,
            "elapsed_time_minutes": elapsed_time
        });

        // 파일 경로를 절대 경로로 지정
        let file_path = "/Users/wjdqlscho/20241014_stream_detect/unity_datasets/students_focus.json";
        write_to_file(file_path, &data);
        println!("Total students: {}", students);
        println!("Focused students: {}", focused_students);
        println!("Ratio: {:.2}%", (focused_students as f64 / students as f64) * 100.0);
        println!("Elapsed time: {} minutes", elapsed_time);

        if rx.try_recv().is_ok() {
            break;
        }
    }
}

fn write_to_file(filename: &str, data: &serde_json::Value) {
    let file = OpenOptions::new()
        .write(true)
        .append(true)
        .create(true)
        .open(filename)
        .unwrap_or_else(|_| {
            eprintln!("Failed to open file: {}", filename);
            std::process::exit(1);
        });

    serde_json::to_writer(&file, &data).unwrap();
    writeln!(&file).unwrap();
}
