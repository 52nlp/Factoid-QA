package edu.pku.openqa;

import static org.junit.Assert.*;

import java.util.ArrayList;

import org.junit.Test;

public class GoogleCrawlerTest {

	@Test
	public void SearchResultNotEmpty() {
		GoogleCrawler crawler = new GoogleCrawler();
		String query = "�й����׶����������У�";
		ArrayList<String> result = crawler.getSearchResult(query);
		assertTrue(result != null);
		for (String snippet : result) {
			System.out.println(snippet);
			assertTrue(snippet.length() > 0);
		}
	}

}
