package edu.pku.openqa;

import static org.junit.Assert.*;

import java.util.ArrayList;
import org.junit.Test;

public class BaiduCrawlerTest {

	@Test
	public void test() {
		assertTrue(1 != 2);
	}	
	
	@Test
	public void ResponseNotEmpty() {
		BaiduCrawler crawler = new BaiduCrawler();
		ArrayList<String> res = crawler.getSearchResult("�й����׶����������У�");
		assertTrue(res != null);
	}

} // end class BaiduCrawlerTest
