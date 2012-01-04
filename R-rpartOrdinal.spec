%global packname  rpartOrdinal
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Ordinal classification tree functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rpart 

BuildRequires:    R-devel tex(latex) R-rpart 

%description
This package contains functions that can be called in conjunction with
rpart for deriving a classification tree when the response to be predicted
is ordinal.

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
%doc %{rlibdir}/rpartOrdinal/CITATION
%doc %{rlibdir}/rpartOrdinal/doc
%doc %{rlibdir}/rpartOrdinal/DESCRIPTION
%doc %{rlibdir}/rpartOrdinal/html
%{rlibdir}/rpartOrdinal/Meta
%{rlibdir}/rpartOrdinal/NAMESPACE
%{rlibdir}/rpartOrdinal/help
%{rlibdir}/rpartOrdinal/R
%{rlibdir}/rpartOrdinal/INDEX
%{rlibdir}/rpartOrdinal/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.3-1
- initial package for Fedora