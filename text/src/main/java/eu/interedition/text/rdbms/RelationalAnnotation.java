/*
 * #%L
 * Text: A text model with range-based markup via standoff annotations.
 * %%
 * Copyright (C) 2010 - 2011 The Interedition Development Group
 * %%
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * #L%
 */
package eu.interedition.text.rdbms;

import com.google.common.base.Objects;
import com.google.common.collect.Ordering;
import eu.interedition.text.Annotation;
import eu.interedition.text.Name;
import eu.interedition.text.Range;
import eu.interedition.text.Text;
import eu.interedition.text.mem.SimpleAnnotation;
import eu.interedition.text.util.Annotations;

import java.util.Comparator;

public class RelationalAnnotation extends SimpleAnnotation {
  private static final Ordering<Annotation> ORDERING = Annotations.BASIC_ORDERING.compound(new Comparator<Annotation>() {
    @Override
    public int compare(Annotation o1, Annotation o2) {
      final long difference = ((RelationalAnnotation) o1).id - ((RelationalAnnotation) o2).id;
      return (difference == 0 ? 0 : (difference < 0 ? -1 : 1));
    }
  });

  protected final long id;

  public RelationalAnnotation(Text text, Name name, Range range, byte[] data, long id) {
    super(text, name, range, data);
    this.id = id;
  }

  public RelationalAnnotation(RelationalAnnotation other) {
    super(other);
    this.id = other.id;
  }

  public long getId() {
    return id;
  }

  @Override
  public boolean equals(Object obj) {
    if (id != 0 && obj != null && obj instanceof RelationalAnnotation) {
      return id == ((RelationalAnnotation) obj).id;
    }
    return super.equals(obj);
  }

  @Override
  public int hashCode() {
    return (id == 0 ? super.hashCode() : Objects.hashCode(id));
  }

  @Override
  public String toString() {
    return toStringHelper().addValue(getId()).toString();
  }

  public int compareTo(Annotation o) {
    return ORDERING.compare(this, o);
  }
}
