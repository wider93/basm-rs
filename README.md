# basm.rs

basm.rs는 Rust 코드를 BOJ에 제출 가능한 C 프로그램으로 성능 저하 없이 변환해 주는 프로젝트입니다.

C 외에 64bit Assembly, Rust (메모리 사용량 감소)도 지원합니다.

> 156KB의 자유를 누리십시오!

## 효과

- 입력이 매우 간편하고 직관적입니다.

공백으로 구분된 a와 b를 받아 더한 결과를 출력하는 프로그램은 다음과 같이 작성할 수 있습니다.

```rust
let mut s = String::new();
std::io::stdin().read_to_string(&mut s).unwrap();
let mut input = s.split_whitespace().flat_map(str::parse);
let a: usize = input.next().unwrap();
let b: usize = input.next().unwrap();
println!("{}", a + b);
```

이를 basm에서는 다음과 같이 작성할 수 있습니다.

```rust
use basm::io::{Reader, Writer};

let mut reader: Reader = Default::default();
let mut writer: Writer = Default::default();
let a = reader.next_usize();
let b = reader.next_usize();
writer.write_usize(a + b);
```

- 표시되는 메모리 사용량이 줄어듭니다.

C의 경우 156KB부터, Rust의 경우 2188KB부터, Assembly의 경우 4212KB부터 시작합니다.

- **외부 crate를 사용할 수 있습니다.**

- AVX, AVX2, SSE 등의 SIMD를 사용할 수 있습니다.

- 다양한 최적화 옵션을 선택할 수 있습니다.

- 이미 구현된 자료구조와 알고리즘을 쉽게 가져다 쓸 수 있습니다.

  - Jagged Array (인접 리스트에 사용할 수 있습니다)
  
  - Union-Find (by rank / rem algorithm)

  - DFS (매크로)

  - KMP (Iterator)

  - Fenwick Tree

  - Segment Tree

## 사용법

`basm.rs`는 그 자체로 완전한 Rust cargo 프로젝트입니다.

`src/solution.rs` main() 에 원하는 코드를 삽입하시고,
일반적인 cargo 프로젝트와 같은 방식으로 빌드 / 실행할 수 있습니다.

`release.sh`를 실행하면 제출 가능한 C 코드가 출력됩니다.

`release-asm.sh`를 실행하면 제출 가능한 64bit Assembly 코드가 출력됩니다.

`release-rs.sh`를 실행하면 제출 가능한 Rust 코드가 출력됩니다.

## 주의사항

- Nightly Rust를 요구합니다.

- Python 3을 요구합니다.

- Binutils를 요구합니다.

- `std`를 사용할 수 없습니다.

- `libc`를 사용할 수 없습니다.

- 백준 채점 환경인 Ubuntu 16.04를 기준으로 동작합니다.

## 문제 해결

- 이유를 알 수 없는 Segmentation Fault가 로컬에서 발생하는 경우

스택 크기를 확인해 주세요. 그래도 문제를 해결할 수 없는 경우 이슈를 남겨 주세요.

