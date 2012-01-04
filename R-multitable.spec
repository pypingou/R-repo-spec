%global packname  multitable
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Simultaneous manipulation of multiple arrays of data, with data.list objects

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Many data sets do not easily fit into a single data frame.  Storing such
data in a single data frame often results in either large numbers of
meaningless missing values or storage of redundant information; yet
storing them in multiple data frames often results in long
difficult-to-read workflows.  The multitable package introduces a new data
object called a data.list, which organises several data tables as a single
R object.  The primary goal of multitable is to provide a more intuitive
syntax for manipulating multiple-table data in R.  As data.lists can be
coerced to data.frames, they can be used with all R functions that accept
an object that is coercible to a data.frame (e.g. lm; plot; lme; and many

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/multitable/NEWS
%doc %{rlibdir}/multitable/html
%doc %{rlibdir}/multitable/doc
%doc %{rlibdir}/multitable/DESCRIPTION
%{rlibdir}/multitable/data
%{rlibdir}/multitable/R
%{rlibdir}/multitable/Meta
%{rlibdir}/multitable/NAMESPACE
%{rlibdir}/multitable/help
%{rlibdir}/multitable/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora