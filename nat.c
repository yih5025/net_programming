#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("뭐라도 입력하세요.");
        return 0;
    }

    char str[100];
    strcpy(str, argv[1]);
    int compareNat = strcmp(str, "nat");
    int compareIpv6 = strcmp(str, "ipv6");

    if (compareNat == 0) {
        printf("32비트 주소 공간 고갈\n 크기는 항상 20바이트로 고정한다.\n 주소 자체가 엄청 커졌기 때문에 보내는 내용은 8바이트 밖에 안된다.\n 항상 똑같은 크기를 보내면 전송 속도가 빠르다.\n");
    } else if (compareIpv6 == 0) {
        printf("payload란? : hop limit은 패킷의 수명 역할이다.\n 전세계의 모든 라우터를 IPv4에서 IPv6로 업그레이드 하기엔 어렵다.\n v4와 v6는 헤더 구조가 다르기 때문에 호환이 안된다.\n 새로 나오는 것들은 이전 버전을 호환해야 된다.\n v6 끼리 통신하고 싶은데 중간에 있는 라우터들이 v4라면??\n 그걸 터널링이라는 것으로 해결하면 된다.\n v6 패킷 앞에다 ipv4 헤더를 붙인다.\n 그래서 보내는 ip 주소를 B, 받는 애는 E - Ipv4\n 그래서 Ipv6라도 Ipv4를 거쳐서 연결이 될 수 있다.\n 그래서 B에서 E 까지는 포워딩을 해줄 수 있다.\n 그래서 v6 입장에선 Ipv4을 터널이라고 생각한다.\n 그래서 Ipv4 터널링이라고 한다.\n");
    }

    return 0;
}
