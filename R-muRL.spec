%global packname  muRL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Mailmerge using R, LaTeX, and the Web

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-maps 

BuildRequires:    R-devel tex(latex) R-maps 

%description
Provides mailmerge methods for reading spreadsheets of addresses and other
relevant information to create standardized but customizable letters. 
Provides a method for mapping US ZIP codes, including those of letter
recipients.  Provides a method for parsing and processing html code from
online job postings of the American Political Science Association.

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
%doc %{rlibdir}/muRL/doc
%doc %{rlibdir}/muRL/DESCRIPTION
%doc %{rlibdir}/muRL/html
%{rlibdir}/muRL/NAMESPACE
%{rlibdir}/muRL/LICENSE
%{rlibdir}/muRL/Meta
%{rlibdir}/muRL/R
%{rlibdir}/muRL/help
%{rlibdir}/muRL/INDEX
%{rlibdir}/muRL/data
%{rlibdir}/muRL/demo

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora