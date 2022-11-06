/**
 * @file ImportResource
 * @author sf
 * @date 2022/6/12 16:17
 * @description
 */

package com.secoder.bean;

import org.springframework.stereotype.Component;

@Component
public class ImportResource {
	
	public String importResourceName;
	public Boolean files;
	
	@Override
	public String toString() {
		return "ImportResource{" +
					   "importResourceName='" + importResourceName + '\'' +
					   ", files=" + files +
					   '}';
	}
	
	public String getImportResourceName() {
		return importResourceName;
	}
	public void setImportResourceName(String importResourceName) {
		this.importResourceName = importResourceName;
	}
	
	public Boolean getFiles() {
		return files;
	}
	public void setFiles(Boolean files) {
		this.files = files;
	}
}
