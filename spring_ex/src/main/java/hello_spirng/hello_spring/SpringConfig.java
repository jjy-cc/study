package hello_spirng.hello_spring;

import hello_spirng.hello_spring.aop.TimeTraceAop;
import hello_spirng.hello_spring.repository.JpaMemberRepository;
import hello_spirng.hello_spring.repository.MemberRepository;
import hello_spirng.hello_spring.repository.MemoryMemberRepository;
import hello_spirng.hello_spring.repository.jdbcMemberRepository;
import hello_spirng.hello_spring.service.MemberService;
import jakarta.persistence.EntityManager;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;
import javax.xml.crypto.Data;

@Configuration
public class SpringConfig {

    private final MemberRepository memberRepository;

    @Autowired
    public SpringConfig(MemberRepository memberRepository){
        this.memberRepository = memberRepository;
    }

    @Bean
    public MemberService memberService(){
        return new MemberService(memberRepository);
    }

    @Bean
    public TimeTraceAop timeTraceAop() {
        return new TimeTraceAop();
    }

    //@Bean
   //public MemberRepository memberRepository(){
        //return new MemoryMemberRepository();
        //return new jdbcMemberRepository(dataSource);
        //return new JpaMemberRepository(mem);
   // }
}
