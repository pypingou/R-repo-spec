%global packname  R2HTML
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          HTML exportation for R objects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Includes HTML function and methods to write in an HTML file. Thus, making
HTML reports is easy. Includes a function that allows redirection on the
fly, which appears to be very usefull for teaching purpose, as the student
can keep a copy of the produced output to keep all that he did during the
course. Package comes with a vignette describing how to write HTML reports
for statistical analysis. Finally, a driver for Sweave allows to parse
HTML flat files containing R code and to automatically write the
corresponding outputs (tables and graphs).

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
%doc %{rlibdir}/R2HTML/DESCRIPTION
%doc %{rlibdir}/R2HTML/CITATION
%doc %{rlibdir}/R2HTML/doc
%doc %{rlibdir}/R2HTML/html
%doc %{rlibdir}/R2HTML/NEWS
%{rlibdir}/R2HTML/help
%{rlibdir}/R2HTML/samples
%{rlibdir}/R2HTML/Meta
%{rlibdir}/R2HTML/INDEX
%{rlibdir}/R2HTML/demo
%{rlibdir}/R2HTML/R
%{rlibdir}/R2HTML/NAMESPACE
%{rlibdir}/R2HTML/output

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora