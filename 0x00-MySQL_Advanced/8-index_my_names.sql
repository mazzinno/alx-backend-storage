-- createe an index idx_name_first on the table names and the first letter
CREATE INDEX idx_name_first ON names(name(1));
