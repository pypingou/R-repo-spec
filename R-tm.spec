%global packname  tm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.6
Release:          1%{?dist}
Summary:          Text Mining Package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-slam 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-slam 


%description
A framework for text mining applications within R.

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
%doc %{rlibdir}/tm/NEWS
%doc %{rlibdir}/tm/html
%doc %{rlibdir}/tm/doc
%doc %{rlibdir}/tm/CITATION
%doc %{rlibdir}/tm/DESCRIPTION
%{rlibdir}/tm/stopwords
%{rlibdir}/tm/libs
%{rlibdir}/tm/data
%{rlibdir}/tm/R
RPM build errors:
%{rlibdir}/tm/INDEX
%{rlibdir}/tm/texts
%{rlibdir}/tm/Meta
%{rlibdir}/tm/NAMESPACE
%{rlibdir}/tm/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- initial package for Fedora