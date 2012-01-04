%global packname  xts
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          eXtensible Time Series

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-zoo 


BuildRequires:    R-devel tex(latex) R-zoo



%description
Provide for uniform handling of R's different time-based data classes by
extending zoo, maximizing native format information preservation and
allowing for user level customization and extension, while simplifying
cross-class interoperability.

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
%doc %{rlibdir}/xts/html
%doc %{rlibdir}/xts/doc
%doc %{rlibdir}/xts/NEWS
%doc %{rlibdir}/xts/DESCRIPTION
%{rlibdir}/xts/Meta
%{rlibdir}/xts/R
%{rlibdir}/xts/api_example
%{rlibdir}/xts/data
%{rlibdir}/xts/unitTests
%{rlibdir}/xts/include
%{rlibdir}/xts/libs
%{rlibdir}/xts/NAMESPACE
%{rlibdir}/xts/INDEX
%{rlibdir}/xts/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.2-1
- initial package for Fedora