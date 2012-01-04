%global packname  hash
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Full feature implementation of hash/associated arrays/dictionaries

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-utils 

%description
This package implements a data structure similar to hashes in Perl and
dictionaries in Python but with a purposefully R flavor. For objects of
appreciable size, access using hashes outperforms native named lists and

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
%doc %{rlibdir}/hash/DESCRIPTION
%doc %{rlibdir}/hash/html
%{rlibdir}/hash/NAMESPACE
%{rlibdir}/hash/LICENSE
%{rlibdir}/hash/Meta
%{rlibdir}/hash/R
%{rlibdir}/hash/help
%{rlibdir}/hash/INDEX
%{rlibdir}/hash/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora